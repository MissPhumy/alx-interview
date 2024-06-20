# 0x03. Log Parsing

## Project Overview
The **0x03. Log Parsing** project is designed to help you enhance your Python programming skills, particularly in the areas of data parsing and real-time data stream processing. This project requires you to read from standard input (`stdin`), handle data in a specified format, and perform calculations based on the input data.

## Concepts Needed
To successfully complete this project, you should be familiar with the following concepts and resources:

1. **File I/O in Python**
   - Understand how to read from `sys.stdin` line by line.
   - [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

2. **Signal Handling in Python**
   - Handling keyboard interruptions (CTRL + C) using signal handling in Python.
   - [Python Signal Handling](https://docs.python.org/3/library/signal.html)

3. **Data Processing**
   - Parsing strings to extract specific data points.
   - Aggregating data to compute summaries.

4. **Regular Expressions**
   - Using regular expressions to validate the format of each line.
   - [Python Regular Expressions](https://docs.python.org/3/library/re.html)

5. **Dictionaries in Python**
   - Using dictionaries to count occurrences of status codes and accumulate file sizes.
   - [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

6. **Exception Handling**
   - Handling possible exceptions that may arise during file reading and data processing.
   - [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

By studying these concepts and utilizing the resources provided, you will be well-prepared to tackle the log parsing project, effectively handling data streams, parsing log entries, and computing metrics based on the processed data.

## Additional Resources
- [Mock Technical Interview](https://www.interviewcake.com/mock-interview)

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable
- The length of your files will be tested using `wc`

## Tasks
### 0. Log Parsing
Write a script that reads `stdin` line by line and computes metrics:


- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable
- The length of your files will be tested using `wc`


Possible status codes: 200, 301, 400, 401, 403, 404, 405, 500
If a status code doesn’t appear or is not an integer, don’t print anything for this status code.
plaintext
Copy code
<status code>: <number>
Status codes should be printed in ascending order.
Example
plaintext
Copy code
10.0.0.1 - [2017-02-05 23:59:59.123456] "GET /projects/260 HTTP/1.1" 200 1000
10.0.0.1 - [2017-02-05 23:59:59.123456] "GET /projects/260 HTTP/1.1" 301 200
10.0.0.1 - [2017-02-05 23:59:59.123456] "GET /projects/260 HTTP/1.1" 400 300

Output after 10 lines or keyboard interruption:
File size: 1500
200: 1
301: 1
400: 1
Warning: In this sample, you will have random values - it’s normal to not have the same output as this one.

