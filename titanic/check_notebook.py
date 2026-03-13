import json
import ast
import sys

notebook_path = '/home/aniket-deshkar/PycharmProjects/Path2AI/titanic/titanic_ml.ipynb'

try:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
except Exception as e:
    print(f"Error reading notebook: {e}")
    sys.exit(1)

for i, cell in enumerate(nb.get('cells', [])):
    if cell.get('cell_type') == 'code':
        source_lines = cell.get('source', [])
        # filtered_source = "".join([line for line in source_lines if not line.strip().startswith('%')])
        # Handle lines that start with % by commenting them out to preserve line numbers
        filtered_lines = []
        for line in source_lines:
            if line.strip().startswith('%'):
                filtered_lines.append('# ' + line)
            else:
                filtered_lines.append(line)
        
        source = "".join(filtered_lines)
        
        try:
            ast.parse(source)
        except SyntaxError as e:
            print(f"Syntax error in cell index {i} (ID: {cell.get('id', 'unknown')}):")
            print(f"  Line {e.lineno}: {e.msg}")
            print(f"  Source fragment: {e.text}")
            print("-" * 20)
            print(source)
            print("-" * 20)
