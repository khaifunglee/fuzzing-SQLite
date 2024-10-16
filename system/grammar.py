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
    "<begin_transaction>":["BEGIN [TRANSACTION]"],
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
  
   
    "<expr>": ["NULL", "<literal>", "<identifier>", "<expr> <operator> <expr>"], # added NULL value (null pointer dereference)

    "<indexed_columns>": ["<column_name>", "<column_name>, <indexed_columns>"],
    "<columns>": ["<column_name>", "<column_name>, <columns>"],
    "<column_name>": ["<identifier>"],
    "<column_names>": ["<string>", "<string>, <column_names>"],
    "<values>": ["<value>", "<value>, <values>", "'A' * 1000000", "'B' * 5000000", "999999999999999999999999999999", "-999999999999999999999999999999"], # added large string & values (buffer overflow)
    "<assignments>":["<assignment>","<assignments>,<assignment>"],
    "<assignment>":["<column_name>=<value>"],
    "<value>": ["<literal>", "'<function_call>'"],
    "<literal>":["<number>","'<string>'","NULL"], # added NULL value (null pointer dereference)
   
    "<pragma_name>": ["cache_size", "encoding", "foreign_keys", "journal_mode", "locking_mode", "synchronous"], 
    "<pragma_value>": ["<signed_number>", "<name>", "<signed_literal>"],
    "<signed_number>": ["-<number>", "<number>"],
    "<name>": ["true", "false", "auto_vacuum", "FULL", "NORMAL", "OFF"],  
    "<signed_literal>": ["'<string>'"],

    "<json_column>": ["column_name", "$.<identifier>"],
    # "<filename>": ["'<string>'"],

    "<condition>": ["<expression>"],
    "<expression>":["NULL", "<value>","expression><operator><expression>","(<expression>)"],
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
  
    "<special_char>":["!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","{","|",";",":","''",",",".","<",">","/","?","`","~", "\\", "\'", "\""],
    "<letter>": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
                "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}
