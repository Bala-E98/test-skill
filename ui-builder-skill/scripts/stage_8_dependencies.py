"""
Stage 8: Dependency Management
===============================

Manages npm package installation for Syncfusion components.

Based on specification requirements.
"""

import json
import subprocess
from pathlib import Path
from context import UIBuilderContext, DependencyEntry


# ============================================================================
# DEPENDENCY DETECTION
# ============================================================================

def check_installed_packages(project_dir: str) -> dict:
    """
    Read package.json to see what's already installed.
    
    Returns:
        Dict of {package_name: version}
    """
    package_json_path = Path(project_dir) / "package.json"
    
    if not package_json_path.exists():
        return {}
    
    try:
        with open(package_json_path, 'r') as f:
            package_json = json.load(f)
        
        installed = {}
        installed.update(package_json.get("dependencies", {}))
        installed.update(package_json.get("devDependencies", {}))
        
        return installed
    except:
        return {}


def resolve_dependency_versions(required_packages: list) -> list:
    """
    Resolve appropriate versions for required packages.
    
    Args:
        required_packages: List of package names
    
    Returns:
        List of DependencyEntry objects
    """
    dependencies = []
    
    # Syncfusion package version (latest stable)
    syncfusion_version = "^25.1.35"  # Update as needed
    
    for package in required_packages:
        if package.startswith("@syncfusion/"):
            dependencies.append(DependencyEntry(
                package=package,
                version=syncfusion_version,
                installed=False,
                peer_deps={"react": "^18.0.0", "react-dom": "^18.0.0"}
            ))
        else:
            # Non-Syncfusion packages (shouldn't happen in this skill)
            dependencies.append(DependencyEntry(
                package=package,
                version="latest",
                installed=False
            ))
    
    return dependencies


def check_conflicts(context: UIBuilderContext, installed: dict) -> list:
    """
    Check for version conflicts with existing packages.
    
    Args:
        context: UIBuilderContext with dependencies
        installed: Dict of currently installed packages
    
    Returns:
        List of conflict dicts
    """
    conflicts = []
    
    for dep in context.dependencies:
        if dep.package in installed:
            current_version = installed[dep.package]
            required_version = dep.version
            
            # Simple conflict detection (exact match or range)
            if not (current_version.startswith(required_version.lstrip("^~")) or 
                    required_version in ["latest", "*"]):
                conflicts.append({
                    "package": dep.package,
                    "current": current_version,
                    "required": required_version,
                    "resolution": "upgrade"  # or "keep" or "compromise"
                })
    
    return conflicts


# ============================================================================
# PACKAGE INSTALLATION
# ============================================================================

def install_packages(context: UIBuilderContext, dry_run: bool = False) -> tuple:
    """
    Install required npm packages.
    
    Args:
        context: UIBuilderContext with required_packages
        dry_run: If True, don't actually run npm install
    
    Returns:
        (success: bool, message: str)
    """
    if not context.required_packages:
        return True, "No packages to install"
    
    packages_to_install = [
        f"{dep.package}@{dep.version}"
        for dep in context.dependencies
        if not dep.installed
    ]
    
    if not packages_to_install:
        return True, "All packages already installed"
    
    if dry_run:
        return True, f"Would install: {', '.join(packages_to_install)}"
    
    # Detect package manager
    project_path = Path(context.project_dir)
    if (project_path / "yarn.lock").exists():
        cmd = ["yarn", "add"] + packages_to_install
    elif (project_path / "pnpm-lock.yaml").exists():
        cmd = ["pnpm", "add"] + packages_to_install
    else:
        cmd = ["npm", "install"] + packages_to_install
    
    try:
        result = subprocess.run(
            cmd,
            cwd=context.project_dir,
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        if result.returncode == 0:
            return True, f"Successfully installed {len(packages_to_install)} packages"
        else:
            return False, f"Installation failed: {result.stderr}"
    
    except subprocess.TimeoutExpired:
        return False, "Installation timeout (5 minutes)"
    except FileNotFoundError:
        return False, "npm/yarn/pnpm not found. Please install Node.js package manager."
    except Exception as e:
        return False, f"Installation error: {str(e)}"


# ============================================================================
# MAIN STAGE FUNCTION
# ============================================================================

def manage_dependencies(context: UIBuilderContext) -> UIBuilderContext:
    """
    Stage 8: Manage npm dependencies.
    
    Steps:
    1. Check what's already installed
    2. Resolve versions for required packages
    3. Check for conflicts
    4. Install missing packages
    
    Args:
        context: UIBuilderContext with required_packages populated
    
    Returns:
        Updated context with dependencies installed
    """
    context.current_stage = 8
    
    # Validate prerequisites
    if not context.required_packages:
        # Not an error - some components might not need extra packages
        return context
    
    # Check currently installed packages
    installed = check_installed_packages(context.project_dir)
    
    # Resolve dependency versions
    context.dependencies = resolve_dependency_versions(context.required_packages)
    
    # Mark already installed packages
    for dep in context.dependencies:
        if dep.package in installed:
            dep.installed = True
    
    # Check for version conflicts
    context.conflicts = check_conflicts(context, installed)
    
    # Install packages (in production - for now, just report)
    # Note: Actual installation should be done carefully in production
    # For MVP, we'll just prepare the list
    
    import sys
    print(f"\n📦 Dependency Management:", file=sys.stderr)
    print(f"   Required packages: {len(context.required_packages)}", file=sys.stderr)
    print(f"   Already installed: {sum(1 for d in context.dependencies if d.installed)}", file=sys.stderr)
    print(f"   To install: {sum(1 for d in context.dependencies if not d.installed)}", file=sys.stderr)
    
    if context.conflicts:
        print(f"   ⚠️  Version conflicts: {len(context.conflicts)}", file=sys.stderr)
    
    return context


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_dependency_report(context: UIBuilderContext) -> str:
    """
    Generate human-readable dependency report.
    
    Returns:
        Formatted report string
    """
    report = f"""
📦 DEPENDENCY MANAGEMENT REPORT

Total Required Packages: {len(context.required_packages)}

"""
    
    if context.dependencies:
        report += "Package Details:\n"
        for dep in context.dependencies:
            status = "✓ Installed" if dep.installed else "⏳ To install"
            report += f"  • {dep.package}@{dep.version} - {status}\n"
    
    if context.conflicts:
        report += f"\n⚠️  Version Conflicts ({len(context.conflicts)}):\n"
        for conflict in context.conflicts:
            report += f"  • {conflict['package']}: {conflict['current']} → {conflict['required']}\n"
            report += f"    Resolution: {conflict['resolution']}\n"
    
    report += "\nInstallation Command:\n"
    packages_to_install = [dep.package for dep in context.dependencies if not dep.installed]
    if packages_to_install:
        report += f"  npm install {' '.join(packages_to_install)}\n"
    else:
        report += "  (no installation needed)\n"
    
    return report


if __name__ == "__main__":
    # Test dependency management
    import sys
    
    if len(sys.argv) > 1:
        project_dir = sys.argv[1]
    else:
        project_dir = "."
    
    # Mock context
    context = UIBuilderContext(
        user_request="test",
        project_dir=project_dir
    )
    context.required_packages = [
        "@syncfusion/ej2-react-inputs",
        "@syncfusion/ej2-react-buttons",
        "@syncfusion/ej2-base"
    ]
    
    context = manage_dependencies(context)
    
    print(get_dependency_report(context))
