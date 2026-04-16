---
name: ui-builder-skill
description: AI-driven React UI component generator using Syncfusion. Guides AI through 8-stage orchestrated workflow to generate production-ready components with WCAG 2.1 AA accessibility and responsive design. No manual API knowledge required.
license: Proprietary
compatibility: React 18+, Next.js 13+, Vite, Create React App; Node.js 18+; Syncfusion license
metadata:
  version: "2.0"
  architecture: "Agent Skills Spec Compliant"
  target-release: "Q2 2026"
  supported-frameworks: "React 18+, Next.js 13+ (App Router & Pages Router), Vite, Create React App"
allowed-tools: read write
---

# UI Builder Skill

## Overview

The **UI Builder Skill** is a frontend-only React component generator that orchestrates an AI agent through 8 stages to generate production-ready UI components powered by Syncfusion.

This spec is **Agent Skills Specification compliant** with one-level-deep file references for optimal context loading by AI agents.

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
├── SKILL.md                              # This file (Agent Skills spec compliant)
├── references/                           # One-level-deep stage guides + support docs
│   ├── stage-1-intent-analysis.md        # Stage 1 guidance document
│   ├── stage-2-project-detection.md      # Stage 2 guidance document
│   ├── stage-3-layout-confirmation.md    # Stage 3 guidance document (USER DECISION)
│   ├── stage-4-component-picking.md      # Stage 4 guidance document (FULLY AUTO)
│   ├── stage-6-code-generation.md        # Stage 6 guidance document
│   ├── stage-7-validation.md             # Stage 7 guidance document (USER DECISION)
│   ├── stage-8-dependencies.md           # Stage 8 guidance document
│   ├── SYNCFUSION-MAPPING.md             # Component skills catalog
│   ├── LAYOUT-VARIANTS.md                # Pre-designed variant options (2 per type)
│   ├── WEB-STANDARDS.md                  # WCAG 2.1 AA + security + performance rules
│   ├── CODE-BLOCKS.md                    # Prebuilt code patterns
│   ├── EXAMPLES.md                       # Real generated code samples
│   └── TROUBLESHOOTING.md                # Error solutions & FAQ
└── assets/                               # Static resources
    └── validation-rules.md               # Validation checklist for Stage 7
```

**Note:** No scripts/ directory (removed in v2.0). All guidance is AI-native markdown.
Old stages 5 and 9 (preview + insertion) removed. Stages renumbered 1,2,3,4,6,7,8.

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

## How It Works: 8-Stage AI Orchestration (Stateless)

The skill orchestrates **8 stages of pure AI reasoning** with **only 2 user decision points**.

**Key Architecture:**
- **No UIBuilderContext**: Stateless design; conversation history maintains state
- **Pure AI reasoning**: Each stage reads guidance docs, analyzes context, makes decisions
- **2 user decisions**: Stage 3 (layout variant) + Stage 7 (validation result)
- **6 fully automated stages**: 1, 2, 4, 6, 8 + final code insertion
- **Stage 4 is fully automatic**: AI picks components without user interaction

```
User Request
    ↓
[Stage 1: Intent Analysis] 
  AI reads query → identifies component type & features
    ↓
[Stage 2: Project Detection]
  AI scans project → detect framework, language, preferences
    ↓
[Stage 3: Layout Confirmation] ⭐ USER DECISION #1
  AI presents 2 layout variants
  User chooses → locks layout
    ↓
[Stage 4: Component Picking] (FULLY AUTOMATIC)
  AI maps layout to Syncfusion components
  No user interaction needed
    ↓
[Stage 6: Code Generation]
  AI generates .tsx, .css, TypeScript interfaces
  With accessibility + responsive design built-in
    ↓
[Stage 7: Validation] ⭐ USER DECISION #2
  AI validates WCAG 2.1 AA + security + performance
  Binary result: PASS ✓ or FAIL ✗
  User confirms or overrides
    ↓
[Stage 8: Dependencies]
  AI detects required packages
  Presents npm install command or runs it
    ↓
[Code Insertion]
  AI inserts files into project
  Updates imports, verifies build
    ↓
