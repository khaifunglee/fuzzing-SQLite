# Implement your grammar here in the `grammar` variable.
# You may define additional functions, e.g. for generators.
# You may not import any other modules written by yourself.
# That is, your entire implementation must be in `grammar.py`
# and `fuzzer.py`.

grammar = {
    "<start>": ["<statements>"],
    "<statements>": ["<statement>;", "<statements> <statement>;"],

    # SQL statements
    "<statement>": [
        "<create_table>",
        "<drop_table>",
        "<drop_view>",
        "<drop_index>",
        "<insert_stmt>",
        "<update_stmt>",
        "<delete_stmt>",
        "<select_stmt>",
        "<begin_transaction>",
        "<commit>",
        "<rollback>",
        "<create_index>",
        "<create_view>",
        "<create_trigger>",
        "<create_virtual_table>",
        "<alter_table>",
        "<explain_stmt>",
        "<simple_function_invocation>",
        "<pragma_stmt>",
        "<reindex_stmt>",
        "<savepoint_stmt>",
        "<release_stmt>",
        "<rollback_to_savepoint>",
        "<upsert_stmt>",
        "<window_function_invocation>",
        "<comment_syntax>",
        "<nested_select>",
        "<subquery>",
        "<json_functions>",
        "<drop_trigger>",
        "<aggregate_function_invocation>",
        "<vacuum_stmt>",
        "<analyze_stmt>",
        "<attach_stmt>",
        # "<detach_stmt>"
    ],

    # ALTER TABLE statements
    "<alter_table>": [
        "ALTER TABLE <table_name> RENAME TO <table_name>;", 
        "ALTER TABLE <table_name> RENAME COLUMN <column_name> TO <column_name>;", 
        "ALTER TABLE <table_name> ADD COLUMN <column_def>;", 
        "ALTER TABLE <table_name> DROP COLUMN <column_name>;"
    ],

    # CREATE INDEX statements
    "<create_index>": [
        "CREATE INDEX [IF NOT EXISTS] <index_name> ON <table_name> (<indexed_columns>) [WHERE <condition>]",
        "CREATE UNIQUE INDEX [IF NOT EXISTS] <index_name> ON <table_name> (<indexed_columns>) [WHERE <condition>]"
    ],

    # CREATE TABLE, VIEW, TRIGGER, VIRTUAL TABLE statements
    "<create_table>": ["CREATE TABLE IF NOT EXISTS <table_name> (<table_columns_def>);"],
    "<create_view>": ["CREATE VIEW <view_name> AS SELECT <select_list> FROM <table_references> WHERE <condition>;"],
    "<create_trigger>": ["CREATE TRIGGER <trigger_name> AFTER INSERT ON <table_name> FOR EACH ROW BEGIN <statement>; END;"],
    "<create_virtual_table>": [
        "CREATE VIRTUAL TABLE [IF NOT EXISTS] <table_name> USING <module_name> (<module_arguments>)"
    ],

    # DROP statements
    "<drop_table>": ["DROP TABLE IF EXISTS <table_name>"],
    "<drop_view>": ["DROP VIEW IF EXISTS <view_name>;"],
    "<drop_trigger>": ["DROP TRIGGER IF EXISTS <trigger_name>"],
    "<drop_index>": ["DROP INDEX IF EXISTS <index_name>"],

    # INSERT, UPDATE, DELETE statements
    "<insert_stmt>": ["INSERT INTO <table_name> (<column_names>) VALUES (<values>);"],
    "<update_stmt>": ["UPDATE <table_name> SET <assignments> [WHERE <condition>]"],
    "<delete_stmt>": ["DELETE FROM <table_name> [WHERE <condition>]"],

    # SELECT statement
    "<select_stmt>": ["SELECT <select_list> FROM <table_references> WHERE <condition>;"],

    # Transaction control
    "<begin_transaction>": ["BEGIN [TRANSACTION]"],
    "<commit>": ["COMMIT [TRANSACTION]"],
    "<rollback>": ["ROLLBACK [TRANSACTION]"],

    # EXPLAIN statements
    "<explain_stmt>": ["EXPLAIN <sql_stmt>", "EXPLAIN QUERY PLAN <sql_stmt>"],

    # Function invocation
    "<simple_function_invocation>": ["<function_name>(<expr>)"],

    # PRAGMA statement
    "<pragma_stmt>": [
        "PRAGMA <pragma_name> = <pragma_value>", 
        "PRAGMA <pragma_name>(<pragma_value>)", 
        "PRAGMA <pragma_name>"
    ],

    # REINDEX statement
    "<reindex_stmt>": [
        "REINDEX <collation_name>;", 
        "REINDEX <table_name>;", 
        "REINDEX <index_name>;"
    ],

    # Savepoints and transactions
    "<savepoint_stmt>": ["SAVEPOINT <savepoint_name>"],
    "<release_stmt>": ["RELEASE SAVEPOINT <savepoint_name>"],
    "<rollback_to_savepoint>": ["ROLLBACK TRANSACTION TO SAVEPOINT <savepoint_name>"],

    # UPSERT statement
    "<upsert_stmt>": [
        "ON CONFLICT (<columns>) DO NOTHING", 
        "ON CONFLICT (<columns>) DO UPDATE SET <column_name> = <expr> [WHERE <expr>]"
    ],

    # Window function invocation
    "<window_function_invocation>": [
        "<window_func>(<expr>) OVER <window_defn>",
        "<window_func>(<expr> <filter_clause>) OVER <window_defn>"
    ],

    # Comments
    "<comment_syntax>": [
        "-- <anything_except_newline>",
        "/* <anything_except_*/> */"
    ],

    # Additional SQL statements
    "<vacuum_stmt>": ["VACUUM"],
    "<analyze_stmt>": ["ANALYZE [<table_name>]"],
    "<attach_stmt>": ["ATTACH DATABASE '<filename>' AS <schema_name>"],
    # "<detach_stmt>": ["DETACH DATABASE <schema_name>"],

    # Aggregate functions
    "<aggregate_function_invocation>": [
        "COUNT(<expr>)", "SUM(<expr>)", "AVG(<expr>)", "MIN(<expr>)", "MAX(<expr>)"
    ],

    # Nested SELECT queries
    "<nested_select>": [
        "SELECT <select_list> FROM <table_references> WHERE <condition> AND <subquery>",
        "SELECT <select_list> FROM (<nested_select>) WHERE <condition>"
    ],

    # Subquery
    "<subquery>": ["(SELECT <select_list> FROM <table_name> WHERE <condition>)"],

    # JSON functions
    "<json_functions>": [
        "JSON(<arguments>)",
        "JSON_ARRAY(<arguments>)",
        "JSON_OBJECT(<arguments>)",
        "JSON_QUOTE(<expr>)",
        "JSON_EXTRACT(<expr>, <path>)",
        "JSON_SET(<expr>, <path>, <value>)",
        "JSON_REPLACE(<expr>, <path>, <value>)",
        "JSON_REMOVE(<expr>, <path>)",
        "JSON_INSERT(<expr>, <path>, <value>)",
        "JSON_TYPE(<expr>)",
        "JSON_VALID(<expr>)",
        "JSON_ARRAY_LENGTH(<expr>)",
        "JSON_TREE(<expr>)"
    ],

    # Schema name
    "<schema_name>": ["main", "temp", "<identifier>"],

    # Table columns definition
    "<table_columns_def>": ["<table_column_def>", "<table_column_def>, <table_columns_def>"],
    "<table_column_def>": ["<column_name> <data_type> <column_constraints>"],

    # Column definitions
    "<column_def>": ["<column_name> <data_type> <column_constraints>"],

    # Column constraints
    "<column_constraints>": ["", "<column_constraint><column_constraints>"],
    "<column_constraint>": [
        "NOT NULL", "UNIQUE", "PRIMARY KEY", "CHECK (<condition>)", 
        "DEFAULT <value>", "COLLATE <collation_name>", "GENERATED ALWAYS AS (<expression>)"
    ],

    # Data types
    "<data_type>": ["INTEGER", "REAL", "TEXT", "BLOB", "NUMERIC", "BOOLEAN", "DATE", "TIME", "DATETIME"],

    # Table name, column name, etc.
    "<table_name>": ["<identifier>"],
    "<view_name>": ["<identifier>"],
    "<column_name>": ["<identifier>"],
    "<indexed_columns>": ["<column_name>", "<column_name>, <indexed_columns>"],
    "<columns>": ["<column_name>", "<column_name>, <columns>"],

    # Literals, values, and expressions
    "<expr>": ["<literal>", "<identifier>", "<expr> <operator> <expr>"],
    "<literal>": ["<number>", "'<string>'", "NULL"],
    "<operator>": ["+", "-", "*", "/", "%", "AND", "OR", "=", "!=" , "<", "<=", ">", ">="],

    # Function calls
    "<function_name>": ["ABS", "LENGTH", "SUBSTR", "RANDOM", "UPPER", "LOWER", "COUNT", "SUM", "AVG", "MIN", "MAX"],

    # Arguments and identifiers
    "<arguments>": ["<value>", "<arguments>, <value>"],
    "<value>": ["<literal>", "'<string>'"],
    "<identifier>": ["<letter>", "<identifier><letter_or_digit>"],
    "<letter_or_digit>": ["<letter>", "<digit>"],
    "<string>": ["<char>", "<char><string>"],
    "<char>": ["<letter>", "<digit>", "<special_char>"],
    "<number>": ["<integer>", "<float>"],
    "<integer>": ["<digit>", "<digit><integer>"],
    "<float>": ["<integer>.<integer>"],

    # Special characters and digits
    "<special_char>": ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", ",", ".", "<", ">", "/", "?", "`", "~"],
    "<letter>": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                 "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],

    # Adding missing definitions
    "<index_name>": ["<identifier>"],
    "<expression>": ["<expr>"],
    "<condition>": ["<expr>", "<expr> <operator> <expr>"],
    "<path>": ["<string>"],
    "<savepoint_name>": ["<identifier>"],
    "<sql_stmt>": ["<statement>"],
    "<column_names>": ["<column_name>", "<column_name>, <column_names>"],
    "<module_arguments>": ["<value>", "<value>, <module_arguments>"],
    "<values>": ["<value>", "<value>, <values>"],
    "<pragma_name>": ["<identifier>"],
    "<select_list>": ["<column_name>", "<column_name>, <select_list>"],
    "<trigger_name>": ["<identifier>"],
    "<anything_except_newline>": ["<char>", "<char><anything_except_newline>"],
    "<module_name>": ["<identifier>"],
    "<collation_name>": ["<identifier>"],
    "<table_references>": ["<table_name>", "<table_name>, <table_references>"],
    "<window_func>": ["<function_name>"],
    "<window_defn>": ["PARTITION BY <columns>", "ORDER BY <columns>"],
    "<filter_clause>": ["FILTER (WHERE <condition>)"],
    "<assignments>": ["<column_name> = <expr>", "<column_name> = <expr>, <assignments>"],
    "<pragma_value>": ["<value>"],
    "<filename>": ["'<string>'"],
    "<anything_except_*/>": ["<char>", "<char><anything_except_*/>"],
}
