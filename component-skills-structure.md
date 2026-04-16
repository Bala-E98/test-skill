**Component Skills in user project:**

- `.agent/skills/syncfusion-react-grid/SKILL.md` → GridComponent for data tables with sorting, filtering, pagination
- `.agent/skills/syncfusion-react-charts/SKILL.md` → ChartComponent for dashboards and analytics
- `.agent/skills/syncfusion-react-dropdowns/SKILL.md` → DropDownListComponent for filters and selections
- `.agent/skills/syncfusion-react-inputs/SKILL.md` → TextBoxComponent for forms and data entry
- `.agent/skills/syncfusion-react-datepicker/SKILL.md` → DatePickerComponent for date selection


**Component Skill Repository Structure:**
- **Location:** `.agent/skills/<component-name>/` directory
- **SKILL.md (Primary Skill File)** — < 5000 tokens
  ```markdown
---
name: syncfusion-react-grid
description: Implements Syncfusion React Grid component for feature-rich data tables and grids. Use this when working with data display, sorting, filtering, grouping, aggregates, editing, or exporting. This skill covers grid configuration, CRUD operations, virtual scrolling or infinite scrolling,  hierarchy grids, state persistence, and advanced data management features for data-intensive applications.
metadata:
  author: "Syncfusion Inc"
  version: "33.1.44"
---
  ```
  - Component overview, capabilities summary
  - Required and optional props (quick reference)
  - Event handlers (list)
  - Alternative components
  - Reference index (pointers to detailed docs)
- **references/ (Progressive Disclosure)** — Loaded on-demand
  - `data-binding.md` — Detailed data binding patterns
  - `filtering.md` — Filtering implementation guide
  - `editing.md` — Edit mode and CRUD operations
  - `performance.md` — Virtual scrolling, lazy loading
  - `getting-started.md` — Quick start example
  - Examples, patterns, advanced configurations

**Skill Versioning:**
- All component skills include a version in SKILL.md header
- **No minimum agent version requirement** (all skills recently launched, compatible with current agent)
- Version advisory only; agent reads all versions without breaking


## Syncfusion React Component Skills

| Skill Name | Description |
|---|---|
| syncfusion-react-grid | Feature-rich data table component with sorting, filtering, pagination, grouping, and editing |
| syncfusion-react-common | Shared utilities and base components for Syncfusion React library |
| syncfusion-react-themes | Theme configuration and styling system for Syncfusion components |
| syncfusion-react-scheduler | Calendar and event scheduling component with appointment management |
| syncfusion-react-gantt-chart | Project timeline and Gantt chart visualization component |
| syncfusion-react-charts | Data visualization charts component (bar, line, area, etc.) |
| syncfusion-react-license | License management and validation for Syncfusion components |
| syncfusion-react-rich-text-editor | Rich text editing component with formatting and content management |
| syncfusion-react-speech-to-text | Voice input and speech recognition component |
| syncfusion-react-accumulation-chart | Pie, doughnut, and accumulation chart visualization component |
| syncfusion-react-chat-ui | Chat interface and messaging component |
| syncfusion-react-treegrid | Hierarchical data table component with tree-like structure |
| syncfusion-react-blockeditor | Block-based content editor component |
| syncfusion-react-ai-assistview | AI assistant UI view component |
| syncfusion-react-barcode | Barcode and QR code generation component |
| syncfusion-react-query-builder | Dynamic query builder component for filter construction |
| syncfusion-react-pivot-table | Pivot table component for data analysis and aggregation |
| syncfusion-react-tabs | Tab navigation and content switching component |
| syncfusion-react-file-manager | File browser and manager component |
| syncfusion-react-treeview | Tree view component for hierarchical data display |
| syncfusion-react-image-editor | Image editing and manipulation component |
| syncfusion-react-inline-ai-assist | Inline AI assistance component |
| syncfusion-react-ribbon | Ribbon menu and toolbar component |
| syncfusion-react-diagram | Diagram and flowchart drawing component |
| syncfusion-react-dropdown-tree | Dropdown component with tree data structure |
| syncfusion-react-maps | Geographic map visualization component |
| syncfusion-react-dialog | Modal dialog and popup component |
| syncfusion-react-dropdownlist | Dropdown list selection component |
| syncfusion-react-calendar | Calendar component for date selection and display |
| syncfusion-react-data-manager | Data service and management component |
| syncfusion-react-datetimepicker | Date and time picker component |
| syncfusion-react-kanban | Kanban board component for task management |
| syncfusion-react-daterangepicker | Date range selection component |
| syncfusion-react-datepicker | Date picker component for single date selection |
| syncfusion-react-timepicker | Time picker component for time selection |
| syncfusion-react-autocomplete | Autocomplete and typeahead input component |
| syncfusion-react-combobox | Combo box component for dropdown selection with search |
| syncfusion-react-list-box | List box component for multi-select options |
| syncfusion-react-uploader | File upload component with drag-and-drop support |
| syncfusion-react-numerictextbox | Numeric input component with validation |
| syncfusion-react-textbox | Text input component for form entry |
| syncfusion-react-mention | Mention/tagging component for user references |
| syncfusion-react-multiselect | Multi-select dropdown component |
| syncfusion-react-notifications | Toast and notification component |
| syncfusion-react-3d-chart | 3D data visualization charts component |
| syncfusion-react-sidebar | Sidebar navigation panel component |
| syncfusion-react-treemaps | Treemap visualization component |
| syncfusion-react-bullet-chart | Bullet chart comparison visualization component |
| syncfusion-react-timeline | Timeline component for sequential event display |
| syncfusion-react-progress-bar | Progress bar component for task completion display |
| syncfusion-react-stock-chart | Stock market data visualization component |
| syncfusion-react-circular-gauge | Circular gauge and speedometer component |
| syncfusion-react-linear-gauge | Linear gauge component for value measurement |
| syncfusion-react-markdown-converter | Markdown to HTML conversion component |
| syncfusion-react-range-navigator | Range navigator for timeline data selection |
| syncfusion-react-buttons | Button component library and variations |
| syncfusion-react-appbar | Application bar header component |
| syncfusion-react-dropdowns | Dropdown components collection |
| syncfusion-react-splitter | Splitter layout component for resizable panes |
| syncfusion-react-carousel | Carousel and image slider component |
| syncfusion-react-dashboard-layout | Dashboard layout component with widget management |
| syncfusion-react-inputs | Input controls collection (textbox, spinner, etc.) |
| syncfusion-react-breadcrumb | Breadcrumb navigation component |
| syncfusion-react-popups | Popup and tooltip component |
| syncfusion-react-stepper | Stepper component for multi-step workflows |
| syncfusion-react-smithchart | Smith chart visualization component |
| syncfusion-react-heatmap | Heatmap data visualization component |
| syncfusion-react-sankey | Sankey diagram visualization component |
| syncfusion-react-3d-circular-chart | 3D circular chart visualization component |
