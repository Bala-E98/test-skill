# Stage 7: Validation

**Purpose:** Validate generated code against web standards. Binary pass/fail result.

**AI Should:**

1. **Validate WCAG 2.1 AA Compliance:**
   - Semantic HTML structure used? (form, label, input, button tags)
   - ARIA labels on form fields?
   - Keyboard navigation supported? (tab order, focus management)
   - Color contrast ≥ 4.5:1 for text?
   - Focus indicator visible on interactive elements?

2. **Check Security:**
   - No XSS vulnerabilities (no dangerouslySetInnerHTML)
   - No hardcoded secrets/API keys
   - Input sanitized if needed
   - No inline event handlers

3. **Verify Performance:**
   - React.memo used for stable components?
   - No unnecessary re-renders?
   - Lazy loading where applicable?
   - Code is optimized?

4. **Check Responsive Design:**
   - Mobile-first approach (320px+)
   - Flexbox/Grid used for layouts?
   - Media queries for breakpoints?
   - Touch targets ≥ 44x44px?

**Validation Result:**

Binary: **PASS ✓** or **FAIL ✗**

**If PASS:**
```
✓ Validation Result: PASS

All standards met:
  ✓ WCAG 2.1 AA accessibility
  ✓ Security checks
  ✓ Performance standards
  ✓ Responsive design
  ✓ Code quality

Ready to proceed to dependencies...
```

**If FAIL:**
```
✗ Validation Result: FAIL

Issues found:
  ✗ Color contrast on label text (3.2:1, need 4.5:1)
  ✗ Form inputs missing aria-describedby attributes

Auto-fixes applied:
  ✓ Increased font size for contrast
  ✓ Added aria-describedby to inputs

Remaining issues: 0
Result: PASS (after fixes)
```

**User Interaction:** ⭐ **USER DECISION #2**

If result is PASS:
```
Ready to generate dependencies?
[Proceed] [Review] [Stop]
```

If result is FAIL (after fixing):
```
Validation failed with 2 issues (not auto-fixable):
  - Form requires aria-live region for errors
  - Need custom input styling

Override and proceed anyway?
[Override & Proceed] [Request Manual Fixes] [Stop]
```

**Status:** ⭐ **USER DECISION #2** - User confirms validation result or overrides.

**Reference:** See WEB-STANDARDS.md for complete validation rules and correction methods.
