#lexer.py
import ply.lex as lex

# Lista de tokens
reserved = {
    'import': 'IMPORT',
    'export': 'EXPORT',
    'discard': 'DISCARD',
    'rename': 'RENAME',
    'print': 'PRINT',
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',
    'limit': 'LIMIT',
    'create': 'CREATE',
    'table': 'TABLE',
    'join': 'JOIN',
    'using': 'USING',
    'procedure': 'PROCEDURE',
    'call': 'CALL',
    'do': 'DO',
    'end': 'END',
    'and': 'AND',
    'as': 'AS'
}

tokens = ['ID', 'NUMBER', 'STRING', 'LE', 'GE', 'NE'] + list(reserved.values())

literals = ['(', ')', '=', '<', '>', ';', ',', '*', '.']

t_LE = r'<='
t_GE = r'>='
t_NE = r'<>'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t
def t_STRING(t):
    r'"([^\"]|\\")*"'
    t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r'-?\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Comentários de uma linha (ignorar o resto da linha)
def t_COMMENT_LINE(t):
    r'\-\-.*'
    pass  # Simplesmente ignora

# Comentários de múltiplas linhas (ignorar tudo entre {- e -})
def t_COMMENT_BLOCK(t):
    r'\{\-([\s\S]*?)\-\}'
    pass  # Também apenas ignora


t_ignore = ' \t\r'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter inválido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
