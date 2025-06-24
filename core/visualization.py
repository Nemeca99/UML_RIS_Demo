"""
Data visualization tools for UML Calculator - Community Edition
"""
import matplotlib.pyplot as plt
import numpy as np

def create_plot(x_values, y_values, title="Function Plot", output_file=None):
    """
    Create a plot from x,y data and save to a file
    
    Args:
        x_values: Array of x values
        y_values: Array of y values
        title: Title for the plot
        output_file: Path to save the plot image
        
    Returns:
        Path to generated image file
    """
    plt.figure(figsize=(10, 6))
    
    # Filter out NaN values for plotting
    mask = ~np.isnan(y_values)
    plt.plot(x_values[mask], y_values[mask])
    
    plt.title(title)
    plt.grid(True)
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Add some margins to the plot
    plt.margins(0.1)
    
    # Save to file if path is provided
    if output_file:
        plt.savefig(output_file)
        plt.close()
        return output_file
    
    # If no file path is provided, create a temporary file
    import tempfile
    import os
    
    temp_file = os.path.join(tempfile.gettempdir(), "uml_calc_plot.png")
    plt.savefig(temp_file)
    plt.close()
    
    return temp_file
