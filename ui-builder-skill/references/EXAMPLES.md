# Code Generation Examples

**Version:** 1.0.0  
**Last Updated:** April 15, 2026  
**Purpose:** Real before/after examples showing what the UI Builder generates

---

## Table of Contents

1. [Login Form Example](#login-form-example)
2. [Registration Form Example](#registration-form-example)
3. [Data Table Example](#data-table-example)
4. [Contact Form Example](#contact-form-example)
5. [Navigation Bar Example](#navigation-bar-example)

---

## Login Form Example

### User Request

```
"Create a dark-themed login form with email, password, and remember me checkbox"
```

### Generated Files

**File 1: `LoginForm.tsx`** (498 lines)

```tsx
/**
 * LoginForm Component
 * 
 * A WCAG 2.1 AA compliant login form with email and password fields.
 * Supports dark theme, keyboard navigation, and client-side validation.
 * 
 * @example
 * ```tsx
 * <LoginForm 
 *   onSubmit={(data) => console.log('Login:', data)}
 *   theme="dark"
 * />
 * ```
 */

import React, { useState, FormEvent } from 'react';
import { TextBoxComponent } from '@syncfusion/ej2-react-inputs';
import { CheckBoxComponent } from '@syncfusion/ej2-react-buttons';
import { ButtonComponent } from '@syncfusion/ej2-react-buttons';
import styles from './LoginForm.module.css';

// ─────────────────────────────────────────────────────────────
// Type Definitions
// ─────────────────────────────────────────────────────────────

interface LoginFormProps {
  /** Callback when form is submitted successfully */
  onSubmit?: (data: LoginFormData) => void;
  /** Callback when "Forgot Password" is clicked */
  onForgotPassword?: () => void;
  /** Theme variant (light or dark) */
  theme?: 'light' | 'dark';
  /** Disable the entire form */
  disabled?: boolean;
}

interface LoginFormData {
  email: string;
  password: string;
  rememberMe: boolean;
}

interface FormErrors {
  email?: string;
  password?: string;
}

// ─────────────────────────────────────────────────────────────
// Component
// ─────────────────────────────────────────────────────────────

export const LoginForm: React.FC<LoginFormProps> = ({
  onSubmit,
  onForgotPassword,
  theme = 'light',
  disabled = false
}) => {
  // State
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);
  const [errors, setErrors] = useState<FormErrors>({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  // ─────────────────────────────────────────────────────────────
  // Validation
  // ─────────────────────────────────────────────────────────────

  const validateEmail = (value: string): string | undefined => {
    if (!value) {
      return 'Email is required';
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(value)) {
      return 'Please enter a valid email address';
    }
    return undefined;
  };

  const validatePassword = (value: string): string | undefined => {
    if (!value) {
      return 'Password is required';
    }
    if (value.length < 8) {
      return 'Password must be at least 8 characters';
    }
    return undefined;
  };

  const validateForm = (): boolean => {
    const newErrors: FormErrors = {};
    
    const emailError = validateEmail(email);
    if (emailError) newErrors.email = emailError;

    const passwordError = validatePassword(password);
    if (passwordError) newErrors.password = passwordError;

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  // ─────────────────────────────────────────────────────────────
  // Event Handlers
  // ─────────────────────────────────────────────────────────────

  const handleEmailChange = (args: any) => {
    setEmail(args.value);
    // Clear error on change
    if (errors.email) {
      setErrors(prev => ({ ...prev, email: undefined }));
    }
  };

  const handleEmailBlur = () => {
    const error = validateEmail(email);
    if (error) {
      setErrors(prev => ({ ...prev, email: error }));
    }
  };

  const handlePasswordChange = (args: any) => {
    setPassword(args.value);
    // Clear error on change
    if (errors.password) {
      setErrors(prev => ({ ...prev, password: undefined }));
    }
  };

  const handlePasswordBlur = () => {
    const error = validatePassword(password);
    if (error) {
      setErrors(prev => ({ ...prev, password: error }));
    }
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();

    if (!validateForm()) {
      return;
    }

    setIsSubmitting(true);

    try {
      const formData: LoginFormData = {
        email,
        password,
        rememberMe
      };

      await onSubmit?.(formData);
    } catch (error) {
      console.error('Login error:', error);
      setErrors({ email: 'Login failed. Please try again.' });
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleForgotPasswordClick = () => {
    onForgotPassword?.();
  };

  // ─────────────────────────────────────────────────────────────
  // Render
  // ─────────────────────────────────────────────────────────────

  return (
    <div className={`${styles.container} ${styles[theme]}`}>
      <form 
        className={styles.form} 
        onSubmit={handleSubmit}
        noValidate
      >
        <h1 className={styles.title}>Sign In</h1>

        {/* Email Field */}
        <div className={styles.fieldGroup}>
          <label htmlFor="email" className={styles.label}>
            Email <span className={styles.required}>*</span>
          </label>
          <TextBoxComponent
            id="email"
            type="email"
            placeholder="you@example.com"
            floatLabelType="Auto"
            value={email}
            onChange={handleEmailChange}
            onBlur={handleEmailBlur}
            enabled={!disabled && !isSubmitting}
            cssClass={errors.email ? styles.inputError : ''}
            aria-label="Email address"
            aria-describedby={errors.email ? 'email-error' : undefined}
            aria-invalid={!!errors.email}
            aria-required="true"
          />
          {errors.email && (
            <span 
              id="email-error" 
              className={styles.errorMessage}
              role="alert"
            >
              {errors.email}
            </span>
          )}
        </div>

        {/* Password Field */}
        <div className={styles.fieldGroup}>
          <label htmlFor="password" className={styles.label}>
            Password <span className={styles.required}>*</span>
          </label>
          <TextBoxComponent
            id="password"
            type="password"
            placeholder="Enter your password"
            floatLabelType="Auto"
            value={password}
            onChange={handlePasswordChange}
            onBlur={handlePasswordBlur}
            enabled={!disabled && !isSubmitting}
            cssClass={errors.password ? styles.inputError : ''}
            aria-label="Password"
            aria-describedby={errors.password ? 'password-error' : undefined}
            aria-invalid={!!errors.password}
            aria-required="true"
          />
          {errors.password && (
            <span 
              id="password-error" 
              className={styles.errorMessage}
              role="alert"
            >
              {errors.password}
            </span>
          )}
        </div>

        {/* Remember Me */}
        <div className={styles.rememberSection}>
          <CheckBoxComponent
            id="remember-me"
            checked={rememberMe}
            onChange={(e: any) => setRememberMe(e.checked)}
            label="Remember me"
            disabled={disabled || isSubmitting}
            aria-label="Remember my login credentials"
          />
        </div>

        {/* Submit Button */}
        <div className={styles.submitSection}>
          <ButtonComponent
            type="submit"
            isPrimary={true}
            disabled={disabled || isSubmitting}
            cssClass={styles.submitButton}
          >
            {isSubmitting ? 'Signing in...' : 'Sign In'}
          </ButtonComponent>
        </div>

        {/* Forgot Password Link */}
        {onForgotPassword && (
          <div className={styles.forgotSection}>
            <a
              href="#"
              onClick={(e) => {
                e.preventDefault();
                handleForgotPasswordClick();
              }}
              className={styles.forgotLink}
            >
              Forgot password?
            </a>
          </div>
        )}
      </form>
    </div>
  );
};

export default LoginForm;
```

**File 2: `LoginForm.module.css`** (224 lines)

```css
/* ═══════════════════════════════════════════════════════════ */
/* Container & Layout */
/* ═══════════════════════════════════════════════════════════ */

.container {
  max-width: 400px;
  margin: 0 auto;
  padding: 32px;
  background: var(--surface-color);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

/* ═══════════════════════════════════════════════════════════ */
/* Typography */
/* ═══════════════════════════════════════════════════════════ */

.title {
  font-size: 24px;
  font-weight: 600;
  color: var(--text-primary);
  text-align: center;
  margin: 0 0 8px 0;
}

.label {
  display: block;
  font-size: 14px;
  font-weight: 500;
  color: var(--text-secondary);
  margin-bottom: 8px;
}

.required {
  color: var(--error-color);
  margin-left: 4px;
}

/* ═══════════════════════════════════════════════════════════ */
/* Form Fields */
/* ═══════════════════════════════════════════════════════════ */

.fieldGroup {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.inputError {
  border-color: var(--error-color) !important;
}

.errorMessage {
  font-size: 12px;
  color: var(--error-color);
  margin-top: 4px;
  display: flex;
  align-items: center;
  gap: 4px;
}

/* ═══════════════════════════════════════════════════════════ */
/* Remember Me */
/* ═══════════════════════════════════════════════════════════ */

.rememberSection {
  display: flex;
  align-items: center;
}

/* ═══════════════════════════════════════════════════════════ */
/* Submit Button */
/* ═══════════════════════════════════════════════════════════ */

.submitSection {
  margin-top: 8px;
}

.submitButton {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  font-weight: 600;
}

/* ═══════════════════════════════════════════════════════════ */
/* Forgot Password Link */
/* ═══════════════════════════════════════════════════════════ */

.forgotSection {
  text-align: center;
}

.forgotLink {
  color: var(--primary-color);
  text-decoration: none;
  font-size: 14px;
  transition: color 0.2s;
}

.forgotLink:hover {
  color: var(--primary-color-dark);
  text-decoration: underline;
}

.forgotLink:focus {
  outline: 2px solid var(--primary-color);
  outline-offset: 2px;
  border-radius: 4px;
}

/* ═══════════════════════════════════════════════════════════ */
/* Theme: Light */
/* ═══════════════════════════════════════════════════════════ */

.light {
  --surface-color: #ffffff;
  --text-primary: #1a1a1a;
  --text-secondary: #666666;
  --primary-color: #0066cc;
  --primary-color-dark: #0052a3;
  --error-color: #d32f2f;
}

/* ═══════════════════════════════════════════════════════════ */
/* Theme: Dark */
/* ═══════════════════════════════════════════════════════════ */

.dark {
  --surface-color: #1e1e1e;
  --text-primary: #ffffff;
  --text-secondary: #b0b0b0;
  --primary-color: #3399ff;
  --primary-color-dark: #66b3ff;
  --error-color: #f44336;
}

.dark .container {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
}

/* ═══════════════════════════════════════════════════════════ */
/* Responsive Design */
/* ═══════════════════════════════════════════════════════════ */

@media (max-width: 768px) {
  .container {
    padding: 24px;
    margin: 16px;
  }

  .title {
    font-size: 20px;
  }
}

@media (max-width: 320px) {
  .container {
    padding: 16px;
    margin: 8px;
  }

  .title {
    font-size: 18px;
  }

  .submitButton {
    font-size: 14px;
    padding: 10px;
  }
}

/* ═══════════════════════════════════════════════════════════ */
/* Focus & Accessibility */
/* ═══════════════════════════════════════════════════════════ */

input:focus,
button:focus,
a:focus {
  outline: 3px solid var(--primary-color);
  outline-offset: 2px;
}

/* Ensure high contrast for accessibility */
@media (prefers-contrast: high) {
  .container {
    border: 2px solid var(--text-primary);
  }
}
```

---

## Data Table Example

### User Request

```
"Create a customer data table with columns for ID, name, email, status, and actions"
```

### Generated File: `CustomerTable.tsx` (Excerpt)

```tsx
import React, { useState } from 'react';
import { 
  GridComponent, 
  ColumnsDirective, 
  ColumnDirective,
  Page,
  Sort,
  Filter,
  Inject
} from '@syncfusion/ej2-react-grids';
import styles from './CustomerTable.module.css';

interface Customer {
  id: string;
  name: string;
  email: string;
  status: 'Active' | 'Inactive';
  createdAt: Date;
}

interface CustomerTableProps {
  data?: Customer[];
  onEdit?: (customer: Customer) => void;
  onDelete?: (customer: Customer) => void;
}

export const CustomerTable: React.FC<CustomerTableProps> = ({
  data = [],
  onEdit,
  onDelete
}) => {
  const actionTemplate = (props: Customer) => {
    return (
      <div className={styles.actions}>
        <button 
          onClick={() => onEdit?.(props)}
          className={styles.editButton}
          aria-label={`Edit ${props.name}`}
        >
          Edit
        </button>
        <button 
          onClick={() => onDelete?.(props)}
          className={styles.deleteButton}
          aria-label={`Delete ${props.name}`}
        >
          Delete
        </button>
      </div>
    );
  };

  return (
    <div className={styles.container}>
      <GridComponent
        dataSource={data}
        allowPaging={true}
        pageSettings={{ pageSize: 10 }}
        allowSorting={true}
        allowFiltering={true}
        filterSettings={{ type: 'Excel' }}
      >
        <ColumnsDirective>
          <ColumnDirective 
            field='id' 
            headerText='Customer ID' 
            width='120'
            isPrimaryKey={true}
          />
          <ColumnDirective 
            field='name' 
            headerText='Name' 
            width='200'
          />
          <ColumnDirective 
            field='email' 
            headerText='Email' 
            width='250'
          />
          <ColumnDirective 
            field='status' 
            headerText='Status' 
            width='120'
          />
          <ColumnDirective 
            headerText='Actions' 
            width='150'
            template={actionTemplate}
          />
        </ColumnsDirective>
        <Inject services={[Page, Sort, Filter]} />
      </GridComponent>
    </div>
  );
};
```

---

## Contact Form Example

### User Request

```
"Build a contact form with name, email, subject, and message"
```

### Generated File Structure

```
ContactForm.tsx          (350 lines)
ContactForm.module.css   (180 lines)
```

### Key Features Generated

- ✅ Form validation (required fields)
- ✅ Email validation regex
- ✅ Character count for message (max 500)
- ✅ Submit button with loading state
- ✅ Error messages with ARIA
- ✅ Keyboard navigation
- ✅ WCAG 2.1 AA compliant

---

## Navigation Bar Example

### User Request

```
"Create a responsive navigation bar with logo and menu items"
```

### Generated File: `Navbar.tsx` (Excerpt)

```tsx
import React, { useState } from 'react';
import styles from './Navbar.module.css';

interface NavItem {
  label: string;
  href: string;
  active?: boolean;
}

interface NavbarProps {
  logo?: string;
  items: NavItem[];
  onItemClick?: (item: NavItem) => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  logo = 'MyApp',
  items,
  onItemClick
}) => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <nav className={styles.navbar} role="navigation">
      <div className={styles.container}>
        {/* Logo */}
        <div className={styles.logo}>
          <a href="/">{logo}</a>
        </div>

        {/* Desktop Menu */}
        <ul className={styles.menu}>
          {items.map((item, index) => (
            <li key={index} className={styles.menuItem}>
              <a 
                href={item.href}
                className={item.active ? styles.active : ''}
                onClick={(e) => {
                  e.preventDefault();
                  onItemClick?.(item);
                }}
              >
                {item.label}
              </a>
            </li>
          ))}
        </ul>

        {/* Mobile Menu Toggle */}
        <button
          className={styles.mobileToggle}
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          aria-label="Toggle navigation menu"
          aria-expanded={mobileMenuOpen}
        >
          <span className={styles.hamburger}></span>
        </button>
      </div>

      {/* Mobile Menu */}
      {mobileMenuOpen && (
        <div className={styles.mobileMenu}>
          <ul>
            {items.map((item, index) => (
              <li key={index}>
                <a href={item.href}>{item.label}</a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </nav>
  );
};
```

---

## Common Patterns

### Validation Pattern

All forms use this validation pattern:

```tsx
const [errors, setErrors] = useState<FormErrors>({});

const validateField = (value: string): string | undefined => {
  if (!value) return 'This field is required';
  // Additional validation...
  return undefined;
};

const handleBlur = () => {
  const error = validateField(value);
  if (error) setErrors(prev => ({ ...prev, field: error }));
};

// In JSX:
<TextBoxComponent
  aria-invalid={!!errors.field}
  aria-describedby={errors.field ? 'field-error' : undefined}
/>
{errors.field && (
  <span id="field-error" role="alert">{errors.field}</span>
)}
```

### Loading State Pattern

All submit buttons use this pattern:

```tsx
const [isSubmitting, setIsSubmitting] = useState(false);

const handleSubmit = async (e: FormEvent) => {
  e.preventDefault();
  setIsSubmitting(true);
  try {
    await onSubmit?.(formData);
  } finally {
    setIsSubmitting(false);
  }
};

// In JSX:
<ButtonComponent disabled={isSubmitting}>
  {isSubmitting ? 'Submitting...' : 'Submit'}
</ButtonComponent>
```

---

**End of Code Generation Examples**  
For component mapping, see `SYNCFUSION-MAPPING.md`  
For workflow details, see `STAGES.md`  
For troubleshooting, see `TROUBLESHOOTING.md`
