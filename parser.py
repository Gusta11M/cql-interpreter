#parser.py
import ply.yacc as yacc
from lexer import tokens


# Gramatica de Parsing
def p_programa(p):
    '''programa : instrucoes'''
    p[0] = p[1]

def p_instrucoes(p):
    '''instrucoes : instrucoes instrucao
                  | instrucao'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_instrucao(p):
    '''instrucao : inst_import ';'
                | inst_export ';'
                | inst_discard ';'
                | inst_rename ';'
                | inst_print ';'
                | inst_select ';'
                | inst_create ';'
                | inst_procedure
                | inst_call ';' '''
    p[0] = p[1]

def p_inst_import(p):
    '''inst_import : IMPORT TABLE ID FROM STRING'''
    p[0] = {'op': p[1], 'args': [p[3], p[5]]}

def p_inst_export(p):
    '''inst_export : EXPORT TABLE ID AS STRING'''
    p[0] = {'op': p[1], 'args': [p[3], p[5]]}

def p_inst_discard(p):
    '''inst_discard : DISCARD TABLE ID'''
    p[0] = {'op': p[1], 'args': [p[3]]}

def p_inst_rename(p):
    '''inst_rename : RENAME TABLE ID ID'''
    p[0] = {'op': p[1], 'args': [p[3], p[4]]}

def p_inst_print(p):
    '''inst_print : PRINT TABLE ID'''
    p[0] = {'op': p[1], 'args': [p[3]]}

def p_inst_select(p):
    '''inst_select : SELECT list_select FROM ID opt_where opt_limit'''
    p[0] = {'op': p[1], 'args': [p[2], p[4], p[5], p[6]]}

def p_list_select(p):
    '''list_select : '*'
                  | list_column'''
    p[0] = [p[1]] if p[1] == '*' else p[1]

def p_list_column(p):
    '''list_column : list_column ',' ID
                  | ID'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_opt_where(p):
    '''opt_where : WHERE condicao
                | empty'''
    p[0] = p[2] if len(p) > 2 else None

def p_opt_limit(p):
    '''opt_limit : LIMIT NUMBER
                | empty'''
    p[0] = p[2] if len(p) > 2 else None

def p_condicao(p):
    '''condicao : ID op NUMBER
               | condicao AND condicao'''


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
    p[0] = p[1]

def p_inst_create(p):
    '''inst_create : CREATE TABLE ID inst_select
                   | CREATE TABLE ID FROM ID JOIN ID USING '(' ID ')' '''
    if len(p) == 5:
        p[0] = {'op': 'CREATE', 'args': [p[3], p[4]]}
    else:
        p[0] = {'op': 'CREATE', 'args': [p[3], p[5], p[7], p[10]]}


def p_inst_join(p):
    '''inst_join : JOIN ID USING '(' ID ')' '''
    p[0] = {'op': p[1], 'args': [p[2], p[4]]}

def p_inst_procedure(p):
    '''inst_procedure : PROCEDURE ID DO instrucoes END'''
    p[0] = {'op': p[1], 'args': [p[2], p[4]]}

def p_inst_call(p):
    '''inst_call : CALL ID'''
    p[0] = {'op': p[1], 'args': [p[2]]}

def p_empty(p):
    '''empty :'''
    p[0] = None

def p_error(p):
    if p:
        print(f"Erro de sintaxe perto de {p.value}")
    else:
        print("Erro de sintaxe no fim da entrada")

parser = yacc.yacc()
