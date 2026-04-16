# Layout Variants Catalog

**Version:** 1.0.0  
**Last Updated:** April 15, 2026  
**Purpose:** Complete catalog of pre-designed layout variants for forms, tables, navigation, and common UI patterns

---

## Table of Contents

1. [Login Forms](#login-forms)
2. [Registration Forms](#registration-forms)
3. [Password Reset Forms](#password-reset-forms)
4. [Contact Forms](#contact-forms)
5. [Data Tables](#data-tables)
6. [Navigation Patterns](#navigation-patterns)
7. [Dashboard Layouts](#dashboard-layouts)
8. [Multi-Step Forms](#multi-step-forms)

---

## Login Forms

### Variant A: Minimal Login

**Description:** Simplest login form with just email and password  
**Use Case:** Internal apps, quick prototypes  
**Complexity:** 1/5

**Fields:**
- Email (required)
- Password (required)
- Submit button

**Preview:**
```
┌────────────────────────────────┐
│        Sign In                 │
├────────────────────────────────┤
│                                │
│  Email                         │
│  ┌──────────────────────────┐ │
│  │ you@example.com          │ │
│  └──────────────────────────┘ │
│                                │
│  Password                      │
│  ┌──────────────────────────┐ │
│  │ ••••••••                 │ │
│  └──────────────────────────┘ │
│                                │
│  ┌──────────────────────────┐ │
│  │      Sign In             │ │
│  └──────────────────────────┘ │
│                                │
└────────────────────────────────┘
```

**Components:**
- 2x TextBoxComponent (email, password)
- 1x ButtonComponent (submit)

---

### Variant B: Standard Login (with Remember Me)

**Description:** Standard login with "remember me" and password recovery  
**Use Case:** Most web apps, default choice  
**Complexity:** 2/5

**Fields:**
- Email (required)
- Password (required)
- Remember me (checkbox)
- Forgot password link
- Submit button

**Preview:**
```
┌────────────────────────────────┐
│        Sign In                 │
├────────────────────────────────┤
│                                │
│  Email                         │
│  ┌──────────────────────────┐ │
│  │ you@example.com          │ │
│  └──────────────────────────┘ │
│                                │
│  Password                      │
│  ┌──────────────────────────┐ │
│  │ ••••••••                 │ │
│  └──────────────────────────┘ │
│                                │
│  ☐ Remember me                 │
│                                │
│  ┌──────────────────────────┐ │
│  │      Sign In             │ │
│  └──────────────────────────┘ │
│                                │
│  Forgot password?              │
│                                │
└────────────────────────────────┘
```

**Components:**
- 2x TextBoxComponent (email, password)
- 1x CheckBoxComponent (remember me)
- 1x ButtonComponent (submit)
- 1x Link (forgot password)

---

### Variant C: Social Login

**Description:** Login with email/password + social authentication  
**Use Case:** B2C apps, public-facing products  
**Complexity:** 3/5

**Fields:**
- Email (required)
- Password (required)
- Remember me (checkbox)
- Submit button
- Divider ("or continue with")
- Google login button
- GitHub login button
- Microsoft login button

**Preview:**
```
┌────────────────────────────────┐
│        Sign In                 │
├────────────────────────────────┤
│                                │
│  Email                         │
│  ┌──────────────────────────┐ │
│  │ you@example.com          │ │
│  └──────────────────────────┘ │
│                                │
│  Password                      │
│  ┌──────────────────────────┐ │
│  │ ••••••••                 │ │
│  └──────────────────────────┘ │
│                                │
│  ☐ Remember me                 │
│                                │
│  ┌──────────────────────────┐ │
│  │      Sign In             │ │
│  └──────────────────────────┘ │
│                                │
│  ─────── or continue with ──── │
│                                │
│  [🔵 Google] [⚫ GitHub]       │
│  [🔷 Microsoft]                │
│                                │
└────────────────────────────────┘
```

**Components:**
- 2x TextBoxComponent (email, password)
- 1x CheckBoxComponent (remember me)
- 4x ButtonComponent (submit + 3 social)

---

### Variant D: Two-Factor Authentication

**Description:** Login with optional 2FA code entry  
**Use Case:** High-security apps (banking, healthcare)  
**Complexity:** 4/5

**Fields:**
- Email (required)
- Password (required)
- 2FA code (conditional, 6 digits)
- Submit button

**Preview:**
```
Step 1: Email + Password
┌────────────────────────────────┐
│        Sign In                 │
├────────────────────────────────┤
│  Email                         │
│  ┌──────────────────────────┐ │
│  │ you@example.com          │ │
│  └──────────────────────────┘ │
│  Password                      │
│  ┌──────────────────────────┐ │
│  │ ••••••••                 │ │
│  └──────────────────────────┘ │
│  ┌──────────────────────────┐ │
│  │      Continue            │ │
│  └──────────────────────────┘ │
└────────────────────────────────┘

Step 2: 2FA Code (if enabled)
┌────────────────────────────────┐
│     Enter Security Code        │
├────────────────────────────────┤
│  Check your authenticator app  │
│                                │
│  ┌───┬───┬───┬───┬───┬───┐   │
│  │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │   │
│  └───┴───┴───┴───┴───┴───┘   │
│                                │
│  ┌──────────────────────────┐ │
│  │      Verify              │ │
│  └──────────────────────────┘ │
│                                │
│  Resend code                   │
└────────────────────────────────┘
```

**Components:**
- 2x TextBoxComponent (email, password)
- 1x MaskedTextBoxComponent (6-digit code)
- 2x ButtonComponent (continue, verify)

---

## Registration Forms

### Variant A: Simple Registration

**Description:** Minimal signup form  
**Use Case:** Quick signups, MVPs  
**Complexity:** 2/5

**Fields:**
- Email (required)
- Password (required)
- Confirm password (required)
- Terms checkbox (required)
- Submit button

**Preview:**
```
┌────────────────────────────────┐
│      Create Account            │
├────────────────────────────────┤
│  Email                         │
│  ┌──────────────────────────┐ │
│  │ you@example.com          │ │
│  └──────────────────────────┘ │
│                                │
│  Password                      │
│  ┌──────────────────────────┐ │
│  │ ••••••••                 │ │
│  └──────────────────────────┘ │
│  Password strength: [====   ] │
│                                │
│  Confirm Password              │
│  ┌──────────────────────────┐ │
│  │ ••••••••                 │ │
│  └──────────────────────────┘ │
│                                │
│  ☐ I agree to Terms & Privacy │
│                                │
│  ┌──────────────────────────┐ │
│  │    Create Account        │ │
│  └──────────────────────────┘ │
└────────────────────────────────┘
```

**Components:**
- 3x TextBoxComponent (email, password, confirm)
- 1x CheckBoxComponent (terms)
- 1x ButtonComponent (submit)

---

### Variant B: Detailed Registration

**Description:** Extended signup with personal details  
**Use Case:** Professional platforms, B2B apps  
**Complexity:** 3/5

**Fields:**
- First name (required)
- Last name (required)
- Email (required)
- Phone number (optional)
- Company (optional)
- Role/Job title (dropdown)
- Password (required)
- Confirm password (required)
- Terms checkbox (required)
- Newsletter checkbox (optional)
- Submit button

**Preview:**
```
┌────────────────────────────────┐
│      Create Account            │
├────────────────────────────────┤
│  First Name        Last Name   │
│  ┌────────────┐   ┌──────────┐│
│  │ John       │   │ Doe      ││
│  └────────────┘   └──────────┘│
│                                │
│  Email                         │
│  ┌──────────────────────────┐ │
│  │ john@example.com         │ │
│  └──────────────────────────┘ │
│                                │
│  Phone (optional)              │
│  ┌──────────────────────────┐ │
│  │ (555) 123-4567           │ │
│  └──────────────────────────┘ │
│                                │
│  Company / Role                │
│  ┌────────────┐  ┌──────────┐ │
│  │ Acme Corp  │  │ Designer ▼││
│  └────────────┘  └──────────┘ │
│                                │
│  Password                      │
│  ┌──────────────────────────┐ │
│  │ ••••••••                 │ │
│  └──────────────────────────┘ │
│                                │
│  ☑ I agree to Terms           │
│  ☐ Send me product updates    │
│                                │
│  ┌──────────────────────────┐ │
│  │    Create Account        │ │
│  └──────────────────────────┘ │
└────────────────────────────────┘
```

**Components:**
- 5x TextBoxComponent
- 1x MaskedTextBoxComponent (phone)
- 1x DropDownListComponent (role)
- 2x CheckBoxComponent
- 1x ButtonComponent

---

## Password Reset Forms

### Variant A: Request Reset

**Description:** First step - enter email to receive reset link  
**Use Case:** Standard password recovery  
**Complexity:** 1/5

**Preview:**
```
┌────────────────────────────────┐
│      Reset Password            │
├────────────────────────────────┤
│  Enter your email address and  │
│  we'll send you a reset link.  │
│                                │
│  Email                         │
│  ┌──────────────────────────┐ │
│  │ you@example.com          │ │
│  └──────────────────────────┘ │
│                                │
│  ┌──────────────────────────┐ │
│  │   Send Reset Link        │ │
│  └──────────────────────────┘ │
│                                │
│  ← Back to Sign In             │
└────────────────────────────────┘
```

---

### Variant B: Set New Password

**Description:** Second step - enter new password  
**Use Case:** After clicking email link  
**Complexity:** 2/5

**Preview:**
```
┌────────────────────────────────┐
│      Set New Password          │
├────────────────────────────────┤
│  New Password                  │
│  ┌──────────────────────────┐ │
│  │ ••••••••                 │ │
│  └──────────────────────────┘ │
│  Password strength: [======  ] │
│                                │
│  Confirm New Password          │
│  ┌──────────────────────────┐ │
│  │ ••••••••                 │ │
│  └──────────────────────────┘ │
│                                │
│  ┌──────────────────────────┐ │
│  │   Reset Password         │ │
│  └──────────────────────────┘ │
└────────────────────────────────┘
```

---

## Contact Forms

### Variant A: Simple Contact

**Description:** Basic contact form  
**Use Case:** Landing pages, support pages  
**Complexity:** 2/5

**Preview:**
```
┌────────────────────────────────┐
│      Contact Us                │
├────────────────────────────────┤
│  Name                          │
│  ┌──────────────────────────┐ │
│  │ Your name                │ │
│  └──────────────────────────┘ │
│                                │
│  Email                         │
│  ┌──────────────────────────┐ │
│  │ you@example.com          │ │
│  └──────────────────────────┘ │
│                                │
│  Message                       │
│  ┌──────────────────────────┐ │
│  │                          │ │
│  │                          │ │
│  │                          │ │
│  └──────────────────────────┘ │
│                                │
│  ┌──────────────────────────┐ │
│  │   Send Message           │ │
│  └──────────────────────────┘ │
└────────────────────────────────┘
```

---

## Data Tables

### Variant A: Read-Only Table

**Description:** Simple data display with pagination  
**Use Case:** Reports, logs  
**Complexity:** 2/5

**Features:**
- Pagination
- Column headers
- Row selection (optional)

**Preview:**
```
┌─────────────────────────────────────────────────────┐
│  Customers                                          │
├─────────────────────────────────────────────────────┤
│  ☐  ID     Name            Email          Status   │
├─────────────────────────────────────────────────────┤
│  ☐  001    John Doe        john@ex.com    Active   │
│  ☐  002    Jane Smith      jane@ex.com    Active   │
│  ☐  003    Bob Wilson      bob@ex.com     Inactive │
│  ☐  004    Alice Brown     alice@ex.com   Active   │
│                                                     │
├─────────────────────────────────────────────────────┤
│  Showing 1-4 of 42         [◄] 1 2 3 4 5 [►]      │
└─────────────────────────────────────────────────────┘
```

---

### Variant B: Sortable & Filterable Table

**Description:** Interactive table with sorting and filtering  
**Use Case:** Admin panels, data management  
**Complexity:** 3/5

**Features:**
- Sort by column (click header)
- Filter by column (Excel-style)
- Pagination
- Row selection

**Preview:**
```
┌─────────────────────────────────────────────────────┐
│  Customers                     [🔍 Search...]  [+]  │
├─────────────────────────────────────────────────────┤
│  ☐  ID ▲  Name ▼    Email       Status ⚙    Actions│
├─────────────────────────────────────────────────────┤
│  ☐  001   Alice      alice@...  Active     [✏ 🗑]  │
│  ☐  002   Bob        bob@...    Active     [✏ 🗑]  │
│  ☐  003   Charlie    char@...   Inactive   [✏ 🗑]  │
│                                                     │
├─────────────────────────────────────────────────────┤
│  Showing 1-3 of 42         [◄] 1 2 3 4 5 [►]      │
└─────────────────────────────────────────────────────┘
```

---

### Variant C: Inline Editable Table

**Description:** Table with inline editing  
**Use Case:** Data entry, bulk updates  
**Complexity:** 4/5

**Features:**
- Click to edit cells
- Save/cancel per row
- Validation
- Bulk actions

---

## Navigation Patterns

### Variant A: Horizontal Navbar

**Description:** Top navigation bar  
**Use Case:** Most web apps, marketing sites  
**Complexity:** 2/5

**Preview:**
```
┌─────────────────────────────────────────────────────┐
│  [Logo] Home  Products  About  Contact   [Profile]│
└─────────────────────────────────────────────────────┘
```

---

### Variant B: Vertical Sidebar

**Description:** Left sidebar navigation  
**Use Case:** Dashboards, admin panels  
**Complexity:** 2/5

**Preview:**
```
┌─────────┬─────────────────────────────────────┐
│ [Logo]  │                                     │
│         │                                     │
│ 📊 Dash │      Main Content Area             │
│ 📁 Proj │                                     │
│ 👥 Team │                                     │
│ ⚙ Sett  │                                     │
│         │                                     │
│         │                                     │
│ 👤 User │                                     │
└─────────┴─────────────────────────────────────┘
```

---

### Variant C: Top + Side Navigation

**Description:** Combined top bar and sidebar  
**Use Case:** Complex admin interfaces  
**Complexity:** 3/5

**Preview:**
```
┌─────────────────────────────────────────────────────┐
│  [Logo]  Search...                        [Profile]│
├─────────┬───────────────────────────────────────────┤
│ 📊 Dash │                                           │
│ 📁 Proj │      Main Content Area                   │
│ 👥 Team │                                           │
└─────────┴───────────────────────────────────────────┘
```

---

## Dashboard Layouts

### Variant A: Single-Column Dashboard

**Description:** Stacked widgets  
**Use Case:** Mobile-first, simple dashboards  
**Complexity:** 2/5

**Preview:**
```
┌──────────────────────────────┐
│  ┌────────────────────────┐  │
│  │  Total Sales           │  │
│  │  $12,450               │  │
│  └────────────────────────┘  │
│  ┌────────────────────────┐  │
│  │  Recent Orders         │  │
│  │  [Table]               │  │
│  └────────────────────────┘  │
│  ┌────────────────────────┐  │
│  │  Activity Chart        │  │
│  │  [Chart]               │  │
│  └────────────────────────┘  │
└──────────────────────────────┘
```

---

### Variant B: Grid Dashboard

**Description:** 3-column grid layout  
**Use Case:** Analytics, monitoring  
**Complexity:** 3/5

**Preview:**
```
┌────────────────────────────────────────────────┐
│  ┌───────┐  ┌───────┐  ┌───────┐             │
│  │ Sales │  │ Users │  │Revenue│             │
│  │$12.4K │  │ 1,245 │  │$45.2K │             │
│  └───────┘  └───────┘  └───────┘             │
│  ┌─────────────────────────────────┐          │
│  │  Sales Chart                    │          │
│  │  [Line Chart]                   │          │
│  └─────────────────────────────────┘          │
│  ┌──────────────┐  ┌────────────────────┐    │
│  │ Recent Orders│  │ Top Products       │    │
│  │ [Table]      │  │ [List]             │    │
│  └──────────────┘  └────────────────────┘    │
└────────────────────────────────────────────────┘
```

---

## Multi-Step Forms

### Variant A: Linear Wizard

**Description:** Sequential steps, no skipping  
**Use Case:** Onboarding, checkouts  
**Complexity:** 3/5

**Preview:**
```
Step 1: Account Info
┌────────────────────────────────┐
│  Step 1 of 3: Account Info     │
│  [●]────[○]────[○]             │
├────────────────────────────────┤
│  Email                         │
│  ┌──────────────────────────┐ │
│  │ you@example.com          │ │
│  └──────────────────────────┘ │
│                                │
│  [Cancel]          [Next →]   │
└────────────────────────────────┘

Step 2: Personal Details
┌────────────────────────────────┐
│  Step 2 of 3: Personal Details │
│  [●]────[●]────[○]             │
├────────────────────────────────┤
│  First Name      Last Name     │
│  ┌───────────┐  ┌───────────┐ │
│  │ John      │  │ Doe       │ │
│  └───────────┘  └───────────┘ │
│                                │
│  [← Back]          [Next →]   │
└────────────────────────────────┘

Step 3: Confirmation
┌────────────────────────────────┐
│  Step 3 of 3: Confirm          │
│  [●]────[●]────[●]             │
├────────────────────────────────┤
│  Review your information:      │
│                                │
│  Email: john@example.com       │
│  Name: John Doe                │
│                                │
│  [← Back]         [Submit ✓]  │
└────────────────────────────────┘
```

---

**End of Layout Variants Catalog**  
For component mapping, see `SYNCFUSION-MAPPING.md`  
For workflow details, see `STAGES.md`  
For troubleshooting, see `TROUBLESHOOTING.md`
