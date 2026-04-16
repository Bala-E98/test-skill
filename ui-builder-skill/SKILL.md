---
name: ui-builder-skill
description: Generates production-ready React UI webpage using Syncfusion components. Orchestrates 9 sequential stages intent analysis, project detection, layout confirmation, component picking, preview generation, code generation, web standards validation, dependency management, and code insertion. Outputs full TypeScript components with WCAG 2.1 AA accessibility, responsive design, and enterprise-grade quality.
license: Proprietary
compatibility: Requires Node.js 18+, npm/yarn/pnpm, React 18+ projects (Next.js 13+, Vite, or Create React App)
metadata:
  author: Syncfusion
  version: 1.0.0
  supported-frameworks: "React 18+, Next.js 13+ (App Router & Pages Router), Vite, Create React App"
  target-release: "Q2 2026"
allowed-tools: bash npm read write
---

# UI Builder Skill

## Overview

The UI Builder Skill is a **frontend-only** React component generator that creates production-ready UI components and pages using Syncfusion components. It operates exclusively on the frontend layer—generating React components, CSS stylesheets, and TypeScript interfaces—while leaving backend, API, database, and infrastructure concerns to the consuming application.

## What This Skill Does

**✅ Generates:**
- React functional components (`.tsx`/`.jsx`) with hooks
- CSS stylesheets (CSS Modules, Tailwind classes, inline styles)
- TypeScript interfaces for props, state, and event handlers
- Syncfusion component integration with correct imports and props
- Client-side form validation logic
- WCAG 2.1 AA accessibility markup (ARIA attributes, semantic HTML)
- Responsive CSS with mobile-first breakpoints
- Component index exports and barrel files

**❌ Does NOT Generate:**
- Backend code (API routes, server handlers, middleware)
- Database schemas or ORM models
- Authentication/authorization logic
- Server-side validation
- Routing configuration
- Environment secrets or infrastructure config

## Supported Components

- **Forms**: Login, registration, password reset, contact, multi-step wizards
- **Data Display**: Data tables/grids, lists, charts, tree views, kanban boards
- **Navigation**: Navbars, sidebars, breadcrumbs, tabs
- **Common Patterns**: Modals, notifications, dropdowns, carousels
- **Page Templates**: Dashboards, e-commerce, portfolios, user profiles, landing pages

## Skill Structure

```
ui-builder-skill/
├── SKILL.md                              # This file (main entry point)
├── scripts/                              # Executable Python scripts
│   ├── orchestrator.py                   # Main orchestrator (entry point)
│   ├── context.py                        # UIBuilderContext state management
│   ├── stage_1_intent.py                 # Stage 1: Intent Analysis
│   ├── stage_2_detection.py              # Stage 2: Project Detection
│   ├── stage_3_layout.py                 # Stage 3: Layout Confirmation
│   ├── stage_4_components.py             # Stage 4: Component Picking
│   ├── stage_5_preview.py                # Stage 5: Preview Generation
│   ├── stage_6_codegen.py                # Stage 6: Code Generation
│   ├── stage_7_validation.py             # Stage 7: Validation
│   ├── stage_8_dependencies.py           # Stage 8: Dependency Management
│   ├── stage_9_insertion.py              # Stage 9: Code Insertion
│   └── README.md                         # Scripts documentation
└── references/                           # On-demand reference docs
    ├── REFERENCE.md                      # Complete technical reference
    ├── STAGES.md                         # Workflow & decision trees
    ├── SYNCFUSION-MAPPING.md             # Component mapping guide
    ├── WEB-STANDARDS.md                  # WCAG/security checklists
    ├── LAYOUT-VARIANTS.md                # Pre-designed layout catalog
    ├── EXAMPLES.md                       # Generated code samples
    └── TROUBLESHOOTING.md                # Error solutions & FAQ
```

## Quick Start

### Prerequisites

1. **Active React project** (React 18+, Next.js 13+, Vite, or CRA)
2. **Node.js 18+** and npm/yarn/pnpm installed
3. **Syncfusion components library** (auto-installed if missing):
   ```bash
   npx skills add syncfusion/react-ui-components-skills -y
   ```

### Basic Usage

**Example 1: Generate a Login Form**