✓ Complete
```

**Stage Descriptions:**

- **Stage 1 (Intent Analysis)**: Parse user query, identify component type and features. Read: `references/stage-1-intent-analysis.md`
- **Stage 2 (Project Detection)**: Auto-detect framework, language, CSS strategy, component directory. Read: `references/stage-2-project-detection.md`
- **Stage 3 (Layout Confirmation)**: Present 2 pre-designed variants; user confirms choice. Read: `references/stage-3-layout-confirmation.md` + `references/LAYOUT-VARIANTS.md`
- **Stage 4 (Component Picking)**: Map layout elements to Syncfusion components (FULLY AUTOMATED). Read: `references/stage-4-component-picking.md` + `references/SYNCFUSION-MAPPING.md`
- **Stage 6 (Code Generation)**: Generate React with accessibility + responsive design. Read: `references/stage-6-code-generation.md` + `references/CODE-BLOCKS.md`
- **Stage 7 (Validation)**: Validate WCAG 2.1 AA, security, performance. Binary pass/fail. Read: `references/stage-7-validation.md` + `assets/validation-rules.md`
- **Stage 8 (Dependencies)**: Detect packages, resolve conflicts, prepare install command. Read: `references/stage-8-dependencies.md`
- **Code Insertion**: AI inserts files, updates imports, verifies build succeeds.

**User Interaction Summary:**

| Stage | Interaction |
|-------|-------------|
| 1 | None (AI analyzes) |
| 2 | Confirm auto-detected settings |
| 3 | ⭐ Choose layout variant (2 options) |
| 4 | None (AI decides components) |
| 6 | None (AI generates) |
| 7 | ⭐ Confirm validation result (pass/fail/override) |
| 8 | Optional (confirm npm install) |
| Insertion | None (AI executes) |

**Total user decisions: 2**. Rest fully automated with AI reasoning + guidance docs.

## Agent Instructions

### When User Requests UI Component Generation

1. **Validate scope**: Confirm request is for frontend components (not backend/API)
2. **Load guidance**: Read `stage-1-intent-analysis.md` to understand Stage 1
3. **Execute 8-stage flow**: Follow the orchestration flow shown above
4. **Progressive disclosure**: Load stage guides on-demand; load support references only when needed
5. **Maintain conversation history**: Each stage reads previous decisions from conversation context (stateless)

### Stage Execution & Reference Loading

**Stage 1: Intent Analysis**
- Read: `references/stage-1-intent-analysis.md`
- Task: Parse user query, identify component type, resolve ambiguities
- Output: Component type + modifiers + target directory

**Stage 2: Project Detection**
- Read: `references/stage-2-project-detection.md`
- Task: Auto-detect React framework, language, CSS strategy, formatting rules
- Output: Project configuration + user confirmation

**Stage 3: Layout Confirmation** ⭐ USER DECISION #1
- Read: `references/stage-3-layout-confirmation.md` + `references/LAYOUT-VARIANTS.md`
- Task: Present 2 pre-designed variants; ask clarifying questions
- Output: User confirms variant → locks layout specification

**Stage 4: Component Picking** (FULLY AUTOMATED)
- Read: `references/stage-4-component-picking.md` + `references/SYNCFUSION-MAPPING.md`
- Task: Map layout elements to Syncfusion components automatically
- Output: Component mapping locked (no user interaction)

**Stage 6: Code Generation**
- Read: `references/stage-6-code-generation.md` + `references/CODE-BLOCKS.md`
- Task: Generate React .tsx, CSS, TypeScript interfaces
- Ensure: WCAG 2.1 AA accessibility, responsive design, validation logic
- Output: Generated files ready for review

**Stage 7: Validation** ⭐ USER DECISION #2
- Read: `references/stage-7-validation.md` + `assets/validation-rules.md` + `references/WEB-STANDARDS.md`
- Task: Validate against WCAG 2.1 AA, security, performance standards
- Auto-apply fixes where possible
- Output: Binary result (PASS ✓ or FAIL ✗) → user confirms or overrides

**Stage 8: Dependencies**
- Read: `references/stage-8-dependencies.md`
- Task: Detect required Syncfusion packages, resolve version conflicts
- Output: npm install command or auto-install

**Code Insertion**
- Task: Insert generated files into project, update imports, verify build
- Output: Success report with file paths

### Key Differences from v1.0 (Old Spec)

| Aspect | Old (v1.0) | New (v2.0) |
|--------|-----------|-----------|
| **Architecture** | 9 Python scripts + UIBuilderContext state object | 8 pure AI reasoning stages + conversation history |
| **User Interaction** | Multiple confirmations per stage | Only 2 decisions (Stage 3 + Stage 7) |
| **Component Picking** | User reviews and confirms | Fully automated (AI decides) |
| **File Structure** | `scripts/` directory with Python executables | `references/` with markdown guidance docs |
| **Scope** | Includes preview stage + insertion script | Uses AI's native file operations for insertion |
| **State Management** | Unified UIBuilderContext object | Stateless; conversation history = state |

### Boundary Rules (CRITICAL)

**AI agents executing this skill MUST:**

1. **Frontend only**: Never generate backend code (API routes, database schemas, middleware)
2. **Mock data only**: Use `useState` with hardcoded samples; no `fetch()` to real APIs
3. **No secrets**: Exception: `.env.local` for `SYNCFUSION_LICENSE_KEY` when user provides
4. **React components only**: Generate `.tsx`/`.jsx` files in component directories
5. **Redirect backend requests**: *"This skill generates frontend UI only. Backend integration is your app's responsibility. Ready to generate the frontend?"*

### Error Handling

If any stage fails:

1. **Retry once** with same approach
2. **If retry fails**, attempt workaround or skip to next stage
3. **Notify user** with error message from stage output
4. **Offer recovery**: *"Would you like to go back to Stage 3 and choose a different layout?"*
5. **Reference**: `references/TROUBLESHOOTING.md` for common errors

### Resource Loading Strategy (Progressive Disclosure)

**Load SKILL.md first** (you're reading it now) ~400 lines

**Load stage guides on-demand** (each <200 lines):
- `stage-1-intent-analysis.md` → During Stage 1
- `stage-2-project-detection.md` → During Stage 2
- etc.

**Load support references only when needed**:
- `LAYOUT-VARIANTS.md` → When presenting Stage 3 options
- `SYNCFUSION-MAPPING.md` → When picking components in Stage 4
- `WEB-STANDARDS.md` → When validating in Stage 7
- `CODE-BLOCKS.md` → When generating code in Stage 6
- `EXAMPLES.md` → When user asks for examples
- `TROUBLESHOOTING.md` → When errors occur
- `assets/validation-rules.md` → When validating in Stage 7

**Result**: Initial load ~400 lines (SKILL.md only). Full spec available on-demand, never exceeding Agent Skills context limits.

## Configuration & User Customization

### Auto-Detected Settings

During **Stage 2 (Project Detection)**, AI automatically detects:

- **Framework**: React, Next.js (App Router / Pages Router), Vite, Create React App
- **Language**: TypeScript (if `tsconfig.json` exists) or JavaScript
- **Styling**: CSS Modules, Tailwind CSS, CSS-in-JS, or inline styles
- **Formatting**: Prettier/ESLint rules (indentation, quotes, semicolons)
- **Component Directory**: `src/components/`, `app/components/`, or similar

### User Override Options

In **Stage 2**, user can override any detected setting:

```
Detected Settings:
  Framework: Next.js 14 (App Router)
  Language: TypeScript
  CSS: CSS Modules
  Component Directory: app/components/

