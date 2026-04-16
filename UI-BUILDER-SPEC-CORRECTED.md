# UI Builder Skill — Corrected Specification (v2)

**Status:** Ready for Implementation  
**Target Release:** Q2 2026  
**Architecture:** Agent Skills Specification Compliant (Progressive Disclosure)  
**Last Updated:** April 16, 2026

---

## 1. Executive Summary

**UI Builder Skill** is a **frontend-only** React component generator that guides an AI agent through an 8-stage orchestrated workflow to generate production-ready UI components using Syncfusion components.

**Key Characteristics:**
- ✅ **AI-Driven Reasoning** — Pure AI analysis at each stage (no keyword lookups)
- ✅ **Stateless Architecture** — Each stage independent; AI uses conversation history as state
- ✅ **2 User Decisions** — Layout (Stage 3) + Validation (Stage 7)
- ✅ **Fully Automated Components** — Stage 4 (Component Picking) is AI automatic
- ✅ **Progressive Disclosure** — SKILL.md <500 lines; guides load on-demand
- ✅ **No Code Execution Scripts** — No stage_*.py files; pure guidance documents
- ✅ **Direct Code Insertion** — AI writes files directly to user project (IDE agent)

**Scope:** Frontend UI generation only. React 18+, Next.js 13+, Vite, Create React App.

---

## 2. New Folder Structure (Agent Skills Compliant)

```
ui-builder-skill/
│
├── SKILL.md                              # <500 lines: Orchestrator + overview
│                                         # Frontmatter + AI instructions
│
├── references/                           # Progressive disclosure guides
│   ├── stage-1-intent-analysis.md        # Intent analysis guidance
│   ├── stage-2-project-detection.md      # Project detection guidance
│   ├── stage-3-layout-confirmation.md    # Layout variant options
│   ├── stage-4-component-picking.md      # Component selection logic
│   ├── stage-6-code-generation.md        # Code generation standards
│   ├── stage-7-validation.md             # Validation framework
│   ├── stage-8-dependencies.md           # Dependency detection
│   │
│   ├── SYNCFUSION-MAPPING.md             # Component skills reference
│   ├── LAYOUT-VARIANTS.md                # 2 variants per component type
│   ├── WEB-STANDARDS.md                  # WCAG 2.1 AA + security + perf
│   ├── CODE-BLOCKS.md                    # Prebuilt code references
│   ├── EXAMPLES.md                       # Real generated code samples
│   └── TROUBLESHOOTING.md                # Error solutions & FAQ
│
├── assets/
│   └── validation-rules.md               # Validation checklist reference
│
└── README.md                             # (Optional) Skill overview

❌ NO: scripts/, stage-5, stage-9, UIBuilderContext
✅ YES: Pure AI reasoning, conversation history as state
```

---

## 3. Key Architectural Changes from Old Spec

| Aspect | Old Spec | New Spec | Benefit |
|--------|----------|----------|---------|
| **Orchestration** | scripts/stage-*.py files execute stages | SKILL.md guides AI through stages | AI reasons, doesn't execute templates |
| **State Management** | UIBuilderContext passed between stages | Conversation history maintains state | Stateless, flexible, agent-native |
| **Component Picking** | JSON lookup + keyword matching | AI analyzes skills + query (Stage 4) | Intelligent, contextual decisions |
| **Intent Analysis** | Keyword extraction (stage-1-intent.py) | AI pure reasoning | No keyword limitations |
| **Stage 5 (Preview)** | Generate interactive preview | REMOVED (skip directly to code) | Faster workflow, less context |
| **Stage 9 (Insertion)** | scripts/stage-9-insertion.py | AI writes files directly | Agent-native, no extra layer |
| **Validation** | Checklist scanning | AI pure reasoning + rules ref | Intelligent explanation |
| **File Structure** | scripts/ + references/ | references/ + assets/ only | Simpler, Agent Skills compliant |

---

## 4. The 8-Stage Orchestration Flow