```
User: "Create a login form with email, password, and remember me checkbox"

Skill executes:
  → Detects project structure
  → Presents 3 layout variants (simple, with social login, with 2FA)
  → User confirms variant
  → Maps to Syncfusion components (TextBox, Button, CheckBox)
  → Generates preview
  → Validates WCAG 2.1 AA compliance
  → Installs dependencies
  → Inserts code into project

Output:
  ✓ components/LoginForm/LoginForm.tsx
  ✓ components/LoginForm/LoginForm.module.css
  ✓ components/LoginForm/index.ts
```

**Example 2: Generate a Data Table**

```
User: "Build a customer data table with sorting and filtering"

Output:
  ✓ components/CustomerTable/CustomerTable.tsx (with Syncfusion DataGrid)
  ✓ Mock data included (useState with sample customers)
  ✓ Responsive design (mobile-first)
  ✓ Accessibility compliance
```

## How It Works: 9-Stage Pipeline

The skill orchestrates **9 sequential stages** internally. Each stage enriches a unified `UIBuilderContext` state object.

```
┌─────────────────────────────────────────────────────────────┐
│ Stage 1: Intent Analysis & Setup                           │
│   Parse user request → classify intent → initialize context│
├─────────────────────────────────────────────────────────────┤
│ Stage 2: Project Detection & Configuration                 │
│   Scan project → detect framework → read preferences       │
├─────────────────────────────────────────────────────────────┤
│ Stage 3: Layout Confirmation                                │
│   Present 2-3 layout variants → user confirms structure    │
├─────────────────────────────────────────────────────────────┤
│ Stage 4: Component Picking                                  │
│   Map layout → Syncfusion components → user confirms picks │
├─────────────────────────────────────────────────────────────┤
│ Stage 5: Preview Generation                                 │
│   Generate interactive HTML preview → user approves        │
├─────────────────────────────────────────────────────────────┤
│ Stage 6: Code Generation                                    │
│   Generate .tsx, .css, TypeScript interfaces               │
├─────────────────────────────────────────────────────────────┤
│ Stage 7: Web Standards Validation                           │
│   Validate WCAG 2.1 AA, security, performance, SEO         │
├─────────────────────────────────────────────────────────────┤
│ Stage 8: Dependency Management                              │
│   Detect packages → resolve conflicts → npm install        │
├─────────────────────────────────────────────────────────────┤
│ Stage 9: Code Insertion/Integration                         │
│   Insert files → update imports → verify build             │
└─────────────────────────────────────────────────────────────┘
```

**Entry Point**: `scripts/orchestrator.py` — see implementation for detailed stage execution logic.

## Agent Instructions

### Activation

When the user requests UI component generation:

1. **Validate request scope**: Confirm it's a frontend component/page request (not backend/API)
2. **Load orchestrator**: Execute `scripts/orchestrator.js` with user request
3. **Follow pipeline**: Execute stages 1-9 sequentially (each stage may load additional resources)
4. **Progressive disclosure**: Load reference docs and templates only when needed

### Execution Flow

**Stage 1: Intent Analysis** (`scripts/stage_1_intent.py`)
- Parse natural language request
- Classify intent: `generate_component`, `generate_page`, `modify_component`
- Extract component type, modifiers, target directory
- Resolve ambiguities with clarifying questions
- Initialize `UIBuilderContext` state object
- **Reference**: Keyword classification logic in script

**Stage 2: Project Detection** (`scripts/stage_2_detection.py`)
- Scan for `package.json`, `tsconfig.json`, `next.config.js`, etc.
- Detect framework (React, Next.js App/Pages Router, Vite, CRA)
- Read preferences (TypeScript, CSS strategy, formatting rules)
- Identify component directory (`src/components/`, `app/components/`)
- Handle Syncfusion license key (prompt if missing, inject `registerLicense()`)
- **Reference**: Project config files

**Stage 3: Layout Confirmation** (`scripts/stage_3_layout.py`)
- Present 2-3 layout variants specific to component type
- Ask clarifying questions (fields, features, styling)
- User confirms structure and requirements
- Validate selections
- **Reference**: `references/LAYOUT-VARIANTS.md` for variant catalog

**Stage 4: Component Picking** (`scripts/stage_4_components.py`)
- Map layout elements to Syncfusion components
- Query Syncfusion skills library for available components
- Present component selections with explanations
- User confirms or selects alternatives
- **Reference**: `references/SYNCFUSION-MAPPING.md` for component mapping

