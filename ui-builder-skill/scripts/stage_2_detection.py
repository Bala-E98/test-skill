"""
Stage 2: Project Detection & Configuration
===========================================

Detects React project framework, TypeScript, CSS strategy, and component directory.

Based on Section 5.6 of the specification.
"""

import json
from pathlib import Path
from typing import Optional, Dict, Any
from context import UIBuilderContext, Framework, CSSStrategy


# ============================================================================
# PROJECT DETECTION FUNCTIONS
# ============================================================================

def detect_framework(project_path: Path, package_json: dict) -> str:
    """
    Detect React framework type.
    
    Returns:
        Framework enum value (nextjs-app, nextjs-pages, vite, cra)
    """
    dependencies = {
        **package_json.get("dependencies", {}),
        **package_json.get("devDependencies", {})
    }
    
    # Check for Next.js
    if "next" in dependencies:
        # Check for App Router (Next.js 13+)
        app_dir = project_path / "app"
        if app_dir.exists() and app_dir.is_dir():
            return Framework.NEXTJS_APP.value
        else:
            return Framework.NEXTJS_PAGES.value
    
    # Check for Vite
    elif "vite" in dependencies:
        return Framework.VITE.value
    
    # Default to Create React App
    else:
        return Framework.CRA.value


def detect_component_directory(framework: str, project_path: Path) -> str:
    """
    Determine standard component directory for framework.
    
    Returns:
        Relative path to component directory
    """
    if framework == Framework.NEXTJS_APP.value:
        return "app/components"
    elif framework == Framework.NEXTJS_PAGES.value:
        return "components"
    elif framework == Framework.VITE.value:
        return "src/components"
    else:  # CRA
        return "src/components"


def detect_typescript(project_path: Path) -> bool:
    """Check if project uses TypeScript"""
    tsconfig_path = project_path / "tsconfig.json"
    return tsconfig_path.exists()


def detect_css_strategy(package_json: dict) -> str:
    """
    Detect CSS styling strategy.
    
    Returns:
        CSSStrategy enum value (css-modules, tailwind, css-in-js, inline)
    """
    dependencies = {
        **package_json.get("dependencies", {}),
        **package_json.get("devDependencies", {})
    }
    
    # Check for Tailwind
    if "tailwindcss" in dependencies:
        return CSSStrategy.TAILWIND.value
    
    # Check for CSS-in-JS libraries
    css_in_js_libs = ["styled-components", "@emotion/react", "@emotion/styled", "styled-jsx"]
    if any(lib in dependencies for lib in css_in_js_libs):
        return CSSStrategy.CSS_IN_JS.value
    
    # Default to CSS Modules
    return CSSStrategy.CSS_MODULES.value


def detect_formatting_config(project_path: Path) -> Dict[str, Any]:
    """
    Read Prettier and ESLint configuration.
    
    Returns:
        Dict with formatting preferences
    """
    config = {
        "indentation": 2,
        "use_semicolons": True,
        "quote_style": "single",
        "use_tabs": False
    }
    
    # Try to read .prettierrc
    prettier_files = [
        ".prettierrc",
        ".prettierrc.json",
        ".prettierrc.js",
        "prettier.config.js"
    ]
    
    for filename in prettier_files:
        prettier_path = project_path / filename
        if prettier_path.exists():
            try:
                if filename.endswith(".json") or filename == ".prettierrc":
                    with open(prettier_path, 'r') as f:
                        prettier_config = json.load(f)
                        config["indentation"] = prettier_config.get("tabWidth", 2)
                        config["use_semicolons"] = prettier_config.get("semi", True)
                        config["quote_style"] = "single" if prettier_config.get("singleQuote", False) else "double"
                        config["use_tabs"] = prettier_config.get("useTabs", False)
                        break
            except:
                pass
    
    return config


