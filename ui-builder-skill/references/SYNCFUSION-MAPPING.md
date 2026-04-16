# Syncfusion Component Mapping Reference

**Version:** 1.0.0  
**Last Updated:** April 15, 2026  
**Purpose:** Complete reference for mapping UI layout fields to Syncfusion React components

---

## Table of Contents

1. [Overview](#overview)
2. [Form Input Components](#form-input-components)
3. [Selection Components](#selection-components)
4. [Button Components](#button-components)
5. [Data Display Components](#data-display-components)
6. [Layout & Container Components](#layout--container-components)
7. [Navigation Components](#navigation-components)
8. [Dialog & Popup Components](#dialog--popup-components)
9. [Date & Time Components](#date--time-components)
10. [Rich Text & Media Components](#rich-text--media-components)
11. [Mapping Decision Trees](#mapping-decision-trees)
12. [Package Dependencies](#package-dependencies)

---

## Overview

### 1.1 Mapping Philosophy

Each UI field type is mapped to the **most semantically appropriate Syncfusion component** that:
- Provides the required functionality
- Supports full accessibility (WCAG 2.1 AA)
- Integrates with the project's design system
- Minimizes over-engineering (don't use complex component for simple need)

### 1.2 Quick Reference Table

| Field Type | Syncfusion Component | Package | Notes |
|------------|----------------------|---------|-------|
| **Text Input** | TextBoxComponent | @syncfusion/ej2-react-inputs | General text, email, URL, search |
| **Textarea** | TextAreaComponent | @syncfusion/ej2-react-inputs | Multi-line text |
| **Number Input** | NumericTextBoxComponent | @syncfusion/ej2-react-inputs | Integers, decimals with spinner |
| **Password** | TextBoxComponent (type="password") | @syncfusion/ej2-react-inputs | Masked text entry |
| **Masked Input** | MaskedTextBoxComponent | @syncfusion/ej2-react-inputs | Phone, SSN, credit card patterns |
| **Checkbox** | CheckBoxComponent | @syncfusion/ej2-react-buttons | Single toggle |
| **Radio Button** | RadioButtonComponent | @syncfusion/ej2-react-buttons | Mutually exclusive options |
| **Toggle Switch** | SwitchComponent | @syncfusion/ej2-react-buttons | On/Off state |
| **Dropdown Select** | DropDownListComponent | @syncfusion/ej2-react-dropdowns | Static list, single selection |
| **Multi-Select** | MultiSelectComponent | @syncfusion/ej2-react-dropdowns | Multiple selections with checkboxes |
| **Autocomplete** | AutoCompleteComponent | @syncfusion/ej2-react-dropdowns | Text input with suggestions |
| **Combobox** | ComboBoxComponent | @syncfusion/ej2-react-dropdowns | Dropdown + free-text entry |
| **Date Picker** | DatePickerComponent | @syncfusion/ej2-react-calendars | Single date selection |
| **Date Range** | DateRangePickerComponent | @syncfusion/ej2-react-calendars | Start + end date |
| **Time Picker** | TimePickerComponent | @syncfusion/ej2-react-calendars | Time selection |
| **DateTime** | DateTimePickerComponent | @syncfusion/ej2-react-calendars | Date + time combined |
| **Button** | ButtonComponent | @syncfusion/ej2-react-buttons | Primary, secondary, danger actions |
| **Icon Button** | ButtonComponent (iconCss) | @syncfusion/ej2-react-buttons | Icon-only button with tooltip |
| **Button Group** | ButtonGroupComponent | @syncfusion/ej2-react-buttons | Toggle between options |
| **Data Grid** | GridComponent | @syncfusion/ej2-react-grids | Tables with sorting, filtering, CRUD |
| **Tree Grid** | TreeGridComponent | @syncfusion/ej2-react-grids | Hierarchical data with expand/collapse |
| **List View** | ListViewComponent | @syncfusion/ej2-react-grids | Scrollable list with selection |
| **Navbar** | NavbarComponent | Custom + Bootstrap | Horizontal navigation |
| **Sidebar** | SidebarComponent | @syncfusion/ej2-react-popups | Collapsible left/right navigation |
| **Accordion** | AccordionComponent | @syncfusion/ej2-react-popups | Expandable sections |
| **Tabs** | TabComponent | @syncfusion/ej2-react-popups | Tab-based content switching |
| **Dialog** | DialogComponent | @syncfusion/ej2-react-popups | Modal dialog boxes |
| **Tooltip** | TooltipComponent | @syncfusion/ej2-react-popups | Hover helper text |
| **Toast** | ToastComponent | @syncfusion/ej2-react-notifications | Non-modal notifications |
| **Spinner** | SpinnerComponent | @syncfusion/ej2-react-popups | Loading indicator |

---

## Form Input Components

### 2.1 TextBoxComponent

**Package:** `@syncfusion/ej2-react-inputs`

**Supported Input Types:**
- `text` - Default, general text
- `email` - Email validation built-in
- `password` - Masked password entry
- `url` - URL validation
- `tel` - Telephone number
- `number` - Numeric input (use NumericTextBox for spinner)
- `search` - Search field with clear button

**Mapping Decision:**

```
Field Type: "email" or "email-address"
  → TextBoxComponent with type="email"
  → Prop: { type: "email", floatLabelType: "Auto" }

Field Type: "password"
  → TextBoxComponent with type="password"
  → Prop: { type: "password", floatLabelType: "Auto" }

Field Type: "search"
  → TextBoxComponent with type="search"
  → Prop: { type: "search", floatLabelType: "Auto", multiline: false }

Field Type: "url" or "website"
  → TextBoxComponent with type="url"
  → Prop: { type: "url", floatLabelType: "Auto" }

Field Type: "text" or generic
  → TextBoxComponent
  → Prop: { type: "text", floatLabelType: "Auto" }
```

**Key Props:**

```tsx
<TextBoxComponent
  type="email"                          // "text" | "email" | "password" | "url"
  placeholder="Enter your email"        // Helper text
  floatLabelType="Auto"                 // Label animation
  enabled={true}                        // Enable/disable
  readonly={false}                      // Read-only mode
  multiline={false}                     // Multi-line textarea
  value={value}                         // Controlled value
  onChange={handleChange}               // Change event
  onBlur={handleBlur}                   // Blur for validation
  ref={inputRef}                        // DOM ref for focus
  enablePersist={false}                 // LocalStorage persistence
  cssClass="e-outline"                  // Outline style
/>
```

**Validation Integration:**

```tsx
const [email, setEmail] = useState('');
const [emailError, setEmailError] = useState('');

const validateEmail = (value: string) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(value)) {
    setEmailError('Invalid email format');
    return false;
  }
  setEmailError('');
  return true;
};

const handleBlur = () => {
  validateEmail(email);
};
```

**Accessibility:**

```tsx
<TextBoxComponent
  type="email"
  placeholder="Enter your email"
  aria-label="Email address"
  aria-describedby={emailError ? "email-error" : undefined}
  aria-invalid={!!emailError}
/>
{emailError && <span id="email-error" className="error">{emailError}</span>}
```

---

### 2.2 NumericTextBoxComponent

**Package:** `@syncfusion/ej2-react-inputs`

**Best For:** Numbers, decimals, currency, percentages

**When to Use vs TextBoxComponent:**
- Use NumericTextBox for: Age, salary, quantity, percentage (has spinner buttons, validation)
- Use TextBoxComponent(type="number") for: Basic number input (lightweight)

**Mapping Decision:**

```
Field Type: "number", "age", "quantity", "count"
  → NumericTextBoxComponent
  → Prop: { min: 0, max: 150, format: "n0" }

Field Type: "currency", "price", "salary"
  → NumericTextBoxComponent
  → Prop: { currency: "USD", format: "c2", min: 0 }

Field Type: "percentage"
  → NumericTextBoxComponent
  → Prop: { format: "p2", min: 0, max: 100 }

Field Type: "decimal", "temperature"
  → NumericTextBoxComponent
  → Prop: { format: "n2", decimals: 2, step: 0.01 }
```

**Key Props:**

```tsx
<NumericTextBoxComponent
  value={42}                            // Current value
  min={0}                               // Minimum allowed
  max={100}                             // Maximum allowed
  step={1}                              // Increment step
  format="n2"                           // Format: "n0" (int), "n2" (2 decimals)
  currency="USD"                        // "USD", "EUR", etc. (use with format="c")
  placeholder="Enter a number"
  enablePersist={false}
  readonly={false}
  enabled={true}
  onChange={handleChange}
/>
```

---

### 2.3 MaskedTextBoxComponent

**Package:** `@syncfusion/ej2-react-inputs`

**Best For:** Phone numbers, SSN, credit cards, postal codes with fixed patterns

**Mask Patterns:**

```
Digit (0-9):        '9'
Digit/space:        '0'
Character (A-Z):    '>'
Character (a-z):    '<'
Character (A-Z/0-9):'?'
Escape character:   '\'
```

**Common Masks:**

```
Phone (US):        (999) 999-9999
Credit Card:       9999-9999-9999-9999
SSN:               999-99-9999
Postal Code (US):  99999 or 99999-9999
Date:              99/99/9999
Time:              99:99:99
```

**Mapping Decision:**

```
Field Type: "phone" or "telephone"
  → MaskedTextBoxComponent
  → Prop: { mask: "(999) 999-9999", placeholder: "(___) ___-____" }

Field Type: "credit-card" or "card"
  → MaskedTextBoxComponent
  → Prop: { mask: "9999-9999-9999-9999", placeholder: "____-____-____-____" }

Field Type: "ssn" or "tax-id"
  → MaskedTextBoxComponent
  → Prop: { mask: "999-99-9999", placeholder: "___-__-____" }

Field Type: "postal-code" or "zip"
  → MaskedTextBoxComponent
  → Prop: { mask: "99999", placeholder: "_____" }
```

**Key Props:**

```tsx
<MaskedTextBoxComponent
  mask="(999) 999-9999"                 // Pattern
  placeholder="(___) ___-____"          // Visual guide
  value={phone}
  onChange={handleChange}
  promptChar="_"                        // Character for empty position
/>
```

---

### 2.4 TextAreaComponent (Custom or HTML)

**Package:** @syncfusion/ej2-react-inputs (or native `<textarea>`)

**When to Use:**
- Long-form text (bio, description, notes)
- Multi-line input with line wrapping

**Implementation Options:**

**Option A: Native HTML (Lightweight)**
```tsx
<textarea
  value={bio}
  onChange={(e) => setBio(e.target.value)}
  placeholder="Enter your bio"
  rows={5}
  className="e-field"
/>
```

**Option B: Syncfusion TextBoxComponent (Styled)**
```tsx
<TextBoxComponent
  type="text"
  multiline={true}
  rows={5}
  placeholder="Enter your bio"
  value={bio}
  onChange={handleChange}
/>
```

---

## Selection Components

### 3.1 CheckBoxComponent

**Package:** `@syncfusion/ej2-react-buttons`

**Best For:** Single boolean toggle, yes/no, agree to terms

**Mapping Decision:**

```
Field Type: "checkbox", "agree", "terms", "remember-me"
  → CheckBoxComponent
  → Prop: { label: "I agree to terms", checked: false }
```

**Key Props:**

```tsx
<CheckBoxComponent
  checked={rememberMe}                  // Boolean state
  onChange={(e) => setRememberMe(e.checked)}
  label="Remember me"                   // Label text
  disabled={false}
  indeterminate={false}                 // Three-state checkbox
/>
```

**Accessibility:**

```tsx
<div className="checkbox-group">
  <CheckBoxComponent
    id="remember-me"
    checked={rememberMe}
    onChange={handleChange}
    label="Remember me"
    aria-label="Remember my login credentials"
  />
</div>
```

---

### 3.2 RadioButtonComponent

**Package:** `@syncfusion/ej2-react-buttons`

**Best For:** Mutually exclusive options (choose one)

**Mapping Decision:**

```
Field Type: "radio", "gender", "role", "plan"
  → RadioButtonComponent (multiple)
  → Options: Array of {label, value}

Example: Gender selection
  Options: [{label: "Male", value: "M"}, 
            {label: "Female", value: "F"},
            {label: "Other", value: "O"}]
```

**Implementation:**

```tsx
const genderOptions = [
  { label: "Male", value: "M" },
  { label: "Female", value: "F" },
  { label: Other", value: "O" }
];

return (
  <fieldset>
    <legend>Gender</legend>
    {genderOptions.map(option => (
      <div key={option.value}>
        <RadioButtonComponent
          id={`gender-${option.value}`}
          name="gender"
          value={option.value}
          checked={gender === option.value}
          onChange={(e) => setGender(e.value)}
          label={option.label}
        />
      </div>
    ))}
  </fieldset>
);
```

---

### 3.3 SwitchComponent

**Package:** `@syncfusion/ej2-react-buttons`

**Best For:** Toggle on/off features, enable/disable settings

**When to Use:**
- Use Switch for: Settings (dark mode, notifications, two-factor auth)
- Use Checkbox for: Terms agreement, single item selection
- Use RadioButton for: Mutually exclusive options

**Mapping Decision:**

```
Field Type: "toggle", "switch", "enable", "disable"
  → SwitchComponent
  → Prop: { checked: false, onChange: handleChange }
```

**Key Props:**

```tsx
<SwitchComponent
  checked={darkMode}
  onChange={(e) => setDarkMode(e.checked)}
  onLabel="On"
  offLabel="Off"
  disabled={false}
/>
```

---

## Selection Components

### 4.1 DropDownListComponent

**Package:** `@syncfusion/ej2-react-dropdowns`

**Best For:** Select one from a list of options (static or dynamic)

**Mapping Decision:**

```
Field Type: "select", "dropdown", "country", "category", "status"
  → DropDownListComponent
  → DataSource: Array of {text, value}

Example: Country selection
  DataSource: [{text: "United States", value: "US"},
               {text: "Canada", value: "CA"},
               ...]
```

**Key Props:**

```tsx
<DropDownListComponent
  dataSource={countries}                // Array or datasource
  fields={{ text: 'text', value: 'value' }}
  value={selectedCountry}
  onChange={(e) => setSelectedCountry(e.value)}
  placeholder="Select a country"
  allowFiltering={true}                 // Enable search
  filterType="Contains"                 // "StartsWith" | "Contains" | "EndsWith"
  popupHeight="250px"
/>
```

**Filtering:**

```tsx
<DropDownListComponent
  dataSource={largeList}                // 1000+ items
  fields={{ text: 'name', value: 'id' }}
  allowFiltering={true}                 // Enable search
  filterBarPlaceholder="Search..."
  noRecordsTemplate="No items found"
/>
```

---

### 4.2 MultiSelectComponent

**Package:** `@syncfusion/ej2-react-dropdowns`

**Best For:** Select multiple items (skills, tags, categories)

**Mapping Decision:**

```
Field Type: "multi-select", "skills", "tags", "interests"
  → MultiSelectComponent
  → DataSource: Array of options
  → Value: Array of selected values
```

**Key Props:**

```tsx
<MultiSelectComponent
  dataSource={skills}
  fields={{ text: 'skill', value: 'id' }}
  value={selectedSkills}                // Array of IDs
  onChange={(e) => setSelectedSkills(e.value)}
  placeholder="Select skills"
  showSelectAll={true}
  allowFiltering={true}
  mode="CheckBox"                       // Shows checkboxes
/>
```

---

### 4.3 AutoCompleteComponent

**Package:** `@syncfusion/ej2-react-dropdowns`

**Best For:** Type-to-search suggestions (countries, cities, product names)

**Mapping Decision:**

```
Field Type: "autocomplete", "search", "typeahead"
  → AutoCompleteComponent
  → DataSource: Array or API endpoint
```

**Key Props:**

```tsx
<AutoCompleteComponent
  dataSource={countries}
  fields={{ text: 'name', value: 'id' }}
  value={selectedCountry}
  onChange={(e) => setSelectedCountry(e.value)}
  placeholder="Type to search..."
  allowFiltering={true}
  minLength={2}                         // Trigger after 2 chars
  highlight={true}
/>
```

---

### 4.4 ComboBoxComponent

**Package:** `@syncfusion/ej2-react-dropdowns`

**Best For:** Dropdown + free-text entry (select from list OR type custom value)

**When to Use:**
- Use Dropdown for: Fixed list (no custom values allowed)
- Use ComboBox for: Mostly fixed list but user can add custom
- Use AutoComplete for: Typeahead search suggestions

**Mapping Decision:**

```
Field Type: "combobox", "other-please-specify", "custom-input"
  → ComboBoxComponent
  → AllowCustom: true (user can type custom value)
```

**Key Props:**

```tsx
<ComboBoxComponent
  dataSource={categories}
  fields={{ text: 'name', value: 'id' }}
  value={selectedCategory}
  onChange={(e) => setSelectedCategory(e.value)}
  placeholder="Select or type..."
  allowCustom={true}                   // Allow free-text entry
  allowFiltering={true}
/>
```

---

## Button Components

### 5.1 ButtonComponent

**Package:** `@syncfusion/ej2-react-buttons`

**Types of Buttons:**

| Type | Usage | Props |
|------|-------|-------|
| **Primary** | Main action (submit, save, create) | `isPrimary={true}` |
| **Secondary** | Alternative action (cancel, dismiss) | (default) |
| **Danger** | Destructive action (delete, remove) | `cssClass="e-danger"` |
| **Outline** | Secondary with border | `cssClass="e-outline"` |
| **Text** | Minimal, text-only | `cssClass="e-text"` |
| **Icon** | Icon-only button | `iconCss="e-icon"` |
| **Icon + Text** | Icon with label | Both `iconCss` and children |

**Mapping Decision:**

```
Field: "submit" button
  → ButtonComponent with isPrimary={true}
  → Prop: { type: "submit", isPrimary: true, content: "Submit" }

Field: "cancel" button
  → ButtonComponent
  → Prop: { type: "button", content: "Cancel" }

Field: "delete" button
  → ButtonComponent with danger styling
  → Prop: { type: "button", cssClass: "e-danger", content: "Delete" }

Field: "icon button" (close, menu, search)
  → ButtonComponent with icon
  → Prop: { iconCss: "e-icons e-close", aria-label: "Close" }
```

**Key Props:**

```tsx
<ButtonComponent
  type="submit"                         // "submit" | "button" | "reset"
  isPrimary={true}                      // Primary/secondary styling
  cssClass="e-danger"                   // Additional CSS: "e-outline", "e-text"
  iconCss="e-icons e-save"              // Icon class
  iconPosition="Left"                   // "Left" | "Right"
  disabled={false}
  onClick={handleClick}
>
  Save
</ButtonComponent>
```

**Icon Button (No Text):**

```tsx
<ButtonComponent
  iconCss="e-icons e-close"
  cssClass="e-icon-btn"
  title="Close"
  aria-label="Close dialog"
  onClick={handleClose}
/>
```

---

## Data Display Components

### 6.1 GridComponent (Data Table)

**Package:** `@syncfusion/ej2-react-grids`

**Best For:** Displaying structured data with sorting, filtering, pagination, CRUD operations

**Mapping Decision:**

```
Field Type: "data-table", "grid", "list" with sortable/filterable
  → GridComponent
  → Columns: Array of {field, headerText, type}
  → DataSource: Array of objects or API endpoint
```

**Key Props:**

```tsx
<GridComponent
  dataSource={customerData}
  allowPaging={true}
  pageSettings={{ pageSize: 12 }}
  allowSorting={true}
  allowFiltering={true}
  filterSettings={{ type: 'Excel' }}
  allowSelection={true}
  selectionSettings={{ type: 'Checkbox' }}
  actionFailure={(args) => console.log('Error:', args)}
>
  <ColumnsDirective>
    <ColumnDirective field='OrderID' headerText='Order ID' width='120'/>
    <ColumnDirective field='CustomerName' headerText='Customer Name' width='150'/>
    <ColumnDirective field='OrderDate' headerText='Order Date' type='date' format='yMd' width='120'/>
    <ColumnDirective field='Amount' headerText='Amount' type='number' format='C2' width='120'/>
  </ColumnsDirective>
  <Inject services={[Page, Sort, Filter, Selection]}/>
</GridComponent>
```

**Common Features:**

| Feature | Service | Props |
|---------|---------|-------|
| **Pagination** | `Page` | `allowPaging={true}`, `pageSettings` |
| **Sorting** | `Sort` | `allowSorting={true}` |
| **Filtering** | `Filter` | `allowFiltering={true}` |
| **Selection** | `Selection` | `allowSelection={true}`, `selectionSettings` |
| **Grouping** | `Group` | `allowGrouping={true}` |
| **Aggregates** | `Aggregate` | `groupSettings`, `aggregates` |
| **Inline Edit** | `Edit` | `editSettings`, `mode: 'Dialog'` |
| **Export** | `ExcelExport`, `PdfExport` | `toolbarClick` event |

---

## Navigation Components

### 7.1 NavbarComponent (Custom Implementation)

For horizontal navigation bars, use standard HTML + Syncfusion styling, or use native Bootstrap navbar.

**Implementation:**

```tsx
export const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <a href="/">MyApp</a>
      </div>
      <ul className="navbar-menu">
        <li><a href="/home">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/services">Services</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>
  );
};
```

---

### 7.2 SidebarComponent

**Package:** `@syncfusion/ej2-react-popups`

**Best For:** Collapsible side navigation, off-canvas menus

**Key Props:**

```tsx
<SidebarComponent
  width="280px"
  target=".main-content"
  type="Over"                           // "Over" | "Push" | "Slide"
  isOpen={isSidebarOpen}
  change={(args) => setIsSidebarOpen(args.isOpen)}
>
  <ul className="sidebar-menu">
    <li><a href="/dashboard">Dashboard</a></li>
    <li><a href="/settings">Settings</a></li>
    <li><a href="/profile">Profile</a></li>
  </ul>
</SidebarComponent>
```

---

### 7.3 TabComponent

**Package:** `@syncfusion/ej2-react-popups`

**Best For:** Content organization in tabs

**Key Props:**

```tsx
<TabComponent>
  <TabItemsDirective>
    <TabItemDirective header={{ text: 'Profile' }}>
      <div>Profile content here</div>
    </TabItemDirective>
    <TabItemDirective header={{ text: 'Settings' }}>
      <div>Settings content here</div>
    </TabItemDirective>
  </TabItemsDirective>
</TabComponent>
```

---

## Dialog & Popup Components

### 8.1 DialogComponent

**Package:** `@syncfusion/ej2-react-popups`

**Best For:** Modal dialogs, confirmation, forms in modal

**Key Props:**

```tsx
<DialogComponent
  isOpen={isOpen}
  onClose={handleClose}
  header="Confirm Action"
  showCloseIcon={true}
  width="400px"
  animationSettings={{ effect: 'Zoom' }}
>
  <div>
    <p>Are you sure you want to delete this item?</p>
    <div className="dialog-footer">
      <ButtonComponent onClick={handleConfirm} isPrimary={true}>
        Delete
      </ButtonComponent>
      <ButtonComponent onClick={handleClose}>
        Cancel
      </ButtonComponent>
    </div>
  </div>
</DialogComponent>
```

---

## Date & Time Components

### 9.1 DatePickerComponent

**Package:** `@syncfusion/ej2-react-calendars`

**Best For:** Single date selection

**Key Props:**

```tsx
<DatePickerComponent
  value={selectedDate}
  onChange={(args) => setSelectedDate(args.value)}
  placeholder="Select a date"
  format="yyyy-MM-dd"
  min={new Date(2020, 0, 1)}
  max={new Date()}
/>
```

---

### 9.2 DateRangePickerComponent

**Package:** `@syncfusion/ej2-react-calendars`

**Best For:** Date range (start + end date)

**Key Props:**

```tsx
<DateRangePickerComponent
  startDate={startDate}
  endDate={endDate}
  change={(args) => {
    setStartDate(args.startDate);
    setEndDate(args.endDate);
  }}
  placeholder="Select date range"
/>
```

---

## Rich Text & Media Components

### 10.1 Rich Text Editor

**Package:** `@syncfusion/ej2-react-richtexteditor`

**Best For:** WYSIWYG text editing with formatting

**Key Props:**

```tsx
<RichTextEditorComponent
  value={content}
  onChange={(args) => setContent(args.value)}
  height="400px"
  toolbarSettings={{
    items: ['Bold', 'Italic', 'Underline', '|', 
            'Formats', '|', 'CreateLink', 'Image']
  }}
/>
```

---

## Mapping Decision Trees

### 11.1 Input Field Selection Tree

```
Is it a boolean (yes/no)?
├─ Is it a toggle/switch (on/off setting)?
│  └─ SwitchComponent
├─ Is it a single checkbox (terms agreement)?
│  └─ CheckBoxComponent
└─ Is it mutually exclusive with other options?
   └─ RadioButtonComponent

Is it a list selection?
├─ Can user select multiple?
│  ├─ MultiSelectComponent with checkboxes
│  └─ CheckBoxComponent group
├─ Can user type custom value?
│  └─ ComboBoxComponent
├─ Is it searchable/typeahead?
│  └─ AutoCompleteComponent
└─ Fixed list, single selection
   └─ DropDownListComponent

Is it a text input?
├─ Multiple lines?
│  └─ TextAreaComponent (multiline: true)
├─ Masked pattern (phone, credit card)?
│  └─ MaskedTextBoxComponent
├─ Email, URL, search?
│  └─ TextBoxComponent (type specific)
├─ Number with spinner?
│  └─ NumericTextBoxComponent
└─ Plain text
   └─ TextBoxComponent

Is it date/time?
├─ Date range (start/end)?
│  └─ DateRangePickerComponent
├─ Date only?
│  └─ DatePickerComponent
├─ Time only?
│  └─ TimePickerComponent
└─ Date + time combined
   └─ DateTimePickerComponent
```

---

## Package Dependencies

### 12.1 By Component

| Component | Package | Version | Dependencies |
|-----------|---------|---------|--------------|
| TextBoxComponent | @syncfusion/ej2-react-inputs | ^20.0.0 | @syncfusion/ej2-base |
| NumericTextBoxComponent | @syncfusion/ej2-react-inputs | ^20.0.0 | @syncfusion/ej2-base |
| MaskedTextBoxComponent | @syncfusion/ej2-react-inputs | ^20.0.0 | @syncfusion/ej2-base |
| ButtonComponent | @syncfusion/ej2-react-buttons | ^20.0.0 | @syncfusion/ej2-base |
| CheckBoxComponent | @syncfusion/ej2-react-buttons | ^20.0.0 | @syncfusion/ej2-base |
| RadioButtonComponent | @syncfusion/ej2-react-buttons | ^20.0.0 | @syncfusion/ej2-base |
| SwitchComponent | @syncfusion/ej2-react-buttons | ^20.0.0 | @syncfusion/ej2-base |
| DropDownListComponent | @syncfusion/ej2-react-dropdowns | ^20.0.0 | @syncfusion/ej2-base |
| MultiSelectComponent | @syncfusion/ej2-react-dropdowns | ^20.0.0 | @syncfusion/ej2-base |
| AutoCompleteComponent | @syncfusion/ej2-react-dropdowns | ^20.0.0 | @syncfusion/ej2-base |
| ComboBoxComponent | @syncfusion/ej2-react-dropdowns | ^20.0.0 | @syncfusion/ej2-base |
| GridComponent | @syncfusion/ej2-react-grids | ^20.0.0 | @syncfusion/ej2-base |
| TreeGridComponent | @syncfusion/ej2-react-grids | ^20.0.0 | @syncfusion/ej2-base |
| DatePickerComponent | @syncfusion/ej2-react-calendars | ^20.0.0 | @syncfusion/ej2-base |
| DateRangePickerComponent | @syncfusion/ej2-react-calendars | ^20.0.0 | @syncfusion/ej2-base |
| TimePickerComponent | @syncfusion/ej2-react-calendars | ^20.0.0 | @syncfusion/ej2-base |
| DateTimePickerComponent | @syncfusion/ej2-react-calendars | ^20.0.0 | @syncfusion/ej2-base |
| DialogComponent | @syncfusion/ej2-react-popups | ^20.0.0 | @syncfusion/ej2-base |
| TooltipComponent | @syncfusion/ej2-react-popups | ^20.0.0 | @syncfusion/ej2-base |
| TabComponent | @syncfusion/ej2-react-popups | ^20.0.0 | @syncfusion/ej2-base |
| AccordionComponent | @syncfusion/ej2-react-popups | ^20.0.0 | @syncfusion/ej2-base |
| SidebarComponent | @syncfusion/ej2-react-popups | ^20.0.0 | @syncfusion/ej2-base |
| ToastComponent | @syncfusion/ej2-react-notifications | ^20.0.0 | @syncfusion/ej2-base |
| RichTextEditorComponent | @syncfusion/ej2-react-richtexteditor | ^20.0.0 | @syncfusion/ej2-base |

### 12.2 Bundle Installation

**All form inputs:**
```bash
npm install @syncfusion/ej2-react-inputs @syncfusion/ej2-react-buttons @syncfusion/ej2-react-dropdowns @syncfusion/ej2-react-calendars @syncfusion/ej2-react-base
```

**All data display:**
```bash
npm install @syncfusion/ej2-react-grids @syncfusion/ej2-react-base
```

**All components:**
```bash
npm install @syncfusion/ej2-react-inputs @syncfusion/ej2-react-buttons @syncfusion/ej2-react-dropdowns @syncfusion/ej2-react-calendars @syncfusion/ej2-react-grids @syncfusion/ej2-react-popups @syncfusion/ej2-react-notifications @syncfusion/ej2-react-richtexteditor @syncfusion/ej2-react-base
```

---

## Appendix: Component Selection Checklist

When mapping a new field:

- [ ] Identify field type (text, select, date, button, etc.)
- [ ] Consider field semantics (what does it represent?)
- [ ] Check if multiple selection needed
- [ ] Check if custom input allowed
- [ ] Determine validation rules
- [ ] Check accessibility requirements
- [ ] Verify component supports selected theme
- [ ] Confirm all required packages in dependencies
- [ ] Test on mobile and desktop viewports
- [ ] Verify keyboard navigation works
- [ ] Verify screen reader announces component correctly

---

**End of Syncfusion Mapping Reference**  
For workflow questions, see `STAGES.md`  
For web standards compliance, see `WEB-STANDARDS.md`  
For troubleshooting, see `TROUBLESHOOTING.md`
