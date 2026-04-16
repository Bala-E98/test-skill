"""
Stage 5: Preview Generation
============================

Generates preview/skeleton of component before code insertion.

Based on Section 5.8 of the specification.
"""

from context import UIBuilderContext


# ============================================================================
# PREVIEW GENERATION FUNCTIONS
# ============================================================================

def generate_ascii_preview(context: UIBuilderContext) -> str:
    """
    Generate ASCII art preview of the component.
    
    Used as fallback when webview/HTML file not available.
    
    Returns:
        ASCII art representation
    """
    component_name = context.layout_metadata.get("variant_name", "Component")
    
    preview = f"""
╔══════════════════════════════════════════════════════════════╗
║  {component_name.center(60)}  ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
"""
    
    for field in context.layout_fields:
        if field.type in ["text", "password", "email"]:
            label = field.label + (" *" if field.required else "")
            preview += f"║  {label:<25}                                 ║\n"
            preview += f"║  [{field.placeholder or 'Enter ' + field.label.lower():^56}]  ║\n"
            preview += "║                                                              ║\n"
        
        elif field.type == "textarea":
            label = field.label + (" *" if field.required else "")
            preview += f"║  {label:<58}  ║\n"
            preview += f"║  ┌{'─' * 56}┐  ║\n"
            preview += f"║  │{' ' * 56}│  ║\n"
            preview += f"║  │{' ' * 56}│  ║\n"
            preview += f"║  │{' ' * 56}│  ║\n"
            preview += f"║  └{'─' * 56}┘  ║\n"
            preview += "║                                                              ║\n"
        
        elif field.type == "checkbox":
            preview += f"║  ☐ {field.label:<55}  ║\n"
            preview += "║                                                              ║\n"
        
        elif field.type == "button":
            preview += f"║  ┌{'─' * 56}┐  ║\n"
            preview += f"║  │{field.label.center(56)}│  ║\n"
            preview += f"║  └{'─' * 56}┘  ║\n"
            preview += "║                                                              ║\n"
        
        elif field.type == "link":
            preview += f"║  {field.label:<58}  ║\n"
            preview += "║                                                              ║\n"
        
        elif field.type == "divider":
            preview += f"║  {'─' * 25} {field.label} {'─' * 25}  ║\n"
            preview += "║                                                              ║\n"
    
    preview += "╚══════════════════════════════════════════════════════════════╝\n"
    
    # Add accessibility notes
    preview += """
Accessibility Features:
  ✓ Semantic HTML structure (<form>, <input>, <button>)
  ✓ ARIA labels and descriptions
  ✓ Keyboard navigation support (tab order)
  ✓ Focus indicators (visible on all interactive elements)
  ✓ Required field indicators (*)
  ✓ Error message associations (aria-describedby)

Responsive Breakpoints:
  • Mobile: 320px - 767px (stacked layout)
  • Tablet: 768px - 1023px (optimized for touch)
  • Desktop: 1024px+ (full layout)

Color Contrast: WCAG 2.1 AA compliant (≥ 4.5:1)
"""
    
    return preview


