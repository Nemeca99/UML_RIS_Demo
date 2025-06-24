"""
UML Calculator - Community Edition
Core implementation with limited functionality
"""
import os
import sys

def ris(a, b, context=None):
    """
    Simplified RIS implementation for the Community Edition
    
    This is a demonstration version with limited rule implementation.
    Enterprise version contains the complete Recursive Integration System.
    
    Args:
        a, b: Input values
        context: Optional context parameters
    
    Returns:
        Result of RIS operation
    """
    # Special case: if one of the values is zero, return addition
    if a == 0 or b == 0:
        return a + b
        
    # If values are equal, multiply them
    if a == b:
        return a * b
        
    # If a is divisible by b with no remainder, divide them
    if a % b == 0 and a > b:
        return a / b
        
    # Simple case for demonstration purposes
    if a > b and (a % 3 == 0 or b % 3 == 0):
        return a * b
        
    # Default behavior
    return a + b

def ris_explain(a, b, context=None):
    """
    Generate explanation for RIS operation (limited version)
    
    Args:
        a, b: Input values
        context: Optional context parameters
    
    Returns:
        (result, explanation) tuple
    """
    result = ris(a, b, context)
    
    # Generate simple explanation
    if a == 0 or b == 0:
        explanation = f"When one value is zero, RIS performs Addition: {a} + {b} = {result}"
    elif a == b:
        explanation = f"When values are equal, RIS performs Multiplication: {a} × {b} = {result}"
    elif a % b == 0 and a > b:
        explanation = f"When a is divisible by b, RIS performs Division: {a} ÷ {b} = {result}"
    elif a > b and (a % 3 == 0 or b % 3 == 0):
        explanation = f"Special case demonstration: {a} × {b} = {result}"
    else:
        explanation = f"Default operation is Addition: {a} + {b} = {result}"
    
    explanation += "\n\nNote: This is a simplified version. The Enterprise Edition includes the complete Recursive Integration System with advanced mathematical foundations."
    
    return result, explanation
