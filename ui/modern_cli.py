"""
UML Calculator Community Edition - Modern CLI
A beautiful command-line interface built with Rich and Typer
"""
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.syntax import Syntax
from rich.theme import Theme
import json
import csv
import datetime
import sys
import os
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
from pathlib import Path

# Add path to core modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.ris_community import ris, ris_explain
try:
    # Import symbolic and visualization modules if available
    from core.symbolic import evaluate_expression, generate_plot_data, solve_equation
    from core.visualization import create_plot
    SYMBOLIC_AVAILABLE = True
except ImportError:
    SYMBOLIC_AVAILABLE = False

try:
    # Import UML generation module if available
    from core.uml_generator import UMLGenerator
    UML_GENERATOR = UMLGenerator()
    UML_AVAILABLE = True
except ImportError:
    UML_AVAILABLE = False

# Define UML Calculator theme
UML_THEMES = {
    "default": {
        "info": "blue",
        "warning": "yellow",
        "danger": "red bold",
        "success": "green",
        "title": "blue bold",
        "heading": "cyan bold",
        "key": "magenta",
        "value": "green",
        "ris_op": "bright_green",
        "ris_result": "bright_cyan"
    },
    "dark": {
        "info": "cyan",
        "warning": "yellow",
        "danger": "red bold",
        "success": "bright_green",
        "title": "cyan bold",
        "heading": "blue bold",
        "key": "bright_magenta",
        "value": "bright_green",
        "ris_op": "green",
        "ris_result": "cyan"
    },
    "light": {
        "info": "blue",
        "warning": "yellow",
        "danger": "red",
        "success": "green",
        "title": "blue bold",
        "heading": "cyan",
        "key": "magenta",
        "value": "green",
        "ris_op": "green",
        "ris_result": "blue"
    }
}

# Initialize CLI components
app = typer.Typer()
console = Console(theme=Theme(UML_THEMES["default"]))
current_theme = "default"
calculation_history = []

def change_theme(theme_name):
    """Change the console theme"""
    global console, current_theme
    if theme_name in UML_THEMES:
        console = Console(theme=Theme(UML_THEMES[theme_name]))
        current_theme = theme_name
        return True
    return False

def add_to_history(operation, inputs, result):
    """Add calculation to history"""
    calculation_history.append({
        "timestamp": datetime.datetime.now().isoformat(),
        "operation": operation,
        "inputs": inputs,
        "result": result
    })

@app.command()
def calc(expression: str):
    """Calculate the result of a mathematical expression"""
    try:
        if not SYMBOLIC_AVAILABLE:
            console.print("[danger]Symbolic calculation module not available in Community Edition[/danger]")
            return
            
        result = evaluate_expression(expression)
        console.print(Panel(f"[key]Expression:[/key] [value]{expression}[/value]"))
        console.print(f"[key]Result:[/key] [ris_result]{result}[/ris_result]")
        
        add_to_history("calc", {"expression": expression}, result)
    except Exception as e:
        console.print(f"[danger]Error:[/danger] {str(e)}")

@app.command()
def ris_calc(a: int, b: int):
    """Perform RIS calculation on two integers (Community Edition)"""
    try:
        result, explanation = ris_explain(a, b)
        
        console.print(Panel(f"[key]RIS Operation:[/key] RIS({a}, {b})"))
        console.print(f"[key]Result:[/key] [ris_result]{result}[/ris_result]")
        console.print(Panel(explanation, title="Explanation"))
        
        add_to_history("ris", {"a": a, "b": b}, result)
    except Exception as e:
        console.print(f"[danger]Error:[/danger] {str(e)}")

@app.command()
def plot(expression: str, x_range: str = "-10,10"):
    """Plot a mathematical function (simplified version)"""
    try:
        if not SYMBOLIC_AVAILABLE:
            console.print("[danger]Plotting module not available in Community Edition[/danger]")
            return
            
        try:
            x_min, x_max = map(float, x_range.split(','))
        except ValueError:
            console.print("[danger]Invalid x_range format. Use 'min,max' format.[/danger]")
            return
            
        x_values, y_values = generate_plot_data(expression, x_min, x_max)
        
        # Create a temporary file for the plot
        temp_dir = Path("./temp")
        temp_dir.mkdir(exist_ok=True)
        plot_file = temp_dir / f"plot_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        
        create_plot(x_values, y_values, expression, str(plot_file))
        
        console.print(Panel(f"[key]Expression:[/key] [value]{expression}[/value]"))
        console.print(f"[success]Plot saved to:[/success] {plot_file}")
        console.print("\n[info]For better visualization, check the saved PNG file[/info]\n")
        
        # Simple ASCII visualization
        console.print("[heading]ASCII Plot Preview:[/heading]")
        height = 10
        width = 50
        plot_ascii(x_values, y_values, width, height)
        
        add_to_history("plot", {"expression": expression, "x_range": x_range}, str(plot_file))
    except Exception as e:
        console.print(f"[danger]Error:[/danger] {str(e)}")

