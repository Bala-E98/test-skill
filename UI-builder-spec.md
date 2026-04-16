# UI Builder Skill — Project Specification

## 1. Executive Summary

> **Purpose:** A single, unified **frontend-only** skill that orchestrates production-ready **React UI component and page generation** — such as login forms, ecommerce dashboards, portfolios, and more — directly inside existing projects using VS Code, Cursor, or any agent-supported editor, powered by Syncfusion components — with zero manual API knowledge required.
>
> **Scope:** This skill operates **exclusively on the frontend layer**. It generates React components, CSS stylesheets, and TypeScript interfaces. It does not generate backend code, API routes, database schemas, server logic, or any non-frontend artifacts. See Section 1.1 for the full scope boundary.
>
> **Architecture:** The UI Builder Skill contains all orchestration logic (9 sequential stages) and references external components/instructions. Syncfusion components are sourced directly from the official **[syncfusion/react-ui-components-skills](https://github.com/syncfusion/react-ui-components-skills)** repository — production-ready and officially maintained. Install with:
> ```bash
> npx skills add syncfusion/react-ui-components-skills -y
> ```

**Status:** Ready for Implementation  
**Target Release:** Q2 2026  
**Primary Users:** React developers, frontend engineers, rapid prototypers

---

### 1.1 Scope & Boundaries

> ⚠️ **This section is critical for AI agents acting on this spec. Read before executing any stage.**

This skill is a **frontend React code generator**. The table below defines the hard boundaries of what this skill does and does not do.

#### ✅ In Scope — What This Skill Generates

| Category | Examples |
|---|---|
| **React components** | `.tsx` / `.jsx` functional components with hooks |
| **CSS stylesheets** | `.module.css`, Tailwind classes, inline style objects |
| **TypeScript interfaces** | Props interfaces, state types, event handler types |
| **Syncfusion component integration** | Correct imports, props, and event wiring for `@syncfusion/ej2-react-*` packages |
| **Client-side form validation** | `useState`-based validation logic, error message rendering |
| **Accessibility markup** | ARIA attributes, semantic HTML, focus management within the component |
| **Responsive CSS** | Media queries, mobile-first breakpoints within stylesheets |
| **Component index exports** | Updating `index.ts` barrel files for clean imports |
| **Syncfusion license injection** | `registerLicense()` call in the frontend app entry point |
| **Frontend data-fetching hooks** *(Phase 3)* | `useEffect`/`useQuery`-based hooks for connecting components to APIs |

#### ❌ Out of Scope — What This Skill Never Generates

| Category | Examples | Who Is Responsible |
|---|---|---|
| **Backend / server code** | API routes, Express handlers, Next.js Route Handlers (`app/api/`), server actions | Consuming application |
| **Database layer** | Prisma schemas, SQL queries, ORM models, migrations | Consuming application |
| **Authentication logic** | JWT handling, session management, OAuth provider config, middleware | Consuming application |
| **Server-side validation** | Backend input validation, sanitization on the server | Consuming application |
| **Document `<head>` modifications** | `<meta>` tags, Open Graph tags, canonical URLs, `<title>` | Consuming app's layout file (e.g., Next.js Metadata API) |
| **Routing configuration** | `next.config.js` routes, React Router setup, URL structure | Consuming application |
| **Environment secrets** | API keys, database URLs, auth secrets | Developer / DevOps |
| **Infrastructure / deployment** | Dockerfiles, CI/CD pipelines, hosting config | DevOps |
| **Non-React frameworks** *(Phase 1)* | Vue, Angular, Svelte, server-rendered templates | Future phases |

#### 🔶 Boundary Rules for AI Agents

When executing this skill, an AI agent **must**:

1. **Only create or modify files in the frontend component directory** (detected in Stage 2). Never touch `app/api/`, `pages/api/`, `server/`, `backend/`, or any directory outside the frontend source tree.
2. **Never generate `async` server functions**, Route Handlers, Server Actions, or any code that runs outside the browser.
3. **Never read or write environment secrets**. The only environment variable interaction allowed is writing `SYNCFUSION_LICENSE_KEY` to `.env.local` when the user explicitly provides the key (Stage 2, Section 5.6.5).
4. **Treat all data as mock/local state** until Phase 3 API templates are implemented. Use `useState` with hardcoded sample data, never `fetch()` calls to real endpoints.
5. **If a user request implies backend work** (e.g., "connect this form to my database", "add an API endpoint"), respond with: *"This skill generates frontend UI only. The backend integration is your application's responsibility. I can generate the frontend form/component — shall I proceed?"*

---

### 1.2 Enterprise Integration Guide

This section is for enterprise architecture teams evaluating whether this skill fits into their tech stack and development process.

#### Overview: The Skill as a Frontend Code Generation Layer

The UI Builder Skill sits between your **design requirements** and your **React component layer**. It is intentionally scoped to not touch backend, routing, or infrastructure concerns — leaving those to your existing enterprise systems.

```
Enterprise Architecture Layers
═══════════════════════════════════════════════════════════════

┌─ Infrastructure / DevOps ─────────────────────────────────────┐
│  (Docker, Kubernetes, CI/CD, deployment) — YOUR RESPONSIBILITY│
└────────────────────────────────────────────────────────────────┘

┌─ Backend / Services Layer ────────────────────────────────────┐
│  (APIs, databases, auth, logging) — YOUR RESPONSIBILITY       │
└────────────────────────────────────────────────────────────────┘

┌─ State Management / Data Fetching ───────────────────────────┐
│  (Redux, Zustand, React Query, etc.)                          │
│  Phase 1: Mock data (useState)   — UI BUILDER               │
│  Phase 3: Data hooks (useQuery)  — UI BUILDER (partial)     │
│  Integration to real APIs        — YOUR RESPONSIBILITY       │
└────────────────────────────────────────────────────────────────┘

┌─ Component Layer ─────────────────────────────────────────────┐
│  (React components, TypeScript, styling)   ← UI BUILDER      │
│  [Generated by this skill]                                    │
└────────────────────────────────────────────────────────────────┘

┌─ Design / UX ──────────────────────────────────────────────────┐
│  (Design specs, accessibility standards, brand guidelines)    │
│  — PROVIDED BY YOUR TEAM                                      │
└────────────────────────────────────────────────────────────────┘
```

#### What Your Enterprise Provides

| Responsibility | Your Task | Example |
|---|---|---|
| **API contracts** | Define endpoint URLs, request/response shapes | `GET /api/v1/customers` returns `{ id, name, email, role }` |
| **Authentication** | JWT tokens, OAuth, SAML integration | Your auth service provides bearer token in Authorization header |
| **Authorization (RBAC)** | Define user roles and permissions | Your backend middleware enforces `can_view_customers: true` before serving data |
| **Data transformation** | Business logic between API response and component state | Convert ISO dates to display format, compute derived fields |
| **Error handling** | Global error boundaries, retry logic, offline handling | Your app handles 500 errors, network timeouts, 401 unauthorized |
| **Design system / tokens** | Brand colors, typography, spacing, component theme | Your design team maintains Syncfusion theme customization |
| **Security** | Input validation on backend, CSP headers, secure cookies | Server-side validation mirrors frontend rules; Syncfusion license key protected |
| **Performance** | Caching strategy, code splitting setup, monitoring | Your app implements service workers, bundle analysis, performance tracking |
| **Testing** | Unit/integration/E2E test strategy and infrastructure | Your QA team runs tests (UI Builder generates component structure, not tests) |

#### What the Skill Provides

| Responsibility | Skill Task | Benefit to Enterprise |
|---|---|---|
| **Component scaffolding** | Generates `.tsx` with props, state, event handlers | Saves 2-4 hours per component; consistent code quality |
| **Syncfusion integration** | Correct component imports, props, event bindings | Eliminates API documentation lookup; reduces component mistakes |
| **Accessibility** | WCAG 2.1 AA markup, ARIA labels, focus management | Compliance out-of-box; reduces QA cycles for a11y |
| **Responsive design** | Mobile-first CSS with tested breakpoints | Works across devices; no responsive redesign needed later |
| **TypeScript interfaces** | Properly typed props, events, and internal state | Type safety from day one; reduces runtime bugs |
| **Styling consistency** | Enforces project's CSS strategy (CSS Modules, Tailwind, etc.) | All components match project conventions automatically |

#### Worked Example: Enterprise Dashboard Integration

Here's how an enterprise team would use this skill to build a customer dashboard.

**Step 1: Your Backend Team Sets Up API**

```bash
# Your API endpoint (you provide this)
GET /api/v1/dashboard/customers
Authorization: Bearer <jwt_token>

Response:
{
  "data": [
    { "id": 1, "name": "Acme Corp", "status": "active", "revenue": 500000, "lastContact": "2026-04-10" }
  ],
  "pagination": { "total": 150, "page": 1, "limit": 10 },
  "meta": { "error": null }
}
```

**Step 2: UI Builder Generates Component**

```
User prompt: "Create a customer dashboard table with columns for name, status, revenue, and last contact date"

UI Builder generates:
  ✓ CustomerDashboard.tsx
    - DataGrid component from Syncfusion
    - Column definitions (name, status, revenue, lastContact)
    - Mock data for 10 customers in useState
    - Pagination UI (10 rows per page)
    - Sorting and filtering on columns
    - WCAG 2.1 AA compliant markup
    - Responsive design (mobile: single column, desktop: full table)
```

**Step 3: Your Frontend Team Wires to Real API (5-10 min task)**

```typescript
// CustomerDashboard.tsx — Generated by UI Builder
export const CustomerDashboard: React.FC = () => {
  const [customers, setCustomers] = useState<Customer[]>(MOCK_CUSTOMERS); // ← Replace this line
  
  // Your code adds:
  useEffect(() => {
    fetchCustomers(); // Call your API
  }, []);

  const fetchCustomers = async () => {
    try {
      const response = await fetch('/api/v1/dashboard/customers', {
        headers: { Authorization: `Bearer ${getToken()}` }
      });
      const data = await response.json();
      setCustomers(data.data); // Use real data
    } catch (error) {
      // Your error handling
    }
  };

  // Rest of component (auto-generated by UI Builder) stays the same ✓
  return (
    <DataGridComponent dataSource={customers} ...>
      {/* Columns auto-generated */}
    </DataGridComponent>
  );
};
```

**Step 4: Your Ops Team Deploys**

- Component is production-ready from day 1
- TypeScript types ensure no runtime surprises
- Accessibility compliance reduces support tickets
- Responsive design works on all enterprise devices
- Syncfusion license is managed via environment variable

**Total time saved vs. manual development:**
- Manually coding DataGrid component: 2-3 hours
- UI Builder + 5-min wiring: 10 minutes
- **Savings: 2.5 hours per component**

---

#### Enterprise Scenarios

| Scenario | UI Builder Role | Your Responsibility |
|---|---|---|
| **Rapid MVP dashboard** | Generate all UI components in 1 day | Wire data sources, deploy to staging |
| **Design system consistency** | Enforce accessibility & responsive design across team | Maintain design tokens, manage component library versioning |
| **Onboarding new feature** | Generate form/table scaffolding in minutes | Implement business logic, validation rules, API calls |
| **Compliance audit** | Generated code passes WCAG 2.1 AA and security checks out-of-box | You verify server-side validation, auth config, infrastructure |
| **Large team scaling** | Junior devs generate components quickly without deep React knowledge | Senior devs review and wire to real APIs; maintain code standards |

---

#### When NOT to Use This Skill

- ❌ You need a custom component not in Syncfusion (use manual React)
- ❌ You have a highly custom design system (modify generated code post-generation)
- ❌ You need real-time collaborative components (use specialized tools)
- ❌ You need generated tests (wait for Phase 3, or write manually)

---

#### Integration Checklist for Enterprise Teams

- [ ] **Authentication:** Confirm JWT/OAuth middleware is in place
- [ ] **API contracts:** Define backend endpoints before UI generation begins
- [ ] **Design tokens:** Customize Syncfusion theme to match your brand
- [ ] **Error handling:** Establish global error boundary and retry strategy
- [ ] **Performance budget:** Set lighthouse targets; monitor bundle size
- [ ] **Testing strategy:** Decide on E2E test coverage (Cypress, Playwright, etc.)
- [ ] **Security scan:** Run OWASP/dependency audit on generated component dependencies
- [ ] **Accessibility validation:** Auditors verify WCAG 2.1 AA compliance
- [ ] **Deployment:** Test in staging environment before production rollout

---

## 2. Agent Skills Implementation

### 2.1 Directory Structure (Agent Skills Spec Compliant)

The UI Builder Skill follows the [Agent Skills Specification](https://agentskills.io/specification) for optimal agent loading and progressive disclosure:

```
ui-builder-skill/
├── SKILL.md                              # Required: Metadata + Instructions
├── scripts/                              # Executable code — JavaScript (Node.js)
│   ├── orchestrator.js                   # Main orchestrator entry point
│   ├── stage-1-intent.js through stage-9-insertion.js  # Each stage
│   ├── context.js                        # UIBuilderContext state management
│   ├── utils.js                          # Shared utilities & helpers
│   └── config.js                         # Configuration & defaults
├── references/                           # Documentation (on-demand loading)
│   ├── REFERENCE.md, STAGES.md, SYNCFUSION-MAPPING.md
│   ├── WEB-STANDARDS.md, LAYOUT-VARIANTS.md, EXAMPLES.md
│   └── TROUBLESHOOTING.md
└── assets/                               # Static resources
    ├── templates/                        # React component & CSS templates (.tsx, .module.css)
    ├── data/                             # Reference data (.json)
    ├── examples/                         # Sample generated output
    └── images/                           # Diagrams & visuals (.png)
```

### 2.2 Progressive Disclosure Pattern

The skill optimizes context loading by separating content into phases:

| Phase | File | Load Trigger | Content |
|-------|------|--------------|---------|
| **Startup** | SKILL.md | Agent startup | name, description, compatibility (metadata only) |
| **Activation** | scripts/orchestrator.js | Skill activated | Main entry point + stage orchestration (~5KB) |
| **Execution** | scripts/stage-X.js | Stage runs | Individual stage code (~3-8KB per stage) |
| **Reference** | references/*.md | On-demand | Detailed documentation (~10-50KB per file) |
| **Generation** | assets/templates/ | Code generation | Template files (~2-5KB each) |
| **Validation** | assets/data/*.json | Validation phase | Rules, mappings, keywords (~5-20KB) |

**Result:** Core skill loads ~5KB, full documentation available on-demand (no context waste)

### 2.3 SKILL.md Format (Entry Point)

```yaml
---
name: ui-builder-skill
description: Generates production-ready React UI components using Syncfusion. 
             Orchestrates 9 sequential stages from intent analysis to code insertion. 
             Use for creating login forms, dashboards, data tables, navigation components, 
             and more. Supports React 18+, Next.js 13+, Vite, and Create React App with 
             full TypeScript, WCAG 2.1 AA accessibility, and web standards compliance.
license: Proprietary
compatibility: Requires Node.js 18+, npm/yarn/pnpm, React 18+ projects (Next.js 13+, Vite, or Create React App)
metadata:
  author: your-org
  version: "1.0.0"
  stages: "9"
  supported-frameworks: "React 18+, Next.js 13+, Vite, Create React App"
allowed-tools: bash npm read write
---
```

Followed by skill instructions that reference `scripts/orchestrator.js` and documentation in `references/`.

### 2.4 System Components

1. **UI Builder Skill** (Main Orchestrator)
   - **Entry File:** `scripts/orchestrator.js`
   - Single entry point that processes user requests end-to-end
   - Integrates with VS Code, Cursor, and other agent-supported editors
   - Interprets natural language requests to identify component requirements
   - Orchestrates 9 sequential execution stages internally
   - Maintains unified state throughout workflow (`UIBuilderContext` from `scripts/context.js`)
   - Returns production-ready code and integration verification

2. **Internal Orchestration Stages** (Files in `scripts/`)
   - **Stage 1** (`stage-1-intent.js`) — Intent Analysis & Setup
   - **Stage 2** (`stage-2-detection.js`) — Project Detection & Configuration
   - **Stage 3** (`stage-3-layout.js`) — Layout Confirmation Workflow
   - **Stage 4** (`stage-4-components.js`) — Component Picking
   - **Stage 5** (`stage-5-preview.js`) — Preview Generation
   - **Stage 6** (`stage-6-codegen.js`) — Code Generation
   - **Stage 7** (`stage-7-validation.js`) — Web Standards Compliance Validation
   - **Stage 8** (`stage-8-dependencies.js`) — Dependency Management
   - **Stage 9** (`stage-9-insertion.js`) — Code Insertion/Integration

3. **Referenced Instructions** (Files in `references/`)
   - **Layout Recommendation Engine** (referenced by Stage 3)
   - **Web Standards Checklist** (referenced by Stage 7)
   - **Best Practices Guidelines** (referenced throughout all stages)
   - **Syncfusion Component Mapping** (referenced by Stage 4)
   - **All documented in reference files** (loaded on-demand, not in memory)

4. **Syncfusion Components Library** (External Reference)
   - Official `syncfusion/react-ui-components-skills` repository
   - Pre-built, production-ready components for React
   - Maintained by Syncfusion team
   - Referenced during Stage 4 for component mapping
   - Installed during Stage 8 via npm

### 2.5 Data Flow Through Stages

```
User Request (Natural Language)
    ↓
┌────────────────────────────────────────────────────────────────┐
│  scripts/orchestrator.js (Main Entry - Loads UIBuilderContext) │
├────────────────────────────────────────────────────────────────┤
│                                                                  │
│  STAGE 1: scripts/stage-1-intent.js                            │
│    └─ Parse requirements, classify intent, initialize context   │
│    └─ References: assets/data/keywords.json                    │
│                                                                  │
│  STAGE 2: scripts/stage-2-detection.js                         │
│    └─ Scan user's project, detect framework                    │
│    └─ Read preferences (TypeScript, CSS strategy, formatting)  │
│                                                                  │
│  STAGE 3: scripts/stage-3-layout.js                            │
│    └─ Present 2-3 layout variants, confirm with user           │
│    └─ References: assets/data/component-variants.json          │
│    └─ References: references/LAYOUT-VARIANTS.md                │
│                                                                  │
│  STAGE 4: scripts/stage-4-components.js                        │
│    └─ Map layout elements to Syncfusion components             │
│    └─ References: assets/data/syncfusion-components.json       │
│    └─ References: references/SYNCFUSION-MAPPING.md             │
│                                                                  │
│  STAGE 5: scripts/stage-5-preview.js                           │
│    └─ Generate interactive HTML preview                        │
│    └─ Uses: assets/templates/ for skeleton                     │
│                                                                  │
│  STAGE 6: scripts/stage-6-codegen.js                           │
│    └─ Generate .tsx, .module.css, TypeScript interfaces        │
│    └─ Uses: assets/templates/component/, stylesheet/           │
│                                                                  │
│  STAGE 7: scripts/stage-7-validation.js                        │
│    └─ Validate WCAG 2.1 AA, security, performance, SEO         │
│    └─ References: assets/data/validation-rules.json            │
│    └─ References: references/WEB-STANDARDS.md                  │
│                                                                  │
│  STAGE 8: scripts/stage-8-dependencies.js                      │
│    └─ Detect packages, resolve conflicts, run npm install      │
│                                                                  │
│  STAGE 9: scripts/stage-9-insertion.js                         │
│    └─ Insert files into user's project, update imports         │
│    └─ Verify build success                                     │
│                                                                  │
└────────────────────────────────────────────────────────────────┘
    ↓
Success Response to User with File Locations and Checklist
```

### 2.6 UIBuilderContext — Unified State Schema

**Location:** `scripts/context.js` - Single source of truth passed through all 9 stages

The `UIBuilderContext` is the unified state object that every stage reads from and writes to. It must be fully initialized by Stage 1 and enriched by each subsequent stage. Full type definitions documented in `scripts/context.js`.

**Key Properties (High-Level Overview):**

```typescript
interface UIBuilderContext {
  // ── Stage 1: Intent Analysis ─────────────────────────────
  intent: 'generate_component' | 'generate_page' | 'modify_component' | 'unknown'
  componentType: string              // e.g., "form/login"
  modifiers: string[]                // e.g., ["feature:remember-me", "styling:dark"]
  executionPlan: StageId[]          // [2, 3, 4, 5, 6, 7, 8, 9]

  // ── Stage 2: Project Detection ───────────────────────────
  project: {
    framework: 'nextjs-app' | 'nextjs-pages' | 'vite' | 'cra'
    reactVersion: string
    language: 'typescript' | 'javascript'
    componentDir: string             // e.g., "app/components/"
    styleMethod: 'css-modules' | 'tailwind' | 'inline'
    packageManager: 'npm' | 'yarn' | 'pnpm'
  }

  // ── Stage 3: Layout Confirmation ─────────────────────────
  layout: {
    variantId: string                // e.g., "login-form-variant-b"
    fields: LayoutField[]            // Confirmed fields
    features: string[]               // Enabled features
    confirmed: boolean
  }

  // ── Stage 4: Component Picking ───────────────────────────
  componentMap: ComponentMapping[]   // Each field → Syncfusion component
  requiredPackages: string[]         // @syncfusion/* packages

  // ── Stage 5: Preview ─────────────────────────────────────
  preview: {
    deliveryMechanism: 'webview' | 'html-file' | 'markdown'
    userApproved: boolean
  }

  // ── Stage 6: Code Generation ────────────────────────────
  generatedFiles: GeneratedFile[]    // path, content, type
  componentName: string              // e.g., "LoginForm"
  targetFilePath: string

  // ── Stage 7: Validation ──────────────────────────────────
  validation: {
    passed: boolean
    violations: ValidationIssue[]    // WCAG, security, performance
    autoFixed: string[]
  }

  // ── Stage 8: Dependencies ────────────────────────────────
  dependencies: {
    toInstall: DependencyEntry[]
    conflicts: ConflictEntry[]
    installCompleted: boolean
  }

  // ── Stage 9: Insertion ───────────────────────────────────
  insertion: {
    filesCreated: string[]
    buildVerified: boolean
  }

  // ── Pipeline Control ─────────────────────────────────────
  currentStage: StageId              // 1-9
  pipelineStatus: 'running' | 'completed' | 'failed'
}
```

See `scripts/context.js` for complete type definitions and all properties.

type StageId = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;

interface LayoutField {
  id: string;
  label: string;
  type: 'text' | 'email' | 'password' | 'checkbox' | 'select' | 'button' | 'link' | 'custom';
  required: boolean;
}

interface ComponentMapping {
  fieldId: string;
  syncfusionComponent: string;    // e.g., "TextBoxComponent"
  importPackage: string;          // e.g., "@syncfusion/ej2-react-inputs"
  props: Record<string, unknown>;
  selectedByUser: boolean;
}

interface GeneratedFile {
  path: string;
  content: string;
  type: 'component' | 'stylesheet' | 'index' | 'test';
}

interface ValidationIssue {
  code: string;
  category: 'accessibility' | 'security' | 'performance' | 'seo' | 'html-semantics';
  severity: 'error' | 'warning';
  description: string;
  autoFixable: boolean;
}

interface DependencyEntry {
  package: string;
  version: string;
  type: 'production' | 'dev';
  peerDeps: Record<string, string>;
}

interface ConflictEntry {
  package: string;
  existingVersion: string;
  requiredVersion: string;
  resolution: 'upgrade' | 'keep' | 'compromise';
}

interface StageResult {
  stageId: StageId;
  status: 'success' | 'skipped' | 'failed';
  timestamp: string;
  durationMs: number;
}

interface RollbackCheckpoint {
  stageId: StageId;
  snapshot: Partial<UIBuilderContext>;
  filesBackedUp: string[];
  timestamp: string;
}
```

---

### 2.7 Specification Model: What UI Builder Provides

**Documentation:** See `references/REFERENCE.md` for detailed specification layer documentation.

The UI Builder acts as a **specification layer** that defines everything needed for code generation:

**Layout Specifications:**
- Field ordering and grouping
- Form structure (single-step vs. multi-step)
- Data table columns and interactions
- Navigation hierarchy and positioning
- Responsive breakpoints and adaptations

**Component Specifications:**
- Which Syncfusion components to use (TextBox, DataGrid, Button, etc.)
- Component props and configuration
- Event handlers and interactions
- Validation rules and error handling
- Placeholder text and labels

**Styling Specifications:**
- Theme (light/dark/custom)
- Color palette
- Typography (fonts, sizes, weights)
- Spacing and padding rules
- Border and shadow styles
- CSS class naming conventions (if using CSS Modules)

**Standards Specifications:**
- Accessibility level (WCAG 2.1 AA compliance)
- Responsive design targets (mobile-first, breakpoints)
- Code quality rules (TypeScript, JSDoc, etc.)
- Performance requirements (lazy loading, optimization)
- Security constraints (input sanitization, CSP compatibility)
- SEO requirements (semantic HTML, meta tags for public components)

**AI Agent's Role:**
Takes these UI Builder specifications and generates production-ready React code that:
1. Implements the exact layout specified
2. Uses the correct Syncfusion components with proper props
3. Applies all styling rules consistently
4. Follows web standards and best practices
5. Includes proper accessibility, error handling, and security features
6. Maintains code quality according to specified standards

**Example:**
```
UI Builder Input:
  Layout: "Login form with email, password, remember-me checkbox"
  Components: "Syncfusion TextBox for email/password, Checkbox for remember-me"
  Styling: "Dark theme, centered layout, 400px width"
  Standards: "WCAG 2.1 AA, mobile-first, TypeScript, semantic HTML"

↓

AI Agent Output:
  └─ LoginForm.tsx
     - Semantic HTML structure with proper form elements
     - Syncfusion TextBox & Checkbox with ARIA labels
     - Keyboard navigation support (tab order, focus management)
     - Dark theme CSS applied
     - Mobile-first responsive design
     - Form submission logic with input validation
     - Error messages with accessibility attributes
     - TypeScript interfaces for type safety
     - Touch-friendly buttons (44x44px minimum)
     - Color contrast ≥ 4.5:1 for all text
```

---

## 3. Supported UI Components & Pages

### 3.1 Component Categories

**Form Components:**
- Login forms (simple, with OAuth, with 2FA)
- Registration/signup forms
- Password reset/recovery forms
- Contact forms
- Subscription/newsletter forms
- Multi-step forms and wizards

**Data Display:**
- Data tables/grids with sorting, filtering, pagination
- Lists and listviews
- Charts and visualizations
- Tree views
- Kanban boards
- Calendar views

**Navigation:**
- Navigation bars/headers
- Side navigation/sidebars
- Breadcrumbs
- Tabs and tab navigation
- Pagination controls

**Common Patterns:**
- Modals and dialogs
- Toast notifications
- Dropdown menus
- Carousel/sliders
- Badges and tags
- Tooltips

**Page Templates:**
- Dashboard/analytics pages
- E-commerce product catalog
- E-commerce checkout flow
- Portfolio/showcase pages
- User profile pages
- Settings pages
- Landing pages

### 3.2 Customization Options

- **Color Schemes:** Light/dark theme support
- **Styling:** Tailored CSS and inline styles
- **Responsive Design:** Mobile-first, tablet, desktop breakpoints
- **Accessibility:** WCAG 2.1 AA compliance
- **Internationalization:** Multi-language support preparation

---

## 4. Technical Requirements

### 4.1 Environment & Dependencies

**Supported Frameworks:**
- React 18+
- Next.js 13+ (App Router and Pages Router)
- Vite-based React projects
- Create React App

**Supported Environments:**
- VS Code (latest 2 versions)
- Cursor IDE
- Any agent-supported editor with skills capability

**Required Packages:**
- `@syncfusion/ej2-react-buttons`
- `@syncfusion/ej2-react-dropdowns`
- `@syncfusion/ej2-react-grids`
- `@syncfusion/ej2-react-inputs`
- `@syncfusion/ej2-react-popups`
- `@syncfusion/ej2-react-calendars`
- `@syncfusion/ej2-react-charts`
- `@syncfusion/ej2-react-richtexteditor`
- And other Syncfusion React packages as needed

**Styling:**
- CSS Modules support
- Tailwind CSS compatibility
- Syncfusion theming system

### 4.2 Code Generation Standards

UI Builder enforces web standards and best practices to ensure generated code is production-ready and maintainable.

**Code Quality Requirements:**
- ES6+ syntax (no var, use const/let)
- TypeScript support (optional but recommended)
- Proper component structure and naming conventions
- Commented code where complex logic exists
- No console.log statements in production code
- PropTypes or TypeScript interfaces for type safety

**Formatting:**
- Consistent indentation (2 spaces)
- Semicolons required
- JSX formatting standards
- Exported components as named and default exports as appropriate

### 4.2.5 Reference Documentation Structure

All detailed documentation is stored in `references/` and loaded on-demand:

| File | Content | Usage |
|------|---------|-------|
| `references/REFERENCE.md` | Complete technical reference for all 9 stages | When detailed stage info needed |
| `references/STAGES.md` | Step-by-step workflows with decision trees | When understanding workflow logic |
| `references/SYNCFUSION-MAPPING.md` | Component mapping reference guide | During Stage 4 (Component Picking) |
| `references/WEB-STANDARDS.md` | WCAG 2.1 AA rules, security, performance checklists | During Stage 7 (Validation) |
| `references/LAYOUT-VARIANTS.md` | Full catalog of form/table/nav variants | During Stage 3 (Layout Confirmation) |
| `references/TROUBLESHOOTING.md` | Common errors, debugging tips, FAQ | On user request |
| `references/EXAMPLES.md` | Real before/after generated code samples | For learning/reference |

**Optimization Note:** Main SKILL.md instruction file stays under 500 lines by referencing these on-demand files.

### 4.3 Web Standards & Best Practices

**Accessibility (WCAG 2.1 AA Compliance):**
- Proper semantic HTML structure (header, nav, main, aside, footer tags)
- ARIA labels and roles where appropriate
- Keyboard navigation support (tab order, focus management)
- Color contrast ratios ≥ 4.5:1 for text
- Alt text for images
- Screen reader friendly form labels and error messages

**Responsive Design:**
- Mobile-first approach (design for mobile, then expand)
- Flexible layouts using CSS Flexbox/Grid
- Responsive typography (fluid font sizes)
- Touch-friendly interactive elements (minimum 44x44px)
- Tested on: mobile (320px), tablet (768px), desktop (1024px+)

**Performance:**
- Minimize unnecessary re-renders (React.memo, useMemo where needed)
- Lazy load components (React.lazy, dynamic imports)
- Optimize images (appropriate formats, sizes)
- CSS-in-JS efficiency (minimal runtime overhead)
- Code splitting for large component libraries

**HTML Semantics:**
- Use semantic HTML5 elements (`<button>` not `<div>` for buttons)
- Proper heading hierarchy (h1 → h6, no skipping levels)
- Form elements with associated labels
- List elements for list content (`<ul>`, `<ol>`, `<li>`)
- Link elements for navigation (`<a>` tags with href)

**React Best Practices:**
- Functional components with hooks (no class components)
- Custom hooks for reusable logic
- Prop drilling avoided (Context API or state management for deep trees)
- Controlled components for form inputs
- Error boundaries for error handling
- Proper cleanup in useEffect (subscriptions, timers)

**Progressive Enhancement:**
> **Scope note:** Generated components are React components and therefore require JavaScript to render and function — this is expected and by design. Progressive enhancement in this context means ensuring the *HTML structure* is semantic and meaningful so content is accessible to crawlers and assistive technologies even before hydration, not that the app works with JS disabled.
- Semantic HTML structure ensures content is crawlable and readable before React hydration
- CSS layout and typography are functional without JavaScript (no JS-dependent layout)
- Graceful degradation for older browsers (no bleeding-edge CSS without fallbacks)
- Feature detection over browser detection
- No breaking CSS or functionality in older browsers

**SEO Considerations (for public-facing components — frontend markup only):**
> **Scope note:** The UI Builder generates frontend component markup only. SEO concerns are limited to what is within the React component tree. Document-level concerns (meta tags, Open Graph, canonical URLs) must be handled by the consuming application using its framework's mechanism (e.g., Next.js `<Metadata>` API, React Helmet). The skill generates the correct *semantic HTML structure* that makes a component SEO-friendly, but does not modify `<head>` or routing configuration.
- Semantic HTML structure and heading hierarchy (generated by the skill)
- Descriptive, meaningful text content and `alt` attributes (generated by the skill)
- `lang` attribute on root elements where applicable (generated by the skill)
- Structured data (JSON-LD `<script>` block) injected into the component where semantically appropriate (e.g., a product card)
- Open Graph and meta tags: **out of scope** — the consuming application's layout/page file is responsible
- URL structure and routing: **out of scope** — the consuming application is responsible
- Fast Time-to-First-Contentful-Paint (TTFCP): addressed via frontend performance practices (lazy loading, minimal re-renders)

**Security:**
- Sanitize user input to prevent XSS
- No hardcoded secrets or API keys
- HTTPS enforced for external resources
- Content Security Policy (CSP) headers compatible
- No inline event handlers (e.g., `onClick="code()"` - use React handlers)

---

## 5. User Workflows

All workflows execute within the single **UI Builder Skill**, which orchestrates 9 sequential stages internally. Reference section 2.2 for the complete data flow.

### 5.1 Basic Component Generation Workflow

**High-Level Steps:**

1. **User opens editor** with active React/Next.js project
2. **User activates UI Builder Skill** through command palette or chat
3. **User describes component** in natural language (e.g., "Create a login form with email, password, and remember me checkbox")

**Stages Executed (See Detailed Sections Below):**

4. **Stage 2** — Project Detection & Configuration → Identify project structure and preferences
5. **Stage 3** — Layout Confirmation → Present 2-3 layout variants; user confirms structure
6. **Stage 4** — Component Picking → Map layout elements to Syncfusion components; user confirms picks
7. **Stage 5** — Preview Generation → Create interactive preview for user visualization
8. **Stage 6** — Code Generation → Generate React code with semantic HTML, validation, accessibility
9. **Stage 7** — Web Standards Compliance Validation → Validate code against WCAG 2.1 AA, security, performance
10. **Stage 8** — Dependency Management → Detect required packages; resolve version conflicts; install
11. **Stage 9** — Code Insertion/Integration → Insert files, update imports, verify build

12. **User receives confirmation** with file locations and verification checklist
13. **User can refine** component through iterative requests (repeats stages 3+ as needed)

### 5.2 Page Generation Workflow

Same stages as component generation (5.1), but applied iteratively to multiple component sections.

**High-Level Steps:**

1. **User requests full page** (e.g., "Build an e-commerce product catalog page")
2. **Skill breaks down** into logical sections/components (header, search, grid, footer)
3. **For each section**, repeat stages from 5.1:
   - **Stage 2** — Project Detection (once for whole project)
   - **Stage 3** — Layout Confirmation for each component type
   - **Stage 4** — Component Picking for each component
   - **Stage 5** — Preview Generation for each component
   - **Stage 6** — Code Generation for each component
   - **Stage 7** — Web Standards Compliance Validation for each component

4. **Stage 8** — Dependency Management (collect all dependencies, install once)
5. **Create page layout file** integrating all components
6. **Apply responsive design** and ensure consistency across sections
7. **Update routing** if needed (for Next.js/multi-file setups)
8. **Stage 5** — Preview complete page
9. **User reviews and approves**
10. **Stage 9** — Code Insertion/Integration for all files
11. **User receives confirmation** with page location and component file references

### 5.3 Customization Workflow

User can iteratively refine a generated component through modification requests.

**High-Level Steps:**

1. **User has generated component** (from workflow 5.1 or 5.2)
2. **User requests modification** (e.g., "Change theme to dark", "Add field", "Improve accessibility")
3. **Skill identifies and reads existing component** to extract current specifications:
   - **Parse the `.tsx` file:** Extract JSDoc comments, prop interface, state definitions (useState hooks), Syncfusion component usage
   - **Parse the `.module.css`:** Extract theme variables, responsive breakpoints, color scheme
   - **Reconstruct `UIBuilderContext`:** Build a context object representing the current state as if the component had just been generated (Stages 1-6 output)
   - **If JSDoc is missing or incomplete:** Ask user for clarification (e.g., *"What fields does this form have?"*)
4. **Skill analyzes modification impact:**
   - **Layout structure changes?** → Restart from Stage 3 (Layout Confirmation)
   - **Only styling changes?** → Jump to Stage 6 (Code Generation) with updated specs
   - **Only component changes?** → Jump to Stage 4 (Component Picking) with updated specs

5. **Execute applicable stages** (3, 4, 5, 6, 7 as needed)
6. **Stage 5** — Preview Generation → Show diff between old and new code
7. **User approves** modifications
8. **Stage 9** — Code Insertion → Replace old file with updated component
9. **User receives confirmation** of changes

**Best Practice:** The skill includes comprehensive JSDoc in all generated components to make this reverse-engineering step reliable. If a component is manually edited after generation and JSDoc is removed/altered, the customization workflow may fail or ask for clarification.

### 5.4 Stage 1: Intent Analysis & Setup

**Purpose:** Parse and validate the user's natural language request, resolve any ambiguities, initialize the `UIBuilderContext`, and determine which subsequent stages to execute.

**Workflow Steps:**

1. **Skill receives the user's raw natural language request**
2. **Skill tokenizes and classifies the request:**
   - Identify primary intent (generate component, generate page, modify existing, or unknown)
   - Extract component type keywords (form, table, nav, dashboard, etc.)
   - Extract modifiers (dark theme, multi-step, with OAuth, TypeScript, etc.)
3. **Skill checks for ambiguity** — if intent is unclear, ask a single targeted clarifying question before proceeding
4. **Skill initializes `UIBuilderContext`** with all extracted values (see Section 2.4)
5. **Skill determines execution plan:** which stages are required for this request
6. **Skill confirms plan to user** (one-line summary) and proceeds

#### 5.4.1 Intent Classification

**Recognized Intent Types:**

| Intent | Example Trigger Phrases | Stages Executed |
|---|---|---|
| `generate_component` | "Create a login form", "Build a data table" | 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 |
| `generate_page` | "Build an e-commerce page", "Create a dashboard" | 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 (iterative per section) |
| `modify_component` | "Change theme to dark", "Add a field to my form" | 2 → 3/4/5 (as needed) → 6 → 7 → 9 |
| `unknown` | Vague or unsupported request | → Ask clarifying question |

**Extraction Rules:**

- **Component type** is extracted from nouns: "login form" → `form/login`, "data grid" → `table/data`
- **Modifiers** are extracted from adjectives/prepositional phrases: "with OAuth" → `feature:oauth`, "dark theme" → `styling:dark`
- **Target** is extracted if user specifies a file or location: "in the auth folder" → `targetDir:auth/`

#### 5.4.2 Ambiguity Resolution

If the request maps to more than one possible intent or component type, the skill asks **one clarifying question** before proceeding. It does not ask multiple questions at once.

**Ambiguity Triggers:**

| Ambiguous Input | Clarifying Question |
|---|---|
| "Build me a form" (no type) | "What kind of form? (e.g., login, registration, contact, multi-step)" |
| "Add a component" (no type) | "What component would you like to add? (e.g., a data table, navigation bar, modal)" |
| "Make it better" | "Which component would you like to improve, and what aspect? (e.g., accessibility, styling, layout)" |
| Request mentions both "form" and "table" | "Should this be a form with an embedded table, or two separate components?" |

**Fallback:** If intent cannot be determined after one clarifying question, the skill responds with the supported component list (Section 3.1) and prompts the user to restart.

#### 5.4.3 Stage 1 Output (Context Initialization)

At the end of Stage 1, the `UIBuilderContext` is populated with:

```
Intent:        generate_component
ComponentType: form/login
Modifiers:     [feature:remember-me, styling:dark]
TargetDir:     (unset — to be resolved in Stage 2)
ExecutionPlan: [Stage 2, Stage 3, Stage 4, Stage 5, Stage 6, Stage 7, Stage 8, Stage 9]
```

The skill then outputs a one-line confirmation:

```
✓ Understood: Generating a dark-themed login form with "Remember Me" support.
  Starting project detection...
```

---

### 5.5 Stage 3: Layout Confirmation Workflow

**Purpose:** Ensure generated components match user's exact structural requirements before code insertion.

**Workflow Steps:**

1. **User describes component** with natural language request
2. **Skill identifies component type** (form, data table, navigation, etc.)
3. **Skill presents layout options** specific to that component type
4. **Skill asks clarifying questions** (see section 5.5.1 below)
5. **User confirms layout variant** and requirements
6. **Skill validates and confirms** specifications tailored to user needs
7. **Stage is complete** - proceed to Component Picking
8. **User can approve** or requests modifications before proceeding
9. **Modifications loop back** to re-present options if needed

#### 5.5.1 Standard Clarification Questions

**For Form Components:**
- What fields are required? (e.g., email, password, name, phone)
- Should it include optional features? (remember me, social login, 2FA, password strength meter)
- What is the submission behavior? (single-step, multi-step/wizard, inline save)
- How should errors be displayed? (inline messages, toast notifications, dialog)
- Should there be validation feedback? (real-time, on blur, on submit)

**For Data Display Components:**
- What data will be displayed? (rows, columns, structure)
- What interactions are needed? (sorting, filtering, pagination, inline editing)
- Should it be responsive? (mobile-first, desktop-first, adaptive)
- What actions should be available? (export, print, delete, view details)

**For Navigation Components:**
- How many menu items? (small <5, medium 5-10, large >10)
- Should it be hierarchical? (flat, single-level dropdown, multi-level)
- Layout preference? (horizontal top, vertical sidebar, collapsible)
- Mobile behavior? (always visible, hamburger menu, drawer)

**For All Components:**
- Styling preference? (light/dark theme, custom colors)
- Should it integrate with existing components? (context, state management)
- Any accessibility requirements? (screen reader optimization, keyboard navigation)
- TypeScript or JavaScript?

#### 5.5.2 Layout Variant Catalogs

**Login Forms:**
- **Variant A:** Minimal (email, password, submit button)
- **Variant B:** With "Remember Me" and "Forgot Password" link
- **Variant C:** With social login buttons (Google, GitHub, Microsoft)
- **Variant D:** With email verification step
- **Variant E:** With 2FA/MFA option
- **Variant F:** Multi-step (email verification → password setup → profile)

**Registration Forms:**
- **Variant A:** Simple (email, password, confirm password, submit)
- **Variant B:** With name and phone fields
- **Variant C:** With interest/role selection
- **Variant D:** With terms acceptance and email preferences
- **Variant E:** Multi-step wizard (account → profile → preferences)

**Data Tables:**
- **Variant A:** Read-only display, pagination only
- **Variant B:** With sorting and filtering
- **Variant C:** With row selection and bulk actions
- **Variant D:** With inline editing
- **Variant E:** With expandable rows and details view
- **Variant F:** With server-side pagination and virtual scrolling

**Navigation:**
- **Variant A:** Horizontal navbar with logo and menu items
- **Variant B:** Vertical sidebar with collapsible sections
- **Variant C:** Top navbar + left sidebar combo
- **Variant D:** Hamburger menu (mobile-responsive)
- **Variant E:** Breadcrumb navigation for hierarchical pages

#### 5.5.3 Confirmation Dialog

Before code insertion, display:
```
✓ Component Type: [e.g., Login Form - Variant C with OAuth]
✓ Fields/Items: [list confirmed structure]
✓ Features: [list enabled features]
✓ Styling: [theme, color scheme]
✓ Target Location: [file path where code will be inserted]

[Preview/Skeleton visualization]

Ready to generate? [Confirm] [Modify] [Cancel]
```

#### 5.5.4 Change Request Handling

If user requests modifications after layout confirmation:
1. **Identify specific changes** (add field, remove feature, change order)
2. **Re-confirm modified layout** (show updated preview)
3. **Apply changes** to generated code
4. **Show diff** of what changed
5. **Allow further refinement** or finalize

#### 5.5.5 Layout Recommendation Logic

> **Phase Note:** Two tiers of this engine exist across phases:
> - **Phase 1 (MVP):** Keyword-only matching — the top variant is pre-selected based solely on keyword extraction (Step 1 below). Context scoring (Steps 2–3) is skipped. The user still sees 2–3 options but the recommendation is based on keywords alone.
> - **Phase 2:** Full scoring algorithm — includes project-type context analysis, variant weighted scoring, and recommendation refinement over time.
>
> Both phases use the same user-facing output format (Step 4) and choice flow (Step 5).

The **Layout Recommendation Engine** intelligently suggests the best 2-3 variants based on requirement analysis, reducing decision fatigue.

**Recommendation Scoring Algorithm:**

1. **Extract Keywords** from user request:
   - **Security/Enterprise:** "enterprise", "security", "compliance", "2FA", "MFA", "audit", "healthcare", "finance"
   - **Simplicity:** "simple", "minimal", "basic", "quick", "easy"
   - **Social/Public:** "social", "OAuth", "public", "signup", "invite"
   - **Scalability:** "mobile", "large dataset", "many users", "performance", "real-time"
   - **Workflows:** "multi-step", "wizard", "verification", "approval"

2. **Analyze Context:**
   - **Project type** (from package.json): B2B app → favor enterprise variants; SaaS → favor secure + simple; Public site → favor social features
   - **Existing components** (detected from codebase): Match style consistency
   - **Team size** (estimated): Small team → favor simplicity; Large team → favor enterprise features
   - **Regulatory context** (from project description): Finance/Healthcare → high security; B2C → simplicity

3. **Score Each Variant:**
   - Assign weight 0-1 to each variant based on keyword matches
   - Example (Login Form):
     - User: "Enterprise app with strong security"
     - Variant A (Minimal): 0.2 → low match (too simple for enterprise)
     - Variant E (2FA): **0.95** → high match (security keyword, enterprise keyword)
     - Variant F (Multi-step): 0.85 → good match (workflow keyword, enterprise keyword)

4. **Recommendation Output:**
   Display top 3 ranked variants with explanations:
   ```
   Based on your requirement "Enterprise app with strong security", we recommend:
   
   🥇 RECOMMENDED: Variant E (2FA/MFA)
      ✓ Matches: enterprise security, compliance needs
      ✓ Best for: Strong authentication requirements
   
   🥈 ALTERNATIVE: Variant F (Multi-step Verification)
      ✓ Matches: workflow, identity verification
      ✓ Best for: Enhanced identity vetting
   
   ℹ️ OTHER OPTIONS: Variants A-D available (show all others)
   ```

5. **User Choice Flow:**
   - User can accept top recommendation (1-click)
   - User can select alternative
   - User can view all variants + customize manually
   - All choices are logged for recommendation refinement

### 5.7 Stage 4: Component Picking

**Purpose:** After layout confirmation, intelligently select and map the most appropriate Syncfusion components to fulfill the confirmed layout specifications.

**Workflow Steps:**

1. **User confirms layout variant** (from Layout Confirmation workflow)
2. **Skill extracts component requirements** from confirmed specifications
3. **Skill queries Syncfusion skills library** for available components
4. **Skill analyzes component compatibility** with layout requirements
5. **Skill maps components** to layout elements (form fields, buttons, containers, etc.)
6. **Skill presents component selection** with explanations
7. **User confirms component picks** (or requests alternatives)
8. **Skill is ready** for code generation using selected components with confirmed specifications

#### 5.5.1 Component Mapping Logic

**How Component Picking Works:**

For each layout element defined in the confirmed variant, the agent must:

1. **Identify the element type:** (e.g., "text input field", "button", "data table", "dropdown")
2. **Query Syncfusion skills library** for matching components
3. **Evaluate available options** based on:
   - Component capabilities (supports required props and events)
   - Accessibility compliance (WCAG 2.1 AA support)
   - Performance characteristics
   - Theme/styling compatibility with confirmed style specifications
   - Size and complexity suitability for the context

4. **Select best match** or present top 2-3 options

**Example: Login Form with Email & Password**

```
Layout Confirmation Result:
  ✓ Component Type: Login Form - Variant B (with Remember Me)
  ✓ Fields: email input, password input, remember-me checkbox
  ✓ Buttons: submit button, forgot password link

↓

Component Picking Analysis:

Field: "email input"
  Available Syncfusion options:
    - TextBox (from ej2-react-inputs) ← RECOMMENDED
      ✓ Supports email type validation
      ✓ Accessible labels and aria attributes
      ✓ Theme support (light/dark)
      ✓ Mobile-friendly
    - MaskedTextBox (from ej2-react-inputs)
      ↓ Overkill for simple email (can use TextBox with type="email")

Field: "password input"
  Available Syncfusion options:
    - TextBox with type="password" ← RECOMMENDED
      ✓ Standard secure password input
      ✓ Accessibility compatible
    - Custom obscured input
      ↓ Unnecessary (use standard TextBox)

Field: "remember-me checkbox"
  Available Syncfusion options:
    - CheckBox (from ej2-react-buttons) ← RECOMMENDED
      ✓ Native checkbox with label support
      ✓ WCAG 2.1 compliant

Field: "submit button"
  Available Syncfusion options:
    - Button (from ej2-react-buttons) ← RECOMMENDED
      ✓ Semantic HTML button element
      ✓ Accessibility features
      ✓ Theme support

Field: "forgot password link"
  Available Syncfusion options:
    - Standard HTML <a> tag ← RECOMMENDED
      ✓ Semantic link element
      ✓ Native browser behavior
```

#### 5.5.2 Component Selection Presentation

Before code generation, display selected components:

```
✓ Component Mapping - Login Form (Variant B)

Field: Email Address
  → TextBox (ej2-react-inputs)
     Props: type="email", label="Email", placeholder="Enter your email"
     Validation: Required, email format

Field: Password
  → TextBox (ej2-react-inputs)
     Props: type="password", label="Password", placeholder="Enter your password"
     Validation: Required, min length

Field: Remember Me
  → CheckBox (ej2-react-buttons)
     Props: label="Remember me"
     Default: unchecked

Button: Submit
  → Button (ej2-react-buttons)
     Props: label="Sign In", type="submit"
     Events: onClick (form submission)

Link: Forgot Password
  → Native <a> tag
     Props: href="/forgot-password", label="Forgot password?"

Required Packages:
  - @syncfusion/ej2-react-inputs
  - @syncfusion/ej2-react-buttons

[Confirm Components] [Select Alternatives] [Cancel]
```

#### 5.5.3 Component Alternative Selection

If user requests different components:

1. **User clicks "Select Alternatives"** on any component
2. **Skill displays compatible options** for that element
3. **User selects preferred component** (with explanation of pros/cons)
4. **Agent updates mapping** with user selection
5. **Agent regenerates component selection preview** with updated mappings
6. **Process repeats** until user approves all components

**Example Component Alternatives Dialog:**

```
Select Component for: Email Address Input

Currently Selected: TextBox (ej2-react-inputs)
  ✓ Standard text input with email validation
  ✓ Lightweight
  ✓ Full accessibility support

Other Options:

□ MaskedTextBox (ej2-react-inputs)
  - Supports input masking
  - Better for strict email format enforcement
  - Slightly heavier than TextBox
  - Recommended for: Enterprise email validation

□ AutoComplete (from ej2-react-dropdowns)
  - Can suggest known email domains
  - More interactive
  - Better for: Known user lists, email suggestion

[Select] [Cancel]
```

#### 5.5.4 Component Mapping Standards

**Requirements for Component Picking:**

1. **Use official Syncfusion components** from `@syncfusion/ej2-react-*` packages only
2. **Map to most semantically appropriate component** (use TextBox for text input, not a custom div)
3. **Verify accessibility compatibility** (all selected components must support WCAG 2.1 AA)
4. **Check theme/styling consistency** (all components must support selected theme)
5. **Validate prop compatibility** with confirmed specifications
6. **Document why each component was selected** in code comments
7. **List all required packages** in mapping preview

#### 5.5.5 Integration with Layout Confirmation

**Sequential Workflow:**

```
1. User describes component (natural language)
   ↓
2. Layout Confirmation (confirm structure/fields)
   ↓
3. Component Picking (map to Syncfusion components)
   ↓
4. Code Generation (generate code from specs + component picks)
```

The Component Picking skill assumes:
- Layout variant is already confirmed
- All field/structure requirements are finalized
- Component mapping is the final step before code generation

### 5.6 Stage 2: Project Detection & Configuration

**Purpose:** Automatically detect the target project's structure, framework, and configuration to ensure generated code integrates seamlessly.

**Workflow Steps:**

1. **Skill scans project root** for configuration files
2. **Agent detects project type** (React, Next.js App Router, Next.js Pages Router, Vite, CRA)
3. **Agent identifies target directory** for component insertion
4. **Agent reads project preferences** (TypeScript, CSS strategy, formatting rules)
5. **Agent verifies Syncfusion compatibility** with existing setup
6. **Agent reports detection results** to user
7. **User confirms or overrides** detected settings
8. **Configuration is locked** for code generation

#### 5.6.1 Detection Logic

**Files Scanned:**

1. **package.json** (required)
   - Extract project name, type, version
   - Identify React version (18+)
   - Detect Next.js, Vite, Create React App
   - Check existing Syncfusion dependencies
   - Read npm/yarn/pnpm preference

2. **tsconfig.json** (optional)
   - Detect TypeScript usage
   - Extract strictness settings
   - Identify JSX handling (react, react-jsx)
   - Check paths/aliases configuration

3. **next.config.js** (Next.js only)
   - Confirm Next.js version
   - Detect App Router vs Pages Router
   - Check transpilation settings
   - Read custom webpack config

4. **vite.config.ts/js** (Vite only)
   - Confirm Vite setup
   - Check React plugin configuration
   - Identify build output directory

5. **.prettierrc / prettier.config.js** (optional)
   - Extract formatting preferences (tabs/spaces, semi, quotes)
   - Ensure generated code matches project style

6. **.eslintrc / eslint.config.js** (optional)
   - Extract linting rules
   - Identify code quality standards
   - Check plugin requirements

7. **src/components/** or **app/components/** directory
   - Identify standard component structure
   - Check naming conventions (component-name.tsx vs ComponentName.tsx)
   - Detect existing component patterns

#### 5.6.2 Detection Output

**Example Detection Report:**

```
🔍 PROJECT DETECTION REPORT

Project Type: React with Next.js App Router
  ✓ Framework: Next.js 14.0.0
  ✓ Router: App Router
  ✓ Runtime: Node.js

Code Preferences:
  ✓ Language: TypeScript (strict mode)
  ✓ JSX Transform: Automatic (react/jsx-runtime)
  ✓ Formatting: Prettier (2 spaces, semicolons, single quotes)
  ✓ Linting: ESLint with React hooks plugin

Project Structure:
  ✓ Component Directory: app/components/
  ✓ Naming Convention: PascalCase (.tsx files)
  ✓ Import Style: ES6 modules

Syncfusion Compatibility:
  ✓ React version (18.2.0): COMPATIBLE
  ✓ Next.js version (14.0.0): COMPATIBLE
  ⚠️ Syncfusion packages: NOT INSTALLED
     Packages needed: @syncfusion/ej2-react-inputs, @syncfusion/ej2-react-buttons

Target Directory for Generated Code:
  → app/components/

[Confirm Settings] [Override Settings] [Cancel]
```

#### 5.6.3 Settings Override

If user needs to override detected settings:

```
⚙️ OVERRIDE DETECTION SETTINGS

Current Settings:
  • Component Directory: app/components/
  • Language: TypeScript
  • Formatting: Prettier (2 spaces)
  • Style Method: CSS Modules

Override Individual Settings:

✓ Framework Type: Next.js App Router (locked)
☐ Component Directory: [__________] (app/components/)
☐ Language: ⦿ TypeScript ○ JavaScript
☐ Indentation: ○ 2 spaces ○ 4 spaces ○ Tabs
☐ Style Method: ⦿ CSS Modules ○ Tailwind ○ Inline styles
☐ Use Named Exports: ⦿ Yes ○ No

[Save Overrides] [Reset to Defaults] [Cancel]
```

#### 5.6.4 Validation Checks

Before proceeding with code generation, verify:

- ✓ React 18+ is installed
- ✓ Next.js (if detected) version is 13+
- ✓ TypeScript configuration is valid (if used)
- ✓ Target component directory exists or can be created
- ✓ Project build tools are compatible

If validation fails, provide:
- Clear error message explaining the issue
- Recommended fix
- Manual setup instructions (if needed)

#### 5.6.5 Syncfusion License Key Handling

Syncfusion components require a valid license key registered via `registerLicense()` at application startup. The skill must detect, prompt for, and inject the license key as part of project setup.

**Detection (in order of priority):**

1. **Environment variable** — check for `SYNCFUSION_LICENSE_KEY` or `NEXT_PUBLIC_SYNCFUSION_LICENSE_KEY` in `.env`, `.env.local`, or `.env.production`
2. **Existing registration call** — search project files for `registerLicense(` to determine if already configured
3. **Not found** — prompt user (see below)

**Prompt (if license key not found):**

```
⚠️  SYNCFUSION LICENSE KEY REQUIRED

Syncfusion components require a license key to run without a license banner.

Options:

A) ✓ RECOMMENDED: Add license key now
   • Get a free Community License or trial at: https://www.syncfusion.com/account/manage-trials
   • Enter your license key: [_________________________________]
   • The skill will add it to your .env.local file and inject registerLicense() into your app entry point

B) Skip for now
   • A license watermark/banner will appear in the UI
   • You can add the license key manually later by calling:
     registerLicense('YOUR_KEY') before your app renders

[Add License Key] [Skip]
```

**Injection (if user provides key):**

1. Write `SYNCFUSION_LICENSE_KEY=<key>` to `.env.local` (and add to `.gitignore` if not already listed)
2. Insert the following at the top of the application entry point (detected from project type):

| Framework | Entry Point | Injection Code |
|---|---|---|
| Next.js App Router | `app/layout.tsx` | `import { registerLicense } from '@syncfusion/ej2-base'; registerLicense(process.env.NEXT_PUBLIC_SYNCFUSION_LICENSE_KEY ?? '');` |
| Next.js Pages Router | `pages/_app.tsx` | Same as above |
| Vite / CRA | `src/main.tsx` or `src/index.tsx` | `import { registerLicense } from '@syncfusion/ej2-base'; registerLicense(import.meta.env.VITE_SYNCFUSION_LICENSE_KEY ?? '');` |

3. Add `@syncfusion/ej2-base` to `requiredPackages` if not already present
4. Store `syncfusionLicenseKey: 'injected'` in `UIBuilderContext.project` (key value is never stored in context — only injection status)

### 5.8 Stage 5: Preview Generation

**Purpose:** Generate a preview/skeleton of the component before insertion to let users visualize and approve the output.

#### 5.7.0 Preview Delivery Mechanism

The preview is delivered differently depending on the editor environment. The chosen mechanism is stored in `UIBuilderContext.preview.deliveryMechanism`.

| Environment | Delivery Mechanism | Description |
|---|---|---|
| **VS Code** | `webview` *(preferred)* | A VS Code Webview Panel opens beside the editor showing a rendered, interactive HTML preview. The skill generates a self-contained HTML file and loads it into the panel. |
| **Cursor IDE** | `webview` | Same as VS Code — Cursor supports the VS Code extension API and Webview Panels. |
| **Other agent editors** | `html-file` | A temporary `.html` file is written to `{projectRoot}/.ui-builder/preview/{ComponentName}.preview.html` and the user is prompted to open it in their browser. The file is deleted after the user approves or cancels. |
| **Fallback (no UI)** | `markdown` | If neither webview nor file output is available, the preview is rendered as annotated ASCII art in the chat/response window (see Section 5.7.1). |

**Detection Logic:**

```
if (editor supports VS Code Webview API)  → deliveryMechanism = 'webview'
else if (file system write access)        → deliveryMechanism = 'html-file'
else                                      → deliveryMechanism = 'markdown'
```

**Note on `html-file` cleanup:** The temporary preview file must be deleted on pipeline completion (success, cancellation, or error). If the pipeline crashes before cleanup, the skill checks for and removes stale preview files on next invocation.

**Relationship to Confirmation Dialog (Section 5.5.3):** The confirmation dialog in Stage 3 is a *text-based structural summary* (field list, variant name, target path). The Stage 5 preview is a *visual rendering* of the component. Both are required checkpoints — Stage 3 confirms the specification, Stage 5 confirms the visual output.

**Workflow Steps:**

1. **Agent takes confirmed layout + component picks + web standards specs**
2. **Agent determines delivery mechanism** (see table above)
3. **Agent generates preview markup** (self-contained HTML skeleton with inline CSS)
4. **Agent applies styling** (dummy theme/colors matching confirmed style specs)
5. **Agent delivers preview** via selected mechanism (Webview, file, or markdown)
6. **Preview shows:** layout structure, component placements, responsive behavior
7. **User can interact** with preview (resize, test inputs, toggle responsive breakpoints) *(Webview only)*
8. **User approves** preview or requests modifications
9. **Preview feedback** is captured into `UIBuilderContext.preview` for final code generation

#### 5.7.1 Preview Content

**What's Shown in Preview:**

```
COMPONENT PREVIEW
════════════════════════════════════════════════════════════════

Component: Login Form - Variant B

Mobile View (320px)
┌─────────────────────────────┐
│  Sign In                    │
│                             │
│  ┌─────────────────────┐   │
│  │ Email              │   │
│  │ [example@email.com]│   │
│  └─────────────────────┘   │
│                             │
│  ┌─────────────────────┐   │
│  │ Password           │   │
│  │ [••••••••••]        │   │
│  └─────────────────────┘   │
│                             │
│  ☐ Remember me              │
│                             │
│  ┌─────────────────────┐   │
│  │   Sign In           │   │
│  └─────────────────────┘   │
│                             │
│  Forgot password?           │
└─────────────────────────────┘

Desktop View (1280px)
┌────────────────────────────────────────────────┐
│                    Sign In                      │
│                                                 │
│  ┌──────────────────────────────────────┐     │
│  │ Email Address                        │     │
│  │ [example@email.com                  ]│     │
│  └──────────────────────────────────────┘     │
│                                                 │
│  ┌──────────────────────────────────────┐     │
│  │ Password                             │     │
│  │ [••••••••••••••••••••••••••••••••••• ]│     │
│  └──────────────────────────────────────┘     │
│                                                 │
│  ☐ Remember me     [Forgot password?]         │
│                                                 │
│  ┌──────────────────────────────────────┐     │
│  │         Sign In                      │     │
│  └──────────────────────────────────────┘     │
└────────────────────────────────────────────────┘

Accessibility Features Shown:
  ✓ Focus indicators (blue outline on inputs)
  ✓ Semantic labels above each field
  ✓ Error state example (red border + error message)
  ✓ Keyboard tab order visualization

Color Contrast Check:
  ✓ All text: WCAG AA compliant (≥4.5:1)
  ✓ Focus indicators: Visible on all backgrounds
```

#### 5.7.2 Interactive Preview Features

**User Can:**

- Resize viewport to test responsiveness (mobile 320px → tablet 768px → desktop 1280px)
- Toggle theme (light/dark mode if applicable)
- Test form interactions (type in inputs, check/uncheck checkbox, hover states)
- Inspect accessibility features (keyboard nav, focus order, ARIA labels)
- View styling details (spacing, typography, colors with hex codes)
- Check error/loading/empty states if applicable

#### 5.7.3 Preview Feedback

User can provide feedback before generation:

```
PREVIEW FEEDBACK

Does this preview match your expectations?

✓ Layout structure and field order
✓ Responsive behavior on mobile view
✓ Styling and color scheme
✓ Accessibility indicators (focus, keyboard nav)
✓ Form interactions and behavior

Issues or changes needed?

☐ Change layout (show different variant options)
☐ Add/remove fields
☐ Adjust styling (colors, spacing, fonts)
☐ Improve accessibility (specific needs)
☐ Adjust responsive breakpoints
☐ Other: [_____________________]

Notes: [_________________________________]

[Approve & Generate] [Request Modifications] [Cancel]
```

### 5.9 Stage 6: Code Generation

**Purpose:** Transform confirmed layout specifications, component picks, and styling rules into production-ready React code.

**Workflow Steps:**

1. **Skill receives:** Layout variant (confirmed), Component picks (confirmed), Web standards specs, Project config
2. **Skill determines code structure:** File organization, component hierarchy, imports
3. **Skill generates component code** with:
   - Semantic HTML structure
   - Syncfusion component integration
   - Props and event handlers
   - Validation logic
   - Error/loading/empty states
   - Accessibility attributes
   - Responsive classes
4. **Skill applies styling** based on project configuration (CSS Modules, Tailwind, inline)
5. **Skill adds documentation** (JSDoc, usage comments, web standards notes)
6. **Generated code is validated** for syntax errors
7. **Code is ready for insertion**

#### 5.8.1 Code Generation Template

**Structure Generated:**

```typescript
/**
 * LoginForm Component
 * 
 * A secure login form with email and password fields.
 * Implements WCAG 2.1 AA accessibility standards.
 * 
 * @component
 * @example
 * return <LoginForm onSubmit={handleLogin} />
 */

import React, { useState } from 'react';
import { TextBoxComponent } from '@syncfusion/ej2-react-inputs';
import { CheckBoxComponent } from '@syncfusion/ej2-react-buttons';
import { ButtonComponent } from '@syncfusion/ej2-react-buttons';
import styles from './LoginForm.module.css';

interface LoginFormProps {
  onSubmit?: (email: string, password: string, rememberMe: boolean) => void;
  onForgotPassword?: () => void;
}

export const LoginForm: React.FC<LoginFormProps> = ({
  onSubmit,
  onForgotPassword
}) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [isLoading, setIsLoading] = useState(false);

  // Validation logic
  const validateForm = (): boolean => {
    const newErrors: Record<string, string> = {};
    
    if (!email) {
      newErrors.email = 'Email is required';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      newErrors.email = 'Please enter a valid email address';
    }
    
    if (!password) {
      newErrors.password = 'Password is required';
    } else if (password.length < 6) {
      newErrors.password = 'Password must be at least 6 characters';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  // Form submission handler
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!validateForm()) return;
    
    setIsLoading(true);
    try {
      onSubmit?.(email, password, rememberMe);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={styles.container} role="main">
      <form onSubmit={handleSubmit} className={styles.form} noValidate>
        <h1 className={styles.title}>Sign In</h1>
        
        {/* Email Field */}
        <div className={styles.fieldGroup}>
          <label htmlFor="email" className={styles.label}>
            Email Address
            <span className={styles.required} aria-label="required">*</span>
          </label>
          <TextBoxComponent
            id="email"
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => {
              setEmail(e.target.value);
              if (errors.email) setErrors({ ...errors, email: '' });
            }}
            onBlur={validateForm}
            aria-invalid={!!errors.email}
            aria-describedby={errors.email ? 'email-error' : undefined}
            className={errors.email ? styles.inputError : ''}
          />
          {errors.email && (
            <div id="email-error" className={styles.errorMessage} role="alert">
              {errors.email}
            </div>
          )}
        </div>

        {/* Password Field */}
        <div className={styles.fieldGroup}>
          <label htmlFor="password" className={styles.label}>
            Password
            <span className={styles.required} aria-label="required">*</span>
          </label>
          <TextBoxComponent
            id="password"
            type="password"
            placeholder="Enter your password"
            value={password}
            onChange={(e) => {
              setPassword(e.target.value);
              if (errors.password) setErrors({ ...errors, password: '' });
            }}
            onBlur={validateForm}
            aria-invalid={!!errors.password}
            aria-describedby={errors.password ? 'password-error' : undefined}
            className={errors.password ? styles.inputError : ''}
          />
          {errors.password && (
            <div id="password-error" className={styles.errorMessage} role="alert">
              {errors.password}
            </div>
          )}
        </div>

        {/* Remember Me Checkbox */}
        <div className={styles.rememberMeGroup}>
          <CheckBoxComponent
            id="rememberMe"
            label="Remember me"
            checked={rememberMe}
            onChange={(e) => setRememberMe(e.checked ?? false)}
          />
        </div>

        {/* Submit Button */}
        <ButtonComponent
          isPrimary
          type="submit"
          disabled={isLoading}
          className={styles.submitButton}
          aria-busy={isLoading}
        >
          {isLoading ? 'Signing in...' : 'Sign In'}
        </ButtonComponent>

        {/* Forgot Password Link */}
        <div className={styles.footerLinks}>
          <a
            href="#"
            onClick={(e) => {
              e.preventDefault();
              onForgotPassword?.();
            }}
            className={styles.link}
          >
            Forgot password?
          </a>
        </div>
      </form>

      {/* Skip to main content (for screen readers) */}
      <a href="#main-content" className={styles.skipLink}>
        Skip to main content
      </a>
    </div>
  );
};

export default LoginForm;
```

#### 5.8.2 Code Generation Rules

**Must Follow:**

1. **Semantic HTML:** Use `<form>`, `<input>`, `<button>`, `<label>` elements appropriately
2. **Accessibility:** Include `aria-*` attributes, `role`, `aria-describedby`, `aria-invalid`
3. **TypeScript:** Full type safety with interfaces for props
4. **Error Handling:** Validation, error messages, try-catch blocks
5. **Responsive Design:** CSS classes for mobile/tablet/desktop breakpoints
6. **Performance:** React.memo for stable components, avoid unnecessary re-renders
7. **Security:** Sanitize inputs, no dangerouslySetInnerHTML, validate on server-side too
8. **Documentation:** JSDoc comments, usage examples in code
9. **State Management:** Local state with useState, Context if sharing across components
10. **Event Handlers:** Proper event typing, prevent default where needed

#### 5.8.3 Styling Integration

**Generated CSS (CSS Modules Example):**

```css
/* LoginForm.module.css */

.container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.title {
  font-size: 24px;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 24px;
  text-align: center;
}

.fieldGroup {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.label {
  font-size: 14px;
  font-weight: 500;
  color: var(--text-secondary);
}

.required {
  color: var(--error-color);
  margin-left: 4px;
}

/* Input Styling */
.inputError {
  border-color: var(--error-color) !important;
}

.errorMessage {
  font-size: 12px;
  color: var(--error-color);
  margin-top: 4px;
}

/* Responsive Design */
@media (max-width: 768px) {
  .container {
    padding: 16px;
  }
  
  .title {
    font-size: 20px;
  }
}

@media (max-width: 320px) {
  .container {
    padding: 12px;
  }
  
  .form {
    gap: 12px;
  }
}
```

### 5.10 Stage 7: Web Standards Compliance Validation

**Purpose:** Validate generated code against WCAG 2.1 AA, semantic HTML, security, performance, and SEO standards before insertion.

**Workflow Steps:**

1. **Agent receives generated code** (component, styles, exports)
2. **Skill scans code** against compliance checklist
3. **Agent identifies violations** or warnings
4. **Agent auto-fixes common issues** (where possible)
5. **Agent reports results** to user with details
6. **User reviews** compliance report
7. **If issues remain,** user can:
   - Accept and proceed (acknowledgment)
   - Request fixes before insertion
   - Customize compliance level (strict/moderate/basic)

#### 5.9.1 Compliance Checklist

**Accessibility (WCAG 2.1 AA):**

```
☐ Semantic HTML Elements
  ✓ Uses <form> for forms (not <div>)
  ✓ Uses <button> for buttons (not <div> with click handler)
  ✓ Uses <input> with proper types
  ✓ Uses <label> with htmlFor attribute
  ✓ Uses <h1-h6> for headings in proper order
  
☐ ARIA Attributes
  ✓ aria-label on icon-only buttons
  ✓ aria-describedby linking inputs to error messages
  ✓ aria-invalid on invalid form fields
  ✓ aria-live for dynamic content updates
  ✓ aria-required on required fields
  ✓ role="alert" on error messages
  ✓ role="main" on main content container
  
☐ Keyboard Navigation
  ✓ All interactive elements are focusable (tab order logical)
  ✓ Focus indicators are visible (not display: none)
  ✓ Escape key closes modals/dropdowns
  ✓ Enter key submits forms
  ✓ No keyboard traps
  
☐ Color & Contrast
  ✓ Text contrast ≥ 4.5:1 (normal text)
  ✓ Text contrast ≥ 3:1 (large text)
  ✓ Color not the only visual indicator
  ✓ Focus indicator visible on all backgrounds
  
☐ Responsive & Touch
  ✓ Touch targets ≥ 44x44px (minimum)
  ✓ Layout responsive at 320px, 768px, 1024px+
  ✓ Readable font sizes (≥16px on mobile)
  ✓ No horizontal scrolling on mobile
  
☐ Media & Images
  ✓ Alt text provided for all images
  ✓ Captions for videos
  ✓ Transcripts for audio
```

**HTML Semantics:**

```
☐ Proper Element Usage
  ✓ Semantic elements used (header, nav, main, aside, footer)
  ✓ No empty headings or missing heading levels
  ✓ Proper list structure (<ul>, <ol>, <li>)
  ✓ Links use <a> with href (not <button> for navigation)
  ✓ Buttons use <button> element (not <a> with click handler)

☐ Form Structure
  ✓ Form fields have associated labels
  ✓ Required fields marked with aria-required
  ✓ Error messages linked to fields
  ✓ Form validation on blur/submit
```

**Security:**

```
☐ Input Validation
  ✓ User input is validated on the client (frontend responsibility)
  ℹ️ Server-side validation is out of scope — the consuming application is responsible for validating all inputs on the backend before processing
  ✓ No eval() or Function() constructors
  
☐ Content Injection
  ✓ No dangerouslySetInnerHTML() without sanitization
  ✓ User-generated content is escaped
  ✓ No inline event handlers (onclick="code()")
  
☐ Secrets & Keys
  ✓ No hardcoded API keys
  ✓ No secrets in client-side code
  ✓ Environment variables used for sensitive data
  
☐ Dependencies
  ✓ Syncfusion packages from official registry
  ✓ No malicious or deprecated packages
```

**Performance:**

```
☐ Rendering
  ✓ React.memo used for stable components
  ✓ Unnecessary re-renders avoided
  ✓ Lazy loading for large components
  
☐ Code Size
  ✓ No duplicate code
  ✓ Small bundle impact
  ✓ Tree-shakeable exports
  
☐ Images & Assets
  ✓ Optimized image formats
  ✓ Proper sizing (not overloaded)
  ✓ Lazy loaded if below fold
```

**SEO (for public components — frontend markup only):**

```
☐ Semantic HTML (within component scope)
  ✓ Proper heading hierarchy (h1 → h6, no skipped levels)
  ✓ Meaningful alt text on all images
  ✓ Structured data (Schema.org JSON-LD <script> block) where applicable
  ℹ️ Page titles and meta tags: OUT OF SCOPE — handled by the consuming
     application's layout file (e.g., Next.js Metadata API)
  
☐ Crawlability
  ✓ Semantic HTML content is crawlable (not hidden behind JS-only rendering)
  ✓ Navigation uses <a> tags with real href values (not JS-only onClick)
  ✓ Proper link structure within the component
  ℹ️ URL structure and routing: OUT OF SCOPE — consuming application's responsibility
```

#### 5.9.2 Validation Report

**Example Output:**

```
✓ WEB STANDARDS COMPLIANCE REPORT

Component: LoginForm
Generated: 2026-04-14 14:32:15

═══════════════════════════════════════════════════════════

ACCESSIBILITY (WCAG 2.1 AA)
Overall: ✓ PASS (18/18 checks)

  ✓ Semantic HTML Elements (5/5)
    • Uses <form> element
    • Uses <label htmlFor> for inputs
    • Uses <button> for submit
    • Uses <input type="email"> for email field
    • Uses <input type="password"> for password field

  ✓ ARIA Attributes (6/6)
    • aria-invalid on email field ✓
    • aria-describedby linking to error message ✓
    • aria-required on password field ✓
    • aria-live="polite" on error container ✓
    • role="alert" on error messages ✓
    • role="main" on form container ✓

  ✓ Keyboard Navigation (4/4)
    • Tab order is logical ✓
    • Focus indicators visible ✓
    • Enter submits form ✓
    • Escape closes modal (if applicable) ✓

  ✓ Color & Contrast (3/3)
    • Text contrast 7.2:1 (WCAG AAA) ✓
    • Focus indicator visible (2px blue outline) ✓
    • Color not only indicator for errors ✓

═══════════════════════════════════════════════════════════

SECURITY
Overall: ✓ PASS (4/4 checks)

  ✓ Input Handling
    • Email validated with regex pattern ✓
    • Password minimum length enforced ✓
    • No dangerouslySetInnerHTML ✓

  ✓ Secrets & Keys
    • No hardcoded API keys ✓
    • No sensitive data in code ✓

═══════════════════════════════════════════════════════════

PERFORMANCE
Overall: ✓ PASS (3/3 checks)

  ✓ Code Quality
    • React.memo applied to component ✓
    • No console.log statements ✓
    • Proper error boundary support ✓

═══════════════════════════════════════════════════════════

⚠️  WARNINGS (2)

  ⚠️  Performance: Missing loading state optimization
     → Consider useMemo for validation logic
     → Issue: Validation runs on every keystroke
     → Fix: Debounce validation with 300ms delay

  ⚠️  Accessibility: Color contrast in dark mode not verified
     → Please test on dark theme backgrounds
     → Recommendation: Test with dark theme CSS

═══════════════════════════════════════════════════════════

[✓ Approve & Insert] [Request Fixes] [Review Details]
```

#### 5.9.3 Auto-Fix Capabilities

**Agent Can Auto-Fix:**

- Missing aria-labels on icon buttons
- Missing aria-describedby for error messages
- Missing htmlFor on labels
- Improper heading hierarchy (reorganize)
- Focus indicators removed (restore visibility)
- Non-semantic button divs (convert to <button>)
- XSS vulnerabilities (sanitize content)
- Hardcoded strings (extract to props/constants)

**User Must Fix Manually:**

- Color contrast issues (requires design decision)
- Keyboard trap logic (requires UX decision)
- API key exposure (requires architecture change)
- Performance bottlenecks (requires optimization strategy)

### 5.11 Stage 8: Dependency Management

**Purpose:** Detect required Syncfusion packages, manage versions, and handle installation with conflict resolution.

**Workflow Steps:**

1. **Skill analyzes generated code** for Syncfusion imports
2. **Skill extracts required packages** (e.g., @syncfusion/ej2-react-inputs)
3. **Skill reads current package.json** for existing versions
4. **Skill checks for version conflicts** with existing setup
5. **Skill determines installation strategy:**
   - Already installed? → Skip
   - Missing? → Add to dependencies
   - Version mismatch? → Resolve conflict
6. **Skill displays dependency report** to user
7. **User approves** installation plan
8. **Skill executes installation** (npm install / yarn add / pnpm add)
9. **Verification** that packages installed correctly

#### 5.10.1 Dependency Detection

**Extracted from Component Import:**

```typescript
// Generated code uses:
import { TextBoxComponent } from '@syncfusion/ej2-react-inputs';
import { CheckBoxComponent } from '@syncfusion/ej2-react-buttons';

// Skill determines required packages:
✓ @syncfusion/ej2-react-inputs
✓ @syncfusion/ej2-react-buttons
```

#### 5.10.2 Dependency Report

**Example Output:**

```
📦 DEPENDENCY MANAGEMENT REPORT

Component: LoginForm

Current Dependencies in package.json:
  ✓ React 18.2.0 (required: ≥18.0.0)
  ✓ Next.js 14.0.0 (required: ≥13.0.0)
  ✗ @syncfusion/ej2-react-inputs (NOT INSTALLED)
  ✗ @syncfusion/ej2-react-buttons (NOT INSTALLED)

Installation Plan:
  Package: @syncfusion/ej2-react-inputs
    → Version: 25.1.35 (latest stable, matches Next.js 14 compatibility)
    → Type: production dependency
    → Peer dependencies: react@^18.0.0
    → Size: ~2.3 MB
    → Status: ✓ COMPATIBLE

  Package: @syncfusion/ej2-react-buttons
    → Version: 25.1.35 (matches inputs version for consistency)
    → Type: production dependency
    → Peer dependencies: react@^18.0.0
    → Size: ~1.1 MB
    → Status: ✓ COMPATIBLE

Package Manager Detection:
  ✓ Detected: npm (v10.0.0)
  Alternative: yarn, pnpm

Installation Command:
  $ npm install @syncfusion/ej2-react-inputs@25.1.35 @syncfusion/ej2-react-buttons@25.1.35

Estimated Download Time: ~30 seconds
Estimated Installation Time: ~45 seconds

[Install Now] [Use Different Version] [Skip Installation] [Cancel]
```

#### 5.10.3 Conflict Resolution

**If Version Mismatch Detected:**

```
⚠️  VERSION CONFLICT DETECTED

Existing Syncfusion Package:
  • @syncfusion/ej2-react-inputs: 24.1.0 (already installed)

Required by New Component:
  • @syncfusion/ej2-react-inputs: 25.1.35 (LoginForm requires latest)

Conflict Resolution Options:

A) ✓ RECOMMENDED: Upgrade to 25.1.35
   Pros: 
    • Full compatibility with all new components
    • Latest features and security patches
    • Consistent across entire project
   Cons:
    • May require testing of existing components
    • Changelog review recommended
   Breaking Changes: None (minor version bump)

B) Use Existing 24.1.0
   Pros:
    • No version upgrade required
    • Existing code unchanged
   Cons:
    • LoginForm may have incompatibilities
    • Features may be missing
    • Not recommended

