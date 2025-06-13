# CQL Interpreter — A Custom Query Language Processor

## Overview

This project implements a fully functional interpreter for a Custom Query Language (CQL), designed to perform SQL-like operations on CSV data files. Developed in Python, the interpreter supports commands such as import, export, select, join, and procedural programming constructs, enabling flexible data manipulation and querying.

The interpreter includes:
- Lexical analysis and parsing via PLY (Python Lex-Yacc).
- Abstract Syntax Tree (AST) evaluation with support for custom procedures.
- CSV file loading, saving, and transformation.
- Command-line interface with both batch file execution and interactive modes.

## Features

- Import and export CSV tables.
- Select columns with filtering conditions and limits.
- Create new tables from select queries or join operations.
- Define and call custom procedures.
- Interactive shell for real-time query execution.
- Error handling and syntax validation.

## Technologies Used

- Python 3.x
- PLY (Python Lex-Yacc) for lexical analysis and parsing
- Standard Python libraries: csv, ast, pathlib, os, sys

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Installation

1. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

- To run the interpreter in file mode:

```bash
python main.py path/to/your/script.cql
# or
python main.py script.cql # if script.cql is inside input folder
```

- To use the interactive mode, simply run:

```bash
python main.py
```

Then enter commands terminated with a semicolon (;), calling files .csv bettween (" "), with the full path or just the name, if the file is inside data folder.

## Project Structure

```bash
cql-interpreter/
├── data/                   # Samples CSV files
│   ├── observations.csv        
│   ├── stations.csv   
│   └── weather_stations.csv      
├── input/                  # Examples of CQL input scripts
│   ├── example_a.cql         
│   ├── example_b.cql    
│   ├── example_c.cql
│   ├── example_d.cql     
│   └── input.cql           
├── src/         
│   ├── lexer.py            # Lexical analyzer
│   ├── parser.py           # Grammar and parser
│   ├── interpreter_eval.py # AST evaluator
│   ├── csv_manager.py      # CSV management
│   └── main.py             # Entry point
├── .gitignore
├── README.md
└── requirements.txt
```

## Collaboration and Contributions

This project was developed as a group assignment in an academic environment.
Please note that although the repository is hosted under the GitHub account [Gusta11M](https://github.com/Gusta11M), the contributions registered under the GitHub account [GustaM11](https://github.com/GustaM11) were made by me (the same person), using a separate school-associated account.

## Skills Demonstrated

- Language design and implementation (custom query language).
- Lexical analysis and parsing with PLY.
- AST construction and evaluation.
- File I/O and data manipulation in Python.
- Procedural programming and control flow implementation.
- Development of command-line interfaces (CLI).
- Team collaboration and version control practices.

## License

[MIT License](LICENSE)

---
