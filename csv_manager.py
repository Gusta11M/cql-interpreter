#csv_manager.py
import csv
import ast

def load_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        columns = next(reader)  # Obtém a primeira linha como cabeçalhos
        columns = [col.strip() for col in columns]  # Remove espaços extras dos nomes das colunas
        rows = []

        for row in reader:
            # Ignora linhas de comentário (que começam por '#')
            if not row or row[0].strip().startswith('#'):
                continue
            # Ignora linhas vazias
            if all(cell.strip() == '' for cell in row):
                continue
            # Verifica se o número de colunas corresponde ao numero de colunas
            if len(row) != len(columns):
                continue
            rows.append([parse_value(cell.strip()) for cell in row])

        
    return {'columns': columns, 'rows': rows}

def save_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(data['columns'])
        for row in data['rows']:
            writer.writerow(row)

def parse_value(val):
    try:
        # Tenta interpretar como uma lista (coordenadas)
        if val.startswith('[') and val.endswith(']'):
            return ast.literal_eval(val)  # Converte para lista de floats
        # Tenta converter para float ou int
        if '.' in val:
            return float(val)
        return int(val)
    except (ValueError, SyntaxError):
        return val  # Retorna o valor como string caso não consiga converter
