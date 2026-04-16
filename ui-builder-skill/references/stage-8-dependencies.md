# Stage 8: Dependencies

**Purpose:** Detect required packages, resolve version conflicts, prepare npm install command.

**AI Should:**

1. **Detect Required Packages:**
   - Scan generated code imports
   - List all @syncfusion/ej2-react-* packages used
   - Check for other dependencies (react, react-dom, etc.)

2. **Check Project's package.json:**
   - What packages already installed?
   - What versions are currently in use?
   - Any version conflicts?

3. **Resolve Conflicts:**
   - If Syncfusion package already installed:
     - Is version compatible?
     - Suggest upgrade if needed
   - If peer dependencies conflict:
     - Recommend resolution (upgrade, downgrade, or compromise)

4. **Prepare Installation Command:**
   - Generate npm/yarn/pnpm install command
   - List packages to add
   - List packages to upgrade (if needed)

**Example Output:**

```
✓ Dependency Analysis

New Packages to Install:
  - @syncfusion/ej2-react-inputs (latest)
  - @syncfusion/ej2-react-buttons (latest)

Existing Packages:
  ✓ react@18.2.0 (compatible)
  ✓ react-dom@18.2.0 (compatible)

Conflicts: None

Install Command:
$ npm install @syncfusion/ej2-react-inputs @syncfusion/ej2-react-buttons

Alternatively with yarn:
$ yarn add @syncfusion/ej2-react-inputs @syncfusion/ej2-react-buttons

Or with pnpm:
$ pnpm add @syncfusion/ej2-react-inputs @syncfusion/ej2-react-buttons
```

**User Interaction:**
User confirms npm install or does it manually:
```
Ready to install dependencies?
[Install] [Show Command] [Skip]
```

**Status:** AI detects and prepares. User decides whether to install now or later.
