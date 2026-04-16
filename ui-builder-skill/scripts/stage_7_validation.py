"""
Stage 7: Web Standards Compliance Validation
=============================================

Validates generated code against WCAG 2.1 AA, security, and performance standards.

Based on Section 5.10 of the specification.
"""

import re
from context import UIBuilderContext, ValidationIssue


# ============================================================================
# VALIDATION RULES
# ============================================================================

def validate_accessibility(context: UIBuilderContext) -> list:
    """
    Validate WCAG 2.1 AA compliance.
    
    Returns:
        List of ValidationIssue objects
    """
    issues = []
    
    for file in context.generated_files:
        if file.type != "component":
            continue
        
        content = file.content
        
        # Check for semantic HTML
        if "<form" not in content and "form" in context.component_type:
            issues.append(ValidationIssue(
                code="A11Y001",
                severity="error",
                message="Forms should use <form> element for semantic HTML",
                file_path=file.path,
                auto_fixable=True
            ))
        
        # Check for button vs div clickable
        if re.search(r'<div[^>]*onClick', content):
            issues.append(ValidationIssue(
                code="A11Y002",
                severity="error",
                message="Use <button> element instead of <div> with onClick",
                file_path=file.path,
                auto_fixable=True
            ))
        
        # Check for label associations
        if "<input" in content:
            inputs_without_labels = re.findall(r'<input[^>]*id="([^"]+)"', content)
            for input_id in inputs_without_labels:
                if f'htmlFor="{input_id}"' not in content:
                    issues.append(ValidationIssue(
                        code="A11Y003",
                        severity="warning",
                        message=f"Input '{input_id}' should have associated label with htmlFor",
                        file_path=file.path,
                        auto_fixable=False
                    ))
        
        # Check for ARIA labels on icon buttons
        if "Button" in content and "aria-label" not in content:
            issues.append(ValidationIssue(
                code="A11Y004",
                severity="info",
                message="Consider adding aria-label to buttons for screen readers",
                file_path=file.path,
                auto_fixable=False
            ))
    
    return issues


def validate_security(context: UIBuilderContext) -> list:
    """
    Validate security best practices.
    
    Returns:
        List of ValidationIssue objects
    """
    issues = []
    
    for file in context.generated_files:
        if file.type != "component":
            continue
        
        content = file.content
        
        # Check for dangerouslySetInnerHTML
        if "dangerouslySetInnerHTML" in content:
            issues.append(ValidationIssue(
                code="SEC001",
                severity="error",
                message="Avoid dangerouslySetInnerHTML to prevent XSS attacks",
                file_path=file.path,
                auto_fixable=False
            ))
        
        # Check for eval()
        if re.search(r'\beval\s*\(', content):
            issues.append(ValidationIssue(
                code="SEC002",
                severity="error",
                message="Never use eval() - major security risk",
                file_path=file.path,
                auto_fixable=False
            ))
        
        # Check for hardcoded secrets (simple pattern)
        secret_patterns = [
            r'apiKey\s*=\s*["\'][^"\']{20,}["\']',
            r'password\s*=\s*["\'][^"\']+["\']',
            r'token\s*=\s*["\'][^"\']{20,}["\']'
        ]
        for pattern in secret_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                issues.append(ValidationIssue(
                    code="SEC003",
                    severity="warning",
                    message="Potential hardcoded secret detected. Use environment variables.",
                    file_path=file.path,
                    auto_fixable=False
                ))
        
        # Check for inline event handlers
        if re.search(r'on\w+="[^"]+"', content):
            issues.append(ValidationIssue(
                code="SEC004",
                severity="warning",
                message="Avoid inline event handlers. Use React event handlers.",
                file_path=file.path,
                auto_fixable=True
            ))
    
    return issues


def validate_performance(context: UIBuilderContext) -> list:
    """
    Validate performance best practices.
    
    Returns:
        List of ValidationIssue objects
    """
    issues = []
    
    for file in context.generated_files:
        if file.type != "component":
            continue
        
        content = file.content
        
        # Check for console.log in production
        if re.search(r'\bconsole\.(log|warn|error)', content):
            issues.append(ValidationIssue(
                code="PERF001",
                severity="warning",
                message="Remove console statements before production",
                file_path=file.path,
                auto_fixable=True
            ))
        
        # Check for inline styles (when CSS Modules available)
        if context.css_strategy == "css-modules" and re.search(r'style=\{\{', content):
            issues.append(ValidationIssue(
                code="PERF002",
                severity="info",
                message="Consider moving inline styles to CSS Module for better performance",
                file_path=file.path,
                auto_fixable=False
            ))
        
        # Check for large components (simple heuristic)
        if len(content.split('\n')) > 300:
            issues.append(ValidationIssue(
                code="PERF003",
                severity="info",
                message="Component is large (>300 lines). Consider splitting into smaller components.",
                file_path=file.path,
                auto_fixable=False
            ))
    
    return issues


