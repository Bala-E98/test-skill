# UI Builder Skill — Stages Workflow Reference

**Version:** 1.0.0  
**Last Updated:** April 15, 2026  
**Purpose:** Step-by-step workflow guide for each of the 9 pipeline stages

---

## Table of Contents

1. [Stage 1: Intent Analysis](#stage-1-intent-analysis)
2. [Stage 2: Project Detection](#stage-2-project-detection)
3. [Stage 3: Layout Confirmation](#stage-3-layout-confirmation)
4. [Stage 4: Component Picking](#stage-4-component-picking)
5. [Stage 5: Preview Generation](#stage-5-preview-generation)
6. [Stage 6: Code Generation](#stage-6-code-generation)
7. [Stage 7: Validation](#stage-7-validation)
8. [Stage 8: Dependency Resolution](#stage-8-dependency-resolution)
9. [Stage 9: File Insertion](#stage-9-file-insertion)
10. [Cross-Stage Decision Trees](#cross-stage-decision-trees)

---

## Stage 1: Intent Analysis

**Goal:** Parse user request and extract component requirements

**Input:** Natural language string  
**Output:** UIBuilderContext with ui_type, required_fields, complexity_score

**Workflow:**

1. **Tokenize request** - Split into words, remove stop words
2. **Keyword matching** - Check against keyword database:
   - Form keywords: "login", "signup", "form", "authentication"
   - Table keywords: "grid", "data", "table", "display", "list"
   - Navigation keywords: "navbar", "menu", "sidebar", "header"
3. **Score candidates** - Each UI type gets a 0.0-1.0 score
4. **Confidence check:**
   - If top score > 0.8 → Proceed with that type
   - If top score 0.5-0.8 → Show top 2-3 options to user
   - If top score < 0.5 → Ask clarifying question
5. **Extract modifiers** - dark theme, mobile-first, validation, etc.
6. **Complexity scoring** - 1-5 scale based on feature count
7. **Initialize context** - Create UIBuilderContext object

**Decision Tree:**

```
User says: "Create a login form"
  ├─ Keywords found: "login", "form"
  ├─ Candidate: "form/login" (score: 0.95)
  ├─ Confidence: > 0.8 ✓
  ├─ Extract fields: ["email", "password"]
  ├─ Extract modifiers: []
  ├─ Complexity: 2
  └─ Proceed to Stage 2

User says: "Build me a UI"
  ├─ No high-confidence keywords
  ├─ Candidates: "form/generic" (0.3), "data-table" (0.25)
  ├─ Confidence: < 0.5 ✗
  ├─ Ask: "What kind of UI? (login form, data table, etc.)"
  └─ Return to Stage 1 after clarification
```

**Ambiguity Resolution:**

Ask ONE clarifying question if needed:
- "What kind of form? (login, registration, contact, etc.)"
- "What data will this table display?"
- "Where should the navigation be? (top bar, sidebar, etc.)"

**Error Handling:**
- No confident match after clarification → Show UI type list (Section 3.1 of main spec)

---

## Stage 2: Project Detection

**Goal:** Analyze workspace and detect framework, project type, structure

**Input:** Workspace root path  
**Output:** UIBuilderContext with framework, component_directory, preferences

**Workflow:**

1. **Scan project root** for config files:
   - package.json (required)
   - tsconfig.json / jsconfig.json
   - next.config.js
   - vite.config.ts
   - .prettierrc / prettier.config.js
   - .eslintrc / eslint.config.js

2. **Detect framework:**
   - Check package.json dependencies
   - If "next" → Next.js (check for app/ folder for App Router)
   - Else if "vite" → Vite
   - Else if "react-scripts" → Create React App
   - Else → Unknown React project

3. **Identify component directory:**
   - Next.js App Router → app/components/ (create if missing)
   - Next.js Pages Router → src/components/
   - Vite/CRA → src/components/
   - Fallback → components/

4. **Read preferences:**
   - TypeScript? (check tsconfig.json presence)
   - CSS strategy? (CSS Modules, Tailwind, inline)
   - Indentation? (spaces/tabs from .prettierrc)
   - Semicolons? (from .eslintrc)

5. **Check dependencies:**
   - React 18+? Required
   - Syncfusion installed? (for skipping install)
   - Package manager? (npm, yarn, pnpm from lock files)

6. **Report detection** and ask user to confirm or override

**Detection Checklist:**

```
✓ Framework: Next.js 14.0.0 (App Router)
✓ Language: TypeScript (strict)
✓ Component Directory: app/components/
✓ CSS Strategy: CSS Modules
✓ Package Manager: npm
✓ React Version: 18.2.0 (compatible)
✓ Syncfusion: Not installed (will add in Stage 8)
```

**Error Handling:**
- No package.json → "This doesn't look like a React project. Aborting."
- React not found → "React not in dependencies. Aborting."
- Unsupported React version → Warn but continue

---

## Stage 3: Layout Confirmation

**Goal:** Present layout variants and get user approval

**Input:** ui_type, required_fields  
**Output:** UIBuilderContext with selected_layout_variant, confirmed layout structure

**Workflow:**

1. **Load variant catalog** for ui_type (from LAYOUT-VARIANTS.md)
2. **Filter variants** by required_fields:
   - Login form + email + password → Show login variants only
   - Data table + sort/filter → Show grid variants only
3. **Score variants** based on:
   - Required field match (100% match = highest score)
   - Complexity match (user wants simple → show minimal variants)
   - Trend/popularity (common layouts ranked higher)
4. **Present top 3 variants:**
   - Variant name and description
   - ASCII preview or skeleton
   - Feature list
5. **Get user selection:**
   - Show "Select Layout" dialog
   - User picks one
   - Confirm: "Ready to generate?"
6. **Allow modifications:**
   - "Add field" / "Remove field" / "Change order"
   - Re-confirm layout
7. **Lock layout** - Pass to Stage 4

**Example Dialog:**

```
LAYOUT SELECTION

Component Type: Login Form

Recommended Variants (ranked by match):

1. ✓ RECOMMENDED: Modern Centered (Variant A)
   └─ Fields: email, password, remember-me
   └─ Features: forget password link
   └─ Preview: [centered form, 400px width]

2. Minimal (Variant B)
   └─ Fields: email, password
   └─ Features: submit only
   └─ Preview: [compact form]

3. With OAuth (Variant C)
   └─ Fields: email, password, social buttons
   └─ Features: Google, GitHub login
   └─ Preview: [form with social buttons]

[Select Variant A] [Show Others] [Cancel]
```

---

## Stage 4: Component Picking

**Goal:** Map layout fields to Syncfusion components

**Input:** selected_layout_variant  
**Output:** UIBuilderContext with syncfusion_components[]

**Workflow:**

1. **Extract fields** from confirmed layout
2. **For each field:**
   - Identify field type (text, select, date, button, etc.)
   - Query Syncfusion component mapping table
   - Determine best component match
3. **Build component specs:**
   ```python
   {
     "field": "email",
     "component": "TextBoxComponent",
     "package": "@syncfusion/ej2-react-inputs",
     "props": { "type": "email", "required": true }
   }
   ```
4. **Show mapping preview** to user for approval
5. **Allow overrides** - User can select alternative component
6. **Collect all packages** for Stage 8

**Mapping Decision:**

```
Field: "email"
  └─ TextBoxComponent (type="email") ✓

Field: "country"
  ├─ Option 1: DropDownListComponent (recommended)
  ├─ Option 2: ComboBoxComponent (if custom value allowed)
  └─ Option 3: AutoCompleteComponent (if searchable)

Field: "date-of-birth"
  └─ DatePickerComponent ✓
```

**Error Handling:**
- Unsupported field type → Ask user for clarification
- Missing component mapping → Use generic TextBox fallback + warn

---

## Stage 5: Preview Generation

**Goal:** Generate interactive preview for user approval

**Input:** layout_structure, syncfusion_components  
**Output:** ascii_preview, html_preview_url

**Workflow:**

1. **Choose delivery mechanism:**
   - VS Code Webview? → Load interactive HTML preview
   - HTML file? → Write temp file, prompt to open
   - Terminal only? → Show ASCII art preview
2. **Generate preview:**
   - Render component structure
   - Apply dummy theme/colors
   - Show mobile (320px) + desktop (1280px) versions
3. **Display interactivity:**
   - Functional form inputs
   - Focus indicators
   - Validation error states
   - Hover/active states
4. **Get user feedback:**
   - "Does this look right?"
   - "Changes needed?" (add field, change layout, adjust styling)
5. **Apply modifications** or proceed to Stage 6

**Preview Content:**
- Component layout visualization
- Responsive breakpoint demo
- Accessibility features (focus outline, keyboard nav)
- Color contrast validation
- Interactive form testing

---

## Stage 6: Code Generation

**Goal:** Generate production-ready React component code

**Input:** all context data (layout, components, project config)  
**Output:** .tsx file, .module.css file, TypeScript interfaces

**Workflow:**

1. **Select template** based on ui_type
2. **Generate component code:**
   - Import statements
   - Props interface
   - State initialization
   - Event handlers
   - JSX render
3. **Generate CSS:**
   - Layout classes
   - Responsive media queries
   - Component-specific styles
   - Theme variables
4. **Generate TypeScript interfaces:**
   - Props type
   - Event handler types
   - Form data types
5. **Apply formatting:**
   - Project indentation style
   - Semicolon rules
   - Quote style
6. **Add documentation:**
   - JSDoc comments
   - Usage examples in comments
   - Web standards notes

**Output Files:**
- `ComponentName.tsx` - React component
- `ComponentName.module.css` - Styles
- Export ready for use

---

## Stage 7: Validation

**Goal:** Validate code against web standards

**Input:** generated_code, css_code  
**Output:** validation_results (pass/fail with issues)

**Workflow:**

1. **Accessibility audit:**
   - WCAG 2.1 AA compliance check
   - ARIA labels present?
   - Color contrast ≥ 4.5:1?
   - Keyboard navigation supported?
   - Focus indicators visible?
2. **Security scan:**
   - No dangerouslySetInnerHTML?
   - No eval()?
   - No hardcoded secrets?
3. **Performance check:**
   - No console.log in production?
   - Unnecessary re-renders?
   - Large assets?
4. **Code quality:**
   - No var declarations?
   - Proper TypeScript types?
   - Unused variables?
5. **Report results:**
   - ✓ Pass (0 errors)
   - ⚠ Warnings (0 errors, N warnings)
   - ✗ Fail (N errors)
6. **Auto-fix issues** where possible
7. **Get user approval** for remaining warnings

---

## Stage 8: Dependency Resolution

**Goal:** Determine and resolve npm packages

**Input:** syncfusion_components[], framework  
**Output:** npm_packages[], install_command

**Workflow:**

1. **Extract unique packages** from component specs
2. **Check package.json** for existing packages
3. **Identify missing packages**
4. **Resolve version conflicts:**
   - Use latest compatible version
   - Respect existing versions if already installed
5. **Generate install command:**
   ```bash
   npm install @syncfusion/ej2-react-inputs @syncfusion/ej2-react-buttons
   ```
6. **Run npm install** (with user confirmation)
7. **Verify installation** - Check node_modules

**Version Strategy:**
- If package installed → Keep existing version
- If package missing → Install latest ^20.0.0
- If conflict → Ask user which version to use

---

## Stage 9: File Insertion

**Goal:** Write files to project and verify build

**Input:** generated_code, css_code, component_directory  
**Output:** files_written[], build_status

**Workflow:**

1. **Confirm file write** with user (show preview)
2. **Check if files exist:**
   - If exists → Ask overwrite or rename
   - If not → Create new
3. **Write component file** (.tsx)
4. **Write CSS file** (.module.css)
5. **Update barrel exports** (index.ts if exists)
6. **Run build check:**
   ```bash
   npm run build  # or tsc --noEmit
   ```
7. **Verify success:**
   - Build passes? ✓ Done
   - Build fails? Show errors, offer rollback
8. **Report completion:**
   - Files written: [list]
   - Next steps: How to import and use

**Error Handling:**
- Permission denied → "Cannot write to directory"
- Build errors → "Fix these errors before proceeding"
- Rollback available → "Want to undo?"

---

## Cross-Stage Decision Trees

### When to Loop Back

**User requests modification during preview (Stage 5):**
```
User: "Add email verification step"
  └─ Decision: Loop back to Stage 3 (Layout change)
  └─ Re-run: Stages 3, 4, 5, 6, 7, 9

User: "Change color to blue"
  └─ Decision: Loop back to Stage 6 (CSS only)
  └─ Re-run: Stage 6, 7, 9 (skip 8, already installed)
```

### When to Skip Stages

**Modifying existing component:**
```
User: "Update existing LoginForm"
  └─ Skip Stage 1 (already have ui_type)
  └─ Skip Stage 2 (already have framework)
  └─ Skip Stage 8 (already have dependencies)
  └─ Run: 3, 4, 5, 6, 7, 9
```

---

## Appendix: Stage Timing

| Stage | Target Time | Notes |
|-------|------------|-------|
| 1 | < 1 sec | NLP + keyword matching |
| 2 | < 2 sec | File system scan |
| 3 | varies | Includes user interaction |
| 4 | < 1 sec | Component mapping lookup |
| 5 | < 2 sec | Preview generation |
| 6 | < 3 sec | Template rendering |
| 7 | < 2 sec | Static analysis |
| 8 | < 1 sec | Package resolution |
| 9 | < 5 sec | File write + build |
| **Total** | **< 20 sec** | Excluding user confirmation |

---

**End of Stages Workflow Reference**  
For technical details, see `REFERENCE.md`  
For component mapping, see `SYNCFUSION-MAPPING.md`  
For troubleshooting, see `TROUBLESHOOTING.md`
