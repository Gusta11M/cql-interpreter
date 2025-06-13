import csv_manager as csvm

# Global dictionaries to store tables and procedures
tables = {}
procedures = {}

class InterpreterEval:
    # Map operators to their respective static methods
    operators = {
        'PRINT': lambda args: InterpreterEval._print_table(args[0]),
        'IMPORT': lambda args: InterpreterEval._import_table(args[0], args[1]),
        'EXPORT': lambda args: InterpreterEval._export_table(args[0], args[1]),
        'DISCARD': lambda args: InterpreterEval._discard_table(args[0]),
        'RENAME': lambda args: InterpreterEval._rename_table(args[0], args[1]),
        'SELECT': lambda args: InterpreterEval._select(args[0], args[1], args[2], args[3]),
        'CREATE': lambda args: InterpreterEval._create(args),
        'PROCEDURE': lambda args: InterpreterEval._define_procedure(args[0], args[1]),
        'CALL': lambda args: InterpreterEval._call_procedure(args[0]),
    }

    @staticmethod
    def evaluate(ast):
        # Evaluate an abstract syntax tree (AST) node
        if isinstance(ast, dict):
            op = ast['op']

            # For CREATE, do not evaluate args recursively
            if op == 'CREATE':
                return InterpreterEval.operators[op](ast['args'])

            # Evaluate arguments recursively if they are dicts (AST nodes), else pass as is
            args = [InterpreterEval.evaluate(a) if isinstance(a, dict) else a for a in ast['args']]

            if op in InterpreterEval.operators:
                return InterpreterEval.operators[op](args)
            else:
                raise Exception(f"Unsupported operator: {op}")
        else:
            return ast

    @staticmethod
    def _print_table(tablename):
        # Print the table columns and rows if the table exists
        if tablename in tables:
            data = tables[tablename]
            print(','.join(data['columns']))
            for row in data['rows']:
                print(','.join(map(str, row)))
        else:
            print(f"Table {tablename} not found.")

    @staticmethod
    def _import_table(name, filename):
        # Import a CSV file into a table
        tables[name] = csvm.load_csv(filename)

    @staticmethod
    def _export_table(name, filename):
        # Export a table to a CSV file if it exists
        if name in tables:
            csvm.save_csv(tables[name], filename)
        else:
            print(f"Table {name} not found for export.")

    @staticmethod
    def _discard_table(name):
        # Remove a table from storage if it exists
        if name in tables:
            del tables[name]

    @staticmethod
    def _rename_table(oldname, newname):
        # Rename a table if the old name exists
        if oldname in tables:
            tables[newname] = tables.pop(oldname)
        else:
            print(f"Table {oldname} not found for renaming.")

    @staticmethod
    def _select(columns, table, condition, limit):
        # Select columns from a table with optional condition and limit
        if table not in tables:
            print(f"Table {table} not found.")
            return

        data = tables[table]
        cols = data['columns']
        # Determine which column indices to include in the result
        idxs = list(range(len(cols))) if columns == ['*'] else [cols.index(c) for c in columns]

        result = []
        for row in data['rows']:
            if InterpreterEval._check_condition(row, cols, condition):
                result.append([row[i] for i in idxs])
            if limit and len(result) >= limit:
                break

        # Print the resulting selected columns and rows
        print(','.join([cols[i] for i in idxs]))
        for r in result:
            print(','.join(map(str, r)))

    @staticmethod
    def _check_condition(row, cols, cond):
        # Evaluate a condition on a given row
        if not cond:
            return True
        if isinstance(cond, tuple):
            if cond[0] == 'AND':
                return (InterpreterEval._check_condition(row, cols, cond[1]) and
                        InterpreterEval._check_condition(row, cols, cond[2]))
            col, op, val = cond
            value = row[cols.index(col)]
            if op == '=': return value == val
            if op == '<>': return value != val
            if op == '<': return value < val
            if op == '>': return value > val
            if op == '<=': return value <= val
            if op == '>=': return value >= val
        return False

    @staticmethod
    def _create(args):
        table_name = args[0]

        if len(args) == 2:
            # args[1] is a SELECT AST
            return InterpreterEval._create_from_select(table_name, args[1])
        elif len(args) == 4:
            # args: [table_name, t1, t2, column]
            return InterpreterEval._create_from_join(table_name, args[1], args[2], args[3])
        else:
            raise Exception(f"Unknown CREATE format: {args}")

    @staticmethod
    def _create_from_select(name, select_ast):
        from copy import deepcopy
        columns, table, condition, limit = select_ast['args']
        data = tables[table]
        cols = data['columns']
        idxs = list(range(len(cols))) if columns == ['*'] else [cols.index(c) for c in columns]

        result = []
        for row in data['rows']:
            if InterpreterEval._check_condition(row, cols, condition):
                result.append([row[i] for i in idxs])
            if limit and len(result) >= limit:
                break

        # Store the result as a new table with copied data
        tables[name] = {'columns': [cols[i] for i in idxs], 'rows': deepcopy(result)}

    @staticmethod
    def _create_from_join(name, t1, t2, column):
        # Create a new table by joining two existing tables on a column
        if t1 not in tables or t2 not in tables:
            print(f"One or both tables {t1}, {t2} do not exist.")
            return

        table1 = tables[t1]
        table2 = tables[t2]
        try:
            idx1 = table1['columns'].index(column)
            idx2 = table2['columns'].index(column)
        except ValueError:
            print(f"Column {column} does not exist in one of the tables.")
            return

        # Combine columns from both tables, avoiding duplicate join column
        columns = table1['columns'] + [c for i, c in enumerate(table2['columns']) if i != idx2]
        rows = []
        for r1 in table1['rows']:
            for r2 in table2['rows']:
                if r1[idx1] == r2[idx2]:
                    rows.append(r1 + [v for i, v in enumerate(r2) if i != idx2])

        tables[name] = {'columns': columns, 'rows': rows}

    @staticmethod
    def _define_procedure(name, statements):
        # Define a procedure by saving its statements
        procedures[name] = statements

    @staticmethod
    def _call_procedure(name):
        # Execute the statements inside a procedure if it exists
        if name in procedures:
            for stmt in procedures[name]:
                InterpreterEval.evaluate(stmt)
        else:
            print(f"Procedure {name} not found.")