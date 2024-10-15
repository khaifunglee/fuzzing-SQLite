#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Code is modifed/simplified based on the Mutation-Based Fuzzer in the FuzzingBook
# "Mutation-Based Fuzzing" - a chapter of "The Fuzzing Book"
# Web site: https://www.fuzzingbook.org/html/MutationFuzzer.html

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import re
from typing import List
from fuzzingbook.Fuzzer import Fuzzer

# List of mutation operators
def delete_random_character(s: str) -> str:
    """Returns s with a random character deleted"""
    if s == "":
        return s

    pos = random.randint(0, len(s) - 1)
    return s[:pos] + s[pos + 1:]

def insert_random_character(s: str) -> str:
    """Returns s with a random character inserted"""
    pos = random.randint(0, len(s))
    random_character = chr(random.randrange(32, 127))
    return s[:pos] + random_character + s[pos:]

def flip_random_character(s: str) -> str:
    """Returns s with a random bit flipped in a random position"""
    if s == "":
        return s

    pos = random.randint(0, len(s) - 1)
    c = s[pos]
    bit = 1 << random.randint(0, 6)
    new_c = chr(ord(c) ^ bit)
    return s[:pos] + new_c + s[pos + 1:]

# New mutation operators
def swap_two_characters(s: str) -> str:
    """Swaps two random characters in the string"""
    if len(s) < 2:
        return s

    pos1, pos2 = random.sample(range(len(s)), 2)
    s_list = list(s)
    s_list[pos1], s_list[pos2] = s_list[pos2], s_list[pos1]
    return ''.join(s_list)

def duplicate_random_character(s: str) -> str:
    """Duplicates a random character in the string"""
    if s == "":
        return s

    pos = random.randint(0, len(s) - 1)
    return s[:pos] + s[pos] + s[pos + 1:]

def remove_random_substring(s: str, min_len: int = 2, max_len: int = 5) -> str:
    """Removes a random substring of length between min_len and max_len"""
    if len(s) <= min_len:
        return s

    length = random.randint(min_len, min(max_len, len(s)))
    start_pos = random.randint(0, len(s) - length)
    return s[:start_pos] + s[start_pos + length:]

def insert_random_sql_keyword(s: str) -> str:
    """Inserts a random SQL keyword into the string."""
    sql_keywords = ['SELECT', 'INSERT', 'UPDATE', 'DELETE', 'WHERE', 'FROM', 'JOIN', 'ORDER BY', 'GROUP BY']
    keyword = random.choice(sql_keywords)
    pos = random.randint(0, len(s))
    return s[:pos] + ' ' + keyword + ' ' + s[pos:]

def replace_column_with_function(s: str) -> str:
    """Replaces a random column with a SQL function."""
    sql_functions = ['COUNT()', 'SUM()', 'MAX()', 'MIN()', 'AVG()']
    func = random.choice(sql_functions)
    columns = re.findall(r'[a-zA-Z_]\w*', s)  # Find column-like tokens
    if columns:
        column = random.choice(columns)
        return s.replace(column, func, 1)
    return s

def delete_random_sql_clause(s: str) -> str:
    """Deletes a random SQL clause from the string."""
    sql_clauses = ['WHERE', 'ORDER BY', 'GROUP BY', 'HAVING']
    for clause in sql_clauses:
        if clause in s:
            s = s.replace(clause, '', 1)
            break
    return s

def insert_random_parentheses(s: str) -> str:
    """Inserts random parentheses into the SQL string."""
    pos = random.randint(0, len(s))
    if random.random() < 0.5:
        return s[:pos] + '(' + s[pos:]
    else:
        return s[:pos] + ')' + s[pos:]

def negate_conditions(s: str) -> str:
    """Negates a comparison condition in the query."""
    s = re.sub(r'(\s*>\s*)', ' <= ', s)
    s = re.sub(r'(\s*<\s*)', ' >= ', s)
    s = re.sub(r'(\s*=\s*)', ' != ', s)
    return s