**Stage 5: Preview Generation** (`scripts/stage_5_preview.py`)
- Generate self-contained HTML preview
- Determine delivery mechanism (Webview, file, or markdown)
- Show responsive breakpoints, accessibility features
- User approves or requests modifications
- **Reference**: Preview templates in script

**Stage 6: Code Generation** (`scripts/stage_6_codegen.py`)
- Generate `.tsx` component with semantic HTML
- Create CSS stylesheet (CSS Modules, Tailwind, or inline)
- Generate TypeScript interfaces for props and state
- Add JSDoc documentation and usage comments
- Include validation logic, error handling, event handlers
- **Reference**: `references/EXAMPLES.md` for code patterns

**Stage 7: Web Standards Validation** (`scripts/stage_7_validation.py`)
- Validate WCAG 2.1 AA compliance (semantic HTML, ARIA, keyboard nav, contrast)
- Check security (input sanitization, no XSS vulnerabilities)
- Verify performance (React.memo, lazy loading)
- Validate SEO markup (heading hierarchy, semantic structure)
- Auto-fix common issues
- Present compliance report
- **Reference**: `references/WEB-STANDARDS.md` for validation rules

**Stage 8: Dependency Management** (`scripts/stage_8_dependencies.py`)
- Detect required Syncfusion packages
- Check existing `package.json` for version conflicts
- Resolve conflicts (upgrade, keep, compromise)
- Run `npm install` (or yarn/pnpm)
- Verify installation success
- **Reference**: Package resolution logic in script

**Stage 9: Code Insertion** (`scripts/stage_9_insertion.py`)
- Insert generated files into project
- Update index/barrel exports
- Inject Syncfusion license registration (if needed)
- Verify build compiles successfully
- Present success report with file locations
- **Reference**: `references/TROUBLESHOOTING.md` for error handling

### Boundary Rules (Critical)

**AI agents executing this skill MUST:**

1. **Only modify frontend files** — Never touch `app/api/`, `pages/api/`, `server/`, `backend/` directories
2. **Never generate async server functions** — No Route Handlers, Server Actions, or backend code
3. **Never read/write secrets** — Exception: Write `SYNCFUSION_LICENSE_KEY` to `.env.local` when user provides it
4. **Use mock data until API wiring** — Use `useState` with hardcoded samples, no `fetch()` to real endpoints
5. **Redirect backend requests** — If user asks for backend work, respond: *"This skill generates frontend UI only. The backend integration is your application's responsibility. I can generate the frontend component—shall I proceed?"*

### Error Handling

If any stage fails:
1. **Capture error** in `UIBuilderContext.stageResults[stageId].error`
2. **Attempt recovery** (e.g., retry with fallback options)
3. **If unrecoverable**, present error to user with troubleshooting steps
4. **Rollback checkpoint** — Option to revert to last successful stage
5. **Consult**: `references/TROUBLESHOOTING.md` for common errors

### Resource Loading Strategy

**Optimize context by loading on-demand:**

| Resource | When to Load |
|----------|--------------|
| `scripts/orchestrator.py` | On skill activation |
| `scripts/stage_*.py` | When executing that stage |
| `scripts/context.py`, `scripts/README.md` | On skill activation (shared utilities) |
| `references/*.md` | Only when detailed info needed (see table below) |

**Reference Documentation Loading:**

| Reference File | Load When | Purpose |
|----------------|-----------|---------|
| `REFERENCE.md` | Need technical details on stages | Complete stage-by-stage technical reference |
| `STAGES.md` | Need workflow decision trees | Step-by-step workflows with decision logic |
| `SYNCFUSION-MAPPING.md` | Stage 4: Component Picking | Component mapping and selection guides |
| `WEB-STANDARDS.md` | Stage 7: Validation | WCAG, security, performance checklists |
| `LAYOUT-VARIANTS.md` | Stage 3: Layout Confirmation | Pre-designed variant catalog |
| `EXAMPLES.md` | Need code examples or patterns | Real generated code samples |
| `TROUBLESHOOTING.md` | Errors or user questions | Error solutions and FAQ |

**Result**: Core skill loads ~5-10KB, full documentation available but not loaded unless needed.

## Configuration