C) Use Minimum Compatible Version: 24.2.0
   Pros:
    • Smaller upgrade from current 24.1.0
    • Better compatibility with existing code
   Cons:
    • Still requires upgrade
    • May miss features from 25.1.35

[Option A - Upgrade] [Option B - Keep Current] [Option C - Compromise]
```

#### 5.10.4 Post-Installation Verification

After installation:

```
✓ DEPENDENCIES INSTALLED SUCCESSFULLY

Verified Packages:
  ✓ @syncfusion/ej2-react-inputs@25.1.35 (2.3 MB)
  ✓ @syncfusion/ej2-react-buttons@25.1.35 (1.1 MB)

Updated package.json:
  "dependencies": {
    "react": "^18.2.0",
    "next": "^14.0.0",
    "+ "@syncfusion/ej2-react-inputs": "^25.1.35",
    "+ "@syncfusion/ej2-react-buttons": "^25.1.35"
  }

Installation Time: 42 seconds
Total Downloaded: 3.4 MB

Next Steps:
  1. Restart your development server (if running)
  2. Components are ready for use
  3. Type definitions available for TypeScript

Ready to insert LoginForm component? [Proceed] [Cancel]
```

### 5.12 Stage 9: Code Insertion/Integration

**Purpose:** Insert generated code into the project at the correct location with proper imports, exports, and no conflicts.

**Workflow Steps:**

1. **Skill determines target file** based on project config (e.g., src/components/LoginForm.tsx)
2. **Skill checks for name conflicts** (file already exists? component already named?)
3. **Skill generates file** with component code + exports
4. **Skill updates project imports** (if needed):
   - Create component index file exports
   - Update parent component imports
5. **Skill verifies syntax** (no TypeScript errors, proper formatting)
6. **Skill inserts file** into project
7. **Skill reports insertion result** to user
8. **User can verify** in editor

#### 5.11.1 Target Directory Detection

**Insertion Logic:**

```
Project Structure Detected: Next.js App Router
Target Directory Options (in order of preference):

