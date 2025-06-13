import csv
import ast
import os
from pathlib import Path

# Default folder to look for input CSV files
INPUT_FOLDER = "..\\data"

def load_csv(filename):
    filename = Path(filename)
    # If filename does not specify a folder, prepend the INPUT_FOLDER path
    if(filename.parent == Path('.')):
        filepath = os.path.join(INPUT_FOLDER, filename)
    else: 
        filepath = filename

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        columns = next(reader)  # Get the first row as column headers
        columns = [col.strip() for col in columns]  # Strip extra whitespace from column names
        rows = []

        for row in reader:
            # Skip comment lines (starting with '#')
            if not row or row[0].strip().startswith('#'):
                continue
            # Skip empty lines
            if all(cell.strip() == '' for cell in row):
                continue
            # Skip rows where the number of columns doesn't match the header count
            if len(row) != len(columns):
                continue

            # Parse each cell value in the row
            rows.append([parse_value(cell.strip()) for cell in row])

    return {'columns': columns, 'rows': rows}

def save_csv(data, filename):
    filename = Path(filename)
    # If filename does not specify a folder, prepend the INPUT_FOLDER path
    if(filename.parent == Path('.')):
        filepath = os.path.join(INPUT_FOLDER, filename)
    else: 
        filepath = filename

    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(data['columns'])  # Write the column headers
        for row in data['rows']:
            writer.writerow(row)  # Write each data row

def parse_value(val):
    try:
        # Try to interpret the value as a list (e.g., coordinates)
        if val.startswith('[') and val.endswith(']'):
            return ast.literal_eval(val)  # Convert to list of floats or ints
        # Try to convert to float or int
        if '.' in val:
            return float(val)
        return int(val)
    except (ValueError, SyntaxError):
        # Return as string if conversion fails
        return val