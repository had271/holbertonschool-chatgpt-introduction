#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Computes the factorial of a non-negative integer using recursion.
        The factorial of a number n (written as n!) is defined as:
        n! = n × (n−1) × ... × 1, with 0! = 1.

    Parameters:
        n (int): A non-negative integer whose factorial will be calculated.

    Returns:
        int: The factorial value of the given integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


f = factorial(int(sys.argv[1]))
print(f)
