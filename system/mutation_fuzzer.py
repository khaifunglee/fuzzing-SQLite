#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Code is modifed/simplified based on the Mutation-Based Fuzzer in the FuzzingBook
# "Mutation-Based Fuzzing" - a chapter of "The Fuzzing Book"
# Web site: https://www.fuzzingbook.org/html/MutationFuzzer.html

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
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
            swap_two_characters,        # New mutation operator 1
            duplicate_random_character, # New mutation operator 2
            remove_random_substring     # New mutation operator 3
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