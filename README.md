# ⚙️ CQL Interpreter — A Custom Query Language Processor

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PLY](https://img.shields.io/badge/PLY-Lex%20%26%20Yacc-green?style=for-the-badge)
![CSV](https://img.shields.io/badge/Data-CSV-blue?style=for-the-badge&logo=filezilla&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-Command%20Line-ff69b4?style=for-the-badge)
![MIT License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)

---

## 📄 Overview

This project implements a fully functional interpreter for a **Custom Query Language (CQL)**, designed to perform SQL-like operations on `.csv` data files.  
Developed in Python, it supports commands such as:

- `IMPORT`, `EXPORT`, `SELECT`, `JOIN`
- Custom procedure definitions
- Batch or interactive execution

Includes:

- Lexical analysis and parsing via **PLY**
- AST-based evaluation
- CLI for scripting and REPL
- Robust error handling and syntax validation

---

## ✨ Features

✅ Import and export CSV tables  
✅ Select columns with filtering and limits  
✅ JOIN multiple CSV tables  
✅ Create and call **custom procedures**  
✅ Interactive mode for on-the-fly testing  
✅ Full error feedback with line reporting

---

## 🛠️ Technologies Used

- 🐍 Python 3.x
- 🧠 [PLY (Python Lex-Yacc)](https://www.dabeaz.com/ply/)
- 📁 Python CSV, AST, Pathlib, OS, Sys (standard libraries)

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.6+
- pip (Python package installer)

### 📦 Installation

1. Create and activate a virtual environment (recommended):

**Linux/macOS** 
```bash
python -m venv venv  
source venv/bin/activate  
```
**Windows**  
```bash
python -m venv venv  
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```
---

## 🧪 Usage

➡️ To run the interpreter with a CQL file:
```bash
python main.py path/to/your/script.cql  
# or 
python main.py script.cql *(if file is in `input/` folder)*
```

➡️ To enter interactive mode:

```bash
python main.py
```
Then enter CQL commands ending with `;`, referencing `.csv` files in quotes (`"filename.csv"`).  
If the file is in the `data/` folder, you can just use the name.

---

## 📁 Project Structure

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

---

## 🤝 Collaboration & Contributions

This project was developed in a **group setting** as part of an academic course.

ℹ️ Although the repository is hosted under [Gusta11M](https://github.com/Gusta11M), the commits from [GustaM11](https://github.com/GustaM11) represent the same person — using a separate school GitHub account.

---

## 🧠 Skills Demonstrated

- 🏗️ Language design (custom query language)  
- 📚 Lexical parsing and grammar with PLY  
- 🌲 AST construction and evaluation  
- 🧪 File I/O and CSV data manipulation  
- 🧵 Procedural control flow (e.g., loops, blocks)  
- 🖥️ Command-line interface (CLI) development  
- 🤝 Git/GitHub collaboration in team-based environment

---

## 📄 License

This project is licensed under the [MIT License](LICENSE)

---