### Project Setup Detection

The skill auto-detects:
- **Framework**: React, Next.js (App/Pages Router), Vite, CRA
- **Language**: TypeScript or JavaScript
- **Styling**: CSS Modules, Tailwind, inline styles, or CSS-in-JS
- **Formatting**: Prettier/ESLint rules (indentation, quotes, semicolons)
- **Structure**: Component directory location

### Customization Options

Users can override detected settings:
- Component output directory
- TypeScript vs JavaScript
- CSS strategy (Modules, Tailwind, inline)
- Theme (light, dark, custom)
- Accessibility level (WCAG AA, AAA, or custom)
- Named vs default exports

### Syncfusion License

**Required for production use**. The skill handles license key management:

1. **Check** for existing `SYNCFUSION_LICENSE_KEY` in `.env.local`
2. **Prompt user** if missing: *"Get a free Community License at https://www.syncfusion.com/account/manage-trials"*
3. **If provided**, write to `.env.local` and inject `registerLicense()` into app entry point
4. **If skipped**, warn that watermark will appear

## Standards & Best Practices

All generated code follows:

- **ES6+ syntax** (const/let, arrow functions, destructuring)
- **TypeScript** (optional but recommended, full type safety)
- **Semantic HTML5** (proper element usage, heading hierarchy)
- **WCAG 2.1 AA** (ARIA labels, keyboard nav, color contrast ≥4.5:1)
- **Responsive design** (mobile-first, breakpoints at 320px, 768px, 1024px)
- **Performance** (React.memo, lazy loading, optimized re-renders)
- **Security** (input sanitization, no XSS, no hardcoded secrets)
- **SEO-friendly markup** (semantic structure, proper headings)

## Examples

See `references/EXAMPLES.md` for complete before/after code samples.

**Quick Reference:**

- **Login form**: TextBox (email), TextBox (password), CheckBox (remember), Button (submit)
- **Data table**: DataGrid with sorting, filtering, pagination, row selection
- **Dashboard**: Multiple components orchestrated (header, sidebar, main content, footer)
- **Registration wizard**: Multi-step form with progress indicator and validation

## Troubleshooting

**Common Issues:**

| Issue | Solution |
|-------|----------|
| "Project type not detected" | Ensure `package.json` exists with React dependency |
| "Syncfusion license banner appears" | Add license key via Stage 2 prompt |
| "Build fails after insertion" | Check `references/TROUBLESHOOTING.md` for conflict resolution |
| "Component not rendering" | Verify import paths and ensure parent component imports correctly |

**Full guide**: See `references/TROUBLESHOOTING.md`

## Additional Resources

All reference documentation follows progressive disclosure—load only when needed:

| Reference File | Purpose | When to Use |
|----------------|---------|-------------|
| `references/REFERENCE.md` | Complete technical reference for all 9 stages | Need detailed stage specifications |
| `references/STAGES.md` | Step-by-step workflows with decision trees | Understanding workflow logic |
| `references/SYNCFUSION-MAPPING.md` | Component mapping reference guide | During Stage 4 (Component Picking) |
| `references/WEB-STANDARDS.md` | WCAG 2.1 AA, security, performance rules | During Stage 7 (Validation) |
| `references/LAYOUT-VARIANTS.md` | Full catalog of form/table/nav variants | During Stage 3 (Layout Confirmation) |
| `references/EXAMPLES.md` | Real before/after generated code samples | For learning or reference |
| `references/TROUBLESHOOTING.md` | Common errors, debugging tips, FAQ | When errors occur or user has questions |

**Note**: Each reference file includes a table of contents and is under 800 lines for optimal loading.

## License & Attribution

- **UI Builder Skill**: Proprietary (Syncfusion)
- **Syncfusion Components**: Requires valid Syncfusion license (Community, Trial, or Commercial)
- **Official Components Repository**: https://github.com/syncfusion/react-ui-components-skills

## Support

For issues or questions:
1. Check `references/TROUBLESHOOTING.md` for common problems
2. Verify your project meets prerequisites (React 18+, Node.js 18+)
3. Ensure Syncfusion license is valid and registered
4. Review generated code compliance report for warnings

---

**Version**: 1.0.0 (Phase 1 MVP)  
**Last Updated**: April 15, 2026  
**Target Release**: Q2 2026
