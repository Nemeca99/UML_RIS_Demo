# UML Calculator User Guide (Community Edition)

## Overview

UML Calculator is a versatile mathematical tool that combines standard mathematical operations with UML diagram generation capabilities. This Community Edition demonstrates the core functionality while providing practical utility for everyday calculations and visualizations.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/uml-calculator.git
```

2. Install dependencies:
```bash
cd uml-calculator
pip install -r requirements.txt
```

## Running the Calculator

### Interactive Mode

Launch the calculator in interactive mode:

```bash
python calculator.py
```

Or on Windows, use the batch file:
```bash
run_calculator.bat
```

### Command Mode

You can also run specific commands directly:

```bash
python calculator.py calc "2 + 3*5"
python calculator.py ris_calc 6 3
python calculator.py plot "x^2 - 4" -10,10
```

## Available Commands

### Basic Math Operations

- `calc <expression>` - Evaluate a mathematical expression
  Example: `calc "3*x^2 - 5*x + 2"`

- `solve <equation>` - Solve an equation for x
  Example: `solve "x^2 - 4 = 0"`

### RIS Operations

- `ris_calc <a> <b>` - Perform RIS calculation on two integers
  Example: `ris_calc 6 3`

### Visualization

- `plot <expression> [x_range]` - Plot a mathematical function
  Example: `plot "sin(x)" -3.14,3.14`

### UML Generation

- `uml <command>` - Generate UML diagram
  Available commands:
  - `rules` - Generate RIS rules diagram
  - `equation` - Generate equation diagram
  - `function` - Generate function diagram

### Utility Commands

- `theme <name>` - Change UI theme (default, dark, light)
- `history` - Show calculation history
- `history json file.json` - Export history to JSON
- `history csv file.csv` - Export history to CSV
- `about` - Display information about UML Calculator
- `help` - Show help information

## Batch Processing

For processing multiple calculations at once, use the batch processor:

```bash
python process_batch.py sample_data/sample_batch.csv results.json
```

The input CSV should have the following format:
```csv
operation,expression,a,b
calc,2 + 3*5,,
ris,,6,3
```

## Community vs Enterprise Features

This Community Edition includes:

- Standard mathematical operations
- Basic UML diagram generation
- Terminal-based user interface
- Limited RIS operations

The Enterprise Edition additionally includes:

- Complete RIS implementation with advanced mathematical foundations
- Advanced UML generation capabilities
- Integration with external systems
- Custom extensions and support

## Getting Help

If you encounter any issues or have questions about the Community Edition, please open an issue in the GitHub repository.

For inquiries about the Enterprise Edition, please contact:
[your contact information]
