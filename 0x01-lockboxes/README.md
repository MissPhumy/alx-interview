# 0x01. Lockboxes

## Overview
This project involves developing a solution to determine if all boxes in a series of locked boxes can be opened. Each box is numbered sequentially and may contain keys to other boxes. The challenge is to write a method that verifies whether it's possible to unlock all the boxes starting from the first one, which is already unlocked.

## Key Concepts and Resources
1. **Lists and List Manipulation**
   - Accessing, iterating, and modifying lists.
   - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

2. **Graph Theory Basics**
   - Traversal algorithms like DFS or BFS.
   - [Graph Theory](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/graph-representation)

3. **Algorithmic Complexity**
   - Understanding time and space complexity.
   - [Big O Notation](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)

4. **Recursion**
   - Recursive approach for traversal.
   - [Recursion in Python](https://realpython.com/python-thinking-recursively/)

5. **Queue and Stack**
   - BFS or DFS implementations.
   - [Python Queue and Stack](https://www.geeksforgeeks.org/stack-in-python/)

6. **Set Operations**
   - Using sets to track visited boxes and available keys.
   - [Python Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)

## Requirements
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3
- Code should use PEP 8 style
- All files must be executable

## Task: Lockboxes
Write a method to determine if all boxes can be opened.

### Prototype:
```python
def canUnlockAll(boxes):
boxes is a list of lists
A key with the same number as a box opens that box
All keys are positive integers
The first box boxes[0] is unlocked
Return:
True if all boxes can be opened, else False.


