# parser.py
import ply.yacc as yacc
from lexer import tokens

# Defining operator precedence
precedence = (
    ('left', 'AND'),
)

# Parsing Grammar Rules

def p_program(p):
    '''program : instructions'''
    # The root of the parsing tree: a program consists of instructions
    p[0] = p[1]

def p_instructions(p):
    '''instructions : instructions instruction
                    | instruction'''
    # An instructions list is either a single instruction or multiple instructions
    if len(p) == 3:
        p[0] = p[1] + [p[2]]  # Append instruction to the list
    else:
        p[0] = [p[1]]  # Single instruction becomes a list with one element

def p_instruction(p):
    '''instruction : inst_import ';'
                   | inst_export ';'
                   | inst_discard ';'
                   | inst_rename ';'
                   | inst_print ';'
                   | inst_select ';'
                   | inst_create ';'
                   | inst_procedure
                   | inst_call ';' '''
    # An instruction can be one of several commands, some ending with a semicolon
    p[0] = p[1]

def p_inst_import(p):
    '''inst_import : IMPORT TABLE ID FROM STRING'''
    # Import command: import a table with ID from a string source
    p[0] = {'op': p[1], 'args': [p[3], p[5]]}

def p_inst_export(p):
    '''inst_export : EXPORT TABLE ID AS STRING'''
    # Export command: export a table with ID as a string destination
    p[0] = {'op': p[1], 'args': [p[3], p[5]]}

def p_inst_discard(p):
    '''inst_discard : DISCARD TABLE ID'''
    # Discard command: discard a table with given ID
    p[0] = {'op': p[1], 'args': [p[3]]}

def p_inst_rename(p):
    '''inst_rename : RENAME TABLE ID ID'''
    # Rename command: rename a table from old ID to new ID
    p[0] = {'op': p[1], 'args': [p[3], p[4]]}

def p_inst_print(p):
    '''inst_print : PRINT TABLE ID'''
    # Print command: print a table by its ID
    p[0] = {'op': p[1], 'args': [p[3]]}

def p_inst_select(p):
    '''inst_select : SELECT list_select FROM ID opt_where opt_limit'''
    # Select command: select columns from a table, with optional WHERE and LIMIT clauses
    p[0] = {'op': p[1], 'args': [p[2], p[4], p[5], p[6]]}

def p_list_select(p):
    '''list_select : '*'
                   | list_column'''
    # List of columns to select: either all columns (*) or specific columns
    p[0] = [p[1]] if p[1] == '*' else p[1]

def p_list_column(p):
    '''list_column : list_column ',' ID
                   | ID'''
    # List of column IDs separated by commas
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_opt_where(p):
    '''opt_where : WHERE condition
                 | empty'''
    # Optional WHERE clause: either a condition or empty
    p[0] = p[2] if len(p) > 2 else None

def p_opt_limit(p):
    '''opt_limit : LIMIT NUMBER
                 | empty'''
    # Optional LIMIT clause: either a number or empty
    p[0] = p[2] if len(p) > 2 else None

def p_condition(p):
    '''condition : ID op NUMBER
                 | condition AND condition'''
    # Condition can be a simple comparison or an AND combination of conditions
    if p[2] == 'AND':
        p[0] = ('AND', p[1], p[3])
    else:
        p[0] = (p[1], p[2], p[3])

def p_op(p):
    '''op : "="
          | NE
          | "<"
          | ">"
          | LE
          | GE'''
    # Comparison operators supported
    p[0] = p[1]

def p_inst_create(p):
    '''inst_create : CREATE TABLE ID inst_select
                   | CREATE TABLE ID FROM ID JOIN ID USING '(' ID ')' '''
    # Create command can be either from a selection or from joining tables
    if len(p) == 5:
        p[0] = {'op': 'CREATE', 'args': [p[3], p[4]]}
    else:
        p[0] = {'op': 'CREATE', 'args': [p[3], p[5], p[7], p[10]]}

def p_inst_procedure(p):
    '''inst_procedure : PROCEDURE ID DO instructions END'''
    # Procedure definition: procedure name followed by instructions block
    p[0] = {'op': p[1], 'args': [p[2], p[4]]}

def p_inst_call(p):
    '''inst_call : CALL ID'''
    # Procedure call by ID
    p[0] = {'op': p[1], 'args': [p[2]]}

def p_empty(p):
    '''empty :'''
    # Empty production for optional rules
    p[0] = None

def p_error(p):
    # Error handling: print syntax error with context if available
    if p:
        print(f"Syntax error near {p.value}")
    else:
        print("Syntax error at end of input")

# Build the parser
parser = yacc.yacc()