def replace_random_join_type(s: str) -> str:
    """Replaces a random SQL JOIN type with another."""
    join_types = ['INNER JOIN', 'LEFT JOIN', 'RIGHT JOIN', 'FULL JOIN', 'CROSS JOIN']
    for join in join_types:
        if join in s:
            other_join = random.choice(join_types)
            return s.replace(join, other_join, 1)
    return s

def duplicate_random_clause(s: str) -> str:
    """Duplicates a random SQL clause."""
    sql_clauses = ['SELECT', 'WHERE', 'FROM', 'ORDER BY', 'GROUP BY']
    for clause in sql_clauses:
        if clause in s:
            pos = s.find(clause)
            return s[:pos] + s[pos:pos + len(clause)] + ' ' + s[pos:]
    return s

def change_literal_data_type(s: str) -> str:
    """Changes the data type of a literal in the query."""
    literals = re.findall(r"'[^']*'|\d+", s)  # Match strings or numbers
    if literals:
        literal = random.choice(literals)
        if literal.isdigit():
            new_literal = "'" + ''.join(random.choice('abcdef') for _ in range(3)) + "'"
        else:
            new_literal = str(random.randint(1, 100))
        return s.replace(literal, new_literal, 1)
    return s

def insert_sql_comment(s: str) -> str:
    """Inserts a SQL comment at a random position."""
    pos = random.randint(0, len(s))
    return s[:pos] + ' -- comment ' + s[pos:]

def change_random_table_name(s: str) -> str:
    """Changes a table name to a random string."""
    tables = re.findall(r'[a-zA-Z_]\w*', s)  # Find potential table names
    if tables:
        table = random.choice(tables)
        new_table = 'tbl_' + ''.join(random.choice('abcdef') for _ in range(5))
        return s.replace(table, new_table, 1)
    return s


class MyMutationFuzzer(Fuzzer):
    """Base class for mutational fuzzing"""

    def __init__(self, seed: List[str],
                 min_mutations: int = 2,
                 max_mutations: int = 10) -> None:
        """Constructor.
        `seed` - a list of (input) strings to mutate.
        `min_mutations` - the minimum number of mutations to apply.
        `max_mutations` - the maximum number of mutations to apply.
        """
        self.seed = seed
        self.min_mutations = min_mutations
        self.max_mutations = max_mutations
        self.reset()

    def reset(self) -> None:
        """Set population to initial seed.
        To be overloaded in subclasses."""
        self.population = self.seed
        self.seed_index = 0

    def mutate(self, inp: str) -> str:
        """Return s with a random mutation applied"""
        mutators = [
            delete_random_character,
            insert_random_character,
            flip_random_character,
            swap_two_characters,          # New mutation operator 1
            duplicate_random_character,   # New mutation operator 2
            remove_random_substring,      # New mutation operator 3
            insert_random_sql_keyword,    # New mutation operator 4
            replace_column_with_function, # New mutation operator 5
            delete_random_sql_clause,     # New mutation operator 6
            insert_random_parentheses,    # New mutation operator 7
            negate_conditions,            # New mutation operator 8
            replace_random_join_type,     # New mutation operator 9
            duplicate_random_clause,      # New mutation operator 10
            change_literal_data_type,     # New mutation operator 11
            insert_sql_comment,           # New mutation operator 12
            change_random_table_name      # New mutation operator 13
        ]
        mutator = random.choice(mutators)
        return mutator(inp)

    def create_candidate(self) -> str:
        """Create a new candidate by mutating a population member"""
        candidate = random.choice(self.population)
        trials = random.randint(self.min_mutations, self.max_mutations)
        for _ in range(trials):
            candidate = self.mutate(candidate)
        return candidate

    def add_seed(self, seed: str) -> None:
        self.population.append(seed)
        print("New seed has been added to the corpus")

    def fuzz(self) -> str:
        if self.seed_index < len(self.seed):
            # Still seeding
            self.inp = self.seed[self.seed_index]
            self.seed_index += 1
        else:
            # Mutating
            self.inp = self.create_candidate()
        return self.inp