1. ✓ RECOMMENDED: app/components/
   Reasoning:
   • Matches project structure detection
   • Consistent with existing components
   • Non-route-specific (reusable from any page)

2. app/components/auth/
   Reasoning:
   • Component is auth-related (LoginForm)
   • Existing auth components directory

3. Custom directory: [_________________]

Selected Target: app/components/LoginForm.tsx
```

#### 5.11.2 Name Conflict Detection

Before insertion:

```
✓ FILE NAME CHECK

Proposed File: app/components/LoginForm.tsx

✓ File does not exist (safe to create)
✓ Component name "LoginForm" is unique in project
✓ No naming conflicts detected

Ready to insert at: app/components/LoginForm.tsx
```

**If Conflict Detected:**

```
⚠️  NAME CONFLICT DETECTED

Proposed File: app/components/LoginForm.tsx
Status: FILE ALREADY EXISTS

Conflict Resolution Options:

A) ✓ RECOMMENDED: Use New Component Name
   → New name: LoginFormV2.tsx
   → File: app/components/LoginFormV2.tsx
   → Reason: Preserve existing component

B) Replace Existing File
   → Overwrite: app/components/LoginForm.tsx
   → Risk: Loss of existing code
   → Recommended only if regenerating

C) Use Different Directory
   → Path: app/components/auth/LoginForm.tsx
   → Reason: More specific component grouping

