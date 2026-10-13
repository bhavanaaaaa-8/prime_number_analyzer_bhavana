# Prime Number Checker and Generator

## Description
This Python program checks whether a number is prime and generates all prime numbers within a user-specified range. It uses a reusable `is_prime()` function and an efficient divisibility-checking method to reduce unnecessary calculations.

## Features
- Checks whether a number is prime.
- Generates all prime numbers within a specified range.
- Uses a reusable `is_prime(n)` function.
- Checks divisibility only up to the square root of the number.
- Handles edge cases such as negative numbers, 0, and 1.
- Validates the range to ensure the starting number does not exceed the ending number.

## Requirements
- Python 3.x

## How to Run
1. Make sure Python 3 is installed.
2. Save the program as `prime_checker.py`.
3. Open a terminal in the folder containing the file.
4. Run the following command:

   ```bash
   python prime_checker.py
   ```

## Example Output

```text
-5: Not prime
0: Not prime
1: Not prime
2: Prime
3: Prime
4: Not prime
9: Not prime
17: Prime
25: Not prime

Enter starting number: 10
Enter ending number: 30
Prime numbers between 10 and 30:
11 13 17 19 23 29
```

## Edge Cases Tested
- Negative numbers are not prime.
- 0 and 1 are not prime.
- 2 is the smallest prime number.
- Composite numbers such as 4, 9, and 25 are not prime.
- Invalid ranges are rejected.

## Algorithm
1. Check whether the number is less than or equal to 1. If so, return `False`.
2. Check divisibility from 2 up to the square root of the number.
3. If any divisor is found, return `False`; otherwise, return `True`.
4. Iterate through the specified range and print every number for which `is_prime()` returns `True`.

## Time Complexity
- **Prime check:** O(√n) time.
- **Range generation:** Approximately O((b − a + 1)√b) in the worst case, where `a` and `b` are the starting and ending numbers.

## Learning Outcomes
- Understanding prime numbers and divisibility.
- Creating and reusing Python functions.
- Using loops, conditional statements, and return values.
- Testing edge cases and improving algorithm efficiency.

## Author
Created as a Python programming practice project.
