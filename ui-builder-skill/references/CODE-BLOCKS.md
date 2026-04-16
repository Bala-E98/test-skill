# Code Blocks Reference

**Purpose:** Prebuilt code patterns and standards for reference during code generation.

## React Component Structure

```typescript
/**
 * LoginForm Component
 * 
 * Renders a login form with email, password, and remember-me toggle.
 * Supports client-side validation and theme switching.
 * 
 * @component
 * @example
 * <LoginForm 
 *   onSubmit={(email, password) => handleLogin(email, password)}
 *   onForgotPassword={() => navigate('/forgot-password')}
 * />
 */

import React, { useState } from 'react';
import { TextBoxComponent } from '@syncfusion/ej2-react-inputs';
import { ButtonComponent } from '@syncfusion/ej2-react-buttons';
import { CheckBoxComponent } from '@syncfusion/ej2-react-buttons';
import styles from './LoginForm.module.css';

interface LoginFormProps {
  onSubmit?: (email: string, password: string, rememberMe: boolean) => void;
  onForgotPassword?: () => void;
}

interface ValidationErrors {
  email?: string;
  password?: string;
}

export const LoginForm: React.FC<LoginFormProps> = ({
  onSubmit,
  onForgotPassword
}) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);
  const [errors, setErrors] = useState<ValidationErrors>({});
  const [isLoading, setIsLoading] = useState(false);

  const validateForm = (): boolean => {
    const newErrors: ValidationErrors = {};
    
    if (!email) {
      newErrors.email = 'Email is required';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      newErrors.email = 'Please enter a valid email';
    }
    
    if (!password) {
      newErrors.password = 'Password is required';
    } else if (password.length < 6) {
      newErrors.password = 'Password must be at least 6 characters';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }
    
    setIsLoading(true);
    try {
      onSubmit?.(email, password, rememberMe);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <h1 className={styles.title}>Sign In</h1>
      
      {/* Email Field */}
      <div className={styles.fieldGroup}>
        <label htmlFor="email" className={styles.label}>
          Email Address <span className={styles.required}>*</span>
        </label>
        <TextBoxComponent
          id="email"
          type="email"
          placeholder="you@example.com"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          aria-label="Email address"
          aria-describedby={errors.email ? 'email-error' : undefined}
          aria-invalid={!!errors.email}
          className={errors.email ? styles.inputError : ''}
        />
        {errors.email && (
          <span id="email-error" className={styles.errorMessage} role="alert">
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
          placeholder="••••••••"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          aria-label="Password"
          aria-describedby={errors.password ? 'password-error' : undefined}
          aria-invalid={!!errors.password}
          className={errors.password ? styles.inputError : ''}
        />
        {errors.password && (
          <span id="password-error" className={styles.errorMessage} role="alert">
            {errors.password}
          </span>
        )}
      </div>

      {/* Remember Me Checkbox */}
      <div className={styles.rememberGroup}>
        <CheckBoxComponent
          id="rememberMe"
          label="Remember me"
          checked={rememberMe}
          onChange={(e) => setRememberMe(e.checked ?? false)}
          aria-label="Remember me on this device"
        />
      </div>

      {/* Submit Button */}
      <ButtonComponent
        isPrimary={true}
        className={styles.submitButton}
        disabled={isLoading}
      >
        {isLoading ? 'Signing In...' : 'Sign In'}
      </ButtonComponent>

      {/* Forgot Password Link */}
      <div className={styles.footer}>
        <button
          type="button"
          className={styles.forgotLink}
          onClick={onForgotPassword}
          aria-label="Go to forgot password page"
        >
          Forgot password?
        </button>
      </div>
    </form>
  );
};

export default LoginForm;
```

## CSS Modules Pattern

```css
/* LoginForm.module.css */

.form {
  max-width: 400px;
  margin: 0 auto;
  padding: 32px 20px;
  background: var(--bg-primary);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.title {
  font-size: 24px;
  font-weight: 600;
  color: var(--text-primary);
  text-align: center;
  margin-bottom: 24px;
}

.fieldGroup {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 16px;
}

.label {
  font-size: 14px;
  font-weight: 500;
  color: var(--text-secondary);
}

.required {
  color: var(--error-color);
  margin-left: 4px;
}

.inputError {
  border-color: var(--error-color) !important;
}

.errorMessage {
  font-size: 12px;
  color: var(--error-color);
  margin-top: 4px;
}

.rememberGroup {
  margin-bottom: 16px;
}

.submitButton {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  font-weight: 600;
  border-radius: 4px;
}

.footer {
  text-align: center;
  margin-top: 16px;
}

.forgotLink {
  background: none;
  border: none;
  color: var(--primary-color);
  cursor: pointer;
  font-size: 14px;
  text-decoration: none;
  padding: 0;
}

.forgotLink:hover {
  text-decoration: underline;
}

/* Responsive Design */
@media (max-width: 768px) {
  .form {
    padding: 20px 16px;
  }

  .title {
    font-size: 20px;
    margin-bottom: 20px;
  }
}

@media (max-width: 320px) {
  .form {
    padding: 16px 12px;
  }

  .title {
    font-size: 18px;
  }
}
```

## TypeScript Interface Pattern

```typescript
// types.ts

/**
 * Props for LoginForm component
 */
export interface LoginFormProps {
  /** Callback when form is submitted with valid data */
  onSubmit?: (email: string, password: string, rememberMe: boolean) => void;
  
  /** Callback when forgot password link is clicked */
  onForgotPassword?: () => void;
}

/**
 * Validation error state for form fields
 */
export interface ValidationErrors {
  email?: string;
  password?: string;
}

/**
 * Internal form state
 */
export interface FormState {
  email: string;
  password: string;
  rememberMe: boolean;
  isLoading: boolean;
  errors: ValidationErrors;
}
```

---

All code must follow: ES6+, TypeScript, semantic HTML, WCAG 2.1 AA, responsive design, security best practices.

For real code samples, see EXAMPLES.md.
