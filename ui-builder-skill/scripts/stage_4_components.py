"""
Stage 4: Component Picking
===========================

Maps layout fields to Syncfusion components.

Based on Section 5.7 of the specification.
"""

from context import UIBuilderContext, ComponentMapping, LayoutField


# ============================================================================
# SYNCFUSION COMPONENT CATALOG
# ============================================================================

# Maps field types to Syncfusion components
COMPONENT_MAP = {
    "text": {
        "component": "TextBoxComponent",
        "package": "@syncfusion/ej2-react-inputs",
        "description": "Standard text input with validation support"
    },
    "password": {
        "component": "TextBoxComponent",
        "package": "@syncfusion/ej2-react-inputs",
        "description": "Password input with masking"
    },
    "email": {
        "component": "TextBoxComponent",
        "package": "@syncfusion/ej2-react-inputs",
        "description": "Email input with validation"
    },
    "checkbox": {
        "component": "CheckBoxComponent",
        "package": "@syncfusion/ej2-react-buttons",
        "description": "Checkbox for boolean selections"
    },
    "button": {
        "component": "ButtonComponent",
        "package": "@syncfusion/ej2-react-buttons",
        "description": "Primary action button"
    },
    "textarea": {
        "component": "TextBoxComponent",
        "package": "@syncfusion/ej2-react-inputs",
        "description": "Multi-line text input"
    },
    "dropdown": {
        "component": "DropDownListComponent",
        "package": "@syncfusion/ej2-react-dropdowns",
        "description": "Dropdown selection list"
    },
    "datepicker": {
        "component": "DatePickerComponent",
        "package": "@syncfusion/ej2-react-calendars",
        "description": "Date selection calendar"
    },
    "column": {
        "component": "ColumnDirective",
        "package": "@syncfusion/ej2-react-grids",
        "description": "Data grid column"
    }
}

# Special mappings (not Syncfusion components)
NATIVE_COMPONENTS = {
    "link": {
        "component": "a",
        "package": None,
        "description": "Native anchor tag"
    },
    "divider": {
        "component": "hr",
        "package": None,
        "description": "Native horizontal rule"
    }
}


# ============================================================================
# COMPONENT MAPPING FUNCTIONS
# ============================================================================

def map_field_to_component(field: LayoutField) -> ComponentMapping:
    """
    Map a layout field to appropriate Syncfusion component.
    
    Args:
        field: LayoutField to map
    
    Returns:
        ComponentMapping with component details
    """
    field_type = field.type
    
    # Check if it's a native component
    if field_type in NATIVE_COMPONENTS:
        comp_info = NATIVE_COMPONENTS[field_type]
        return ComponentMapping(
            field_id=field.id,
            component=comp_info["component"],
            package=comp_info["package"],
            props={},
            selected_by_user=False
        )
    
    # Map to Syncfusion component
    if field_type in COMPONENT_MAP:
        comp_info = COMPONENT_MAP[field_type]
        
        # Build default props
        props = {
            "placeholder": field.placeholder or f"Enter {field.label.lower()}",
            "required": field.required
        }
        
        # Special props for password
        if field_type == "password":
            props["type"] = "password"
        
        # Special props for textarea
        if field_type == "textarea":
            props["multiline"] = True
        
        return ComponentMapping(
            field_id=field.id,
            component=comp_info["component"],
            package=comp_info["package"],
            props=props,
            selected_by_user=False
        )
    
    # Fallback to TextBox for unknown types
    return ComponentMapping(
        field_id=field.id,
        component="TextBoxComponent",
        package="@syncfusion/ej2-react-inputs",
        props={"placeholder": field.placeholder or field.label},
        selected_by_user=False
    )


def extract_required_packages(mappings: list) -> list:
    """
    Extract unique list of required npm packages.
    
    Args:
        mappings: List of ComponentMapping objects
    
    Returns:
        List of unique package names
    """
    packages = set()
    for mapping in mappings:
        if mapping.package:  # Skip None (native components)
            packages.add(mapping.package)
    
    return sorted(list(packages))


# ============================================================================
# MAIN STAGE FUNCTION
# ============================================================================

def pick_components(context: UIBuilderContext) -> UIBuilderContext:
    """
    Stage 4: Map layout fields to Syncfusion components.
    
    For each field in the confirmed layout, selects the appropriate
    Syncfusion component and configures default props.
    
    Args:
        context: UIBuilderContext with layout_fields populated
    
    Returns:
        Updated context with component_mappings and required_packages
    """
    context.current_stage = 4
    
    # Validate layout fields exist
    if not context.layout_fields:
        context.mark_failed("No layout fields to map. Stage 3 must complete first.")
        return context
    
    # Map each field to a component
    mappings = []
    for field in context.layout_fields:
        mapping = map_field_to_component(field)
        mappings.append(mapping)
    
    context.component_mappings = mappings
    
    # Extract required packages
    context.required_packages = extract_required_packages(mappings)
    
    # Add base package if not already present
    if "@syncfusion/ej2-base" not in context.required_packages:
        context.required_packages.insert(0, "@syncfusion/ej2-base")
    
    return context


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_component_mapping_report(context: UIBuilderContext) -> str:
    """
    Generate human-readable component mapping report.
    
    Returns:
        Formatted report string
    """
    if not context.component_mappings:
        return "No component mappings"
    
    report = f"""
✓ Component Mapping - {context.selected_variant}

Field → Component Mappings:
"""
    
    for mapping in context.component_mappings:
        # Find the original field
        field = next((f for f in context.layout_fields if f.id == mapping.field_id), None)
        if field:
            if mapping.package:
                report += f"  • {field.label:<20} → {mapping.component:<25} ({mapping.package})\n"
            else:
                report += f"  • {field.label:<20} → <{mapping.component}> (native HTML)\n"
    
    report += f"\nRequired Packages ({len(context.required_packages)}):\n"
    for pkg in context.required_packages:
        report += f"  • {pkg}\n"
    
    return report


if __name__ == "__main__":
    # Test component picking
    from stage_1_intent import analyze_intent
    from stage_3_layout import confirm_layout
    
    test_request = "Create a login form with remember me"
    
    print("Stage 4: Component Picking - Test Results")
    print("=" * 60)
    
    # Stages 1-3
    context = UIBuilderContext(user_request=test_request)
    context = analyze_intent(context)
    context = confirm_layout(context)
    
    # Stage 4
    context = pick_components(context)
    
    print(get_component_mapping_report(context))