def plot_ascii(x, y, width=50, height=10):
    """Create a simple ASCII plot"""
    if len(x) < 2 or len(y) < 2:
        console.print("[danger]Not enough points to plot[/danger]")
        return
        
    # Filter out inf and nan values
    valid_indices = [i for i, val in enumerate(y) if not (abs(val) == float('inf') or val != val)]
    if not valid_indices:
        console.print("[danger]No valid points to plot[/danger]")
        return
        
    x_valid = [x[i] for i in valid_indices]
    y_valid = [y[i] for i in valid_indices]
    
    y_min = min(y_valid)
    y_max = max(y_valid)
    
    if y_min == y_max:
        y_min -= 1
        y_max += 1
    
    plot = [[' ' for _ in range(width)] for _ in range(height)]
    
    for i in range(len(x_valid)):
        x_pos = int((x_valid[i] - min(x_valid)) / (max(x_valid) - min(x_valid)) * (width - 1)) if max(x_valid) != min(x_valid) else width // 2
        y_pos = height - 1 - int((y_valid[i] - y_min) / (y_max - y_min) * (height - 1)) if y_max != y_min else height // 2
        
        if 0 <= x_pos < width and 0 <= y_pos < height:
            plot[y_pos][x_pos] = '*'
    
    # Draw axes
    x_axis = height - 1 - int((0 - y_min) / (y_max - y_min) * (height - 1)) if y_min < 0 < y_max else None
    y_axis = int((0 - min(x_valid)) / (max(x_valid) - min(x_valid)) * (width - 1)) if min(x_valid) < 0 < max(x_valid) else None
    
    if x_axis is not None and 0 <= x_axis < height:
        for i in range(width):
            if plot[x_axis][i] == ' ':
                plot[x_axis][i] = '-'
    
    if y_axis is not None and 0 <= y_axis < width:
        for i in range(height):
            if plot[i][y_axis] == ' ':
                plot[i][y_axis] = '|'
    
    # Print the plot
    for row in plot:
        console.print(''.join(row))
    
    # Print axes labels
    console.print(f"y-range: [{y_min:.2f}, {y_max:.2f}]")
    console.print(f"x-range: [{min(x_valid):.2f}, {max(x_valid):.2f}]")

@app.command()
def solve(equation: str):
    """Solve an equation for x (Community Edition)"""
    try:
        if not SYMBOLIC_AVAILABLE:
            console.print("[danger]Equation solving module not available in Community Edition[/danger]")
            return
            
        solution = solve_equation(equation)
        
        console.print(Panel(f"[key]Equation:[/key] [value]{equation}[/value]"))
        if isinstance(solution, list):
            console.print("[key]Solutions:[/key]")
            for i, sol in enumerate(solution):
                console.print(f"  x_{i+1} = [ris_result]{sol}[/ris_result]")
        else:
            console.print(f"[key]Solution:[/key] x = [ris_result]{solution}[/ris_result]")
        
        add_to_history("solve", {"equation": equation}, solution)
    except Exception as e:
        console.print(f"[danger]Error:[/danger] {str(e)}")

@app.command()
def uml(command: str = typer.Argument(..., help="UML command: rules, equation, or function")):
    """Generate UML diagram (Community Edition - limited functionality)"""
    try:
        if not UML_AVAILABLE:
            console.print("[danger]UML generation module not available in Community Edition[/danger]")
            return
            
        console.print(Panel(f"[heading]UML Generator - Community Edition[/heading]"))
        console.print("[info]This is a limited demonstration of UML capabilities.[/info]")
        console.print("[info]The Enterprise Edition includes full UML generation features.[/info]")
        
        if command == "rules":
            # Generate simple RIS rules diagram
            console.print("[key]Generating RIS Rules UML Diagram...[/key]")
            console.print("[info]Community Edition includes only basic rules visualization[/info]")
            # In a real implementation, this would call UML_GENERATOR
        elif command == "equation":
            # Generate sample equation diagram
            console.print("[key]Generating Equation UML Diagram...[/key]")
            console.print("[info]Sample equation representation in Community Edition[/info]")
            # In a real implementation, this would call UML_GENERATOR
        elif command == "function":
            # Generate sample function diagram
            console.print("[key]Generating Function UML Diagram...[/key]")
            console.print("[info]Sample function representation in Community Edition[/info]")
            # In a real implementation, this would call UML_GENERATOR
        else:
            console.print(f"[danger]Unknown UML command: {command}[/danger]")
            console.print("[info]Available commands: rules, equation, function[/info]")
    except Exception as e:
        console.print(f"[danger]Error:[/danger] {str(e)}")

