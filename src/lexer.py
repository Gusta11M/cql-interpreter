# lexer.py
import ply.lex as lex

# Reserved keywords in the language
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

# List of token names recognized by the lexer
tokens = ['ID', 'NUMBER', 'STRING', 'LE', 'GE', 'NE'] + list(reserved.values())

# Single-character literals (operators, delimiters)
literals = ['(', ')', '=', '<', '>', ';', ',', '*', '.']

# Token definitions using regular expressions
t_LE = r'<='            # Less than or equal
t_GE = r'>='            # Greater than or equal
t_NE = r'<>'            # Not equal

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Check if the identifier is a reserved word
    t.type = reserved.get(t.value.lower(), 'ID')
    return t

def t_STRING(t):
    r'"([^\"]|\\")*"'
    # Remove the surrounding quotes
    t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r'-?\d+(\.\d+)?'
    # Convert string to float if it contains a decimal point, otherwise to int
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Single-line comment: ignore everything after '--' on the line
def t_COMMENT_LINE(t):
    r'\-\-.*'
    pass  # Ignore the comment

# Multi-line comment: ignore everything between '{-' and '-}'
def t_COMMENT_BLOCK(t):
    r'\{\-([\s\S]*?)\-\}'
    pass  # Ignore the comment block

# Characters to ignore (spaces, tabs, carriage returns)
t_ignore = ' \t\r'

# Track line numbers for error reporting
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling for invalid characters
def t_error(t):
    print(f"Invalid character: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()