# Stage 1: Intent Analysis

**Purpose:** Parse and validate the user's natural language request, identify component type and modifiers, resolve ambiguities.

**AI Should:**
- Read the user's raw query carefully
- Identify primary intent: `generate_component`, `generate_page`, or `modify_existing`
- Extract component type (e.g., "login form" → form/login, "data table" → table/data)
- Extract modifiers (e.g., "dark theme" → styling:dark, "with OAuth" → feature:oauth)
- Identify target directory if specified (e.g., "in the auth folder" → targetDir:auth/)

**Ambiguity Resolution:**
If the request is unclear, ask ONE clarifying question. Examples:

| Ambiguous Input | Clarifying Question |
|---|---|
| "Build me a form" | "What kind of form? (login, registration, contact, multi-step)" |
| "Add a component" | "What component would you like? (data table, navigation, modal, etc.)" |
| "Make it better" | "Which component and what aspect? (accessibility, styling, layout)" |

**Output to User:**
One-line confirmation:
```
✓ Understood: Generating a dark-themed login form with "Remember Me" support.
Starting project detection...
```

**Reference:** For component type catalog, see LAYOUT-VARIANTS.md

**Status:** This stage requires NO user interaction for confirmation. AI decides intent based on pure reasoning.
