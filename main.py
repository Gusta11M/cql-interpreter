from lexer import lexer
from parser import parser
from interpreter_eval import InterpreterEval
import sys

def interpretar(data):
    ast = parser.parse(data, lexer=lexer)
    if isinstance(ast, list):
        for stmt in ast:
            InterpreterEval.evaluate(stmt)
    else:
        InterpreterEval.evaluate(ast)

def main():
    if len(sys.argv) > 1:
        # Modo com ficheiro
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            data = f.read()
        interpretar(data)
    else:
        # Modo interativo
        print("Modo interativo (escreve comandos e termina com CTRL+D ou CTRL+Z):")
        buffer = ""
        try:
            while True:
                line = input(">>> ")
                if line.strip().endswith(";"):
                    buffer += line + "\n"
                    interpretar(buffer)
                    buffer = ""
                else:
                    print("\n; Não encontrado \n")
                    #buffer += line + "\n"
        except EOFError:
            print("\nFim do modo interativo.")

if __name__ == "__main__":
    main()