[Confirm] [Override Each] [Cancel]
```

### Syncfusion License Configuration

The skill handles license key setup:

1. **Check** for existing `SYNCFUSION_LICENSE_KEY` in `.env.local`
2. **If missing**, prompt user: *"Get a free Community License at https://www.syncfusion.com/account/manage-trials"*
3. **If provided**, write to `.env.local` + inject `registerLicense()` in app entry
4. **If skipped**, proceed but warn that watermark will appear in preview

---

## Code Generation Standards

All generated code includes:

### Accessibility (WCAG 2.1 AA)
- ✅ Semantic HTML5 (`<form>`, `<label>`, `<input>`, `<button>`)
- ✅ ARIA labels and descriptions
- ✅ Keyboard navigation (tab order, focus management)
- ✅ Color contrast ≥ 4.5:1
- ✅ Focus indicators on interactive elements

### Responsive Design
- ✅ Mobile-first CSS (320px base, then scale up)
- ✅ Flexbox/Grid layouts (no fixed widths)
- ✅ Media queries at 768px, 1024px+ breakpoints
- ✅ Touch-friendly buttons (44x44px minimum)

### Security
- ✅ Input validation and sanitization
- ✅ No `dangerouslySetInnerHTML` without sanitization
- ✅ No hardcoded secrets
- ✅ No XSS vulnerabilities

### Performance
- ✅ React.memo for stable components
- ✅ useCallback for event handlers
- ✅ Lazy loading for large components
- ✅ Optimized re-renders

### TypeScript & Types
- ✅ Full type coverage (no `any` types)
- ✅ Props interfaces with JSDoc
- ✅ Event handler signatures
- ✅ State type annotations

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

### Quick Reference by Use Case

| Need | Reference File |
|------|-----------------|
| Understanding workflow | This SKILL.md file |
| How Stage X works | `references/stage-X-*.md` |
| Component options | `references/SYNCFUSION-MAPPING.md` |
| Layout templates | `references/LAYOUT-VARIANTS.md` |
| Code patterns | `references/CODE-BLOCKS.md` |
| Full code examples | `references/EXAMPLES.md` |
| Validation rules | `assets/validation-rules.md` |
| Accessibility/security | `references/WEB-STANDARDS.md` |
| Troubleshooting | `references/TROUBLESHOOTING.md` |

### Architecture Compliance

✅ **Agent Skills Specification Compliant v2.0**
- YAML frontmatter with metadata
- One-level-deep file structure (no nested references between guides)
- Progressive disclosure (core <500 lines, details on-demand)
- Markdown-based guidance (AI-native)
- Clear scope boundaries (frontend only)

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

**Version**: 2.0 (AI-Native Architecture)  
**Last Updated**: April 16, 2026  
**Next Phase**: Observability, multi-language support, advanced orchestration patterns