[Option A] [Option B] [Option C] [Cancel]
```

#### 5.11.3 File Insertion Process

**Generated File:**

```typescript
// app/components/LoginForm.tsx

/**
 * LoginForm Component
 * 
 * A secure login form with email and password fields.
 * Implements WCAG 2.1 AA accessibility standards.
 * 
 * @component
 * @example
 * return <LoginForm onSubmit={handleLogin} />
 */

import React, { useState } from 'react';
import { TextBoxComponent } from '@syncfusion/ej2-react-inputs';
import { CheckBoxComponent } from '@syncfusion/ej2-react-buttons';
import { ButtonComponent } from '@syncfusion/ej2-react-buttons';
import styles from './LoginForm.module.css';

// ... [Component code from Code Generation Skill section 5.8] ...

export const LoginForm: React.FC<LoginFormProps> = ({ ... }) => {
  // ... component implementation ...
};

export default LoginForm;
```

**Generated Stylesheet:**

```css
/* app/components/LoginForm.module.css */

.container {
  /* ... styles from Code Generation ... */
}

/* ... [All CSS from Code Generation] ... */
```

**Create Component Index (if needed):**

```typescript
// app/components/index.ts (updated)

export { LoginForm } from './LoginForm';
export { default as LoginFormDefault } from './LoginForm';
```

#### 5.11.4 Post-Insertion Verification

After file insertion:

```
✓ CODE INSERTION SUCCESSFUL

