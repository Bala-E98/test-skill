"""
UI Builder Context - Unified State Schema
==========================================

Single source of truth passed through all 9 stages.
Each stage reads from and writes to this context object.

Based on Section 2.6 of the specification.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from enum import Enum


# ============================================================================
# ENUMS & CONSTANTS
# ============================================================================

class Intent(str, Enum):
    """User intent classification"""
    GENERATE_COMPONENT = "generate_component"
    GENERATE_PAGE = "generate_page"
    MODIFY_COMPONENT = "modify_component"
    UNKNOWN = "unknown"


class PipelineStatus(str, Enum):
    """Pipeline execution status"""
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class Framework(str, Enum):
    """Supported React frameworks"""
    NEXTJS_APP = "nextjs-app"           # Next.js 13+ App Router
    NEXTJS_PAGES = "nextjs-pages"       # Next.js Pages Router
    VITE = "vite"                       # Vite
    CRA = "cra"                         # Create React App


class CSSStrategy(str, Enum):
    """CSS styling approaches"""
    CSS_MODULES = "css-modules"
    TAILWIND = "tailwind"
    CSS_IN_JS = "css-in-js"
    INLINE = "inline"


# ============================================================================
# DATA MODELS
# ============================================================================

@dataclass
class LayoutField:
    """Represents a single field/element in the layout"""
    id: str                     # Unique identifier (e.g., "email", "password")
    label: str                  # Display label
    type: str                   # Field type (text, password, checkbox, button, etc.)
    required: bool = False      # Whether field is required
    placeholder: str = ""       # Placeholder text
    validation: Dict[str, Any] = field(default_factory=dict)  # Validation rules


@dataclass
class ComponentMapping:
    """Maps a layout field to a Syncfusion component"""
    field_id: str               # References LayoutField.id
    component: str              # Syncfusion component name (e.g., "TextBoxComponent")
    package: str                # npm package (e.g., "@syncfusion/ej2-react-inputs")
    props: Dict[str, Any] = field(default_factory=dict)  # Component props
    selected_by_user: bool = False  # True if user manually selected this component


@dataclass
class GeneratedFile:
    """Represents a generated code file"""
    path: str                   # Relative path from project root
    content: str                # File content
    type: str                   # File type: component, stylesheet, index, test
    language: str = "typescript"  # typescript, javascript, css


@dataclass
class ValidationIssue:
    """Represents a standards compliance issue"""
    code: str                   # Issue code (e.g., "A11Y001", "SEC002")
    severity: str               # error, warning, info
    message: str                # Human-readable description
    file_path: Optional[str] = None  # Affected file
    auto_fixable: bool = False  # Whether skill can auto-fix


@dataclass
class DependencyEntry:
    """Represents a required npm package"""
    package: str                # Package name
    version: str                # Version constraint
    installed: bool = False     # Whether already installed
    peer_deps: Dict[str, str] = field(default_factory=dict)  # Peer dependencies


# ============================================================================
# MAIN CONTEXT CLASS
# ============================================================================

@dataclass
class UIBuilderContext:
    """
    Unified state object for the UI Builder pipeline.
    
    Initialized in Stage 1 and enriched by each subsequent stage.
    All stages receive this context as input and return updated context.
    """
    
    # ── INPUTS (provided by user/orchestrator) ──────────────────────────
    user_request: str           # Original natural language request
    project_dir: str = "."      # Path to React project
    
    # ── STAGE 1: Intent Analysis ────────────────────────────────────────
    intent: str = Intent.UNKNOWN.value  # Classified intent
    component_type: Optional[str] = None  # e.g., "form/login", "table/data"
    modifiers: List[str] = field(default_factory=list)  # e.g., ["styling:dark", "feature:oauth"]
    
    # ── STAGE 2: Project Detection ──────────────────────────────────────
    framework: Optional[str] = None  # Detected framework
    uses_typescript: bool = True     # TypeScript vs JavaScript
    css_strategy: str = CSSStrategy.CSS_MODULES.value  # Styling approach
    component_dir: Optional[str] = None  # Target directory for components
    formatting_config: Dict[str, Any] = field(default_factory=dict)  # Prettier/ESLint rules
    syncfusion_license_key: Optional[str] = None  # "injected" or None
    
    # ── STAGE 3: Layout Confirmation ────────────────────────────────────
    selected_variant: Optional[str] = None  # Chosen layout variant (e.g., "login-variant-b")
    layout_fields: List[LayoutField] = field(default_factory=list)  # Confirmed field list
    layout_metadata: Dict[str, Any] = field(default_factory=dict)  # Additional variant info
    
    # ── STAGE 4: Component Picking ──────────────────────────────────────
    component_mappings: List[ComponentMapping] = field(default_factory=list)  # Field → Component
    
    # ── STAGE 5: Preview Generation ─────────────────────────────────────
    preview_html: Optional[str] = None  # Generated preview markup
    preview_delivery_mechanism: str = "markdown"  # webview, html-file, markdown
    preview_approved: bool = False  # User approval status
    
    # ── STAGE 6: Code Generation ────────────────────────────────────────
    generated_files: List[GeneratedFile] = field(default_factory=list)  # All generated files
    component_name: Optional[str] = None  # Primary component name
    
    # ── STAGE 7: Web Standards Validation ───────────────────────────────
    validation_issues: List[ValidationIssue] = field(default_factory=list)  # Compliance issues
    validation_passed: bool = False  # True if no blocking errors
    
    # ── STAGE 8: Dependency Management ──────────────────────────────────
    required_packages: List[str] = field(default_factory=list)  # Packages to install
    dependencies: List[DependencyEntry] = field(default_factory=list)  # Detailed dep info
    conflicts: List[Dict[str, Any]] = field(default_factory=list)  # Version conflicts
    
    # ── STAGE 9: Code Insertion/Integration ─────────────────────────────
    inserted_files: List[str] = field(default_factory=list)  # Successfully written files
    build_verified: bool = False  # True if build succeeded after insertion
    
    # ── PIPELINE METADATA ───────────────────────────────────────────────
    current_stage: int = 0      # Current stage number (1-9)
    pipeline_status: str = PipelineStatus.RUNNING.value  # running, completed, failed
    error_message: Optional[str] = None  # Error description if failed
    stage_results: List[Dict[str, Any]] = field(default_factory=list)  # Per-stage results
    
    def add_stage_result(self, stage_id: int, duration_ms: float, success: bool, data: Dict[str, Any] = None):
        """Record result of a completed stage"""
        self.stage_results.append({
            "stage_id": stage_id,
            "duration_ms": duration_ms,
            "success": success,
            "data": data or {}
        })
    
    def mark_failed(self, error_message: str):
        """Mark pipeline as failed with error message"""
        self.pipeline_status = PipelineStatus.FAILED.value
        self.error_message = error_message
    
    def mark_completed(self):
        """Mark pipeline as successfully completed"""
        self.pipeline_status = PipelineStatus.COMPLETED.value
    
    def get_component_package_list(self) -> List[str]:
        """Extract unique npm packages from component mappings"""
        packages = set()
        for mapping in self.component_mappings:
            packages.add(mapping.package)
        return sorted(list(packages))
    
    def get_errors(self) -> List[ValidationIssue]:
        """Get all validation errors (blocking issues)"""
        return [issue for issue in self.validation_issues if issue.severity == "error"]
    
    def get_warnings(self) -> List[ValidationIssue]:
        """Get all validation warnings (non-blocking issues)"""
        return [issue for issue in self.validation_issues if issue.severity == "warning"]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert context to dictionary for serialization"""
        return {
            "user_request": self.user_request,
            "intent": self.intent,
            "component_type": self.component_type,
            "framework": self.framework,
            "selected_variant": self.selected_variant,
            "component_name": self.component_name,
            "generated_files_count": len(self.generated_files),
            "validation_errors": len(self.get_errors()),
            "validation_warnings": len(self.get_warnings()),
            "pipeline_status": self.pipeline_status,
            "current_stage": self.current_stage,
            "error_message": self.error_message
        }
