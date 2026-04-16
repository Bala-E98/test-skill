# Stage 6: Code Generation

**Purpose:** Generate production-ready React code, CSS, and TypeScript interfaces with accessibility and web standards compliance.

**AI Should:**

1. **Generate .tsx component file**:
   - React functional component with hooks
   - Proper Syncfusion imports
   - TypeScript interface for props
   - Event handlers and state management
   - Error handling and validation
   - WCAG 2.1 AA accessibility markup (ARIA labels, semantic HTML, focus management)
   - JSDoc comments explaining usage

2. **Generate CSS stylesheet** (based on project preference):
   - CSS Modules: `.module.css` with class names
   - Tailwind: Class-based styling
   - Inline: Style objects in component
   - Responsive design: Mobile-first (320px, 768px, 1024px+)
   - Light/dark theme support if needed

3. **Generate TypeScript interfaces**:
   - Props interface with all prop types
   - State types if using hooks
   - Event handler signatures

4. **Reference code standards** from:
   - WEB-STANDARDS.md (accessibility + security rules)
   - CODE-BLOCKS.md (prebuilt patterns and best practices)

**Code Generation Standards:**

- **Semantic HTML:** Use proper HTML5 elements (`<form>`, `<label>`, `<button>`, etc.)
- **Accessibility:** ARIA labels, roles, aria-describedby, aria-invalid where needed
- **TypeScript:** No `any` types, full type safety
- **Error Handling:** Try-catch blocks, user-friendly error messages
- **Responsive:** Flex/Grid layouts, media queries
- **Performance:** React.memo if needed, useCallback for handlers
- **Security:** No dangerouslySetInnerHTML, sanitize inputs, no hardcoded secrets
- **Comments:** JSDoc on component, explain complex logic

**Example Output Files:**

```
components/LoginForm/
  ├── LoginForm.tsx              (React component)
  ├── LoginForm.module.css       (Styles, if CSS Modules)
  ├── types.ts                   (TypeScript interfaces)
  └── index.ts                   (Barrel export)
```

**User Interaction:** 
Optional review of generated code. No blocking confirmation.

**Status:** AI generates without user decision. User can review/adjust if needed.

**Reference:** See CODE-BLOCKS.md for prebuilt patterns and EXAMPLES.md for real samples.