def check_syncfusion_license(project_path: Path) -> Optional[str]:
    """
    Check if Syncfusion license key is configured.
    
    Returns:
        "found" if configured, None if not found
    """
    # Check .env files
    env_files = [".env", ".env.local", ".env.production"]
    
    for env_file in env_files:
        env_path = project_path / env_file
        if env_path.exists():
            with open(env_path, 'r') as f:
                content = f.read()
                if "SYNCFUSION_LICENSE_KEY" in content or "NEXT_PUBLIC_SYNCFUSION_LICENSE_KEY" in content:
                    return "found"
    
    # Check for registerLicense() call in source files
    src_dirs = ["app", "src", "pages"]
    for src_dir in src_dirs:
        src_path = project_path / src_dir
        if src_path.exists():
            for file_path in src_path.rglob("*.tsx"):
                try:
                    with open(file_path, 'r') as f:
                        if "registerLicense" in f.read():
                            return "found"
                except:
                    pass
    
    return None


# ============================================================================
# MAIN STAGE FUNCTION
# ============================================================================

def detect_project(context: UIBuilderContext) -> UIBuilderContext:
    """
    Stage 2: Detect project configuration.
    
    Scans project directory and detects:
    - Framework (Next.js App/Pages, Vite, CRA)
    - TypeScript usage
    - CSS strategy
    - Component directory
    - Formatting preferences
    - Syncfusion license status
    
    Args:
        context: UIBuilderContext with project_dir set
    
    Returns:
        Updated context with project configuration
    """
    context.current_stage = 2
    project_path = Path(context.project_dir)
    
    # Check if package.json exists
    package_json_path = project_path / "package.json"
    if not package_json_path.exists():
        context.mark_failed(
            "package.json not found. Please ensure this is a valid React project directory."
        )
        return context
    
    # Read package.json
    try:
        with open(package_json_path, 'r', encoding='utf-8') as f:
            package_json = json.load(f)
    except Exception as e:
        context.mark_failed(f"Failed to read package.json: {str(e)}")
        return context
    
    # Check for React dependency
    dependencies = {
        **package_json.get("dependencies", {}),
        **package_json.get("devDependencies", {})
    }
    
    if "react" not in dependencies:
        context.mark_failed(
            "React not found in dependencies. This skill requires a React 18+ project."
        )
        return context
    
    # Detect framework
    context.framework = detect_framework(project_path, package_json)
    
    # Detect component directory
    if not context.component_dir:  # Use user-specified dir if provided
        context.component_dir = detect_component_directory(context.framework, project_path)
    
    # Detect TypeScript
    context.uses_typescript = detect_typescript(project_path)
    
    # Detect CSS strategy
    context.css_strategy = detect_css_strategy(package_json)
    
    # Read formatting config
    context.formatting_config = detect_formatting_config(project_path)
    
    # Check Syncfusion license
    context.syncfusion_license_key = check_syncfusion_license(project_path)
    
    return context


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_detection_report(context: UIBuilderContext) -> str:
    """
    Generate human-readable detection report.
    
    Returns:
        Formatted report string
    """
    report = f"""
🔍 PROJECT DETECTION REPORT

Framework: {context.framework}
Language: {"TypeScript" if context.uses_typescript else "JavaScript"}
CSS Strategy: {context.css_strategy}
Component Directory: {context.component_dir}
Formatting:
  • Indentation: {context.formatting_config.get('indentation', 2)} spaces
  • Semicolons: {"Yes" if context.formatting_config.get('use_semicolons', True) else "No"}
  • Quotes: {context.formatting_config.get('quote_style', 'single')}

Syncfusion License: {"✓ Configured" if context.syncfusion_license_key else "⚠ Not found"}
"""
    return report


if __name__ == "__main__":
    # Test detection
    import sys
    
    if len(sys.argv) > 1:
        project_dir = sys.argv[1]
    else:
        project_dir = "."
    
    context = UIBuilderContext(
        user_request="test",
        project_dir=project_dir
    )
    
    context = detect_project(context)
    
    if context.pipeline_status == "failed":
        print(f"❌ Detection failed: {context.error_message}")
    else:
        print(get_detection_report(context))
