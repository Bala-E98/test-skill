# Troubleshooting & FAQ

**Version:** 1.0.0  
**Last Updated:** April 15, 2026  
**Purpose:** Common errors, solutions, debugging tips, and frequently asked questions

---

## Table of Contents

1. [Installation & Setup Issues](#installation--setup-issues)
2. [Stage-Specific Errors](#stage-specific-errors)
3. [Build & Runtime Errors](#build--runtime-errors)
4. [Syncfusion Component Issues](#syncfusion-component-issues)
5. [Validation Warnings](#validation-warnings)
6. [Performance Issues](#performance-issues)
7. [FAQ](#faq)

---

## Installation & Setup Issues

### Error: "Cannot find module @syncfusion/..."

**Cause:** Syncfusion packages not installed

**Solution:**
```bash
npm install @syncfusion/ej2-react-inputs @syncfusion/ej2-react-buttons @syncfusion/ej2-react-dropdowns
```

Or run the UI Builder's Stage 8 dependency resolver.

---

### Error: "Package.json not found"

**Cause:** Not in a React project root, or no package.json

**Solution:**
1. Navigate to your React project root: `cd /path/to/project`
2. Verify package.json exists: `ls package.json`
3. If missing, initialize: `npm init` or create React app first

---

### Error: "React version not compatible"

**Cause:** React version < 18.0.0

**Solution:**
```bash
npm install react@^18.0.0 react-dom@^18.0.0
```

Check compatibility: `npm ls react`

---

### Warning: "TypeScript not detected"

**Cause:** No tsconfig.json found, but project uses .ts/.tsx files

**Solution:**
```bash
npx tsc --init
```

Or let UI Builder generate JavaScript (.jsx) instead.

---

## Stage-Specific Errors

### Stage 1: "Could not determine UI type"

**Cause:** Ambiguous or vague user request

**Symptoms:**
- User says "build me a UI" with no specifics
- Multiple high-scoring candidates

**Solution:**
1. Clarify: "What kind of UI? (login form, data table, navigation, etc.)"
2. Show supported types (Section 3.1 of main spec)
3. Ask follow-up: "What fields/data will it have?"

**Prevention:** Be specific in your request:
- ✓ GOOD: "Create a login form with email and password"
- ✗ BAD: "Make me something"

---

### Stage 2: "Cannot write to app/components/"

**Cause:** Directory doesn't exist or no write permission

**Solution:**
```bash
# Create directory manually
mkdir -p app/components

# Check permissions
ls -la app/
```

Or let UI Builder create the directory (it will ask for confirmation).

---

### Stage 3: "No matching layout variant found"

**Cause:** Unusual field combination or custom requirement

**Solution:**
1. Choose the closest variant
2. Request modification after generation
3. Or specify "custom layout" in your request

**Example:**
```
User: "Login form with biometric authentication"
Agent: "No exact match. Closest: Login Variant B. Proceed and customize?"
```

---

### Stage 4: "Component mapping failed for field X"

**Cause:** Unsupported field type or typo

**Solution:**
1. Check field name spelling
2. Use standard field types (text, email, select, date, etc.)
3. Fallback: Agent will use TextBoxComponent and warn

**Supported field types:** See SYNCFUSION-MAPPING.md Section 11.1

---

### Stage 7: "Validation failed: accessibility issues"

**Cause:** Generated code doesn't pass WCAG 2.1 AA

**Common Issues:**
- Missing aria-label on icon button
- Color contrast < 4.5:1
- Missing htmlFor on label

**Solution:**
1. UI Builder auto-fixes common issues
2. Review validation report
3. Manually fix remaining issues (or override with warning)

---

### Stage 8: "npm install failed"

**Cause:** Network issue, version conflict, or permission error

**Symptoms:**
```
npm ERR! code ERESOLVE
npm ERR! ERESOLVE unable to resolve dependency tree
```

**Solution:**
```bash
# Clear cache
npm cache clean --force

# Try with legacy peer deps
npm install --legacy-peer-deps

# Or force install
npm install --force
```

**Prevention:** Keep dependencies updated, avoid incompatible versions.

---

### Stage 9: "Build errors after file insertion"

**Cause:** TypeScript errors, import issues, or syntax errors

**Symptoms:**
```
error TS2304: Cannot find name 'TextBoxComponent'
```

**Solution:**
1. Check imports at top of file
2. Verify packages installed: `npm ls @syncfusion/ej2-react-inputs`
3. Run type check: `npx tsc --noEmit`
4. Restart dev server: `npm run dev`

**Rollback:** UI Builder offers to undo file changes if build fails.

---

## Build & Runtime Errors

### Error: "Module not found: Can't resolve './LoginForm.module.css'"

**Cause:** CSS file not generated or wrong path

**Solution:**
1. Verify CSS file exists: `ls LoginForm.module.css`
2. Check import path matches filename
3. Restart dev server (sometimes cache issue)

---

### Error: "registerLicense is not a function"

**Cause:** @syncfusion/ej2-base not installed

**Solution:**
```bash
npm install @syncfusion/ej2-base
```

Verify license registration in app entry point (app/layout.tsx or src/main.tsx).

---

### Warning: "Syncfusion license banner showing"

**Cause:** License key not registered

**Solution:**
1. Get free license: https://www.syncfusion.com/account/manage-trials
2. Add to .env.local:
   ```
   NEXT_PUBLIC_SYNCFUSION_LICENSE_KEY=your-key-here
   ```
3. Register in app entry:
   ```tsx
   import { registerLicense } from '@syncfusion/ej2-base';
   registerLicense(process.env.NEXT_PUBLIC_SYNCFUSION_LICENSE_KEY || '');
   ```

---

### Error: "Cannot read property 'value' of undefined"

**Cause:** Syncfusion component event handler expecting different structure

**Solution:**
Check event structure in Syncfusion docs:
```tsx
// Correct:
onChange={(args) => setValue(args.value)}

// Wrong:
onChange={(e) => setValue(e.target.value)}  // This is native input
```

---

## Syncfusion Component Issues

### TextBox not showing value

**Cause:** Controlled component without value prop

**Solution:**
```tsx
// Must provide value prop
<TextBoxComponent
  value={email}              // Required for controlled
  onChange={(args) => setEmail(args.value)}
/>
```

---

### DropDownList not filtering

**Cause:** allowFiltering not enabled

**Solution:**
```tsx
<DropDownListComponent
  allowFiltering={true}      // Enable search
  filterType="Contains"
/>
```

---

### GridComponent pagination not working

**Cause:** Missing Page service injection

**Solution:**
```tsx
import { Page } from '@syncfusion/ej2-react-grids';

<GridComponent allowPaging={true}>
  {/* columns */}
  <Inject services={[Page]} />  {/* Required! */}
</GridComponent>
```

---

### DatePicker showing wrong format

**Cause:** Format string not specified

**Solution:**
```tsx
<DatePickerComponent
  format="yyyy-MM-dd"    // ISO format
  // or "MM/dd/yyyy"     // US format
  // or "dd/MM/yyyy"     // EU format
/>
```

---

## Validation Warnings

### Warning: "Missing aria-label on icon button"

**Auto-fix:** Yes (Stage 7 adds aria-label based on icon type)

**Manual fix:**
```tsx
<ButtonComponent
  iconCss="e-icons e-close"
  aria-label="Close dialog"  // Add this
/>
```

---

### Warning: "Color contrast ratio 3.2:1 (fails AA)"

**Auto-fix:** No (requires design decision)

**Manual fix:**
Use darker text or lighter background:
```css
/* Before (fails) */
.text {
  color: #999999;        /* Contrast: 3.2:1 */
  background: #ffffff;
}

/* After (passes) */
.text {
  color: #666666;        /* Contrast: 5.7:1 ✓ */
  background: #ffffff;
}
```

Tool: https://webaim.org/resources/contrastchecker/

---

### Warning: "Heading hierarchy gap (h1 → h3)"

**Auto-fix:** Yes (Stage 7 reorders to h1 → h2)

**Manual fix:**
```tsx
// Before (wrong)
<h1>Title</h1>
<h3>Subtitle</h3>  {/* Skipped h2! */}

// After (correct)
<h1>Title</h1>
<h2>Subtitle</h2>
```

---

## Performance Issues

### Component re-renders too often

**Cause:** Missing React.memo or useCallback

**Solution:**
```tsx
// Wrap with React.memo
export const MyForm = React.memo(({ onSubmit }) => {
  // Use useCallback for stable functions
  const handleSubmit = useCallback((data) => {
    onSubmit(data);
  }, [onSubmit]);

  return <form onSubmit={handleSubmit}>...</form>;
});
```

---

### Large bundle size (> 500KB)

**Cause:** Importing all Syncfusion components

**Solution:**
Only import what you need:
```tsx
// Wrong (imports everything)
import * as Syncfusion from '@syncfusion/ej2-react-inputs';

// Right (tree-shakeable)
import { TextBoxComponent } from '@syncfusion/ej2-react-inputs';
```

---

### Slow initial page load

**Cause:** No code splitting

**Solution:**
```tsx
// Lazy load heavy components
const CustomerTable = React.lazy(() => import('./CustomerTable'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <CustomerTable />
    </Suspense>
  );
}
```

---

## FAQ

### Q: Can I modify generated components?

**A:** Yes! Generated components are fully editable. Best practice:
1. Generate component with UI Builder
2. Review and test
3. Customize as needed
4. Use UI Builder for new components (don't manually duplicate)

---

### Q: Does UI Builder support Vue/Angular/Svelte?

**A:** Phase 1 supports React only. Vue/Angular planned for Phase 2.

---

### Q: Can I use custom Syncfusion themes?

**A:** Yes! Apply custom themes via CSS:
```tsx
import '@syncfusion/ej2-base/styles/material.css';
// Or create custom theme with Syncfusion Theme Studio
```

---

### Q: How do I add backend API integration?

**A:** UI Builder generates frontend-only code. Connect to your API:
```tsx
const handleSubmit = async (formData) => {
  const response = await fetch('/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(formData)
  });
  // Handle response
};

<LoginForm onSubmit={handleSubmit} />
```

---

### Q: Can I generate tests for components?

**A:** Not in Phase 1. Planned for Phase 3. For now, write tests manually:
```tsx
import { render, screen } from '@testing-library/react';
import { LoginForm } from './LoginForm';

test('renders login form', () => {
  render(<LoginForm />);
  expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
});
```

---

### Q: What if I need a component not in Syncfusion?

**A:** UI Builder generates Syncfusion components only. For custom components:
1. Build manually with React
2. Or request addition to Syncfusion library
3. Or use a hybrid approach (some Syncfusion, some custom)

---

### Q: How do I update an existing component?

**A:** Two options:
1. **Regenerate:** Delete old file, re-run UI Builder (recommended if heavily modified)
2. **Modify:** UI Builder can read existing component and apply changes (if JSDoc intact)

---

### Q: Can I deploy generated components to production?

**A:** Yes! Components are production-ready:
- ✅ WCAG 2.1 AA compliant
- ✅ TypeScript typed
- ✅ Security scanned
- ✅ Performance optimized
- ⚠️ Remember to add backend integration
- ⚠️ Test thoroughly in your environment

---

### Q: How do I report bugs or request features?

**A:** Contact your organization's UI Builder support team or file an issue in your internal repository.

---

### Q: Can I use UI Builder with existing codebases?

**A:** Yes! UI Builder detects your project structure and generates compatible code. It won't modify existing files unless you explicitly overwrite.

---

### Q: What happens if Stage 7 validation fails?

**A:** Three options:
1. **Auto-fix:** UI Builder fixes common issues automatically
2. **Review:** Review issues and fix manually
3. **Override:** Accept code with warnings (not recommended for production)

---

### Q: How do I customize generated CSS?

**A:** Edit the .module.css file. Changes persist. Best practice:
1. Use CSS variables for theme customization
2. Add custom classes for brand styling
3. Keep responsive media queries intact

Example:
```css
/* Customize colors */
.light {
  --primary-color: #ff6600;  /* Your brand color */
  --primary-color-dark: #cc5200;
}
```

---

### Q: Can I use UI Builder in CI/CD pipelines?

**A:** Phase 1 is interactive (requires user confirmation). For CI/CD:
- Generate components locally
- Commit to repository
- CI/CD builds/tests as usual

Headless mode planned for Phase 2.

---

**End of Troubleshooting Guide**  
For technical details, see `REFERENCE.md`  
For component mapping, see `SYNCFUSION-MAPPING.md`  
For workflow details, see `STAGES.md`
