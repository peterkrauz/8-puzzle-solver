# N Puzzle Solver

## Description

This repository contains Python files used in implementing three search solutions to the N-Puzzle problem, which were
all developed for a college work in the subject of Intelligent Systems. <br>
The solutions implemented are as follows:

- [Uniform Cost Search](solvers/uniform_cost_search.py)
- [A* (Simple)](solvers/a_star_simple_search.py)
- [A* (Precise)](solvers/a_star_precise_search.py)

### N Puzzle

Initially known as 8 Puzzle, the game consists of a matrix whose value is equal to the matrix's side ^ 2 - 1 For the
famous 3x3 matrix, the game is an 8 Puzzle. A 4x4 matrix would yield a 15 Puzzle, and so on.

## Setup

Clone the repo:

```shell
git clone https://github.com/peterkrauz/n-puzzle-solver.git
```

Enter the new directory:

```shell
cd n-puzzle-solver/
```

Create a Python 3 virtual environment:

```python
python3 - m venv venv
```

Activate the virtual environment:

```python
source venv / bin / activate
```

## Instructions

To run the program, execute the following command:

```python
python puzzle_solver.py
```

Enjoy!