def validate_code_quality(context: UIBuilderContext) -> list:
    """
    Validate code quality and best practices.
    
    Returns:
        List of ValidationIssue objects
    """
    issues = []
    
    for file in context.generated_files:
        if file.type != "component":
            continue
        
        content = file.content
        
        # Check for var usage
        if re.search(r'\bvar\s+\w+', content):
            issues.append(ValidationIssue(
                code="QUALITY001",
                severity="warning",
                message="Use const or let instead of var",
                file_path=file.path,
                auto_fixable=True
            ))
        
        # Check for missing PropTypes or TypeScript types
        if not context.uses_typescript and "PropTypes" not in content:
            issues.append(ValidationIssue(
                code="QUALITY002",
                severity="info",
                message="Consider adding PropTypes for runtime type checking",
                file_path=file.path,
                auto_fixable=False
            ))
        
        # Check for missing key prop in lists
        if re.search(r'\.map\([^)]+\)', content) and "key=" not in content:
            issues.append(ValidationIssue(
                code="QUALITY003",
                severity="warning",
                message="Add key prop when rendering lists with .map()",
                file_path=file.path,
                auto_fixable=False
            ))
    
    return issues


# ============================================================================
# MAIN STAGE FUNCTION
# ============================================================================

def validate_standards(context: UIBuilderContext) -> UIBuilderContext:
    """
    Stage 7: Validate web standards compliance.
    
    Checks generated code against:
    - WCAG 2.1 AA accessibility
    - Security best practices
    - Performance optimization
    - Code quality standards
    
    Args:
        context: UIBuilderContext with generated_files populated
    
    Returns:
        Updated context with validation_issues populated
    """
    context.current_stage = 7
    
    # Validate prerequisites
    if not context.generated_files:
        context.mark_failed("No generated files to validate. Stage 6 must complete first.")
        return context
    
    # Run all validations
    all_issues = []
    all_issues.extend(validate_accessibility(context))
    all_issues.extend(validate_security(context))
    all_issues.extend(validate_performance(context))
    all_issues.extend(validate_code_quality(context))
    
    context.validation_issues = all_issues
    
    # Check if there are blocking errors
    errors = [issue for issue in all_issues if issue.severity == "error"]
    
    if errors:
        context.validation_passed = False
        # Don't fail pipeline, but mark validation as not passed
    else:
        context.validation_passed = True
    
    return context


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_validation_report(context: UIBuilderContext) -> str:
    """
    Generate human-readable validation report.
    
    Returns:
        Formatted report string
    """
    errors = [i for i in context.validation_issues if i.severity == "error"]
    warnings = [i for i in context.validation_issues if i.severity == "warning"]
    info = [i for i in context.validation_issues if i.severity == "info"]
    
    report = f"""
✓ WEB STANDARDS COMPLIANCE REPORT

Component: {context.component_name}
Files Validated: {len(context.generated_files)}

═══════════════════════════════════════════════════════════

SUMMARY:
  Errors: {len(errors)} (blocking issues)
  Warnings: {len(warnings)} (recommended fixes)
  Info: {len(info)} (suggestions)

Overall Status: {"✓ PASS" if context.validation_passed else "✗ FAIL"}

═══════════════════════════════════════════════════════════
"""
    
    if errors:
        report += "\n❌ ERRORS (must fix):\n"
        for issue in errors:
            report += f"  [{issue.code}] {issue.message}\n"
            if issue.file_path:
                report += f"           File: {issue.file_path}\n"
    
    if warnings:
        report += "\n⚠️  WARNINGS (recommended):\n"
        for issue in warnings:
            report += f"  [{issue.code}] {issue.message}\n"
    
    if info:
        report += "\nℹ️  SUGGESTIONS:\n"
        for issue in info:
            report += f"  [{issue.code}] {issue.message}\n"
    
    if not errors and not warnings and not info:
        report += "\n✨ No issues found! Code meets all standards.\n"
    
    return report


if __name__ == "__main__":
    # Test validation
    from stage_1_intent import analyze_intent
    from stage_3_layout import confirm_layout
    from stage_4_components import pick_components
    from stage_5_preview import generate_preview
    from stage_6_codegen import generate_code
    
    test_request = "Create a login form"
    
    print("Stage 7: Web Standards Validation - Test Results")
    print("=" * 60)
    
    # Stages 1-6
    context = UIBuilderContext(user_request=test_request)
    context = analyze_intent(context)
    context.framework = "nextjs-app"
    context.component_dir = "app/components"
    context = confirm_layout(context)
    context = pick_components(context)
    context = generate_preview(context)
    context = generate_code(context)
    
    # Stage 7
    context = validate_standards(context)
    
    print(get_validation_report(context))