@app.command()
def theme(name: str = typer.Argument(..., help="Theme name: default, dark, or light")):
    """Change the UI theme"""
    if change_theme(name):
        console.print(f"[success]Theme changed to: {name}[/success]")
    else:
        console.print(f"[danger]Theme '{name}' not found[/danger]")
        console.print(f"[info]Available themes: {', '.join(UML_THEMES.keys())}[/info]")

@app.command()
def history(export_format: str = None, filename: str = None):
    """Show calculation history with optional export"""
    if not calculation_history:
        console.print("[info]No calculations in history[/info]")
        return
        
    table = Table(title=f"Calculation History ({len(calculation_history)} items)")
    table.add_column("#", style="dim")
    table.add_column("Timestamp", style="dim")
    table.add_column("Operation", style="key")
    table.add_column("Inputs", style="info")
    table.add_column("Result", style="ris_result")
    
    for i, calc in enumerate(calculation_history):
        inputs_str = ", ".join(f"{k}={v}" for k, v in calc["inputs"].items())
        table.add_row(
            str(i+1),
            calc["timestamp"].split("T")[1][:8],
            calc["operation"],
            inputs_str,
            str(calc["result"])
        )
    
    console.print(table)
    
    if export_format:
        if not filename:
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"uml_calc_history_{timestamp}.{export_format}"
            
        try:
            if export_format.lower() == 'json':
                with open(filename, 'w') as f:
                    json.dump(calculation_history, f, indent=2)
            elif export_format.lower() == 'csv':
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['timestamp', 'operation', 'inputs', 'result'])
                    for calc in calculation_history:
                        writer.writerow([
                            calc['timestamp'],
                            calc['operation'],
                            json.dumps(calc['inputs']),
                            calc['result']
                        ])
            else:
                console.print(f"[danger]Unsupported export format: {export_format}[/danger]")
                return
                
            console.print(f"[success]History exported to {filename}[/success]")
        except Exception as e:
            console.print(f"[danger]Export error: {str(e)}[/danger]")

@app.command()
def about():
    """Display information about UML Calculator Community Edition"""
    console.print(Panel.fit(
        Text.from_markup("""
[title]UML Calculator Community Edition[/title]

A modern calculator that combines standard mathematics with UML diagram generation.
This Community Edition demonstrates the core capabilities of UML Calculator.

[heading]Features:[/heading]
- Standard mathematical operations
- Basic function plotting
- Simple UML diagram generation
- Terminal-based user interface with rich formatting
- Limited set of RIS operations

[heading]Enterprise Edition Features:[/heading]
- Complete Recursive Integration System (RIS)
- Advanced UML generation capabilities
- Custom diagram styling and export options
- Integration with external systems

For licensing inquiries about the Enterprise Edition, please contact:
[info]your-email@example.com[/info]
        """),
        title="About UML Calculator",
        border_style="blue"
    ))

@app.command()
def help():
    """Show help information"""
    console.print(Panel.fit(
        Text.from_markup("""
[heading]Available Commands:[/heading]

[key]calc[/key] [value]<expression>[/value] - Evaluate a mathematical expression
[key]ris_calc[/key] [value]<a> <b>[/value] - Perform RIS calculation on two integers
[key]plot[/key] [value]<expression> [x_range][/value] - Plot a mathematical function
[key]solve[/key] [value]<equation>[/value] - Solve an equation for x
[key]uml[/key] [value]<command>[/value] - Generate UML diagram (rules, equation, function)
[key]theme[/key] [value]<name>[/value] - Change UI theme (default, dark, light)
[key]history[/key] [value][export_format] [filename][/value] - Show calculation history
[key]about[/key] - Display information about UML Calculator
[key]help[/key] - Show this help information

[heading]Examples:[/heading]
> [info]calc "2 + 3*5"[/info]
> [info]ris_calc 6 3[/info]
> [info]plot "x^2 - 4" -5,5[/info]
> [info]solve "x^2 - 4 = 0"[/info]
> [info]uml rules[/info]
> [info]theme dark[/info]
> [info]history json history.json[/info]
        """),
        title="UML Calculator Help",
        border_style="blue"
    ))

@app.callback()
def main():
    """UML Calculator - Community Edition"""
    pass

if __name__ == "__main__":
    console.print(Panel.fit(
        "[title]UML Calculator Community Edition[/title]",
        border_style="blue"
    ))
    app()
