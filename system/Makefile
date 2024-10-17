CC = gcc
CFLAGS = -fprofile-arcs -ftest-coverage -fsanitize=address -O1 # -O1 (optimization flag)
LIBS = -lpthread -ldl -lm

# Add AddressSanitizer and MemorySanitizer flags
#SANITIZER_FLAGS = -fsanitize=memory 

all: sqlite3
# Add sanitizer flags to the build command for sqlite3
sqlite3: shell.c sqlite3.c
	$(CC) $(CFLAGS) $^ $(LIBS) -o $@

coverage-html:
	gcovr --html --html-details -o coverage_report.htmla

coverage-csv:
	gcovr --csv --branches --exclude-unreachable-branches -o coverage_report.csv

coverage-verbose:
	gcovr --branches --exclude-unreachable-branches -o coverage_verbose.txt

clean:
	rm -f *.gcda coverage_* *.db plot.pdf

.PHONY: all clean coverage-html coverage-csv coverage-verbose
