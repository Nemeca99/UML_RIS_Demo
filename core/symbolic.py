"""
Mathematical expression handling with symbolic support for UML Calculator - Community Edition
"""
import sympy
import numpy as np
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
from sympy import symbols, sympify, Eq, solve

def evaluate_expression(expr_str, x_value=None):
    """
    Evaluate a mathematical expression
    
    Args:
        expr_str: String expression like "3*x^2 - 5*x + 2"
        x_value: Value to substitute for x if present
        
    Returns:
        Evaluated result
    """
    # Clean up the expression
    expr_str = expr_str.replace("^", "**")  # Replace ^ with ** for exponentiation
    
    # Handle equation with = sign
    if "=" in expr_str:
        sides = expr_str.split("=", 1)
        if len(sides) == 2 and sides[1].strip():
            # This is an equation to solve
            left = sides[0].strip()
            right = sides[1].strip()
            return solve_equation(f"{left} - ({right})")
        else:
            # Just evaluate the left side
            expr_str = sides[0].strip()
    
    # Define symbols
    x, y, z = symbols('x y z')
    
    # Configure sympy parser with implicit multiplication
    transformations = standard_transformations + (implicit_multiplication_application,)
    
    try:
        # Parse the expression
        expr = parse_expr(expr_str, transformations=transformations)
        
        # Substitute x value if provided
        if x_value is not None:
            expr = expr.subs(x, x_value)
        
        # If expression still contains symbols and no x_value was provided
        if expr.free_symbols and x_value is None:
            return expr
        
        # Convert to float for numerical result
        return float(expr)
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {str(e)}")

def generate_plot_data(expr_str, x_min=-10, x_max=10, points=500):
    """
    Generate x,y values for plotting a mathematical expression
    
    Args:
        expr_str: String expression in terms of x
        x_min, x_max: Range for x values
        points: Number of points to generate
        
    Returns:
        (x_values, y_values) as numpy arrays
    """
    # Clean up the expression
    expr_str = expr_str.replace("^", "**")  # Replace ^ with ** for exponentiation
    
    # Define symbol
    x = symbols('x')
    
    # Configure sympy parser with implicit multiplication
    transformations = standard_transformations + (implicit_multiplication_application,)
    
    try:
        # Parse the expression
        expr = parse_expr(expr_str, transformations=transformations)
        
        # Convert sympy expression to numpy function
        f = sympy.lambdify(x, expr, "numpy")
        
        # Generate x values
        x_values = np.linspace(x_min, x_max, points)
        
        # Calculate y values with handling for potential numerical errors
        try:
            y_values = f(x_values)
            
            # Replace infinity and NaN with None for plotting
            y_values = np.where(np.isfinite(y_values), y_values, np.nan)
            
            return x_values, y_values
        except Exception as e:
            raise ValueError(f"Error calculating function values: {str(e)}")
    except Exception as e:
        raise ValueError(f"Error processing expression: {str(e)}")

def solve_equation(equation_str):
    """
    Solve an equation for x
    
    Args:
        equation_str: String equation like "x^2 - 4 = 0" or just "x^2 - 4" (= 0 implied)
        
    Returns:
        Solution(s) for x
    """
    # Clean up the equation
    equation_str = equation_str.replace("^", "**")  # Replace ^ with ** for exponentiation
    
    # Check if equation has = sign
    if "=" in equation_str:
        left, right = equation_str.split("=", 1)
        equation_str = f"{left.strip()} - ({right.strip()})"
    
    # Define symbol
    x = symbols('x')
    
    # Configure sympy parser with implicit multiplication
    transformations = standard_transformations + (implicit_multiplication_application,)
    
    try:
        # Parse the expression
        expr = parse_expr(equation_str, transformations=transformations)
        
        # Solve the equation
        solutions = solve(expr, x)
        
        # Convert complex solutions to strings if needed
        processed_solutions = []
        for sol in solutions:
            try:
                processed_solutions.append(float(sol))
            except (TypeError, ValueError):
                # Keep as sympy expression if cannot convert to float
                processed_solutions.append(str(sol))
        
        if len(processed_solutions) == 1:
            return processed_solutions[0]
        return processed_solutions
    except Exception as e:
        raise ValueError(f"Error solving equation: {str(e)}")