Files Created:
  ✓ app/components/LoginForm.tsx (842 bytes)
  ✓ app/components/LoginForm.module.css (1,241 bytes)

Files Updated:
  ✓ app/components/index.ts (added export)

Imports Available:
  • Named import: import { LoginForm } from '@/components';
  • Default import: import LoginForm from '@/components/LoginForm';

Next Steps:
  1. Component is ready to use in your pages
  2. Example usage (in your page):
     ```
     import { LoginForm } from '@/components';
     
     export default function LoginPage() {
       return <LoginForm onSubmit={handleLogin} />;
     }
     ```

  3. Test the component:
     □ Render in a page
     □ Test form submission
     □ Test accessibility (keyboard nav, screen reader)
     □ Test responsive behavior

[View Component] [View Styles] [Create Usage Example] [Done]
```

#### 5.11.5 Build Verification

Auto-check that the frontend compiles successfully after file insertion.

> **Scope note:** This step verifies **frontend compilation only** — TypeScript types, import resolution, and ESLint rules. It does not validate server-side logic, API routes, or backend behaviour. For Next.js projects, `next build` compiles both client and server code; the skill only treats the result as a pass/fail signal for the frontend component's correctness.

```
🔨 FRONTEND BUILD VERIFICATION

Running: npx tsc --noEmit   (TypeScript type check — no output emitted)
Running: npx eslint {componentFilePath}   (lint check on generated file only)

