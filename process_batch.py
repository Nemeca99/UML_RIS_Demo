"""
Sample batch processor for UML Calculator

This script demonstrates how to process a batch of calculations
"""
import sys
import os
import csv
import json

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from core.ris_community import ris
from core.symbolic import evaluate_expression

def process_batch_file(file_path, output_path=None):
    """Process a CSV file with batch calculations"""
    results = []
    
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                operation = row.get('operation', '').strip().lower()
                
                if operation == 'calc':
                    expression = row.get('expression', '')
                    try:
                        result = evaluate_expression(expression)
                        status = 'success'
                    except Exception as e:
                        result = str(e)
                        status = 'error'
                        
                elif operation == 'ris':
                    try:
                        a = int(row.get('a', 0))
                        b = int(row.get('b', 0))
                        result = ris(a, b)
                        status = 'success'
                    except Exception as e:
                        result = str(e)
                        status = 'error'
                else:
                    result = f"Unknown operation: {operation}"
                    status = 'error'
                    
                results.append({
                    'operation': operation,
                    'inputs': {k: v for k, v in row.items() if k != 'operation'},
                    'result': result,
                    'status': status
                })
        
        # Output results
        if output_path:
            with open(output_path, 'w') as f:
                json.dump(results, f, indent=2)
        
        return results
    
    except Exception as e:
        print(f"Error processing batch file: {str(e)}")
        return []

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python process_batch.py <input_csv> [output_json]")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    results = process_batch_file(input_file, output_file)
    
    # Print summary
    success_count = sum(1 for r in results if r['status'] == 'success')
    error_count = sum(1 for r in results if r['status'] == 'error')
    
    print(f"Processed {len(results)} operations")
    print(f"Success: {success_count}")
    print(f"Errors: {error_count}")
    
    if output_file:
        print(f"Results saved to {output_file}")
