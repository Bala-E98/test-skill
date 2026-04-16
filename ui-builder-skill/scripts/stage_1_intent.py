"""
Stage 1: Intent Analysis & Setup
=================================

Parses user's natural language request and classifies intent.

Based on Section 5.4 of the specification.
"""

import re
from typing import List, Tuple
from context import UIBuilderContext, Intent


# ============================================================================
# KEYWORD DICTIONARIES (from spec Section 5.4.1)
# ============================================================================

# Intent classification keywords
INTENT_KEYWORDS = {
    "generate": ["create", "generate", "build", "add", "make", "new"],
    "modify": ["modify", "change", "update", "edit", "alter", "fix"],
    "page": ["page", "dashboard", "full page", "entire", "complete"]
}

# Component type keywords
COMPONENT_KEYWORDS = {
    "form/login": ["login", "sign in", "signin", "log in", "authentication form"],
    "form/registration": ["register", "signup", "sign up", "registration", "create account"],
    "form/contact": ["contact", "contact form", "feedback", "inquiry"],
    "form/password-reset": ["password reset", "forgot password", "reset password"],
    "table/data": ["table", "grid", "data table", "data grid", "list"],
    "nav/header": ["header", "navbar", "navigation bar", "top nav"],
    "nav/sidebar": ["sidebar", "side nav", "side navigation", "drawer"],
    "page/dashboard": ["dashboard", "admin panel", "analytics"],
    "page/ecommerce": ["ecommerce", "e-commerce", "shop", "store", "product"],
}

# Modifier keywords
MODIFIER_KEYWORDS = {
    "styling:dark": ["dark", "dark theme", "dark mode"],
    "styling:light": ["light", "light theme", "light mode"],
    "feature:oauth": ["oauth", "social login", "google login", "github login"],
    "feature:2fa": ["2fa", "mfa", "two factor", "multi factor"],
    "feature:remember-me": ["remember me", "remember-me", "stay logged in"],
    "feature:validation": ["validation", "validate", "error handling"],
    "feature:multi-step": ["multi-step", "wizard", "step by step"],
    "tech:typescript": ["typescript", "ts"],
    "tech:javascript": ["javascript", "js"],
}


# ============================================================================
# INTENT CLASSIFICATION FUNCTIONS
# ============================================================================

def extract_intent(request: str) -> str:
    """
    Classify user's primary intent.
    
    Returns:
        Intent enum value (generate_component, generate_page, modify_component, unknown)
    """
    request_lower = request.lower()
    
    # Check for modification intent
    if any(keyword in request_lower for keyword in INTENT_KEYWORDS["modify"]):
        return Intent.MODIFY_COMPONENT.value
    
    # Check for page generation
    if any(keyword in request_lower for keyword in INTENT_KEYWORDS["page"]):
        return Intent.GENERATE_PAGE.value
    
    # Check for component generation
    if any(keyword in request_lower for keyword in INTENT_KEYWORDS["generate"]):
        return Intent.GENERATE_COMPONENT.value
    
    # Default to component generation if keywords like "form", "table" are present
    if any(comp_type in request_lower for comp_type in ["form", "table", "nav", "menu"]):
        return Intent.GENERATE_COMPONENT.value
    
    return Intent.UNKNOWN.value


def extract_component_type(request: str) -> str:
    """
    Extract component type from request using keyword matching.
    
    Returns:
        Component type string (e.g., "form/login", "table/data") or None
    """
    request_lower = request.lower()
    
    # Score each component type by keyword matches
    scores = {}
    for comp_type, keywords in COMPONENT_KEYWORDS.items():
        score = sum(1 for keyword in keywords if keyword in request_lower)
        if score > 0:
            scores[comp_type] = score
    
    # Return highest scoring type
    if scores:
        return max(scores.items(), key=lambda x: x[1])[0]
    
    return None


def extract_modifiers(request: str) -> List[str]:
    """
    Extract feature/styling modifiers from request.
    
    Returns:
        List of modifier strings (e.g., ["styling:dark", "feature:oauth"])
    """
    request_lower = request.lower()
    modifiers = []
    
    for modifier, keywords in MODIFIER_KEYWORDS.items():
        if any(keyword in request_lower for keyword in keywords):
            modifiers.append(modifier)
    
    return modifiers


