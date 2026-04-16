# UI Builder Skill - Scripts

Python scripts implementing the 9-stage UI generation pipeline.

## Structure

```
scripts/
├── orchestrator.py          # Main entry point - coordinates all stages
├── context.py               # UIBuilderContext state schema
├── stage_1_intent.py        # Intent analysis & classification
├── stage_2_detection.py     # Project framework detection
├── stage_3_layout.py        # Layout variant selection
├── stage_4_components.py    # Syncfusion component mapping
├── stage_5_preview.py       # Preview generation
├── stage_6_codegen.py       # React code generation
├── stage_7_validation.py    # Web standards validation
├── stage_8_dependencies.py  # npm package management
└── stage_9_insertion.py     # File insertion & build verification
```

## Requirements

- Python 3.8+
- Node.js 18+ (for target React project)
- npm/yarn/pnpm

## Usage

### Basic Component Generation

```bash
python orchestrator.py \
  --request "Create a login form with remember me" \
  --project-dir ./my-react-app
```

### Preview Only (Dry Run)

```bash
python orchestrator.py \
  --request "Build a data table with sorting" \
  --project-dir ~/projects/dashboard \
  --dry-run
```

### With Verbose Output

```bash
python orchestrator.py \
  --request "Generate a registration form" \
  --project-dir . \
  --verbose
```

## Output

The orchestrator outputs JSON to **stdout**:

```json
{
  "status": "completed",
  "intent": "generate_component",
  "component_type": "form/login",
  "framework": "nextjs-app",
  "selected_variant": "login-variant-b",
  "generated_files": [
    "app/components/LoginForm/LoginForm.tsx",
    "app/components/LoginForm/LoginForm.module.css",
    "app/components/LoginForm/index.ts"
  ],
  "inserted_files": [...],
  "validation_issues": [],
  "required_packages": [
    "@syncfusion/ej2-base",
    "@syncfusion/ej2-react-inputs",
    "@syncfusion/ej2-react-buttons"
  ],
  "error": null
}
```

Progress and errors are printed to **stderr**.

## Testing Individual Stages

Each stage can be tested independently:

```bash
# Test intent classification
python stage_1_intent.py

# Test project detection
python stage_2_detection.py ./my-project

# Test layout selection
python stage_3_layout.py

# Test component mapping
python stage_4_components.py

# Test dependency management
python stage_8_dependencies.py ./my-project
```

## Exit Codes

- `0` - Success (component generated)
- `1` - Failure (error occurred)

## Environment

These scripts are designed to be called by:
- AI agents (via SKILL.md)
- CI/CD pipelines
- Developer command line
- IDE extensions

## Notes

- **Stage 1-7**: Pure computation (no side effects)
- **Stage 8**: Reads package.json (no installation in test mode)
- **Stage 9**: Writes files to disk (use --dry-run to preview)

## See Also

- [Complete Specification](../references/REFERENCE.md)
- [Stage Workflows](../references/STAGES.md)
- [Component Mapping](../references/SYNCFUSION-MAPPING.md)
- [Web Standards](../references/WEB-STANDARDS.md)
