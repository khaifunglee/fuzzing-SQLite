# Implement your grammar here in the `grammar` variable.
# You may define additional functions, e.g. for generators.
# You may not import any other modules written by yourself.
# That is, your entire implementation must be in `grammar.py`
# and `fuzzer.py`.



grammar = {
    "<start>":["<statements>"],
    "<statements>":["<statement>;","<statements> <statement>;"],
    "<statement>":[
      "<create_table>",
      "<drop_table>",
      "<drop_view>",
      "<drop_index>",
      "<insert_stmt>",
      "<update_stmt>",
      "<delete_stmt>",
      # "<detach_stmt>",
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
      "<simple_function_invocation>" ,

      "<nested_select>",
      "<subquery>",
      "<json_functions>",
      # "<date_time_function>",
      "<drop_trigger>",
      "<virtual_table_stmt>",
      "<vacuum_stmt>"
      # "<truncate_table>",
      # "<rename_table>",
      # "<rename_column>",
      # "<add_column>",
      # "<modify_column>",
      # "<aggregate_function_invocation>"

    ],


    "<alter_table>": [
    "ALTER TABLE <table_name> RENAME TO <table_name>;", 
    "ALTER TABLE <table_name> RENAME COLUMN <column_name> TO <column_name>;", 
    "ALTER TABLE <table_name> ADD COLUMN <column_def>;", 
    "ALTER TABLE <table_name> DROP COLUMN <column_name>;"
    ],
  
    "<create_index>": [
      "CREATE INDEX [IF NOT EXISTS] <schema_name>.<index_name> ON <table_name> (<indexed_columns>) [WHERE <expr>]",
      "CREATE UNIQUE INDEX [IF NOT EXISTS] <schema_name>.<index_name> ON <table_name> (<indexed_columns>) [WHERE <expr>]"],
    "<create_table>": ["CREATE TABLE IF NOT EXISTS <table_name> (<table_columns_def>);"], 
  # "<create_table>": [
  #       "CREATE TABLE [IF NOT EXISTS] <schema_name>.<table_name> (<table_columns_def>, <table_constraints>);",
  #       "CREATE TEMPORARY TABLE [IF NOT EXISTS] <table_name> AS <select_stmt>;",
  #   ],
    "<create_view>": ["CREATE VIEW <table_name> AS SELECT <select_list> FROM <table_references> WHERE <condition>;"],
    "<create_trigger>": ["CREATE TRIGGER <trigger_name> AFTER INSERT ON <table_name> FOR EACH ROW BEGIN <statement>; END;"],
    "<create_virtual_table>": [
      "CREATE VIRTUAL TABLE [IF NOT EXISTS] <schema_name>.<table_name> USING <module_name> (<module_arguments>)",
      "CREATE VIRTUAL TABLE [IF NOT EXISTS] <table_name> USING <module_name> (<module_arguments>)"
    ],
    
    "<drop_table>": ["DROP TABLE IF EXISTS <table_name>"],
    "<drop_view>": ["DROP VIEW IF EXISTS <view_name>;"],
  
    "<insert_stmt>": ["INSERT INTO <table_name> (<column_names>) VALUES (<values>);"],
    "<update_stmt>":["UPDATE <table_name> SET <assignments> [WHERE <condition>"],
    "<delete_stmt>":["DELETE FROM <table_name> [WHERE <condition>]"],
    "<drop_trigger>": ["DROP TRIGGER IF EXISTS <trigger_name>"],
    "<drop_index>": ["DROP INDEX IF EXISTS <index_name>"],
    # "<detach_stmt>": [
    # "DETACH DATABASE <schema_name>;"],


    "<select_stmt>": ["SELECT <select_list> FROM <table_references> WHERE <condition>;"],
    "<begin_transaction>":["BRGIN [TRANSACTION]"],
    "<commit>":["COMMIT [TRANSACTION"],
    "<rollback>":["ROLLBACK [TRANSACTION]"],
    "<explain_stmt>": ["EXPLAIN <sql_stmt>", "EXPLAIN QUERY PLAN <sql_stmt>"],
    "<explain_stmt>": ["EXPLAIN <query_plan>", "EXPLAIN <sql_stmt>"],
    "<simple_function_invocation>": ["<function_name>(<expr>)"],
    "<pragma_stmt>": ["PRAGMA <schema_name>.<pragma_name> = <pragma_value>", 
                      "PRAGMA <schema_name>.<pragma_name>(<pragma_value>)", 
                      "PRAGMA <pragma_name> = <pragma_value>", 
                      "PRAGMA <pragma_name>(<pragma_value>)",
                      "PRAGMA <pragma_name>"],
    "<reindex_stmt>": [ "REINDEX <collation_name>;","REINDEX <schema_name>.<table_name>;", "REINDEX <schema_name>.<index_name>;"],
    "<savepoint_stmt>": ["SAVEPOINT <savepoint_name>"],
    "<release_stmt>": ["RELEASE SAVEPOINT <savepoint_name>"],
    "<rollback_to_savepoint>": ["ROLLBACK TRANSACTION TO SAVEPOINT <savepoint_name>"],
    "<upsert_stmt>": ["ON CONFLICT ( <columns> ) DO NOTHING", "ON CONFLICT ( <columns>  ) DO UPDATE SET <column_name> = <expr> [WHERE <expr>]" ],

    "<window_function_invocation>": [
      "<window_func>(<expr>) OVER <window_defn>",
      "<window_func>(<expr> <filter_clause>) OVER <window_defn>"
    ],
    "<comment_syntax>": [
      "-- <anything_except_newline>",
      "/* <anything_except_*/> */"],
    "<simple_function_invocation>": ["<function_name>(<expr>)"],

     "<nested_select>": [
         "(SELECT <select_list> FROM <table_references> WHERE <condition>)",
        "(SELECT <select_list> FROM (SELECT <select_list> FROM <table_name>) WHERE <condition>)"
    ],
    "<subquery>": ["(SELECT <select_list> FROM <table_name> WHERE <condition>)"],
  
    # "<hash_function_invocation>": [
    #     "SHA3Init(<input>);", "SHA3Update(<input>, <length>);", "SHA3Final(<output>);"
    # ],
  
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
    "<virtual_table_stmt>": [
      "CREATE VIRTUAL TABLE <table_name> USING fts5(<module_arguments>)",
      "CREATE VIRTUAL TABLE <table_name> USING json_each(<json_column>)",
    ],
    "<vacuum_stmt>": ["VACUUM"],


    # "<truncate_table>": ["TRUNCATE TABLE <table_name>;"],
    # "<rename_table>": ["RENAME TABLE <table_name> TO <table_name>;"],
    # "<rename_column>": [ "ALTER TABLE <table_name> RENAME COLUMN <column_name> TO <column_name>;"],
    # "<add_column>": [ "ALTER TABLE <table_name> ADD COLUMN <column_name> <data_type>;"],
    # "<modify_column>": [ "ALTER TABLE <table_name> MODIFY <column_name> <data_type>;"],

  
    # "<table_constraints>": ["<table_constraint>", "<table_constraint>, <table_constraints>"],
    # "<table_constraint>": [
    #     "PRIMARY KEY (<column_names>)",
    #     "FOREIGN KEY (<column_names>) REFERENCES <table_name>(<column_names>)",
    #     "UNIQUE (<column_names>)",
    #     "CHECK (<condition>)"
    # ],
    # "<table_options>": [
    #     "WITHOUT ROWID"
    # ],
  
    "<schema_name>": ["main", "temp", "<identifier>"],
    # "<index_or_table_name>": ["<identifier>"],
    
    "<table_columns_def>": ["<table_column_def>", "<table_column_def>, <table_columns_def>"],
    "<table_column_def>": ["<column_name><data_type><column_constraints>"],
    "<column_def>": ["<column_name> <data_type> <column_constraints>"],
    "<trigger_name>": ["<identifier>"],
  
    "<column_constraints>":["","<column_constraint><column_constraints>"],
    "<column_constraint>":["NOT NULL","UNIQUE","PRIMARY KEY","CHECK (<condition>)", "DEFAULT <value>", "COLLATE <collation_name>","GENERATED ALWAYS AS (<expression>)"],
    "<data_type>":["INTEGER","REAL","TEXT","BLOB","NUMERIC""BOOLEAN","DATE","TIME","DATETIME"],
    "<table_name>": ["<identifier>"],
    "<collation_name>": ["BINARY", "NOCASE", "RTRIM"],
    "<index_name>": ["<identifier>"],
    "<trigger_name>": ["trigger1", "trigger2", "trigger3"],
    "<module_name>": ["fts3", "fts4", "fts5", "rtree"],
    "<view_name>": ["<identifier>"],
    "<savepoint_name>": ["<identifier>"],

    "<path>": [
    "$", 
    "$.<identifier>", 
    "$[<number>]", 
    "$.<identifier>[<number>]", 
    "$.<identifier>.<identifier>"],
    # "<input>": ["'data_to_hash'", "'another_data'"],  
    # "<length>": ["32", "64", "128"], 
    # "<output>": ["'hashed_result'", "'final_hash'"],

  
    "<module_arguments>": ["<module_argument>", "<module_argument>, <module_arguments>"],
    "<module_argument>": ["<column_name> <data_type>", "tokenize=<literal>", "prefix=<integer>"],
    "<query_plan>": ["QUERY PLAN"],
     "<sql_stmt>": [
        "<alter_table>",
        "<begin_transaction>",
        "<commit>",
        "<create_table>",
        "<create_trigger>",
        "<create_view>",
        "<create_virtual_table>",
        "<delete_stmt>",
        "<drop_table>",
        "<select_stmt>"],

    "<window_defn>": [
      "(PARTITION BY <column_name> ORDER BY <ordering_term>)",
      "(PARTITION BY <column_name>)",
      "(ORDER BY <ordering_term>)",
      "(<window_name>)"],
    "<window_func>": ["ROW_NUMBER", "RANK", "DENSE_RANK", "NTILE", "LEAD", "LAG", "FIRST_VALUE", "LAST_VALUE"],
    "<window_name>": ["window1", "window2", "window3"], 
    "<filter_clause>": ["FILTER (WHERE <condition>)", ""],
    "<ordering_term>": ["<identifier> ASC", "<identifier> DESC"],

    "<anything_except_newline>": [
      "<char>", "<char><anything_except_newline>"],
    "<anything_except_*/>": [
      "<char>", "<char><anything_except_*/>"],
  
   
    "<expr>": ["<literal>", "<identifier>", "<expr> <operator> <expr>"],

    "<indexed_columns>": ["<column_name>", "<column_name>, <indexed_columns>"],
    "<columns>": ["<column_name>", "<column_name>, <columns>"],
    "<column_name>": ["<identifier>"],
    "<column_names>": ["<string>", "<string>, <column_names>"],
    "<values>": ["<value>", "<value>, <values>"],
    "<assignments>":["<assignment>","<assignments>,<assignment>"],
    "<assignment>":["<column_name>=<value>"],
    "<value>": ["<literal>", "'<function_call>'"],
    "<literal>":["<number>","'<string>'","NULL"],
   
    "<pragma_name>": ["cache_size", "encoding", "foreign_keys", "journal_mode", "locking_mode", "synchronous"], 
    "<pragma_value>": ["<signed_number>", "<name>", "<signed_literal>"],
    "<signed_number>": ["-<number>", "<number>"],
    "<name>": ["true", "false", "auto_vacuum", "FULL", "NORMAL", "OFF"],  
    "<signed_literal>": ["'<string>'"],

    "<json_column>": ["column_name", "$.<identifier>"],
    # "<filename>": ["'<string>'"],

    "<condition>": ["<expression>"],
    "<expression>":["<value>","expression><operator><expression>","(<expression>)"],
    "<operator>":["+","-","*","/","%","AND","OR","=","!=","<","<=",">",">="],
    "<select_list>":["*","<columns>"],
    "<table_references>":["<table_name>","<table_references>,<table_name>","<table_references> JOIN <table_name> ON <condition>"],
    "<function_call>":["<function_name>(<arguments>)"],
    "<function_name>":["ABS","LENGTH","SUBSTR","RANDOM","UPPER","LOWER","COUNT","SUM","AVG","MIN","MAX"],

  
    "<arguments>":["<value>","<arguments>,<value>"],
    "<identifier>":["<letter>","<identifier><letter_or_digit>"],
    "<letter_or_digit>":["<letter>","<digit>"],
    "<string>":["<char>","<char><string>"],
    "<char>":["<letter>","<digit>","<special_char>"],
    "<number>":["<integer>","<float>"],
    "<integer>":["<digit>","<digit><integer>"],
    "<float>":["<integer>.<integer>"],
  
    "<special_char>":["!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","{","|",";",":","''",",",".","<",">","/","?","`","~"],
    "<letter>": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
                "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

# grammar = {
#     "<start>": ["<statements>"],
#     "<statements>": ["<statement>;", "<statements> <statement>;"],

#     # SQL statements
#     "<statement>": [
#         "<create_table>",
#         "<drop_table>",
#         "<drop_view>",
#         "<drop_index>",
#         "<insert_stmt>",
#         "<update_stmt>",
#         "<delete_stmt>",
#         "<select_stmt>",
#         "<begin_transaction>",
#         "<commit>",
#         "<rollback>",
#         "<create_index>",
#         "<create_view>",
#         "<create_trigger>",
#         "<create_virtual_table>",
#         "<alter_table>",
#         "<explain_stmt>",
#         "<simple_function_invocation>",
#         "<pragma_stmt>",
#         "<reindex_stmt>",
#         "<savepoint_stmt>",
#         "<release_stmt>",
#         "<rollback_to_savepoint>",
#         "<upsert_stmt>",
#         "<window_function_invocation>",
#         "<comment_syntax>",
#         "<nested_select>",
#         "<subquery>",
#         "<json_functions>",
#         "<drop_trigger>",
#         "<aggregate_function_invocation>",
#         "<vacuum_stmt>",
#         "<analyze_stmt>",
#         "<attach_stmt>",
#         # "<detach_stmt>"
#     ],

#     # ALTER TABLE statements
#     "<alter_table>": [
#         "ALTER TABLE <table_name> RENAME TO <table_name>;", 
#         "ALTER TABLE <table_name> RENAME COLUMN <column_name> TO <column_name>;", 
#         "ALTER TABLE <table_name> ADD COLUMN <column_def>;", 
#         "ALTER TABLE <table_name> DROP COLUMN <column_name>;"
#     ],

#     # CREATE INDEX statements
#     "<create_index>": [
#         "CREATE INDEX [IF NOT EXISTS] <index_name> ON <table_name> (<indexed_columns>) [WHERE <condition>]",
#         "CREATE UNIQUE INDEX [IF NOT EXISTS] <index_name> ON <table_name> (<indexed_columns>) [WHERE <condition>]"
#     ],

#     # CREATE TABLE, VIEW, TRIGGER, VIRTUAL TABLE statements
#     "<create_table>": ["CREATE TABLE IF NOT EXISTS <table_name> (<table_columns_def>);"],
#     "<create_view>": ["CREATE VIEW <view_name> AS SELECT <select_list> FROM <table_references> WHERE <condition>;"],
#     "<create_trigger>": ["CREATE TRIGGER <trigger_name> AFTER INSERT ON <table_name> FOR EACH ROW BEGIN <statement>; END;"],
#     "<create_virtual_table>": [
#         "CREATE VIRTUAL TABLE [IF NOT EXISTS] <table_name> USING <module_name> (<module_arguments>)"
#     ],

#     # DROP statements
#     "<drop_table>": ["DROP TABLE IF EXISTS <table_name>"],
#     "<drop_view>": ["DROP VIEW IF EXISTS <view_name>;"],
#     "<drop_trigger>": ["DROP TRIGGER IF EXISTS <trigger_name>"],
#     "<drop_index>": ["DROP INDEX IF EXISTS <index_name>"],

#     # INSERT, UPDATE, DELETE statements
#     "<insert_stmt>": ["INSERT INTO <table_name> (<column_names>) VALUES (<values>);"],
#     "<update_stmt>": ["UPDATE <table_name> SET <assignments> [WHERE <condition>]"],
#     "<delete_stmt>": ["DELETE FROM <table_name> [WHERE <condition>]"],

#     # SELECT statement
#     "<select_stmt>": ["SELECT <select_list> FROM <table_references> WHERE <condition>;"],

#     # Transaction control
#     "<begin_transaction>": ["BEGIN [TRANSACTION]"],
#     "<commit>": ["COMMIT [TRANSACTION]"],
#     "<rollback>": ["ROLLBACK [TRANSACTION]"],

#     # EXPLAIN statements
#     "<explain_stmt>": ["EXPLAIN <sql_stmt>", "EXPLAIN QUERY PLAN <sql_stmt>"],

#     # Function invocation
#     "<simple_function_invocation>": ["<function_name>(<expr>)"],

#     # PRAGMA statement
#     "<pragma_stmt>": [
#         "PRAGMA <pragma_name> = <pragma_value>", 
#         "PRAGMA <pragma_name>(<pragma_value>)", 
#         "PRAGMA <pragma_name>"
#     ],

#     # REINDEX statement
#     "<reindex_stmt>": [
#         "REINDEX <collation_name>;", 
#         "REINDEX <table_name>;", 
#         "REINDEX <index_name>;"
#     ],

#     # Savepoints and transactions
#     "<savepoint_stmt>": ["SAVEPOINT <savepoint_name>"],
#     "<release_stmt>": ["RELEASE SAVEPOINT <savepoint_name>"],
#     "<rollback_to_savepoint>": ["ROLLBACK TRANSACTION TO SAVEPOINT <savepoint_name>"],

#     # UPSERT statement
#     "<upsert_stmt>": [
#         "ON CONFLICT (<columns>) DO NOTHING", 
#         "ON CONFLICT (<columns>) DO UPDATE SET <column_name> = <expr> [WHERE <expr>]"
#     ],

#     # Window function invocation
#     "<window_function_invocation>": [
#         "<window_func>(<expr>) OVER <window_defn>",
#         "<window_func>(<expr> <filter_clause>) OVER <window_defn>"
#     ],

#     # Comments
#     "<comment_syntax>": [
#         "-- <anything_except_newline>",
#         "/* <anything_except_*/> */"
#     ],

#     # Additional SQL statements
#     "<vacuum_stmt>": ["VACUUM"],
#     "<analyze_stmt>": ["ANALYZE [<table_name>]"],
#     "<attach_stmt>": ["ATTACH DATABASE '<filename>' AS <schema_name>"],
#     # "<detach_stmt>": ["DETACH DATABASE <schema_name>"],

#     # Aggregate functions
#     "<aggregate_function_invocation>": [
#         "COUNT(<expr>)", "SUM(<expr>)", "AVG(<expr>)", "MIN(<expr>)", "MAX(<expr>)"
#     ],

#     # Nested SELECT queries
#     "<nested_select>": [
#         "SELECT <select_list> FROM <table_references> WHERE <condition> AND <subquery>",
#         "SELECT <select_list> FROM (<nested_select>) WHERE <condition>"
#     ],

#     # Subquery
#     "<subquery>": ["(SELECT <select_list> FROM <table_name> WHERE <condition>)"],

#     # JSON functions
#     "<json_functions>": [
#         "JSON(<arguments>)",
#         "JSON_ARRAY(<arguments>)",
#         "JSON_OBJECT(<arguments>)",
#         "JSON_QUOTE(<expr>)",
#         "JSON_EXTRACT(<expr>, <path>)",
#         "JSON_SET(<expr>, <path>, <value>)",
#         "JSON_REPLACE(<expr>, <path>, <value>)",
#         "JSON_REMOVE(<expr>, <path>)",
#         "JSON_INSERT(<expr>, <path>, <value>)",
#         "JSON_TYPE(<expr>)",
#         "JSON_VALID(<expr>)",
#         "JSON_ARRAY_LENGTH(<expr>)",
#         "JSON_TREE(<expr>)"
#     ],

#     # Schema name
#     "<schema_name>": ["main", "temp", "<identifier>"],

#     # Table columns definition
#     "<table_columns_def>": ["<table_column_def>", "<table_column_def>, <table_columns_def>"],
#     "<table_column_def>": ["<column_name> <data_type> <column_constraints>"],

#     # Column definitions
#     "<column_def>": ["<column_name> <data_type> <column_constraints>"],

#     # Column constraints
#     "<column_constraints>": ["", "<column_constraint><column_constraints>"],
#     "<column_constraint>": [
#         "NOT NULL", "UNIQUE", "PRIMARY KEY", "CHECK (<condition>)", 
#         "DEFAULT <value>", "COLLATE <collation_name>", "GENERATED ALWAYS AS (<expression>)"
#     ],

#     # Data types
#     "<data_type>": ["INTEGER", "REAL", "TEXT", "BLOB", "NUMERIC", "BOOLEAN", "DATE", "TIME", "DATETIME"],

#     # Table name, column name, etc.
#     "<table_name>": ["<identifier>"],
#     "<view_name>": ["<identifier>"],
#     "<column_name>": ["<identifier>"],
#     "<indexed_columns>": ["<column_name>", "<column_name>, <indexed_columns>"],
#     "<columns>": ["<column_name>", "<column_name>, <columns>"],

#     # Literals, values, and expressions
#     "<expr>": ["<literal>", "<identifier>", "<expr> <operator> <expr>"],
#     "<literal>": ["<number>", "'<string>'", "NULL"],
#     "<operator>": ["+", "-", "*", "/", "%", "AND", "OR", "=", "!=" , "<", "<=", ">", ">="],

#     # Function calls
#     "<function_name>": ["ABS", "LENGTH", "SUBSTR", "RANDOM", "UPPER", "LOWER", "COUNT", "SUM", "AVG", "MIN", "MAX"],

#     # Arguments and identifiers
#     "<arguments>": ["<value>", "<arguments>, <value>"],
#     "<value>": ["<literal>", "'<string>'"],
#     "<identifier>": ["<letter>", "<identifier><letter_or_digit>"],
#     "<letter_or_digit>": ["<letter>", "<digit>"],
#     "<string>": ["<char>", "<char><string>"],
#     "<char>": ["<letter>", "<digit>", "<special_char>"],
#     "<number>": ["<integer>", "<float>"],
#     "<integer>": ["<digit>", "<digit><integer>"],
#     "<float>": ["<integer>.<integer>"],

#     # Special characters and digits
#     "<special_char>": ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", ",", ".", "<", ">", "/", "?", "`", "~"],
#     "<letter>": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
#                  "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
#                  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
#                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
#     "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],

#     # Adding missing definitions
#     "<index_name>": ["<identifier>"],
#     "<expression>": ["<expr>"],
#     "<condition>": ["<expr>", "<expr> <operator> <expr>"],
#     "<path>": ["<string>"],
#     "<savepoint_name>": ["<identifier>"],
#     "<sql_stmt>": ["<statement>"],
#     "<column_names>": ["<column_name>", "<column_name>, <column_names>"],
#     "<module_arguments>": ["<value>", "<value>, <module_arguments>"],
#     "<values>": ["<value>", "<value>, <values>"],
#     "<pragma_name>": ["<identifier>"],
#     "<select_list>": ["<column_name>", "<column_name>, <select_list>"],
#     "<trigger_name>": ["<identifier>"],
#     "<anything_except_newline>": ["<char>", "<char><anything_except_newline>"],
#     "<module_name>": ["<identifier>"],
#     "<collation_name>": ["<identifier>"],
#     "<table_references>": ["<table_name>", "<table_name>, <table_references>"],
#     "<window_func>": ["<function_name>"],
#     "<window_defn>": ["PARTITION BY <columns>", "ORDER BY <columns>"],
#     "<filter_clause>": ["FILTER (WHERE <condition>)"],
#     "<assignments>": ["<column_name> = <expr>", "<column_name> = <expr>, <assignments>"],
#     "<pragma_value>": ["<value>"],
#     "<filename>": ["'<string>'"],
#     "<anything_except_*/>": ["<char>", "<char><anything_except_*/>"],
# }