def extract_target_directory(request: str) -> str:
    """
    Extract target directory if user specified one.
    
    Examples:
        "create a login form in the auth folder" -> "auth"
        "add a table to components/dashboard" -> "components/dashboard"
    
    Returns:
        Directory path or None
    """
    # Look for patterns like "in the X folder", "to X directory", "at X"
    patterns = [
        r"in (?:the )?([a-zA-Z0-9_/-]+)(?: folder| directory)?",
        r"to (?:the )?([a-zA-Z0-9_/-]+)(?: folder| directory)?",
        r"at ([a-zA-Z0-9_/-]+)"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, request.lower())
        if match:
            return match.group(1)
    
    return None


# ============================================================================
# AMBIGUITY RESOLUTION
# ============================================================================

def check_ambiguity(context: UIBuilderContext) -> Tuple[bool, str]:
    """
    Check if request is ambiguous and return clarifying question.
    
    Returns:
        (is_ambiguous, clarifying_question)
    """
    # Unknown intent
    if context.intent == Intent.UNKNOWN.value:
        return True, (
            "I couldn't determine what you want to create. "
            "Please clarify: Are you trying to create a component (form, table, navigation), "
            "a full page (dashboard, landing page), or modify existing code?"
        )
    
    # No component type identified
    if context.intent in [Intent.GENERATE_COMPONENT.value, Intent.GENERATE_PAGE.value]:
        if not context.component_type:
            return True, (
                "What type of component would you like to create? "
                "Examples: login form, data table, navigation bar, dashboard page, etc."
            )
    
    # Modify intent but no target
    if context.intent == Intent.MODIFY_COMPONENT.value:
        return True, (
            "Which component would you like to modify, and what changes do you want? "
            "Please provide the component name and describe the modification."
        )
    
    return False, ""


# ============================================================================
# MAIN STAGE FUNCTION
# ============================================================================

def analyze_intent(context: UIBuilderContext) -> UIBuilderContext:
    """
    Stage 1: Analyze user intent and initialize context.
    
    This is the entry point for the UI Builder pipeline.
    Extracts intent, component type, and modifiers from natural language.
    
    Args:
        context: UIBuilderContext with user_request set
    
    Returns:
        Updated context with intent, component_type, and modifiers
    """
    context.current_stage = 1
    
    # Extract information from request
    context.intent = extract_intent(context.user_request)
    context.component_type = extract_component_type(context.user_request)
    context.modifiers = extract_modifiers(context.user_request)
    
    # Check for ambiguity
    is_ambiguous, question = check_ambiguity(context)
    if is_ambiguous:
        context.mark_failed(f"Ambiguous request. {question}")
        return context
    
    # Set TypeScript preference if specified
    if "tech:typescript" in context.modifiers:
        context.uses_typescript = True
    elif "tech:javascript" in context.modifiers:
        context.uses_typescript = False
    
    # Extract target directory if specified
    target_dir = extract_target_directory(context.user_request)
    if target_dir:
        context.component_dir = target_dir
    
    return context


# ============================================================================
# HELPER FUNCTIONS FOR TESTING
# ============================================================================

def classify_request(request: str) -> dict:
    """
    Utility function to test intent classification.
    
    Args:
        request: Natural language request
    
    Returns:
        dict with classification results
    """
    context = UIBuilderContext(user_request=request)
    context = analyze_intent(context)
    
    return {
        "intent": context.intent,
        "component_type": context.component_type,
        "modifiers": context.modifiers,
        "success": context.pipeline_status != "failed",
        "error": context.error_message
    }


if __name__ == "__main__":
    # Test examples
    test_requests = [
        "Create a login form with remember me",
        "Build a data table with sorting and filtering",
        "Generate a dark themed dashboard",
        "Add a registration form with OAuth",
        "Make a contact form",
    ]
    
    print("Stage 1: Intent Analysis - Test Results")
    print("=" * 60)
    
    for request in test_requests:
        result = classify_request(request)
        print(f"\nRequest: {request}")
        print(f"  Intent: {result['intent']}")
        print(f"  Type: {result['component_type']}")
        print(f"  Modifiers: {result['modifiers']}")
        print(f"  Success: {result['success']}")
        if result['error']:
            print(f"  Error: {result['error']}")
