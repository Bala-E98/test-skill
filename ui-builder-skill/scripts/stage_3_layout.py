"""
Stage 3: Layout Confirmation
=============================

Presents layout variants and confirms structure with user.

Based on Section 5.5 of the specification.
"""

from typing import List
from context import UIBuilderContext, LayoutField


# ============================================================================
# LAYOUT VARIANT DEFINITIONS
# ============================================================================

# Login Form Variants
LOGIN_VARIANTS = {
    "login-variant-a": {
        "name": "Minimal Login",
        "description": "Simple email and password with submit button",
        "fields": [
            {"id": "email", "label": "Email", "type": "text", "required": True},
            {"id": "password", "label": "Password", "type": "password", "required": True},
            {"id": "submit", "label": "Sign In", "type": "button", "required": True}
        ]
    },
    "login-variant-b": {
        "name": "Login with Remember Me",
        "description": "Email, password, remember me checkbox, and forgot password link",
        "fields": [
            {"id": "email", "label": "Email", "type": "text", "required": True},
            {"id": "password", "label": "Password", "type": "password", "required": True},
            {"id": "remember", "label": "Remember me", "type": "checkbox", "required": False},
            {"id": "submit", "label": "Sign In", "type": "button", "required": True},
            {"id": "forgot", "label": "Forgot password?", "type": "link", "required": False}
        ]
    },
    "login-variant-c": {
        "name": "Login with Social Options",
        "description": "Email/password plus Google, GitHub, Microsoft sign-in buttons",
        "fields": [
            {"id": "email", "label": "Email", "type": "text", "required": True},
            {"id": "password", "label": "Password", "type": "password", "required": True},
            {"id": "remember", "label": "Remember me", "type": "checkbox", "required": False},
            {"id": "submit", "label": "Sign In", "type": "button", "required": True},
            {"id": "divider", "label": "or", "type": "divider", "required": False},
            {"id": "google", "label": "Sign in with Google", "type": "button", "required": False},
            {"id": "github", "label": "Sign in with GitHub", "type": "button", "required": False}
        ]
    }
}

# Registration Form Variants
REGISTRATION_VARIANTS = {
    "registration-variant-a": {
        "name": "Simple Registration",
        "description": "Email, password, confirm password",
        "fields": [
            {"id": "email", "label": "Email", "type": "text", "required": True},
            {"id": "password", "label": "Password", "type": "password", "required": True},
            {"id": "confirm", "label": "Confirm Password", "type": "password", "required": True},
            {"id": "submit", "label": "Create Account", "type": "button", "required": True}
        ]
    },
    "registration-variant-b": {
        "name": "Registration with Profile",
        "description": "Email, password, name, and phone fields",
        "fields": [
            {"id": "name", "label": "Full Name", "type": "text", "required": True},
            {"id": "email", "label": "Email", "type": "text", "required": True},
            {"id": "phone", "label": "Phone Number", "type": "text", "required": False},
            {"id": "password", "label": "Password", "type": "password", "required": True},
            {"id": "confirm", "label": "Confirm Password", "type": "password", "required": True},
            {"id": "terms", "label": "I agree to the terms and conditions", "type": "checkbox", "required": True},
            {"id": "submit", "label": "Create Account", "type": "button", "required": True}
        ]
    }
}

# Data Table Variants
TABLE_VARIANTS = {
    "table-variant-a": {
        "name": "Simple Table",
        "description": "Read-only data display with pagination",
        "fields": [
            {"id": "column-id", "label": "ID", "type": "column", "required": True},
            {"id": "column-name", "label": "Name", "type": "column", "required": True},
            {"id": "column-email", "label": "Email", "type": "column", "required": True}
        ]
    },
    "table-variant-b": {
        "name": "Interactive Table",
        "description": "Sortable, filterable table with search",
        "fields": [
            {"id": "column-id", "label": "ID", "type": "column", "required": True},
            {"id": "column-name", "label": "Name", "type": "column", "required": True},
            {"id": "column-email", "label": "Email", "type": "column", "required": True},
            {"id": "column-status", "label": "Status", "type": "column", "required": True},
            {"id": "column-actions", "label": "Actions", "type": "column", "required": False}
        ]
    }
}

# Contact Form Variants
CONTACT_VARIANTS = {
    "contact-variant-a": {
        "name": "Basic Contact Form",
        "description": "Name, email, and message",
        "fields": [
            {"id": "name", "label": "Name", "type": "text", "required": True},
            {"id": "email", "label": "Email", "type": "text", "required": True},
            {"id": "message", "label": "Message", "type": "textarea", "required": True},
            {"id": "submit", "label": "Send Message", "type": "button", "required": True}
        ]
    }
}

# All variants combined
ALL_VARIANTS = {
    **LOGIN_VARIANTS,
    **REGISTRATION_VARIANTS,
    **TABLE_VARIANTS,
    **CONTACT_VARIANTS
}


