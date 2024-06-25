# 0x04. UTF-8 Validation

## Overview

For the “0x04. UTF-8 Validation” project, you will need to apply your knowledge in bitwise operations, understanding of the UTF-8 encoding scheme, and Python programming skills to validate whether a given dataset represents a valid UTF-8 encoding.

## Concepts Needed

### Bitwise Operations in Python

Understanding how to manipulate bits in Python, including operations like AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), shifts (`<<`, `>>`).

- [Python Bitwise Operators](https://realpython.com/python-bitwise-operators/)

### UTF-8 Encoding Scheme

Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
Understanding the patterns that represent a valid UTF-8 encoded character.

- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
- [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/articles/Unicode.html)

### Data Representation

How to represent and work with data at the byte level.
Handling the least significant bits (LSB) of integers to simulate byte data.

### List Manipulation in Python

Iterating through lists, accessing list elements, and understanding list comprehensions.

- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### Boolean Logic

Applying logical operations to make decisions within the program.

## Project Task

### 0. UTF-8 Validation

Write a method that determines if a given data set represents a valid UTF-8 encoding.
Requirements

- A character in UTF-8 can be 1 to 4 bytes long.
- The data set can contain multiple characters.
- The data will be represented by a list of integers.
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer.

Implementation Tips

- Study the UTF-8 encoding rules to understand how to recognize the start and continuation of multi-byte sequences.
- Use bitwise operations to isolate and check specific bits in each byte.
- Iterate through the list of integers to validate each byte according to UTF-8 rules.
- Pay attention to edge cases, such as incomplete sequences and invalid byte values.
- By studying these concepts and utilizing the resources provided, you will be equipped to tackle the UTF-8 validation project, effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.

**Prototype:**

```python
def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    
    :param data: List of integers representing the data set
    :return: True if data is a valid UTF-8 encoding, else return False
    """
