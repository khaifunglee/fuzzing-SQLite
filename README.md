# fuzzing-SQLite

## Acknowledgement

This project is based on [an interactive exercise](https://jzamudio.com/sql-grammar-based-fuzzer/), presented to the audience at [the Fuzzing and Software Security Summer School](https://fuzzing.comp.nus.edu.sg/), and on [the Fuzzing Book](https://www.fuzzingbook.org/).

## Description

This project involves fuzz testing the SQLite database engine to identify potential vulnerabilities or unexpected behaviour. The focus was on setting up and running automated fuzzing campaigns using various fuzzing tools and techniques to test the robustness of SQLite under abnormal or random input conditions.

## Features
- Integrated multiple fuzzing tools (e.g AFL, grammar fuzzing, mutation fuzzing) for automated testing
- Targeted fuzzing of SQLite's SQL statement handling and query execution logic
- Collected crash inputs for debugging and vulnerability analysis
- Modular and scriptable setup for reproducible testing

## Technologies Used
- C/C++
- SQLite
- AFL++ (American Fuzzy Lop Plus Plus)
- Linux shell scripting
- Git & Github
- Docker

## Prerequisites
- Git or Github (for team collaboration)
- Docker
- Python 3
- AFL++ installed

## Folder Structure

## Setup Instructions
To building the program using Docker, build a 'ready-to-fuzz' Docker image by running the `docker build` command. Two version of Dockerfile are available: one for Intel CPUs and one for Arm64 CPUs.

For Intel CPUS:
```bash
docker build . -t name-of-program -f Dockerfile-Intel
```

For Arm64 CPUs:
```bash
docker build . -t name-of-program -f Dockerfile-Arm64
```

Next, start a Docker container. If the container starts properly, you should see a new container named `name-of-program-container` by running the `docker ps` command.

```bash
docker run -d --name name-of-program-container -p 6080:80 name-of-program
```

Access the Docker container in detached mode with the following command to enter the fuzzing program:
```
docker exec -it name-of-program-container /bin/bash
```
