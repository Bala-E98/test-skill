# Stage 4: Component Picking

**Purpose:** Map confirmed layout elements to Syncfusion components. **FULLY AUTOMATED — NO user interaction.**

**AI Should:**

1. **Read confirmed layout** from Stage 3 (e.g., Login Form with email, password, checkbox, button)
2. **Analyze each layout element**:
   - "Text input field" → TextBox, MaskedTextBox, or AutoComplete?
   - "Checkbox" → CheckBox
   - "Button" → Button or ButtonGroup?
   - "Link" → Native `<a>` tag
3. **Check component capabilities** from SYNCFUSION-MAPPING.md:
   - Does component support required props?
   - Accessibility compatible (WCAG 2.1 AA)?
   - Theme support (light/dark)?
4. **Pick best fit** for each element
5. **List required packages** (@syncfusion/ej2-react-inputs, etc.)

**Component Selection Example:**

```
Layout: Login Form - Variant B (email, password, remember-me, submit)

Component Mapping:

Field: Email Address
  → TextBox (@syncfusion/ej2-react-inputs)
  → Reason: Standard text input, built-in email validation

Field: Password
  → TextBox (@syncfusion/ej2-react-inputs) 
  → Reason: Text input with type="password", supports masking

Field: Remember Me
  → CheckBox (@syncfusion/ej2-react-buttons)
  → Reason: Boolean toggle, full accessibility support

Button: Submit
  → Button (@syncfusion/ej2-react-buttons)
  → Reason: Action button, theme-compatible

Link: Forgot Password
  → Native <a> tag (React component)
  → Reason: Navigation link, not Syncfusion component

Required Packages:
  - @syncfusion/ej2-react-inputs
  - @syncfusion/ej2-react-buttons
```

**NO User Interaction:**
AI automatically selects components. No confirmation needed.

**Output:**
Component mapping locked. Ready for code generation.

**Status:** ✅ **FULLY AUTOMATED** - No user decision required.

**Reference:** See SYNCFUSION-MAPPING.md for component options and capabilities.
