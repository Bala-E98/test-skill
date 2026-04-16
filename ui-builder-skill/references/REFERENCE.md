# UI Builder Skill — Technical Reference

**Version:** 1.0.0  
**Last Updated:** April 15, 2026  
**Purpose:** Complete technical reference for all 9 stages of the UI Builder Skill pipeline

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Stage-by-Stage Reference](#stage-by-stage-reference)
3. [UIBuilderContext State Model](#uibuildercontext-state-model)
4. [Specification Layer Model](#specification-layer-model)
5. [Integration Points](#integration-points)
6. [Error Handling](#error-handling)
7. [Performance Considerations](#performance-considerations)

---

## 1. Architecture Overview

### 1.1 Pipeline Architecture

The UI Builder Skill uses a **9-stage sequential pipeline** that transforms user intent into production-ready React components:

```
User Request
    ↓
┌───────────────────────────────────────────────────────────┐
│  STAGE 1: Intent Analysis                                 │
│  ─────────────────────────────────────────────────────    │
│  Input:  Natural language request                         │
│  Output: ui_type, complexity_score, required_fields       │
│  Tools:  NLP, keyword matching, pattern recognition       │
└───────────────────────────────────────────────────────────┘
    ↓
┌───────────────────────────────────────────────────────────┐
│  STAGE 2: Project Detection                               │
│  ──────────────────────────────────────────────────────   │
│  Input:  Workspace file structure                         │
│  Output: framework, project_type, component_directory     │
│  Tools:  package.json parsing, folder structure analysis  │
└───────────────────────────────────────────────────────────┘
    ↓
┌───────────────────────────────────────────────────────────┐
│  STAGE 3: Layout Confirmation                             │
│  ──────────────────────────────────────────────────────   │
│  Input:  ui_type, required_fields                         │
│  Output: selected_layout_variant                          │
│  Tools:  Variant catalog, user confirmation dialog        │
└───────────────────────────────────────────────────────────┘
    ↓
┌───────────────────────────────────────────────────────────┐
│  STAGE 4: Component Picking                               │
│  ──────────────────────────────────────────────────────   │
│  Input:  selected_layout_variant                          │
│  Output: syncfusion_components[]                          │
│  Tools:  Component mapping table, prop inference          │
└───────────────────────────────────────────────────────────┘
    ↓
┌───────────────────────────────────────────────────────────┐
│  STAGE 5: Preview Generation                              │
│  ──────────────────────────────────────────────────────   │
│  Input:  selected_layout, syncfusion_components           │
│  Output: ascii_preview, html_preview                      │
│  Tools:  ASCII art generator, HTML renderer               │
└───────────────────────────────────────────────────────────┘
    ↓
┌───────────────────────────────────────────────────────────┐
│  STAGE 6: Code Generation                                 │
│  ──────────────────────────────────────────────────────   │
│  Input:  All context data                                 │
│  Output: react_component_code, css_code                   │
│  Tools:  Template rendering, code formatting              │
└───────────────────────────────────────────────────────────┘
    ↓
┌───────────────────────────────────────────────────────────┐
│  STAGE 7: Validation                                      │
│  ──────────────────────────────────────────────────────   │
│  Input:  generated_code                                   │
│  Output: validation_results, warnings                     │
│  Tools:  WCAG checker, security scanner, linter           │
└───────────────────────────────────────────────────────────┘
    ↓
┌───────────────────────────────────────────────────────────┐
│  STAGE 8: Dependency Resolution                           │
│  ──────────────────────────────────────────────────────   │
│  Input:  syncfusion_components[], framework               │
│  Output: npm_packages[], install_commands                 │
│  Tools:  Package resolver, version checker                │
└───────────────────────────────────────────────────────────┘
    ↓
┌───────────────────────────────────────────────────────────┐
│  STAGE 9: File Insertion                                  │
│  ──────────────────────────────────────────────────────   │
│  Input:  react_code, css_code, component_directory        │
│  Output: Written files, updated imports                   │
│  Tools:  File writer, build verification                  │
└───────────────────────────────────────────────────────────┘
    ↓
Production-Ready Component
```

### 1.2 Design Principles

1. **Sequential Processing**: Each stage depends on the output of the previous stage
2. **State Immutability**: Context is passed forward, not mutated
3. **Progressive Disclosure**: Documentation loaded on-demand, not in memory
4. **Fail-Fast**: Errors halt the pipeline immediately with clear messages
5. **User Confirmation**: Critical decisions (layout, file write) require approval

---

## 2. Stage-by-Stage Reference

### Stage 1: Intent Analysis

**Purpose:** Parse natural language input to determine UI component type and requirements.

**Input:**
- `user_request` (string): Natural language description of desired UI

**Output:**
```python
{
    "ui_type": str,              # "login", "registration", "data-table", etc.
    "complexity_score": int,     # 1-5 scale
    "required_fields": list,     # ["email", "password", "remember-me"]
    "optional_features": list,   # ["oauth", "2fa", "password-strength"]
    "theme_preference": str,     # "light", "dark", "auto"
    "responsive": bool           # Mobile-first flag
}
```

**Algorithm:**
1. Tokenize user request
2. Match against keyword database (see `assets/data/keywords.json`)
3. Score confidence for each UI type (0.0-1.0)
4. Select highest-scoring type if confidence > 0.7
5. Extract field names using NLP entity recognition
6. Detect complexity indicators (multi-step, validation, etc.)

**Example:**
```
Input:  "Create a dark-themed login form with email and password"
Output: {
  "ui_type": "login",
  "complexity_score": 2,
  "required_fields": ["email", "password"],
  "optional_features": [],
  "theme_preference": "dark",
  "responsive": true
}
```

**Error Conditions:**
- Ambiguous request (multiple high-confidence matches) → Stage 1 asks for clarification
- No confident match → Stage 1 suggests closest match or requests more detail

---

### Stage 2: Project Detection

**Purpose:** Analyze the workspace to determine framework, project type, and file structure.

**Input:**
- `workspace_root` (path): Absolute path to project root

**Output:**
```python
{
    "framework": str,              # "nextjs", "vite", "cra", "unknown"
    "framework_version": str,      # "13.4.0" (from package.json)
    "project_type": str,           # "typescript", "javascript"
    "component_directory": str,    # "src/components" or "app/components"
    "styles_directory": str,       # "src/styles" or "app/styles"
    "uses_app_router": bool,       # True for Next.js 13+ App Router
    "existing_components": list,   # ["Button.tsx", "Input.tsx"]
    "has_syncfusion": bool,        # True if any @syncfusion/* packages found
    "package_manager": str         # "npm", "yarn", "pnpm"
}
```

**Detection Logic:**
```python
def detect_framework(workspace_root):
    package_json = read_json(workspace_root / "package.json")
    dependencies = {**package_json.get("dependencies", {}), 
                    **package_json.get("devDependencies", {})}
    
    if "next" in dependencies:
        return "nextjs", dependencies["next"]
    elif "vite" in dependencies or exists(workspace_root / "vite.config.js"):
        return "vite", dependencies.get("vite", "unknown")
    elif "react-scripts" in dependencies:
        return "cra", dependencies["react-scripts"]
    else:
        return "unknown", None
```

**Component Directory Resolution:**
- Next.js 13+ App Router: `app/components/` (create if missing)
- Next.js Pages Router: `src/components/` or `components/`
- Vite: `src/components/`
- CRA: `src/components/`

**Error Conditions:**
- No `package.json` found → Abort with error
- React not in dependencies → Abort with error
- Unsupported framework → Warn but continue with generic React approach

---

### Stage 3: Layout Confirmation

**Purpose:** Present layout variants to user and confirm selection.

**Input:**
- `ui_type` (from Stage 1)
- `required_fields` (from Stage 1)
- `optional_features` (from Stage 1)

**Output:**
```python
{
    "selected_layout_variant": str,    # "login-centered-modern"
    "layout_structure": dict,          # Field positions, grouping
    "user_confirmed": bool,            # True after user approval
    "custom_overrides": dict           # User-requested modifications
}
```

**Variant Selection Process:**
1. Load variant catalog from `LAYOUT-VARIANTS.md` or Python constants
2. Filter variants by `ui_type`
3. Score each variant based on required fields match
4. Present top 3 variants with ASCII preview
5. Wait for user selection
6. Apply any custom overrides

**Example:**
```python
LOGIN_VARIANTS = {
    "login-centered-modern": {
        "layout": "centered",
        "width": "400px",
        "fields": ["email", "password"],
        "features": ["remember-me", "forgot-password-link"],
        "preview": """
        ┌────────────────────────────────┐
        │      Login to Your Account     │
        ├────────────────────────────────┤
        │  Email: [________________]     │
        │  Password: [____________]      │
        │  ☐ Remember me                 │
        │  [  Login  ]                   │
        │  Forgot password?              │
        └────────────────────────────────┘
        """
    }
}
```

---

### Stage 4: Component Picking

**Purpose:** Map layout fields to specific Syncfusion React components.

**Input:**
- `selected_layout_variant`
- `required_fields`

**Output:**
```python
{
    "syncfusion_components": [
        {
            "field": "email",
            "component": "TextBoxComponent",
            "package": "@syncfusion/ej2-react-inputs",
            "props": {
                "type": "email",
                "placeholder": "Enter your email",
                "floatLabelType": "Auto",
                "required": True
            }
        },
        {
            "field": "password",
            "component": "TextBoxComponent",
            "package": "@syncfusion/ej2-react-inputs",
            "props": {
                "type": "password",
                "placeholder": "Enter your password",
                "floatLabelType": "Auto",
                "required": True
            }
        }
    ]
}
```

**Component Mapping Table:**
| Field Type | Syncfusion Component | Package |
|------------|----------------------|---------|
| email, text, search | TextBoxComponent | @syncfusion/ej2-react-inputs |
| password | TextBoxComponent (type="password") | @syncfusion/ej2-react-inputs |
| checkbox | CheckBoxComponent | @syncfusion/ej2-react-buttons |
| radio | RadioButtonComponent | @syncfusion/ej2-react-buttons |
| select, dropdown | DropDownListComponent | @syncfusion/ej2-react-dropdowns |
| date | DatePickerComponent | @syncfusion/ej2-react-calendars |
| number | NumericTextBoxComponent | @syncfusion/ej2-react-inputs |
| button, submit | ButtonComponent | @syncfusion/ej2-react-buttons |
| data-table | GridComponent | @syncfusion/ej2-react-grids |

**Prop Inference:**
- Email fields → `type="email"`, add email validation
- Required fields → `required={true}`, ARIA attributes
- Password fields → `type="password"`, optional strength meter
- Buttons → `isPrimary={true}` for primary action

---

### Stage 5: Preview Generation

**Purpose:** Generate ASCII and HTML previews for user verification.

**Input:**
- `selected_layout`
- `syncfusion_components`

**Output:**
```python
{
    "ascii_preview": str,      # Terminal-friendly preview
    "html_preview": str,       # Rendered HTML for browser
    "preview_url": str         # Optional: temp file path
}
```

**ASCII Preview Format:**
```
╔════════════════════════════════════════╗
║          Login to Your Account         ║
╠════════════════════════════════════════╣
║                                        ║
║  📧 Email                              ║
║  ┌──────────────────────────────────┐ ║
║  │ Enter your email                 │ ║
║  └──────────────────────────────────┘ ║
║                                        ║
║  🔒 Password                           ║
║  ┌──────────────────────────────────┐ ║
║  │ ••••••••                         │ ║
║  └──────────────────────────────────┘ ║
║                                        ║
║  ☐ Remember me    Forgot password?    ║
║                                        ║
║  ┌────────────┐                       ║
║  │   Login    │                       ║
║  └────────────┘                       ║
║                                        ║
╚════════════════════════════════════════╝
```

**HTML Preview:**
- Uses actual Syncfusion components (requires Syncfusion CDN or local install)
- Injects minimal CSS for layout
- Opens in VS Code Simple Browser
- Interactive (functional form submission to console)

---

### Stage 6: Code Generation

**Purpose:** Generate production-ready React component and CSS code.

**Input:**
- All context from previous stages

**Output:**
```python
{
    "react_component_code": str,    # Complete .tsx/.jsx file
    "css_code": str,                # CSS Module or stylesheet
    "typescript_interfaces": str,   # Type definitions
    "component_name": str,          # "LoginForm"
    "file_extension": str           # ".tsx" or ".jsx"
}
```

**Code Template Structure:**
```tsx
// LoginForm.tsx
import React, { useState } from 'react';
import { TextBoxComponent } from '@syncfusion/ej2-react-inputs';
import { ButtonComponent } from '@syncfusion/ej2-react-buttons';
import styles from './LoginForm.module.css';

interface LoginFormProps {
  onSubmit?: (data: LoginData) => void;
  theme?: 'light' | 'dark';
}

interface LoginData {
  email: string;
  password: string;
  rememberMe: boolean;
}

export const LoginForm: React.FC<LoginFormProps> = ({ onSubmit, theme = 'light' }) => {
  const [formData, setFormData] = useState<LoginData>({
    email: '',
    password: '',
    rememberMe: false
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit?.(formData);
  };

  return (
    <form className={styles.loginForm} onSubmit={handleSubmit}>
      {/* Component JSX */}
    </form>
  );
};
```

**Code Generation Rules:**
- Use functional components (no class components)
- TypeScript interfaces for props and state
- Proper event handlers with types
- ARIA labels on all form controls
- Semantic HTML structure
- CSS Modules for styling (scoped classes)
- Export both named and default

---

### Stage 7: Validation

**Purpose:** Validate generated code against web standards and best practices.

**Input:**
- `react_component_code`
- `css_code`

**Output:**
```python
{
    "validation_results": {
        "accessibility": {
            "passed": bool,
            "issues": [{"severity": "error", "message": "...", "line": 42}]
        },
        "security": {
            "passed": bool,
            "issues": []
        },
        "performance": {
            "passed": bool,
            "warnings": []
        },
        "code_quality": {
            "passed": bool,
            "warnings": []
        }
    },
    "overall_passed": bool
}
```

**Validation Checks:**

**Accessibility (WCAG 2.1 AA):**
- ✅ All form inputs have labels or aria-label
- ✅ Color contrast ≥ 4.5:1
- ✅ Keyboard navigation supported
- ✅ Focus indicators visible
- ✅ Error messages associated with fields

**Security:**
- ✅ No inline event handlers (onClick in strings)
- ✅ No dangerouslySetInnerHTML without sanitization
- ✅ No eval() or Function() constructors
- ✅ Input fields properly typed

**Performance:**
- ✅ No console.log in production
- ✅ No excessive re-renders (unnecessary useState)
- ✅ Large lists use virtualization

**Code Quality:**
- ✅ No var declarations
- ✅ Consistent indentation
- ✅ Proper import order
- ✅ No unused variables

---

### Stage 8: Dependency Resolution

**Purpose:** Determine required npm packages and generate install commands.

**Input:**
- `syncfusion_components` (from Stage 4)
- `framework` (from Stage 2)

**Output:**
```python
{
    "npm_packages": [
        "@syncfusion/ej2-react-inputs",
        "@syncfusion/ej2-react-buttons"
    ],
    "install_command": "npm install @syncfusion/ej2-react-inputs @syncfusion/ej2-react-buttons",
    "already_installed": ["@syncfusion/ej2-react-buttons"],
    "needs_installation": ["@syncfusion/ej2-react-inputs"]
}
```

**Package Resolution Logic:**
1. Extract unique package names from `syncfusion_components`
2. Check `package.json` for existing packages
3. Filter to only missing packages
4. Generate install command using detected package manager
5. Include version constraints if specified

---

### Stage 9: File Insertion

**Purpose:** Write generated code to files and verify build integrity.

**Input:**
- `react_component_code`
- `css_code`
- `component_directory` (from Stage 2)

**Output:**
```python
{
    "files_written": [
        "/path/to/project/src/components/LoginForm.tsx",
        "/path/to/project/src/components/LoginForm.module.css"
    ],
    "build_status": "success",
    "next_steps": [
        "Import the component: import { LoginForm } from './components/LoginForm'",
        "Use it: <LoginForm onSubmit={handleLogin} />"
    ]
}
```

**File Writing Process:**
1. Confirm with user before writing
2. Check if files already exist (prompt for overwrite)
3. Write component file
4. Write CSS file
5. Update `index.ts` barrel export (if exists)
6. Run build check (`npm run build` or `tsc --noEmit`)
7. Report success or errors

---

## 3. UIBuilderContext State Model

See `scripts/context.py` for the complete dataclass definition.

**Key Fields:**
```python
@dataclass
class UIBuilderContext:
    # Stage 1 outputs
    user_request: str
    ui_type: str
    required_fields: List[str]
    
    # Stage 2 outputs
    framework: str
    component_directory: str
    
    # Stage 3 outputs
    selected_layout_variant: str
    
    # Stage 4 outputs
    syncfusion_components: List[Dict]
    
    # Stage 5 outputs
    preview_data: Dict
    
    # Stage 6 outputs
    generated_code: Dict
    
    # Stage 7 outputs
    validation_results: Dict
    
    # Stage 8 outputs
    dependencies: List[str]
    
    # Stage 9 outputs
    files_written: List[str]
    
    # Meta
    current_stage: int
    errors: List[str]
```

---

## 4. Specification Layer Model

The UI Builder acts as a **specification layer** that defines everything needed for code generation. See main spec Section 2.7 for full details.

**What UI Builder Provides:**
1. **Layout Specifications** - Field ordering, form structure, responsive breakpoints
2. **Component Specifications** - Which Syncfusion components, props, event handlers
3. **Styling Specifications** - Theme, colors, typography, spacing, CSS conventions
4. **Standards Specifications** - WCAG 2.1 AA, responsive targets, code quality rules

**What AI Agent Implements:**
- Production-ready React code that follows all specifications
- Correct Syncfusion component usage with proper props
- Consistent styling and web standards compliance

---

## 5. Integration Points

### 5.1 Syncfusion Components Library

External dependency: `syncfusion/react-ui-components-skills` repository

**Installation:**
```bash
npx skills add syncfusion/react-ui-components-skills -y
```

**Usage in Stage 4:**
- Component mapping table references official Syncfusion component names
- Props are inferred from Syncfusion documentation patterns
- Import statements use official package names

### 5.2 Framework-Specific Integration

**Next.js 13+ App Router:**
- Components go in `app/components/`
- Use `"use client"` directive for interactive components
- CSS Modules supported

**Next.js Pages Router:**
- Components go in `src/components/` or `components/`
- Standard React component structure

**Vite:**
- Components go in `src/components/`
- Fast refresh enabled
- CSS Modules supported

**Create React App:**
- Components go in `src/components/`
- Standard React component structure

---

## 6. Error Handling

### 6.1 Error Categories

**User Errors:**
- Ambiguous request → Ask for clarification
- Unsupported UI type → Suggest closest match
- Missing project structure → Guide to create React project

**System Errors:**
- File write permission denied → Report with fix instructions
- npm install failed → Show error, suggest manual install
- Build errors after insertion → Show errors, offer to rollback

**Validation Errors:**
- Accessibility issues → List issues, offer to fix
- Security concerns → Block file write, report issues
- Code quality warnings → Report but allow override

### 6.2 Error Recovery

1. **Graceful Degradation**: If Stage N fails, provide partial results from Stage N-1
2. **Rollback Support**: Stage 9 can restore previous file state if build fails
3. **Manual Override**: User can skip validation warnings with explicit confirmation

---

## 7. Performance Considerations

### 7.1 Memory Optimization

- **Progressive Disclosure**: Load reference docs only when needed
- **Lazy Loading**: Stage scripts loaded on-demand
- **Minimal Context**: Only essential data passed between stages

### 7.2 Execution Speed

**Target Times:**
- Stage 1 (Intent): < 1 second
- Stage 2 (Detection): < 2 seconds
- Stage 3 (Layout): < 1 second (+ user interaction time)
- Stage 4 (Components): < 1 second
- Stage 5 (Preview): < 2 seconds
- Stage 6 (Code Gen): < 3 seconds
- Stage 7 (Validation): < 2 seconds
- Stage 8 (Dependencies): < 1 second
- Stage 9 (Insertion): < 5 seconds (includes build check)

**Total End-to-End:** < 20 seconds (excluding user confirmation time)

---

## Appendix A: Quick Reference Tables

### A.1 Stage Input/Output Summary

| Stage | Primary Input | Primary Output |
|-------|---------------|----------------|
| 1 | user_request | ui_type, required_fields |
| 2 | workspace_root | framework, component_directory |
| 3 | ui_type, required_fields | selected_layout_variant |
| 4 | selected_layout_variant | syncfusion_components[] |
| 5 | layout, components | ascii_preview, html_preview |
| 6 | all_context | react_code, css_code |
| 7 | react_code, css_code | validation_results |
| 8 | syncfusion_components, framework | npm_packages[], install_command |
| 9 | code, css, component_directory | files_written[] |

### A.2 Supported UI Types

- `login` - Login forms
- `registration` - Sign-up forms
- `password-reset` - Password recovery
- `contact-form` - Contact forms
- `data-table` - Data grids with CRUD
- `dashboard` - Analytics dashboards
- `navigation` - Nav bars, sidebars
- `modal` - Dialog boxes
- `form-wizard` - Multi-step forms

### A.3 Supported Frameworks

| Framework | Detection Method | Component Directory |
|-----------|------------------|---------------------|
| Next.js 13+ App | "next" in deps + app/ folder | app/components/ |
| Next.js Pages | "next" in deps + pages/ folder | src/components/ |
| Vite | "vite" in deps or vite.config.js | src/components/ |
| Create React App | "react-scripts" in deps | src/components/ |

---

**End of Technical Reference**  
For workflow details, see `STAGES.md`  
For component mapping, see `SYNCFUSION-MAPPING.md`  
For troubleshooting, see `TROUBLESHOOTING.md`
