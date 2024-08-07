# 0x0A Prime Game

## Overview
This project involves solving a competitive game scenario using your understanding of prime numbers, game theory, and algorithm optimization. The challenge is to determine the winner of a game based on the strategic removal of prime numbers and their multiples from a set of consecutive integers.

## Concepts Needed

### Prime Numbers
- **Understanding**: Know what prime numbers are.
- **Efficient Algorithms**: Identify prime numbers within a range.
- **Sieve of Eratosthenes**: An efficient algorithm to find all prime numbers up to any given limit.

### Game Theory
- **Principles**: Basic principles of competitive games where players take turns.
- **Optimal Play**: Strategies that lead to a win or loss, and understanding win conditions.

### Dynamic Programming/Memoization
- **Optimization**: Use previous results to make future calculations faster.
- **Efficiency**: Optimize the solution for multiple rounds of the game.

### Python Programming
- **Implementation**: Use loops and conditional statements to implement game logic and algorithms.
- **Data Structures**: Use arrays and lists for storing integers and tracking removed numbers.

## Resources

### Prime Numbers and Sieve of Eratosthenes
- [Khan Academy: Introduction to Prime Numbers](https://www.khanacademy.org/math/pre-algebra/pre-algebra-factors-multiples/pre-algebra-prime-numbers/v/prime-numbers)
- [Sieve of Eratosthenes in Python](https://realpython.com/python-sieve-of-eratosthenes/): A step-by-step guide to implementing the sieve algorithm in Python.

### Game Theory Basics
- [Game Theory Introduction](https://www.investopedia.com/terms/g/gametheory.asp): A simple explanation of game theory and strategic decision-making.

### Dynamic Programming
- [What Is Dynamic Programming With Python Examples](https://www.geeksforgeeks.org/dynamic-programming/): An introduction to dynamic programming with Python examples.

### Python Official Documentation
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html): Managing lists in Python, useful for tracking the game state.

By grasping these concepts and making use of the recommended resources, you will be well-equipped to approach the problem with a solid understanding of both the mathematical and programming challenges involved. The key to success in this project lies in applying efficient algorithms to manage the game’s state and making optimal decisions based on the game’s rules.

## Additional Resources
- [Mock Technical Interview](https://www.pramp.com/)

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

## Tasks

### 0. Prime Game
**Mandatory**

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

**Prototype:** `def isWinner(x, nums)`

- `x` is the number of rounds and `nums` is an array of `n`
- Return the name of the player that won the most rounds
- If the winner cannot be determined, return `None`
- You can assume `n` and `x` will not be larger than 10000
- You cannot import any packages in this task