### Stage Overview
```
User Query
    ↓
Stage 1: Intent Analysis (AI Reasoning)
    ↓
Stage 2: Project Detection (Auto-detect)
    ↓
Stage 3: Layout Confirmation ⭐ USER DECISION #1
    ↓
Stage 4: Component Picking (AI Automatic - FULLY AUTOMATED)
    ↓
Stage 6: Code Generation (AI Codes)
    ↓
Stage 7: Validation ⭐ USER DECISION #2
    ↓
Stage 8: Dependencies (AI Detects)
    ↓
Code Insertion (AI writes files)
    ↓
Success Report
```

### Stage Details

#### **Stage 1: Intent Analysis**
- **Input:** User's natural language query
- **AI Does:** Analyze intent (generate/modify/page), extract component type, identify modifiers
- **User Interaction:** Answer 1 clarifying question if ambiguous
- **Output:** Clear intent + component type + requirements
- **Reference:** `references/stage-1-intent-analysis.md`

#### **Stage 2: Project Detection**
- **Input:** Project root directory
- **AI Does:** Auto-detect framework, language, CSS strategy, Syncfusion license status
- **User Interaction:** Confirm or override detected settings
- **Output:** Project configuration locked for code generation
- **Reference:** `references/stage-2-project-detection.md`

#### **Stage 3: Layout Confirmation** ⭐ **USER DECISION #1**
- **Input:** Confirmed intent from Stage 1
- **AI Does:** Present 2 layout variants, recommend best fit, ask clarifying questions
- **User Decision:** Confirm variant or select alternative
- **Output:** Locked layout specification
- **Reference:** `references/stage-3-layout-confirmation.md` + `references/LAYOUT-VARIANTS.md`

#### **Stage 4: Component Picking** (FULLY AUTOMATED ✅)
- **Input:** Confirmed layout from Stage 3
- **AI Does:** Analyze layout elements → read Syncfusion component skills → pick best components
- **User Interaction:** NONE - AI decides automatically
- **Output:** Component mapping + skill references
- **Reference:** `references/stage-4-component-picking.md` + `references/SYNCFUSION-MAPPING.md`

#### **Stage 6: Code Generation**
- **Input:** Layout + components + project config + web standards
- **AI Does:** Generate .tsx, .css, .ts files with accessibility + standards compliance
- **User Interaction:** Review generated code (optional adjustments)
- **Output:** Production-ready code files
- **Reference:** `references/stage-6-code-generation.md` + `references/WEB-STANDARDS.md` + `references/CODE-BLOCKS.md`

#### **Stage 7: Validation** ⭐ **USER DECISION #2**
- **Input:** Generated code
- **AI Does:** Validate WCAG 2.1 AA + security + performance, auto-fix where possible
- **Validation Result:** PASS ✓ or FAIL ✗
- **User Decision:** If FAIL → Override/Request fixes OR if PASS → Proceed
- **Output:** Validated code + compliance report
- **Reference:** `references/stage-7-validation.md` + `assets/validation-rules.md`

#### **Stage 8: Dependencies**
- **Input:** Generated code + project config
- **AI Does:** Detect required packages, resolve version conflicts, suggest npm install
- **User Interaction:** Confirm npm install (or user runs it)
- **Output:** Dependencies installed or install command provided
- **Reference:** `references/stage-8-dependencies.md`

#### **Code Insertion** (No separate stage)
- **Input:** Validated code + project config
- **AI Does:** Write files to user's project directories
- **User Interaction:** Confirm file locations before insertion
- **Output:** Files inserted + success report with paths

---

## 5. Key Design Decisions

### 5.1 No UIBuilderContext Object
- ❌ **Old approach:** Unified state object passed through all stages
- ✅ **New approach:** Each stage independent; AI reads conversation history to maintain context
- **Why:** Agent-native, stateless, more flexible for conversational interaction

