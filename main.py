from lexer import lexer
from parser import parser
from interpreter_eval import InterpreterEval
import sys
from pathlib import Path
import os

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
        ficheiro = Path(sys.argv[1])
        if(ficheiro.parent == Path('.')):

            ficheiro = Path("input") / ficheiro

            if not ficheiro.exists():
                print(f"Erro: o ficheiro '{ficheiro}' não existe.")
                sys.exit(1)

            if(ficheiro.suffix == '.cql'):
                with open(ficheiro, 'r', encoding='utf-8') as f:
                    data = f.read()
                interpretar(data)
            else:
                print("Formato de ficheiro inválido. O ficheiro deve ter a extensão .cql")
                sys.exit(1)

        else:
            if not ficheiro.exists():
                print(f"Erro: o ficheiro '{ficheiro}' não existe.")
                sys.exit(1)

            if(ficheiro.suffix == '.cql'):
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
