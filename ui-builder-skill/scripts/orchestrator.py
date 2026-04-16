#!/usr/bin/env python3
"""
UI Builder Skill - Main Orchestrator
=====================================

Coordinates execution of all 9 stages in the UI generation pipeline.

Usage:
    python orchestrator.py --request "Create a login form" --project-dir ./my-app

Output:
    JSON result with generated files and status
"""

import sys
import json
import argparse
from pathlib import Path

# Import individual stage modules (will be created separately)
try:
    from stage_1_intent import analyze_intent
    from stage_2_detection import detect_project
    from stage_3_layout import confirm_layout
    from stage_4_components import pick_components
    from stage_5_preview import generate_preview
    from stage_6_codegen import generate_code
    from stage_7_validation import validate_standards
    from stage_8_dependencies import manage_dependencies
    from stage_9_insertion import insert_code
    from context import UIBuilderContext
except ImportError as e:
    print(f"Error importing stage modules: {e}", file=sys.stderr)
    print("Make sure all stage files are in the scripts/ directory", file=sys.stderr)
    sys.exit(1)


def run_pipeline(user_request: str, project_dir: str, dry_run: bool = False):
    """
    Execute all 9 stages sequentially.
    
    Args:
        user_request: Natural language component request
        project_dir: Path to React project
        dry_run: If True, preview only (don't write files)
    
    Returns:
        dict: Result with status, files, and any errors
    """
    # Initialize context
    context = UIBuilderContext(
        user_request=user_request,
        project_dir=project_dir
    )
    
    # Define all 9 stages
    stages = [
        (1, "Intent Analysis & Setup", analyze_intent),
        (2, "Project Detection & Configuration", detect_project),
        (3, "Layout Confirmation", confirm_layout),
        (4, "Component Picking", pick_components),
        (5, "Preview Generation", generate_preview),
        (6, "Code Generation", generate_code),
        (7, "Web Standards Validation", validate_standards),
        (8, "Dependency Management", manage_dependencies),
        (9, "Code Insertion/Integration", insert_code if not dry_run else lambda ctx: ctx)
    ]
    
    # Execute stages sequentially
    for stage_id, stage_name, stage_func in stages:
        try:
            print(f"→ Stage {stage_id}: {stage_name}...", file=sys.stderr)
            
            # Execute stage function
            context = stage_func(context)
            
            # Check if stage failed
            if context.pipeline_status == "failed":
                print(f"✗ Stage {stage_id} failed: {context.error_message}", file=sys.stderr)
                break
            
            print(f"✓ Stage {stage_id} complete", file=sys.stderr)
        
        except Exception as e:
            context.pipeline_status = "failed"
            context.error_message = f"Stage {stage_id} ({stage_name}) error: {str(e)}"
            print(f"✗ {context.error_message}", file=sys.stderr)
            break
    
    # Build result
    result = {
        "status": context.pipeline_status,
        "intent": context.intent,
        "component_type": context.component_type,
        "framework": context.framework,
        "selected_variant": context.selected_variant,
        "generated_files": [f["path"] for f in context.generated_files],
        "inserted_files": context.inserted_files,
        "validation_issues": [
            {
                "code": issue["code"],
                "severity": issue["severity"],
                "message": issue["message"]
            }
            for issue in context.validation_issues
        ],
        "required_packages": context.required_packages,
        "error": context.error_message
    }
    
    return result


def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description="UI Builder Skill - Generate production-ready React components",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python orchestrator.py --request "Create a login form" --project-dir ./my-app
  python orchestrator.py --request "Build a data table with sorting" --project-dir ~/dashboard
  python orchestrator.py --request "Create a login form" --dry-run

For detailed documentation, see: references/REFERENCE.md
        """
    )
    
    parser.add_argument(
        "--request",
        required=True,
        help="Natural language component request (e.g., 'Create a login form with remember me')"
    )
    
    parser.add_argument(
        "--project-dir",
        default=".",
        help="Path to React project directory (default: current directory)"
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be generated without writing files"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed progress information"
    )
    
    args = parser.parse_args()
    
    # Validate project directory exists
    project_path = Path(args.project_dir)
    if not project_path.exists():
        print(f"Error: Project directory not found: {args.project_dir}", file=sys.stderr)
        sys.exit(1)
    
    # Run pipeline
    print(f"\n🚀 UI Builder Skill - Starting pipeline", file=sys.stderr)
    print(f"   Request: {args.request}", file=sys.stderr)
    print(f"   Project: {args.project_dir}\n", file=sys.stderr)
    
    result = run_pipeline(args.request, args.project_dir, args.dry_run)
    
    # Print result summary to stderr
    print(f"\n{'='*60}", file=sys.stderr)
    if result["status"] == "completed":
        print(f"✅ SUCCESS - Component generated", file=sys.stderr)
        print(f"\n📁 Generated files:", file=sys.stderr)
        for file_path in result["generated_files"]:
            print(f"   • {file_path}", file=sys.stderr)
        
        if result["validation_issues"]:
            print(f"\n⚠️  Validation warnings: {len(result['validation_issues'])}", file=sys.stderr)
        
        if result["required_packages"]:
            print(f"\n📦 Install required packages:", file=sys.stderr)
            for pkg in result["required_packages"]:
                print(f"   npm install {pkg}", file=sys.stderr)
    else:
        print(f"❌ FAILED - {result['error']}", file=sys.stderr)
    print(f"{'='*60}\n", file=sys.stderr)
    
    # Output JSON result to stdout
    print(json.dumps(result, indent=2))
    
    # Exit with appropriate code
    sys.exit(0 if result["status"] == "completed" else 1)


if __name__ == "__main__":
    main()