### 5.2 No Scripts/ Directory
- ❌ **Old approach:** 9 Python scripts (orchestrator.py, stage-*.py, etc.)
- ✅ **New approach:** Only guidance documents (references/*.md)
- **Why:** Agent Skills spec says scripts should be "self-contained utilities"; stages are guidance, not executors

### 5.3 Stage 4 Fully Automated
- ❌ **Old approach:** User confirms component picks (Stage 4 → user interaction)
- ✅ **New approach:** AI automatically picks components (Stage 4 → no user interaction)
- **Why:** Component selection is deterministic; AI can reason about best fit based on layout + skills

### 5.4 Only 2 User Decisions
- ✅ **Stage 3 (Layout Confirmation):** User confirms which variant
- ✅ **Stage 7 (Validation Override):** User confirms pass/fail → override if FAIL
- **Why:** Streamlined workflow; AI handles everything except layout intent + validation risk

### 5.5 No Preview Stage
- ❌ **Old approach:** Stage 5 generates interactive HTML preview
- ✅ **New approach:** Skip directly from Stage 4 → Stage 6 (code generation)
- **Why:** Less context, faster workflow; AI can show code instead of visual preview

### 5.6 No Code Insertion Stage
- ❌ **Old approach:** Stage 9 (scripts/stage-9-insertion.py) handles file insertion
- ✅ **New approach:** AI writes files directly (IDE agent mode)
- **Why:** Simpler, more direct; AI agent has file I/O capability

### 5.7 Pure AI Reasoning (No Keyword Lookups)
- ❌ **Old approach:** Stage 1 and 3 used keyword extraction + JSON lookup
- ✅ **New approach:** AI pure reasoning with reference guidance
- **Why:** More intelligent, contextual; AI doesn't need keyword maps

### 5.8 Error Handling with Retry Logic
- **Retry 2x** at any failed stage with fallback approaches
- **Skip on Failure** → If 2 retries fail, skip to next stage with warning
- **Allow Rollback** → User can restart from any previous stage
- **Why:** Resilient, user-controlled recovery

---

## 6. File Descriptions

### 6.1 SKILL.md (500 lines max)

**Structure:**
```yaml
---
name: ui-builder-skill
description: AI-driven React UI component generator using Syncfusion. 
             Guides AI through 8-stage orchestrated workflow to generate 
             production-ready components with WCAG 2.1 AA accessibility.
license: Proprietary
compatibility: React 18+, Node.js 18+, Syncfusion license
allowed-tools: read write
metadata:
  version: "2.0"
  architecture: "Agent Skills Spec Compliant"
---
```

**Body Contents:**
- Overview (what, when, scope boundaries)
- Quick Start (2-3 examples)
- 8-Stage Orchestration Flow (text diagram)
- Error Handling (retry logic)
- Boundary Rules (critical)
- Where to Find Details (reference links)

### 6.2 Stage Guides (Each ~100-200 lines)

| File | Purpose | Usage |
|------|---------|-------|
| `stage-1-intent-analysis.md` | How AI should analyze user intent | During Stage 1 |
| `stage-2-project-detection.md` | What to detect + how to detect | During Stage 2 |
| `stage-3-layout-confirmation.md` | How to present variants + recommendation logic | During Stage 3 |
| `stage-4-component-picking.md` | Component selection algorithm | During Stage 4 |
| `stage-6-code-generation.md` | Code gen patterns + web standards | During Stage 6 |
| `stage-7-validation.md` | Validation logic + binary pass/fail | During Stage 7 |
| `stage-8-dependencies.md` | Dependency detection patterns | During Stage 8 |

### 6.3 Support References

| File | Purpose | When Loaded |
|------|---------|------------|
| `SYNCFUSION-MAPPING.md` | Component skills catalogue | Stage 4 (component picking) |
| `LAYOUT-VARIANTS.md` | 2 variants per component type | Stage 3 (layout confirmation) |
| `WEB-STANDARDS.md` | WCAG 2.1 AA + security + performance | Stage 6 & 7 |
| `CODE-BLOCKS.md` | Prebuilt code references | Stage 6 (code generation) |
| `EXAMPLES.md` | Real generated code samples | On-demand reference |
| `TROUBLESHOOTING.md` | Error solutions & FAQ | On error or user request |

### 6.4 Assets

| File | Purpose | Usage |
|------|---------|-------|
| `validation-rules.md` | Validation checklist | Stage 7 (reference) |

---

## 7. State Management (Stateless Architecture)

### How It Works

**Old approach:**
```
UIBuilderContext {
  intent: {...},
  project: {...},
  layout: {...},
  components: {...},
  generatedCode: {...}
}
// Passed between stages
```

**New approach:**
```
No shared state object.
Each stage reads from conversation history:
  
Stage 1 → User query
Stage 2 → Detected project (auto)
Stage 3 → User confirms layout (conversation)
Stage 4 → AI reads Stage 3 choice from history
Stage 6 → AI reads Stages 1-4 from history
Stage 7 → AI reads code from Stage 6, validates
Stage 8 → AI reads code + project from history
```

**Benefit:** Stateless, agent-native, supports restart from any stage

---

## 8. Error Handling & Recovery

### Retry Logic

At any stage, if AI encounters critical error:
1. **Attempt 1** — Retry with same approach
2. **Attempt 2** — Retry with fallback approach
3. **Skip on Failure** — If 2 retries fail, skip to next stage (with warning)

### Rollback

User can restart from any previous stage:
```
User at Stage 7: "I want to go back to Stage 3"
AI: Reads conversation history up to Stage 3
AI: Restarts from Stage 3 (preserves Stages 1-2)
```

### Validation Failure Override

If Stage 7 validation FAILS:
- Present issues to user
- Ask: "Override and proceed?" or "Request fixes?"
- User decision recorded
- Proceed or fix based on choice

---

## 9. Component Picking (Stage 4) — Why Fully Automated

**Old way:** User reviewed + confirmed component picks
**New way:** AI picks automatically

**Why AI can decide:**
1. Component options are predefined per layout element
2. AI reads Syncfusion component skills library
3. Given requirements, AI selects best fit with reasoning
4. User never needs to wade through component details
5. Fastens workflow; reduces decision fatigue

**Example:**
```
Layout: Login form with email, password, remember-me
  ↓
AI reads stage-4-component-picking.md
AI analyzes: 
  - Email field → TextBox (@syncfusion/ej2-react-inputs)
  - Password → TextBox
  - Checkbox → CheckBox (@syncfusion/ej2-react-buttons)
  - Button → Button
AI shows mapping + reasoning to user
NO USER INTERACTION NEEDED
  ↓
Proceed to Stage 6
```

---

## 10. Scope Boundaries (Critical)

### ✅ In Scope — What This Skill Generates

- React components (.tsx/.jsx)
- CSS stylesheets (CSS Modules, Tailwind, inline)
- TypeScript interfaces
- Syncfusion component integration
- Client-side validation
- WCAG 2.1 AA accessibility markup
- Responsive design
- Component exports
- Syncfusion license injection

### ❌ Out of Scope — What This Skill Never Generates

- Backend / server code (API routes, endpoints)
- Database schemas or ORM models
- Authentication/authorization logic
- Server-side validation
- Routing configuration
- Environment secrets
- Infrastructure / deployment config

---

## 11. User Interaction Model

### Decision Points

| Stage | Decision | Impact |
|-------|----------|--------|
| Stage 1 | Answer clarifying question (if needed) | Clarifies component type |
| Stage 2 | Confirm/override detected settings | Locks project config |
| **Stage 3 ⭐** | Confirm layout variant | **Locks layout structure** |
| Stage 4 | NONE (AI automatic) | AI picks components |
| Stage 6 | Review code (optional) | No blocking |
| **Stage 7 ⭐** | Confirm validation / override | **Binary pass/fail decision** |
| Stage 8 | Confirm npm install | User runs or AI runs |

### Restart Capability

At any stage, user can:
- **Stop** the workflow
- **Later, restart** from any previous stage
- AI reads conversation history to restore context
- Continue from that point

---

## 12. Progressive Disclosure (Agent Skills Compliance)

| Loading Phase | Content | Size | When |
|---------------|---------|------|------|
| **Metadata** | SKILL.md frontmatter (name, description, compat) | ~100 tokens | Skill startup |
| **Instructions** | SKILL.md body (orchestration + overview) | <5000 tokens | Skill activation |
| **Guides** | references/stage-*.md (8 files) | ~2KB each | On-demand per stage |
| **References** | SYNCFUSION-MAPPING, LAYOUT-VARIANTS, etc. | ~5KB each | On-demand |
| **Assets** | validation-rules.md | ~2KB | During Stage 7 |

**Result:** Core skill loads ~5-10KB; full docs available on-demand

---

## 13. Code Generation Standards

All generated code follows:
- **ES6+** syntax (const/let, arrow functions)
- **TypeScript** for type safety
- **Semantic HTML5** (proper element usage)
- **WCAG 2.1 AA** (accessibility compliance)
- **Responsive design** (mobile-first)
- **Performance** (React.memo, lazy loading)
- **Security** (input sanitization, no XSS)
- **SEO-friendly** markup (semantic structure)
- **JSDoc** documentation

---

## 14. Supported Components & Pages

### Component Categories

**Forms:** Login, registration, password reset, contact, multi-step wizards  
**Data Display:** Tables/grids, lists, charts, tree views, kanban boards  
**Navigation:** Navbars, sidebars, breadcrumbs, tabs, pagination  
**Common Patterns:** Modals, notifications, dropdowns, carousels, badges  
**Page Templates:** Dashboards, e-commerce, portfolios, profiles, landing pages

---

## 15. Integration with Syncfusion Component Skills

The skill **reads** the official Syncfusion React components skills library at Stage 4 to:
- Understand available components per category
- Read component best practices + patterns
- Determine component props + event handling
- Select appropriate accessibility features

**Installation:**
```bash
npx skills add syncfusion/react-ui-components-skills -y
```

---

## 16. Boundary Rules for AI Agents (CRITICAL)

When executing this skill, an AI agent **MUST**:

1. **Only modify frontend files** — Never touch `app/api/`, `pages/api/`, `backend/`, etc.
2. **Never generate async/await server functions** — No Route Handlers, Server Actions
3. **Never read/write secrets** — Exception: `SYNCFUSION_LICENSE_KEY` when user provides
4. **Use mock data** — useState with sample data, no real API calls
5. **If user asks backend work** → Respond: *"This skill generates frontend UI only. Backend integration is your responsibility. Shall I proceed with the frontend component?"*

---

## 17. Summary of Changes from Old Spec

| Change | Reason | Impact |
|--------|--------|---------|
| Remove UIBuilderContext | Stateless architecture | More flexible, agent-native |
| Remove scripts/ | Guides ≠ executors | Simpler structure |
| Remove stage-5 (preview) | Less context, faster | Speeds workflow |
| Remove stage-9 (insert) | AI can write files | Simpler orchestration |
| Stage 1 → Pure AI reasoning | No keyword limits | Smarter analysis |
| Stage 4 → Automatic (no user decision) | Deterministic | Faster flow |
| Stage 3 → 2 variants only | Simpler choice | Less decision fatigue |
| Stage 7 → Binary pass/fail | Clear validation | Easy override |
| Progressive disclosure | Agent Skills spec | Efficient context use |

---

## 18. Implementation Checklist

- [ ] Create SKILL.md (<500 lines) with 8-stage orchestration flow
- [ ] Create stage-1-intent-analysis.md with AI reasoning guidance
- [ ] Create stage-2-project-detection.md with auto-detect logic
- [ ] Create stage-3-layout-confirmation.md with 2 variants + recommendation
- [ ] Create stage-4-component-picking.md with component selection logic
- [ ] Create stage-6-code-generation.md with code generation standards
- [ ] Create stage-7-validation.md with binary pass/fail logic
- [ ] Create stage-8-dependencies.md with dependency detection
- [ ] Create SYNCFUSION-MAPPING.md (component reference)
- [ ] Create LAYOUT-VARIANTS.md (2 variants per type)
- [ ] Create WEB-STANDARDS.md (WCAG 2.1 AA + security rules)
- [ ] Create CODE-BLOCKS.md (prebuilt code references)
- [ ] Create EXAMPLES.md (real code samples)
- [ ] Create TROUBLESHOOTING.md (error solutions)
- [ ] Create assets/validation-rules.md (validation checklist)
- [ ] Create README.md (overview)
- [ ] Validate SKILL.md frontmatter against Agent Skills spec
- [ ] Test reference links (one level deep)

---

## 19. Next Steps

1. **Review this corrected spec** with team
2. **Approve structure + orchestration flow**
3. **Create SKILL.md** (orchestrator)
4. **Create stage guides** (references/)
5. **Create support references**
6. **Create assets/validation-rules.md**
7. **Implement AI orchestration**
8. **Test 8-stage workflow**

---

**Questions?** Review sections 3-5 for architectural overview, sections 8-10 for operational details.
