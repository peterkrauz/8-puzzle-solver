# N Puzzle Solver

## Description

This repository contains Python files used in implementing three search solutions that are able to find the quickest number of moves required to solve the N-Puzzle problem. <br>
All files were developed for a college work in the subject of Intelligent Systems. <br>
The solutions implemented are as follows:

- [Uniform Cost Search](solvers/uniform_cost_search.py)
  - Is basically a Breadth-first search given the fact that each Puzzle Board down the search tree has an increasing cost of 1.
- [A* (Simple)](solvers/a_star_simple_search.py)
  - Uses the number of misplaced tiles as heuristic.
- [A* (Precise)](solvers/a_star_precise_search.py)
  - Uses the sum of each tile's [Manhattan Distance](https://en.wikipedia.org/wiki/Taxicab_geometry) to its position in the endgame board. 

### N Puzzle

Initially known as 8 Puzzle, the game consists of a matrix whose value is equal to the (matrix's side ^ 2) - 1. For the
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
python3 -m venv venv
```

Activate the virtual environment:

```python
source venv/bin/activate
```

## Instructions

To run the program, execute the following command:

```python
python puzzle_solver.py
```

Enjoy!