✓ TypeScript compilation successful (no type errors in generated files)
✓ All imports resolved (Syncfusion packages found in node_modules)
✓ ESLint rules passed (generated file matches project lint config)

✓ Component is production-ready!

Note: Run your full project build (npm run build) separately to verify
      end-to-end integration with your application.

[Test in Dev] [Done]
```

---

### 5.14 Error Recovery & Pipeline Rollback

**Purpose:** Define what happens when a stage fails, the user cancels mid-pipeline, or the process crashes — ensuring no partial or corrupt files are left in the project.

#### 5.13.1 Checkpoint Strategy

Rollback checkpoints are created automatically before any stage that **writes to the file system or modifies `package.json`**. These are Stages 8 and 9. Stages 1–7 are non-destructive (read-only or in-memory) and do not require rollback.

| Stage | Destructive? | Checkpoint Created? | What is Backed Up |
|---|---|---|---|
| Stage 1 — Intent Analysis | No | No | — |
| Stage 2 — Project Detection | No | No | — |
| Stage 3 — Layout Confirmation | No | No | — |
| Stage 4 — Component Picking | No | No | — |
| Stage 5 — Preview Generation | Yes (temp file) | Yes | Temp preview file path logged for cleanup |
| Stage 6 — Code Generation | No (in-memory) | No | — |
| Stage 7 — Validation | No | No | — |
| Stage 8 — Dependency Management | **Yes** | **Yes** | Snapshot of `package.json` and `package-lock.json`/`yarn.lock` |
| Stage 9 — Code Insertion | **Yes** | **Yes** | List of files to be created/modified; originals backed up to `.ui-builder/backup/` |

#### 5.13.2 Stage Failure Behavior

When any stage returns a failure status, the following protocol applies:

```
Stage Failure Detected
    ↓