# ============================================================================
# VARIANT SELECTION LOGIC
# ============================================================================

def select_variant(context: UIBuilderContext) -> str:
    """
    Auto-select best variant based on component type and modifiers.
    
    Phase 1 (MVP): Uses keyword matching only.
    Phase 2: Will use scoring algorithm.
    
    Returns:
        Variant ID (e.g., "login-variant-b")
    """
    component_type = context.component_type
    modifiers = context.modifiers
    
    # Login forms
    if component_type == "form/login":
        if "feature:oauth" in modifiers:
            return "login-variant-c"
        elif "feature:remember-me" in modifiers:
            return "login-variant-b"
        else:
            return "login-variant-a"
    
    # Registration forms
    elif component_type == "form/registration":
        if any(mod in modifiers for mod in ["feature:profile", "feature:phone"]):
            return "registration-variant-b"
        else:
            return "registration-variant-a"
    
    # Data tables
    elif component_type == "table/data":
        if any(mod in modifiers for mod in ["feature:sorting", "feature:filtering"]):
            return "table-variant-b"
        else:
            return "table-variant-a"
    
    # Contact forms
    elif component_type == "form/contact":
        return "contact-variant-a"
    
    # Default to first variant if component type not recognized
    return "login-variant-a"


def create_layout_fields(variant_data: dict) -> List[LayoutField]:
    """
    Convert variant field definitions to LayoutField objects.
    
    Args:
        variant_data: Variant dictionary with fields list
    
    Returns:
        List of LayoutField objects
    """
    fields = []
    for field_data in variant_data["fields"]:
        field = LayoutField(
            id=field_data["id"],
            label=field_data["label"],
            type=field_data["type"],
            required=field_data.get("required", False),
            placeholder=field_data.get("placeholder", "")
        )
        fields.append(field)
    
    return fields


# ============================================================================
# MAIN STAGE FUNCTION
# ============================================================================

def confirm_layout(context: UIBuilderContext) -> UIBuilderContext:
    """
    Stage 3: Select and confirm layout variant.
    
    For MVP (Phase 1): Auto-selects variant based on keywords.
    For Phase 2: Will present 2-3 options and allow user choice.
    
    Args:
        context: UIBuilderContext with component_type and modifiers set
    
    Returns:
        Updated context with selected_variant and layout_fields
    """
    context.current_stage = 3
    
    # Select variant
    variant_id = select_variant(context)
    
    # Validate variant exists
    if variant_id not in ALL_VARIANTS:
        context.mark_failed(f"Unknown variant: {variant_id}")
        return context
    
    variant_data = ALL_VARIANTS[variant_id]
    
    # Set context properties
    context.selected_variant = variant_id
    context.layout_fields = create_layout_fields(variant_data)
    context.layout_metadata = {
        "variant_name": variant_data["name"],
        "variant_description": variant_data["description"]
    }
    
    return context


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_layout_preview(context: UIBuilderContext) -> str:
    """
    Generate text preview of selected layout.
    
    Returns:
        ASCII art representation of layout
    """
    if not context.selected_variant:
        return "No variant selected"
    
    variant_name = context.layout_metadata.get("variant_name", "Unknown")
    
    preview = f"""
╔═══════════════════════════════════════════════════════╗
║  {variant_name.center(51)}  ║
╠═══════════════════════════════════════════════════════╣
"""
    
    for field in context.layout_fields:
        if field.type in ["text", "password"]:
            preview += f"║  {field.label:<20} [{'_' * 25}]  ║\n"
        elif field.type == "checkbox":
            preview += f"║  ☐ {field.label:<45}  ║\n"
        elif field.type == "button":
            preview += f"║  [ {field.label.center(47)} ]  ║\n"
        elif field.type == "link":
            preview += f"║  {field.label:<49}  ║\n"
        elif field.type == "divider":
            preview += f"║  {'─' * 20} {field.label} {'─' * 20}  ║\n"
        elif field.type == "textarea":
            preview += f"║  {field.label:<20}                         ║\n"
            preview += f"║  [{'_' * 47}]  ║\n"
    
    preview += "╚═══════════════════════════════════════════════════════╝"
    
    return preview


if __name__ == "__main__":
    # Test layout selection
    from stage_1_intent import analyze_intent
    
    test_requests = [
        "Create a login form with remember me",
        "Build a registration form with profile fields",
        "Generate a data table with sorting",
        "Make a contact form"
    ]
    
    print("Stage 3: Layout Confirmation - Test Results")
    print("=" * 60)
    
    for request in test_requests:
        # Stage 1: Intent
        context = UIBuilderContext(user_request=request)
        context = analyze_intent(context)
        
        # Stage 3: Layout
        context = confirm_layout(context)
        
        print(f"\nRequest: {request}")
        print(f"Selected: {context.selected_variant}")
        print(get_layout_preview(context))
