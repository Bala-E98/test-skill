# Web Standards & Compliance Reference

**Version:** 1.0.0  
**Last Updated:** April 15, 2026  
**Purpose:** WCAG 2.1 AA, security, performance, and code quality standards enforced during Stage 7 validation

---

## Table of Contents

1. [Accessibility Standards (WCAG 2.1 AA)](#accessibility-standards-wcag-21-aa)
2. [Security Standards](#security-standards)
3. [Performance Standards](#performance-standards)
4. [Code Quality Standards](#code-quality-standards)
5. [Validation Checklist](#validation-checklist)
6. [Auto-Fix Rules](#auto-fix-rules)

---

## Accessibility Standards (WCAG 2.1 AA)

### 1.1 Semantic HTML

**Requirement:** Use semantic HTML elements appropriately

**What to Check:**

```tsx
// ✗ BAD - Non-semantic
<div onClick={handleSubmit} className="button">
  Submit
</div>

// ✓ GOOD - Semantic button
<button type="submit" onClick={handleSubmit}>
  Submit
</button>

// ✓ GOOD - Semantic form structure
<form onSubmit={handleSubmit}>
  <fieldset>
    <legend>Contact Information</legend>
    <label htmlFor="email">Email</label>
    <input id="email" type="email" required />
  </fieldset>
</form>
```

**Validation Rules:**
- [ ] All buttons use `<button>` or `<a>` elements (not `<div>`)
- [ ] All form inputs have associated labels via `htmlFor`
- [ ] Forms use `<form>` element, not `<div>`
- [ ] Headings use proper `<h1>-<h6>` hierarchy (no skipping levels)
- [ ] Lists use `<ul>`, `<ol>`, `<li>` (not `<div>` groups)
- [ ] Navigation uses `<nav>` element
- [ ] Main content in `<main>` element

---

### 1.2 ARIA Attributes

**Requirement:** Add ARIA labels where semantic HTML isn't sufficient

**What to Check:**

```tsx
// Icon button without text needs aria-label
<ButtonComponent
  iconCss="e-icons e-close"
  aria-label="Close dialog"
/>

// Form field without visible label needs aria-label
<TextBoxComponent
  type="search"
  placeholder="Search..."
  aria-label="Search products"
/>

// Error message needs aria-describedby
<TextBoxComponent
  aria-invalid={hasError}
  aria-describedby={hasError ? "email-error" : undefined}
/>
<span id="email-error">{errorMessage}</span>

// Custom combobox needs role and aria-expanded
<ComboBoxComponent
  role="combobox"
  aria-expanded={isOpen}
  aria-controls="options-list"
/>
```

**Validation Rules:**
- [ ] Icon-only buttons have `aria-label`
- [ ] Error messages have `aria-describedby`
- [ ] Invalid fields have `aria-invalid="true"`
- [ ] Required fields have `aria-required="true"`
- [ ] Expandable sections have `aria-expanded`
- [ ] Custom components have appropriate `role` attributes

---

### 1.3 Color Contrast

**Requirement:** Ensure readability for users with low vision

**Minimum Ratios (WCAG 2.1 AA):**
- Normal text: 4.5:1
- Large text (18pt+): 3:1
- UI components: 3:1

**What to Check:**

```css
/* ✓ GOOD - Dark text on light background */
.button {
  color: #000000;        /* Contrast ratio: 21:1 */
  background: #ffffff;
}

/* ✗ BAD - Light gray text on light background */
.hint {
  color: #cccccc;        /* Contrast ratio: 1.9:1 (FAILS) */
  background: #ffffff;
}

/* ✓ GOOD - Focus indicator with 3:1 contrast */
.input:focus {
  outline: 3px solid #0066cc;  /* Contrast: 8.6:1 */
}
```

**Validation Rules:**
- [ ] All text has contrast ≥ 4.5:1 (normal) or 3:1 (large)
- [ ] Focus indicators have contrast ≥ 3:1
- [ ] Placeholder text follows same contrast rules
- [ ] Icons used to convey meaning have 3:1 contrast

---

### 1.4 Keyboard Navigation

**Requirement:** All functionality accessible via keyboard

**What to Check:**

```tsx
// ✓ GOOD - Tab order logical, all interactive elements reachable
<form>
  <TextBoxComponent />          {/* Tab 1 */}
  <ButtonComponent />           {/* Tab 2 */}
  <LinkComponent />             {/* Tab 3 */}
</form>

// ✓ GOOD - Escape closes modal
<DialogComponent
  onKeyDown={(e) => {
    if (e.key === 'Escape') handleClose();
  }}
/>

// ✗ BAD - No keyboard support for autocomplete
<AutoCompleteComponent
  onMouseClick={handleSelect}   // Only mouse!
/>
```

**Validation Rules:**
- [ ] All interactive elements in tab order (no negative tabindex)
- [ ] Tab order is logical (left-to-right, top-to-bottom)
- [ ] No keyboard traps (can always Tab out)
- [ ] Escape key closes modals and dropdowns
- [ ] Enter key submits forms and activates buttons
- [ ] Arrow keys work for lists/tables

---

### 1.5 Focus Management

**Requirement:** Users can see where keyboard focus is

**What to Check:**

```tsx
// ✗ BAD - Removed focus outline (accessibility violation)
input:focus {
  outline: none;  /* REMOVES focus visibility! */
}

// ✓ GOOD - Visible focus indicator
input:focus {
  outline: 3px solid #0066cc;
  outline-offset: 2px;
}

// ✓ GOOD - Move focus after modal opens
<DialogComponent
  onOpen={() => {
    submitButtonRef.current?.focus();
  }}
/>
```

**Validation Rules:**
- [ ] Focus indicators always visible (not removed)
- [ ] Focus outline ≥ 3px thick
- [ ] Focus order follows logical flow
- [ ] Focus managed when modal opens (moves to first input)
- [ ] Focus restored when modal closes

---

### 1.6 Form Validation & Error Messages

**Requirement:** Users understand form requirements and errors

**What to Check:**

```tsx
// ✗ BAD - Relies on color alone
<div style={{ color: 'red' }}>Required field</div>

// ✓ GOOD - Text + icon + association
<span id="email-error" role="alert">
  ⚠️ Email is required
</span>
<TextBoxComponent
  aria-describedby="email-error"
  aria-invalid={true}
/>

// ✓ GOOD - Validation at appropriate times
<TextBoxComponent
  onBlur={() => validateEmail(email)}  // On blur
  onChange={() => clearError()}         // Clear on change
/>
```

**Validation Rules:**
- [ ] Required fields marked with * or text label
- [ ] Error messages descriptive (not just "Error")
- [ ] Error messages linked via `aria-describedby`
- [ ] Validation happens at appropriate times (blur, submit)
- [ ] Error messages include fix suggestion
- [ ] Error icons have text alternative

---

## Security Standards

### 2.1 Input Validation

**Requirement:** Prevent XSS and injection attacks

**What to Check:**

```tsx
// ✗ BAD - Unsanitized user input
const userBio = "<img src=x onerror='alert(1)'>";
<div dangerouslySetInnerHTML={{ __html: userBio }} />

// ✓ GOOD - User input rendered as text (safe)
<div>{userBio}</div>

// ✓ GOOD - Sanitize if HTML is truly needed
import DOMPurify from 'dompurify';
const cleanHTML = DOMPurify.sanitize(userBio);
<div dangerouslySetInnerHTML={{ __html: cleanHTML }} />
```

**Validation Rules:**
- [ ] No `dangerouslySetInnerHTML` with user input
- [ ] No `eval()` or `Function()` constructors
- [ ] No inline event handlers (onClick="code()")
- [ ] User input sanitized before display
- [ ] URL validation before navigation

---

### 2.2 Secrets & Environment Variables

**Requirement:** Never expose API keys or secrets

**What to Check:**

```tsx
// ✗ BAD - Hardcoded secret
const API_KEY = "sk_live_12345abcde";
fetch(`/api/data?key=${API_KEY}`);

// ✓ GOOD - Environment variable (Next.js)
const apiKey = process.env.NEXT_PUBLIC_API_KEY;
fetch(`/api/data?key=${apiKey}`);

// ✓ GOOD - Secret in .env.local (never committed)
// .env.local
SYNCFUSION_LICENSE_KEY=xxx...xxx
```

**Validation Rules:**
- [ ] No hardcoded API keys
- [ ] No hardcoded database URLs
- [ ] Environment variable names prefixed (e.g., NEXT_PUBLIC_)
- [ ] .env files in .gitignore
- [ ] Secrets documented as required env vars

---

### 2.3 Dependency Security

**Requirement:** Use trustworthy, well-maintained packages

**What to Check:**

```json
{
  "dependencies": {
    "@syncfusion/ej2-react-inputs": "^20.0.0",
    "@syncfusion/ej2-react-buttons": "^20.0.0"
  }
}
```

**Validation Rules:**
- [ ] All packages from official npm registry
- [ ] No typosquatted package names
- [ ] Syncfusion packages only from @syncfusion org
- [ ] Run `npm audit` regularly
- [ ] No deprecated packages

---

## Performance Standards

### 3.1 Rendering Optimization

**Requirement:** Prevent unnecessary re-renders

**What to Check:**

```tsx
// ✗ BAD - Re-renders on every parent update
export const SearchInput = ({ onSearch }) => {
  return (
    <TextBoxComponent onChange={(e) => onSearch(e.value)} />
  );
};

// ✓ GOOD - Memoized to prevent re-renders
export const SearchInput = React.memo(({ onSearch }) => {
  return (
    <TextBoxComponent onChange={(e) => onSearch(e.value)} />
  );
});

// ✓ GOOD - useCallback prevents handler recreation
const memoizedOnSearch = useCallback((value) => {
  onSearch(value);
}, []);
```

**Validation Rules:**
- [ ] Large components wrapped with React.memo
- [ ] Stable callbacks use useCallback
- [ ] useMemo used for expensive computations
- [ ] No infinite loops in useEffect
- [ ] Cleanup functions in useEffect (subscriptions, timers)

---

### 3.2 Bundle Size

**Requirement:** Keep component bundle size reasonable

**Validation Rules:**
- [ ] Component code < 50KB (uncompressed)
- [ ] No duplicate dependencies
- [ ] Tree-shakeable exports
- [ ] No large images embedded
- [ ] Lazy-loadable for components > 100KB

---

## Code Quality Standards

### 4.1 TypeScript & Type Safety

**Requirement:** Full type safety, no implicit any

**What to Check:**

```tsx
// ✗ BAD - Implicit any
const handleChange = (e) => {
  setValue(e.value);
};

// ✓ GOOD - Explicit types
interface ChangeEvent {
  value: string;
}

const handleChange = (e: ChangeEvent): void => {
  setValue(e.value);
};
```

**Validation Rules:**
- [ ] No `any` types (except explicit escape)
- [ ] Props have TypeScript interface
- [ ] Event handlers properly typed
- [ ] State types defined
- [ ] Return types on functions
- [ ] tsconfig strict mode enabled

---

### 4.2 Code Hygiene

**Requirement:** Clean, maintainable code

**What to Check:**

```tsx
// ✗ BAD - var, console.log in production
var name = "user";
console.log("Debug:", name);
export const Component = () => {
  return <div>{name}</div>;
};

// ✓ GOOD - const, no console, clean
const name = "user";
export const Component: React.FC = () => {
  return <div>{name}</div>;
};
```

**Validation Rules:**
- [ ] No `var` declarations (use `const`/`let`)
- [ ] No `console.log` in production code
- [ ] No unused variables or imports
- [ ] No commented-out code blocks
- [ ] Consistent indentation (2 spaces)
- [ ] Semicolons on all statements
- [ ] Single quotes or double (consistent)

---

## Validation Checklist

**Run this checklist for every generated component:**

```
ACCESSIBILITY
  ✓ All buttons are <button> elements
  ✓ All form fields have labels (or aria-label)
  ✓ Form errors have aria-describedby
  ✓ Icon buttons have aria-label
  ✓ Color contrast ≥ 4.5:1
  ✓ Focus indicators visible
  ✓ Keyboard navigation works
  ✓ No keyboard traps
  ✓ Heading hierarchy correct
  ✓ No color-only warnings

SECURITY
  ✓ No dangerouslySetInnerHTML with user input
  ✓ No eval() or Function()
  ✓ No inline event handlers
  ✓ No hardcoded secrets
  ✓ No suspicious npm packages

PERFORMANCE
  ✓ React.memo on large components
  ✓ useCallback on stable functions
  ✓ No unnecessary re-renders
  ✓ No infinite loops
  ✓ useEffect cleanup functions

CODE QUALITY
  ✓ Full TypeScript types
  ✓ No `any` types
  ✓ No `var` declarations
  ✓ No console.log
  ✓ No unused imports
  ✓ Consistent formatting
```

---

## Auto-Fix Rules

**Stage 7 automatically fixes these issues:**

| Issue | Auto-Fix |
|-------|----------|
| Missing aria-label on icon button | Add based on icon type |
| Missing aria-describedby on error field | Add id to error message |
| Missing htmlFor on label | Match with input id |
| Var declarations | Convert to const/let |
| Console.log statements | Remove completely |
| Unused imports | Remove from import list |
| Heading hierarchy gaps | Reorder to proper hierarchy |
| Missing focus outline | Add visible outline (not removed) |

---

**End of Web Standards Reference**  
For component details, see `SYNCFUSION-MAPPING.md`  
For workflow details, see `STAGES.md`  
For troubleshooting, see `TROUBLESHOOTING.md`