1. Set UIBuilderContext.pipelineStatus = 'failed'
2. Log the failing stage, error message, and stack trace
3. Present user with:

   ❌ STAGE [N] FAILED: [Stage Name]

   Error: [human-readable error description]

   Options:
   A) Retry Stage [N] — attempt the stage again (e.g., transient network error)
   B) Skip Stage [N] — proceed to next stage (only available for non-critical stages)
   C) Roll Back — undo all file system changes and return project to pre-run state
   D) Cancel & Keep — stop pipeline, keep any files already inserted (user takes ownership)

4. If user selects Roll Back:
   → Restore package.json and lock files from checkpoint
   → Delete all files listed in UIBuilderContext.insertion.filesCreated
   → Restore original content of all files in UIBuilderContext.insertion.filesUpdated
   → Delete temporary preview file (if exists)
   → Set pipelineStatus = 'rolled-back'
   → Confirm: "✓ Rollback complete. Project restored to its original state."
```

**Non-critical stages** (can be skipped): Stage 5 (Preview), Stage 7 (Validation with warnings only)
**Critical stages** (cannot be skipped): Stage 2, Stage 6, Stage 8, Stage 9

#### 5.13.3 User Cancellation at Any Stage

If the user cancels at any point during the pipeline:

```
User Cancels
    ↓
If before Stage 8 (no file system writes yet):
  → Discard UIBuilderContext, confirm "Cancelled. No changes were made."

If during/after Stage 8 (package.json modified):
  → Ask: "Packages were installed. Roll back package.json changes? [Yes] [No, keep packages]"

If during/after Stage 9 (files inserted):
  → Ask: "Files were inserted. Roll back all changes? [Yes] [No, keep files]"
  → If Yes: execute rollback as per Section 5.13.2
