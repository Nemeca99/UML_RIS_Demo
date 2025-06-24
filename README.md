# UML Calculator (Community Edition)

A modern calculator that combines standard mathematics with UML diagram generation capabilities, designed for both practical calculations and visualizing mathematical concepts.

## Features

**This Community Edition includes:**

- 🧮 Standard mathematical operations and equation solving
- 📊 Basic function plotting with nice visualization
- 📐 Simplified Recursive Integration System (RIS) operations
- 📈 Terminal-based user interface with rich formatting
- 📋 Calculation history with export capabilities
- 🎨 Multiple UI themes
- 📝 Basic UML diagram generation for mathematical concepts

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/uml-calculator.git
cd uml-calculator

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

```bash
# Start the interactive calculator
python calculator.py

# Or on Windows, simply use:
run_calculator.bat
```

### Direct Command Examples

```bash
# Evaluate a mathematical expression
python calculator.py calc "2 + 3*5"

# Perform an RIS calculation
python calculator.py ris_calc 6 3

# Plot a function
python calculator.py plot "x^2 + 2*x - 3" -10,10

# Solve an equation
python calculator.py solve "x^2 - 4 = 0"

# Generate a simple UML diagram
python calculator.py uml rules
```

## Example Outputs

### Standard Calculations

```
>>> calc "3*x^2 - 5*x + 2"
Expression: 3*x^2 - 5*x + 2
Result: 24.0
```

### RIS Operations

```
>>> ris_calc 6 3
RIS Operation: RIS(6, 3)
Result: 2

Explanation:
When a is divisible by b, RIS performs Division: 6 ÷ 3 = 2

Note: This is a simplified version. The Enterprise Edition includes the complete 
Recursive Integration System with advanced mathematical foundations.
```

### UML Diagrams

The calculator can generate UML diagrams to visualize mathematical operations:

![Sample UML Diagram](docs/images/sample_uml.png)

*Note: Advanced UML diagram features are available in the Enterprise Edition.*

## Available Commands

- `calc <expression>` - Evaluate a mathematical expression
- `ris_calc <a> <b>` - Perform RIS calculation on two integers
- `plot <expression> [x_range]` - Plot a mathematical function
- `solve <equation>` - Solve an equation for x
- `uml <command>` - Generate UML diagram (rules, equation, function)
- `theme <name>` - Change UI theme (default, dark, light)
- `history [export_format] [filename]` - Show calculation history
- `about` - Display information about UML Calculator
- `help` - Show help information

## Enterprise Edition

The Enterprise Edition includes additional features:

- ✨ Complete Recursive Integration System (RIS) with advanced mathematical foundations
- 📊 Advanced UML generation capabilities for complex mathematical structures
- 🔗 Full symbolic integration with advanced equation solving
- 📋 Custom diagram styling and export options
- 🔄 Integration with external systems
- 🛠️ Technical support and custom extensions

For licensing or partnership inquiries about the Enterprise Edition, please contact:
[your contact information]

## License

This Community Edition is licensed under MIT License with Commons Clause. Please see the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions that enhance the community features. Please open an issue or pull request if you'd like to contribute.

*Note: Contributions to core mathematical algorithms or advanced UML generation features may be subject to separate licensing terms.*
