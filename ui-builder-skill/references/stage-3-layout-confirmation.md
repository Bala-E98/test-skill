# Stage 3: Layout Confirmation

**Purpose:** Confirm the exact layout structure before code generation. Present 2 variants and allow user to choose.

**AI Should:**

1. **Read component type** from Stage 1 intent analysis
2. **Look up variants** from LAYOUT-VARIANTS.md for that component type
3. **Present 2 variants** with clear descriptions
4. **Recommend best fit** based on user context and query analysis
5. **Ask clarifying questions** specific to component type
6. **User confirms** or selects alternative variant

**Presentation Format:**

```
✓ Component Type: Login Form

Recommended Layouts (pick one):

📌 Variant A: Minimal (Best for simple apps)
  Fields: Email, Password, Submit button
  Features: Basic validation, light theme
  
🌟 Variant B: Standard (Recommended for most projects)
  Fields: Email, Password, Submit, "Remember me" checkbox
  Features: Validation + remember-me toggle, theme options
  Links: "Forgot password?" link

□ Variant C: Advanced (For enterprise apps)
  Fields: Email, Password, 2FA option, Submit
  Features: Full validation, MFA support, social login buttons

Which variant? [A] [B Recommended] [C]
```

**Clarifying Questions by Component Type:**

**For Forms:**
- What fields are required? (list field names)
- Need optional features? (remember-me, password strength, social login, etc.)
- Multi-step or single-step?
- How to show errors? (inline, toast, dialog)

**For Data Tables:**
- What data columns? (define structure)
- Interactions needed? (sorting, filtering, pagination, row selection)
- Editable rows or read-only?
- Actions? (export, print, delete, view details)

**For Navigation:**
- How many items? (small <5, medium 5-10, large >10)
- Hierarchical? (flat, single dropdown, multi-level)
- Position? (horizontal top, vertical sidebar, both)
- Mobile behavior? (always visible, hamburger menu, drawer)

**For All Components:**
- Light/dark/custom theme?
- TypeScript or JavaScript?
- Any special accessibility needs?

**User Decision:**
User confirms final layout structure. This locks the layout for code generation.

**Output:**
```
✓ Layout Locked: Login Form - Variant B
  - Email field
  - Password field
  - Remember-me checkbox
  - Submit button
  - Forgot password link

Ready for component picking...
```

**Status:** ⭐ **USER DECISION #1** - User must confirm layout variant.

**Reference:** See LAYOUT-VARIANTS.md for full variant catalog.