```

#### 5.13.4 Process Crash Recovery

On next skill invocation after a crash, the skill checks for:
1. A stale `.ui-builder/backup/` directory — if found, prompt: `"A previous run did not complete. Roll back incomplete changes? [Yes] [No, ignore]"`
2. A stale `.ui-builder/preview/*.preview.html` file — silently delete
3. A stale `UIBuilderContext` snapshot (if persisted) — offer to resume from last completed stage

---

## 6. Feature Set

### 6.1 Phase 1 - Core Skills (MVP)

> **All Phase 1 skills are documented in detail in Section 5 (User Workflows)**

- [x] Skill 5.4: Layout Confirmation Workflow (confirm layout structure with variants; includes simplified keyword-based recommendation — Phase 1 tier)
- [x] Skill 5.5: Component Picking Skill (map layout to Syncfusion components)
- [x] Skill 5.6: Project Detection & Configuration (detect project setup)
- [x] Skill 5.7: Preview Generation (create interactive preview)
- [x] Skill 5.8: Code Generation Skill (generate semantic HTML + components + styling)
- [x] Skill 5.9: Web Standards Compliance Validator (WCAG 2.1 AA, security, performance)
- [x] Skill 5.10: Dependency Management (detect/resolve/install packages)
- [x] Skill 5.11: Code Insertion/Integration (insert files, update imports, verify build)
- [x] Parse natural language requests for component types
- [x] Generate basic CRUD form components
- [x] Generate simple data display components
- [x] Handle basic styling with themes
- [x] Error handling and validation messaging
- [x] Support for React and Next.js projects (App Router, Pages Router)
- [x] TypeScript support with full type safety
- [x] JSDoc documentation for all generated code

### 6.2 Phase 2 - Extended Features

- [ ] Layout Recommendation Engine — **full scoring algorithm** (intelligent variant suggestions based on keywords/context scoring; see Section 5.5.5 for the algorithm). Phase 1 ships a **simplified version** — top variant is pre-selected based on keyword matching only, without context scoring or project-type analysis.
- [ ] Complex multi-step forms and wizards (multi-step validation, progress tracking)
- [ ] Advanced data table configurations (server-side pagination, filtering, sorting)
- [ ] Chart and graph generation with sample data
- [ ] Advanced theme customization (light/dark mode toggles, custom color palettes)
- [ ] Performance metrics visualization (component size, render time, optimization suggestions)
- [ ] Batch component generation (multiple components at once)
- [ ] Component templating and reuse library
- [ ] Vite and Create React App full support
- [ ] Advanced state management templates (Redux, Zustand, Recoil)

### 6.3 Phase 3 - Advanced Features

- [ ] Custom component composition (combining multiple Syncfusion components)
- [ ] Advanced accessibility audit with AI-powered fixes
- [ ] SEO optimization for public-facing components
- [ ] Security scanning (XSS, injection vulnerability detection)
- [ ] API integration templates — **frontend only**: generates React data-fetching hooks (`useQuery`, `useFetch`, `useEffect`-based) and TypeScript response type interfaces for connecting components to REST/GraphQL endpoints; does not generate backend API routes or server logic
- [ ] State management setup (Redux, Zustand, Context API templates)
- [ ] Testing code generation (Jest, React Testing Library)
- [ ] Performance profiling and optimization recommendations
- [ ] Design token system integration

---

## 7. Integration Points

> **Note:** Detailed workflows for Integration Points are documented in Section 5 (User Workflows) as individual skills. This section provides summary references only.

### 7.1 Project Detection (See Section 5.6 for Details)

**Overview:**
- Scans project root for configuration files (package.json, tsconfig.json, next.config.js, .prettierrc, .eslintrc)
- Detects framework type (React, Next.js App/Pages Router, Vite, CRA)
- Identifies project structure and existing component directories
- Extracts code preferences (TypeScript, formatting, linting rules)
- Verifies Syncfusion compatibility

### 7.2 Code Insertion (See Section 5.11 for Details)

**Overview:**
- Determines target directory (`src/components/`, `app/components/`, or custom)
- Detects file name conflicts and provides resolution options
- Inserts generated component code with proper exports
- Creates/updates component index files for clean imports
- Verifies TypeScript compilation and build success

### 7.3 Dependency Management (See Section 5.10 for Details)

**Automatic Actions:**
- Detect missing Syncfusion packages
- Suggest/prompt for installation
- Update `package.json` with required versions
- Handle peer dependency conflicts

---

## 8. Success Criteria

### 8.1 Functional Requirements

- ✓ Generated components are syntactically valid React code
- ✓ Components render without errors in target project
- ✓ Components are responsive across desktop, tablet, mobile
- ✓ Accessibility standards are met (WCAG 2.1 AA minimum)
- ✓ Code follows project's linting and formatting rules
- ✓ Web standards compliance verified (semantic HTML, security, performance)
- ✓ All required Syncfusion dependencies are properly installed

### 8.2 User Experience Requirements

- ✓ Natural language requests are correctly interpreted
- ✓ Layout confirmation happens before code generation
- ✓ Layout Recommendation Engine suggests relevant variants
- ✓ Component generation completes in < 5 seconds (after layout confirmation)
- ✓ User can see generated code immediately in project
- ✓ User receives clear feedback and error messages
- ✓ User can iterate and refine components easily

### 8.3 Quality Requirements

- ✓ Generated components have zero hardcoded values (except required demo data)
- ✓ Code includes appropriate comments for complex logic
- ✓ Components follow single responsibility principle
- ✓ Props are properly typed and documented
- ✓ No security vulnerabilities in generated code (XSS, injection prevention)
- ✓ Web standards compliance checklist passed:
  - [ ] Semantic HTML elements used correctly
  - [ ] ARIA labels/roles present where needed
  - [ ] Keyboard navigation functional
  - [ ] Color contrast ≥ 4.5:1
  - [ ] Touch targets ≥ 44x44px
  - [ ] Mobile-first responsive design
  - [ ] No hardcoded secrets/API keys
  - [ ] Input sanitization for user data

---

## 9. Implementation Guidelines

### 9.1 Code Generation Best Practices

1. **Always use Syncfusion components** from installed packages
2. **Validate all user inputs** before code generation
3. **Generate reusable components** with props for customization
4. **Include PropTypes or TypeScript** interfaces for type safety
5. **Use semantic HTML** elements appropriately (button, form, input, label, etc.)
6. **Handle empty states and error states** in components with accessible messaging
7. **Include placeholder data** or data structure comments
8. **Make components composable** - avoid monolithic components
9. **Enforce web standards** in every generated component:
   - All interactive elements keyboard accessible
   - ARIA labels/roles for screen reader users
   - Color contrast ratios meet WCAG AA standards
   - Mobile-responsive by default (mobile-first approach)
   - No hardcoded secrets, API keys, or sensitive data
   - Input sanitization for XSS prevention

### 9.2 Code Generation for Web Standards

**Accessibility First:**
- Generate semantic HTML structure (not div-based layouts)
- Include aria-label, aria-describedby, aria-live where needed
- Ensure focus management for modal dialogs and dynamic content
- Test keyboard navigation (Tab, Enter, Escape keys)

**Performance:**
- Minimize re-renders (use React.memo for stable components)
- Lazy load heavy components
- Avoid prop drilling (use Context API for shared state when needed)
- Include performance comments for optimization opportunities

**Security:**
- Sanitize any user input that will be rendered as HTML
- Use data attributes for storing data (not global variables)
- Avoid eval() or dangerouslySetInnerHTML
- Document any API keys or secrets needed (don't generate them)

**Responsive Design:**
- Mobile breakpoints: 320px, 768px, 1024px, 1280px
- Test on actual devices or responsive viewport
- Use CSS Flexbox/Grid (not floats or tables for layout)
- Readable font sizes at all breakpoints

### 9.3 Error Handling

- **Invalid requests:** Provide clear guidance on what type of components can be generated
- **Missing dependencies:** Prompt user to install required Syncfusion packages
- **Project detection failures:** Provide manual configuration options
- **Generation errors:** Log detailed error messages and suggest corrections
- **Standards violations:** Alert user to any web standards issues and how to fix them

### 9.4 Documentation & Comments

- Each generated component includes:
  - Component purpose (JSDoc comment)
  - Props documentation with types
  - Usage example comments (commented out in code)
  - Any special requirements or assumptions
  - **Web standards checklist** (accessibility, responsive, security notes)
  - Instructions for testing accessibility (keyboard nav, screen reader)

### 9.5 Version Management

- Track Syncfusion package versions used
- Ensure compatibility with locked versions in `package.json`
- Include minimum and maximum version constraints
- Document known compatibility issues with other packages

---

## 10. Installation & Setup

### 10.1 Skills CLI Overview

The UI Builder Skill is installed and invoked via the **`npx skills`** CLI — a package-agnostic tool for managing code generation skills. This is a third-party CLI provided by Prompt (formerly Sourcegraph) that acts as a plugin framework for AI agents.

**What is `npx skills`?**
- A command-line interface for discovering, installing, and running AI-powered code generation skills
- Skills are npm packages that implement a standard interface for AI agents
- The CLI is installed globally and works in any project directory
- Skills can be chained together (e.g., UI Builder → run build → run tests)

**Prerequisites:**
- Node.js 18+ installed
- npm, yarn, or pnpm available
- Access to `npx` (comes with Node.js)

### 10.2 For End Users

#### Installation

```bash
# Install the UI Builder Skill globally (one-time)
npx skills add syncfusion/react-ui-components-skills -y

# Verify installation
npx skills list
# Output: UI Builder Skill v1.0.0 (syncfusion/react-ui-components-skills) ✓
```

#### Usage

```bash
# Activate the skill in your React project directory
cd your-react-project/

# Invoke via chat or editor command
# (Exact invocation depends on your editor integration)
# VS Code: Open command palette → "UI Builder: Generate Component"
# Cursor: Open chat → "@UIBuilder generate a login form"
# Terminal: npx skills invoke UI-Builder "generate a customer table"
```

#### Uninstall

```bash
# Remove the skill
npx skills remove syncfusion/react-ui-components-skills
```

### 10.3 For Integration with Projects

The UI Builder Skill, when invoked, will automatically:

1. **Detect project structure** — Identify React, Next.js (App/Pages Router), Vite, or CRA
2. **Check dependencies** — Scan `package.json` for existing Syncfusion packages
3. **Verify compatibility** — Ensure Node version, React version, and build tools are supported
4. **Prompt for setup** — Ask for missing configuration (Syncfusion license, component directory preferences)
5. **Configure paths** — Read `.prettierrc`, `.eslintrc`, `tsconfig.json` to match project conventions
6. **Proceed with generation** — Execute the 9-stage pipeline

#### Requirements for Project Compatibility

A project must meet these minimum requirements to use the UI Builder Skill:

```
✓ React 18 or higher installed
✓ TypeScript 4.5+ (optional but recommended)
✓ Next.js 13+ OR Vite 4+ OR Create React App 5+ (if using a framework)
✓ npm / yarn / pnpm as package manager
✓ Node.js 18+ runtime
✓ Writable file system (for inserting components)
✓ Internet access (to download Syncfusion packages)

Optional:
  • Prettier config (.prettierrc) — for code formatting consistency
  • ESLint config (.eslintrc) — for linting compatibility
  • Design tokens / CSS variables — for theme integration
```

#### Troubleshooting

| Issue | Solution |
|---|---|
| `command not found: skills` | Run `npm install -g skills-cli` (one-time setup) |
| Skill not found after `npx skills list` | Run `npx skills add syncfusion/react-ui-components-skills -y` again |
| Project not detected | Verify `package.json` exists in the root; supported frameworks must be listed |
| Syncfusion packages fail to install | Check npm registry access; try `npm cache clean --force` |
| TypeScript errors after generation | Ensure `tsconfig.json` has `"jsx": "react-jsx"` or `"jsx": "react"` |
| Components won't render | Verify Syncfusion license key is provided (see Stage 2, Section 5.6.5) |

---

## 11. Testing & Validation

### 11.1 Component Testing

Generated components should:
- Render without errors
- Pass prop validation
- Handle edge cases (empty data, large datasets, etc.)
- Maintain accessibility standards (WCAG 2.1 AA)
- Support keyboard navigation (Tab, Enter, Escape)
- Have semantic HTML structure that is crawlable before React hydration (JavaScript is required for interactivity — this is expected for React components)
- Have proper color contrast ratios

### 11.2 Web Standards Compliance Testing

- **Accessibility:**
  - Automated: axe DevTools, WAVE, Lighthouse audits
  - Manual: Screen reader testing (NVDA, JAWS, VoiceOver)
  - Keyboard-only navigation validation
  - Focus management testing
- **Performance:**
  - Lighthouse performance score > 90
  - First Contentful Paint (FCP) < 1.8s
  - Cumulative Layout Shift (CLS) < 0.1
- **Security:**
  - No XSS vulnerabilities (input sanitization verified)
  - No hardcoded secrets or API keys
  - Content Security Policy compatibility
- **SEO:**
  - Semantic HTML structure validated
  - Meta tags present (for public components)
- **Responsive Design:**
  - Mobile (320px), Tablet (768px), Desktop (1280px) viewports
  - Touch targets minimum 44x44px
  - Readable font sizes at all breakpoints

### 11.3 Project Integration Testing

- Generated code inserts correctly
- No conflicts with existing imports
- Project builds successfully after generation
- No breaking changes to existing code
- Dependencies installed correctly

---

## 6. Implementation & Installation

### 6.1 Agent Skills Structure Compliance

This skill is built according to the [Agent Skills Specification](https://agentskills.io/specification):

**✓ Compliant:**
- Single `SKILL.md` entry point with YAML frontmatter
- `scripts/` directory contains all executable code (**JavaScript/Node.js**)
- `references/` directory contains on-demand documentation
- `assets/` directory contains templates and data files
- Progressive disclosure: metadata (~2KB) → orchestrator (~5KB) → stages (~3-8KB each)
- File references are one level deep from `SKILL.md`
- All paths relative from skill root

**Language Choice: JavaScript**

✅ **Why JavaScript:**
- Native to React/Node.js/npm ecosystem (target platform)
- Direct npm package manager control
- Easy parsing and manipulation of .tsx/.jsx/.ts/.json files
- Cross-platform via Node.js (Windows, macOS, Linux)
- Fast execution with minimal overhead
- Access to npm/npx ecosystem (lodash, prettier, etc.)
- Same language as generated output (easier validation)

**Installation Command:**
```bash
# Validate structure
skills-ref validate ./ui-builder-skill

# Install as skill
npx skills add ./ui-builder-skill -y

# Or publish to registry and install
npm publish
npx skills add ui-builder-skill -y
```

### 6.2 Execution Flow

**User Activation:**
```
1. User opens project in VS Code/Cursor/Agent Editor
2. User types: "Create a login form with email and password"
3. Agent system loads SKILL.md (metadata only, ~2KB)
4. Agent recognizes UI Builder Skill from description
5. Orchestrator activates: scripts/orchestrator.js loads
6. Stage 1-9 execute sequentially, referencing:
   - Reference files from references/ (on-demand)
   - Templates from assets/templates/ (during code gen)
   - Data files from assets/data/ (during validation/mapping)
7. Generated component inserted into user's project
```

### 6.3 File Size & Performance (JavaScript Implementation)

| Component | Size | When Loaded |
|-----------|------|-------------|
| SKILL.md | ~2KB | Startup |
| scripts/orchestrator.js | ~5KB | Activation |
| Each stage-X.js | ~3-8KB | Execution |
| scripts/context.js + utils.js | ~4KB | Startup |
| scripts/config.js | ~2KB | Startup |
| References (all) | ~100KB | On-demand |
| Templates (all) | ~30KB | Generation phase |
| Data files (all) | ~50KB | Validation/mapping phase |
| **Total Core (JavaScript)** | **~16KB** | Always loaded |
| **Total with References** | **~160KB** | With on-demand docs |
| **Total Full** | **~300KB** | Everything |

**Performance Notes:**
- Node.js runtime: Already installed on dev machines
- Execution time per stage: ~100-500ms
- Template processing: Fast (native JavaScript)
- npm integration: Direct (no subprocess overhead)
- Result: Lightweight core, comprehensive features on-demand.

### 6.4 JavaScript Dependencies

**Recommended npm packages for scripts/**

- `prettier` - Code formatting validation
- `lodash` - Utility functions
- `fast-json-parse` - JSON parsing
- `recast` - AST transformation for code updates
- `semver` - Version comparison for dependency resolution
- `glob` - File pattern matching
- `execa` - Execute npm commands

**Built-in Node.js modules (no dependencies):**
- `fs/promises` - File system operations
- `path` - Path manipulation
- `process` - Environment & process control
- `child_process` - Spawn npm install, build commands
- `crypto` - Hashing for cache keys

**Installation:**
```bash
cd scripts
npm init -y
npm install prettier lodash fast-json-parse recast semver glob execa
```

### 6.5 Asset Files Reference

**Key Asset Files:**

- `assets/data/component-variants.json` — Login forms (A-F), Registration (A-E), Data Tables (A-F), Navigation (A-E)
- `assets/data/syncfusion-components.json` — Maps "email input" → "TextBoxComponent from @syncfusion/ej2-react-inputs"
- `assets/data/validation-rules.json` — WCAG 2.1 AA rules, security, performance checks
- `assets/data/keywords.json` — Intent classification ("login", "form", "table", "dark theme", etc.)
- `assets/templates/component/` — React component templates (.tsx)
- `assets/templates/stylesheet/` — CSS module templates (.module.css)
- `assets/templates/interface/` — TypeScript interface templates (.ts)
- `assets/examples/` — Sample generated output for reference

### 6.6 Configuration & Defaults

**Location:** `scripts/config.js` (JavaScript)

Contains default configurations (exported as JavaScript object):
```javascript
module.exports = {
  wcagLevel: 'AA',                          // strict, moderate, basic
  responsiveBreakpoints: [320, 768, 1024],
  defaultIndentation: 2,
  defaultStyleMethod: 'css-modules',
  syncfusionPackageVersion: '^25.1.35',
  validationTimeout: 5000,
  dependencyResolution: 'upgrade',
  // ... more config options
}
```

### 6.7 Validation & Testing

Validate skill structure:
```bash
skills-ref validate ./ui-builder-skill
```

This checks:
- ✓ SKILL.md frontmatter format
- ✓ name field (lowercase, hyphens only)
- ✓ description field (non-empty, <1024 chars)
- ✓ File references one level deep
- ✓ All referenced files exist

---

## 7. Summary: Agent Skills Alignment

| Agent Skills Requirement | UI Builder Implementation |
|---|---|
| Single SKILL.md entry | ✓ SKILL.md with metadata + instructions |
| Progressive disclosure | ✓ Metadata ~2KB, docs on-demand |
| scripts/ for executable | ✓ 12 stage files + orchestrator |
| references/ for docs | ✓ 7 reference files loaded on-demand |
| assets/ for resources | ✓ templates/, data/, examples/, images/ |
| File references one level deep | ✓ All paths from skill root |
| Metadata in frontmatter | ✓ name, description, compatibility, metadata |
| No deeply nested files | ✓ Flat structure under 4 main directories |
| Validation compatible | ✓ Can pass skills-ref validate |

**Result:** Full Agent Skills compliance with efficient context loading and comprehensive functionality.

### 11.4 User Acceptance Testing

- Natural language requests are accurately interpreted
- Generated components match user expectations
- Layout confirmation options are relevant and helpful
- Customization requests produce expected results
- Error messages are helpful and actionable
- Web standards compliance features are transparent to users

---

## 12. Future Enhancements

**Web Standards & Compliance:**
- Progressive Web App (PWA) generation templates
- Web Accessibility audit and auto-fix suggestions
- Design token system integration (CSS variables, responsive typography)
- Automated security scanning for dependencies
- Performance budget enforcement

**Developer Experience:**
- AI-powered component recommendations based on usage patterns
- Component marketplace for sharing custom templates
- Batch operations for generating multiple pages
- Component versioning and migration tools
- Debug mode with generated code explanations

**Integration & Extensibility:**
- Integration with design tools (Figma, Adobe XD, Penpot)
- Custom component library support
- Storybook auto-generation for design systems
- API integration templates with type generation — **frontend only**: React hooks and TypeScript interfaces for consuming REST/GraphQL APIs; no backend code generation
- State management setup (Redux, Zustand, Context API templates)

**Cross-Platform:**
- Cross-framework support (Vue, Angular, Svelte, Lit)
- Mobile framework support (React Native, Flutter)
- Backend template generation (API endpoints, schemas)

---

## 13. Success Metrics

- **Generation Performance:**
  - Layout confirmation + code generation: < 5 seconds total
  - Component error rate: < 1% on initial generation
  - User refinement iterations: ≤ 2 before satisfaction

- **Code Quality:**
  - Code quality score: Matches Syncfusion standards
  - 100% web standards compliance on generated code
  - Zero hardcoded secrets/API keys in components

- **Accessibility:**
  - 100% WCAG 2.1 AA compliance
  - Automatic accessibility audit pass rate: > 95%
  - Keyboard navigation coverage: 100%

- **User Satisfaction:**
  - User satisfaction score: > 4.5/5
  - Layout confirmation accuracy: > 90% first-time matches
  - Adoption rate: > 60% of React developers in beta
  - Net Promoter Score (NPS): > 50

- **Security:**
  - Zero XSS vulnerabilities in generated code
  - Input sanitization: 100% coverage where needed
  - Security audit pass rate: 100%


