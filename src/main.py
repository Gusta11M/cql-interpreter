from lexer import lexer
from parser import parser
from interpreter_eval import InterpreterEval
import sys
from pathlib import Path
import os

def interpret(data):
    """
    Parses the input data and evaluates the resulting AST.
    If the AST is a list of statements, each one is evaluated in sequence.
    """
    ast = parser.parse(data, lexer=lexer)
    if isinstance(ast, list):
        for stmt in ast:
            InterpreterEval.evaluate(stmt)
    else:
        InterpreterEval.evaluate(ast)

def main():
    """
    Entry point of the interpreter.
    Operates in two modes:
    - File mode: Reads and executes .cql files from the input directory or full path.
    - Interactive mode: Accepts user input line-by-line and executes when a complete command is entered.
    """
    if len(sys.argv) > 1:
        # File mode
        file_path = Path(sys.argv[1])

        # If only the filename is given, assume it's in the input folder
        if file_path.parent == Path('.'):
            file_path = Path("..") / "input" / file_path

            if not file_path.exists():
                print(f"Error: file '{file_path}' does not exist.")
                sys.exit(1)

            if file_path.suffix == '.cql':
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = f.read()
                interpret(data)
            else:
                print("Invalid file format. File must have a .cql extension.")
                sys.exit(1)
        else:
            if not file_path.exists():
                print(f"Error: file '{file_path}' does not exist.")
                sys.exit(1)

            if file_path.suffix == '.cql':
                with open(sys.argv[1], 'r', encoding='utf-8') as f:
                    data = f.read()
                interpret(data)
    else:
        # Interactive mode
        print("Interactive mode (enter commands and finish with CTRL+D or CTRL+Z):")
        buffer = ""
        try:
            while True:
                line = input(">>> ")
                if line.strip().endswith(";"):
                    buffer += line + "\n"
                    interpret(buffer)
                    buffer = ""
                else:
                    print("\nMissing semicolon ';' to terminate the command.\n")
        except EOFError:
            print("\nExiting interactive mode.")

if __name__ == "__main__":
    main()