def generate_html_preview(context: UIBuilderContext) -> str:
    """
    Generate self-contained HTML preview.
    
    Used for html-file and webview delivery mechanisms.
    
    Returns:
        Complete HTML document
    """
    component_name = context.component_name or "Component"
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{component_name} Preview - UI Builder</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: #f5f5f5;
            padding: 2rem;
            color: #333;
        }}
        
        .container {{
            max-width: 400px;
            margin: 0 auto;
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        h1 {{
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
            text-align: center;
        }}
        
        .field-group {{
            margin-bottom: 1rem;
        }}
        
        label {{
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
            font-size: 0.875rem;
        }}
        
        .required {{
            color: #d32f2f;
        }}
        
        input[type="text"],
        input[type="password"],
        input[type="email"],
        textarea {{
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
            transition: border-color 0.2s;
        }}
        
        input:focus,
        textarea:focus {{
            outline: none;
            border-color: #1976d2;
            box-shadow: 0 0 0 3px rgba(25, 118, 210, 0.1);
        }}
        
        textarea {{
            min-height: 100px;
            resize: vertical;
        }}
        
        .checkbox-group {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        
        input[type="checkbox"] {{
            width: 18px;
            height: 18px;
            cursor: pointer;
        }}
        
        button {{
            width: 100%;
            padding: 0.75rem;
            background: #1976d2;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: background 0.2s;
        }}
        
        button:hover {{
            background: #1565c0;
        }}
        
        button:focus {{
            outline: none;
            box-shadow: 0 0 0 3px rgba(25, 118, 210, 0.3);
        }}
        
        .link {{
            color: #1976d2;
            text-decoration: none;
            font-size: 0.875rem;
        }}
        
        .link:hover {{
            text-decoration: underline;
        }}
        
        .divider {{
            display: flex;
            align-items: center;
            text-align: center;
            margin: 1.5rem 0;
            color: #666;
            font-size: 0.875rem;
        }}
        
        .divider::before,
        .divider::after {{
            content: '';
            flex: 1;
            border-bottom: 1px solid #ddd;
        }}
        
        .divider span {{
            padding: 0 1rem;
        }}
        
        .info {{
            margin-top: 2rem;
            padding: 1rem;
            background: #e3f2fd;
            border-radius: 4px;
            font-size: 0.875rem;
        }}
        
        .info h3 {{
            font-size: 1rem;
            margin-bottom: 0.5rem;
            color: #1976d2;
        }}
        
        .info ul {{
            list-style-position: inside;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{context.layout_metadata.get('variant_name', component_name)}</h1>
        <form>
"""
    
    # Generate fields
    for field in context.layout_fields:
        if field.type in ["text", "password", "email"]:
            html += f"""
            <div class="field-group">
                <label for="{field.id}">
                    {field.label}
                    {'<span class="required">*</span>' if field.required else ''}
                </label>
                <input 
                    type="{field.type}" 
                    id="{field.id}"
                    placeholder="{field.placeholder or 'Enter ' + field.label.lower()}"
                    {'required' if field.required else ''}
                />
            </div>
"""
        
        elif field.type == "textarea":
            html += f"""
            <div class="field-group">
                <label for="{field.id}">
                    {field.label}
                    {'<span class="required">*</span>' if field.required else ''}
                </label>
                <textarea 
                    id="{field.id}"
                    placeholder="{field.placeholder or 'Enter ' + field.label.lower()}"
                    {'required' if field.required else ''}
                ></textarea>
            </div>
"""
        
        elif field.type == "checkbox":
            html += f"""
            <div class="field-group checkbox-group">
                <input type="checkbox" id="{field.id}" />
                <label for="{field.id}">{field.label}</label>
            </div>
"""
        
        elif field.type == "button":
            html += f"""
            <div class="field-group">
                <button type="submit">{field.label}</button>
            </div>
"""
        
        elif field.type == "link":
            html += f"""
            <div class="field-group">
                <a href="#" class="link">{field.label}</a>
            </div>
"""
        
        elif field.type == "divider":
            html += f"""
            <div class="divider">
                <span>{field.label}</span>
            </div>
"""
    
    html += """
        </form>
    </div>
    
    <div class="container info">
        <h3>Preview Information</h3>
        <ul>
            <li>This is a preview of the generated component</li>
            <li>Actual component will use Syncfusion components</li>
            <li>WCAG 2.1 AA accessibility compliance included</li>
            <li>Responsive design for mobile, tablet, and desktop</li>
        </ul>
    </div>
</body>
</html>
"""
    
    return html


# ============================================================================
# MAIN STAGE FUNCTION
# ============================================================================

def generate_preview(context: UIBuilderContext) -> UIBuilderContext:
    """
    Stage 5: Generate component preview.
    
    Generates both ASCII and HTML previews. The orchestrator or user
    interface can choose which to display based on capabilities.
    
    Args:
        context: UIBuilderContext with layout and components defined
    
    Returns:
        Updated context with preview_html populated
    """
    context.current_stage = 5
    
    # Validate prerequisites
    if not context.layout_fields:
        context.mark_failed("No layout fields. Stage 3 must complete first.")
        return context
    
    # Set component name if not already set
    if not context.component_name:
        if context.component_type:
            # Extract component name from type (e.g., "form/login" -> "LoginForm")
            type_parts = context.component_type.split("/")
            if len(type_parts) == 2:
                context.component_name = type_parts[1].title().replace("-", "") + type_parts[0].title()
        else:
            context.component_name = "Component"
    
    # Generate ASCII preview (always available)
    ascii_preview = generate_ascii_preview(context)
    
    # Generate HTML preview (for webview/file)
    html_preview = generate_html_preview(context)
    
    # Store both in context
    context.preview_html = html_preview
    
    # For MVP, auto-approve preview
    context.preview_approved = True
    
    # Also print ASCII to stderr for visibility
    import sys
    print("\n" + ascii_preview, file=sys.stderr)
    
    return context


if __name__ == "__main__":
    # Test preview generation
    from stage_1_intent import analyze_intent
    from stage_3_layout import confirm_layout
    from stage_4_components import pick_components
    
    test_request = "Create a login form with remember me"
    
    print("Stage 5: Preview Generation - Test Results")
    print("=" * 60)
    
    # Stages 1-4
    context = UIBuilderContext(user_request=test_request)
    context = analyze_intent(context)
    context = confirm_layout(context)
    context = pick_components(context)
    
    # Stage 5
    context = generate_preview(context)
    
    print(f"\nComponent Name: {context.component_name}")
    print(f"Preview Generated: {'Yes' if context.preview_html else 'No'}")
    print(f"Preview Approved: {context.preview_approved}")
