'''  Time complexity: time required to run an algorithm based upon the size of the input data. It is denoted using Big O notation (O). 
    O(1) - Constant time: The algorithm takes the same amount of time regardless of the input size. Example: Accessing an element in an array by index.
    O(n) - Linear time: The algorithm's time increases linearly with the input size. Example: Iterating through a list to find a specific element.
    O(n^2) - Quadratic time: The algorithm's time increases quadratically with the input size. Example: Nested loops iterating through a 2D array.
    O(log n) - Logarithmic time: The algorithm's time increases logarithmically with the input size. Example: Binary search in a sorted array.
     O(n log n) - Linearithmic time: The algorithm's time increases as n log n. Example: Efficient sorting algorithms like Merge Sort and Quick Sort.
     O(2^n) - Exponential time: The algorithm's time doubles with each additional input element. Example: Recursive algorithms that solve problems by dividing them into smaller subproblems, such as the Fibonacci sequence.
     O(n!) - Factorial time: The algorithm's time increases factorially with the input size. Example: Algorithms that generate all permutations of a set, such as the Traveling Salesman Problem.
     O(n^k) - Polynomial time: The algorithm's time increases polynomially with the input size, where k is a constant. Example: Algorithms that involve nested loops with a fixed number of iterations, such as matrix multiplication.
     O(k^n) - Exponential time with a constant base: The algorithm's time increases exponentially with the input size, where k is a constant. Example: Algorithms that generate all subsets of a set, such as the Power Set problem.
     O(n^n) - Super-exponential time: The algorithm's time increases super-exponentially with the input size. Example: Algorithms that generate all possible combinations of a set, such as the Knapsack problem.
     O(log log n) - Double logarithmic time: The algorithm's time increases double logarithmically with the input size. Example: Certain algorithms for finding the median of a list.
     O(sqrt(n)) - Square root time: The algorithm's time increases with the square root of the input size. Example: Algorithms that involve checking for factors of a number, such as primality testing.
     O(n^c) - Polynomial time with a constant exponent: The algorithm's time increases polynomially with the input size, where c is a constant. Example: Algorithms that involve nested loops with a variable number of iterations, such as certain dynamic programming algorithms.
     O(c^n) - Exponential time with a variable base: The algorithm's time increases exponentially with the input size, where c is a variable. Example: Algorithms that generate all possible combinations of a set, such as the Knapsack problem.
     
     
def const_time_example(arr):
    return arr[0]  # O(1)
print(const_time_example([1, 2, 3, 4, 5]))  # Output: 1


def linear_time_example(arr):
    for element in arr:
        print(element)  # O(n)
linear_time_example([1, 2, 3, 4, 5]) # Output: 1 2 3 4 5

def quadratic_time_example(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
print(arr[i], arr[j])  # O(n^2)
quadratic_time_example([1, 2, 3, 4, 5]) # Output: 1 1, 1 2, 1 3, 1 4, 1 5, 2 1, 2 2, 2 3, 2 4, 2 5, ..., 5 5

def logarithmic_time_example(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  # O(log n)
    return -1  # Element not found  
print(logarithmic_time_example([1, 2, 3, 4, 5], 3))  # Output: 2
print(logarithmic_time_example([1, 2, 3, 4, 5], 6))  # Output: -1

def linearithmic_time_example(arr):
    arr.sort()  # O(n log n)
    return arr
print(linearithmic_time_example([5, 3, 1, 4, 2]))  # Output: [1, 2, 3, 4, 5]


def exponential_time_example(n):
    if n <= 1:
        return n
    return exponential_time_example(n - 1) + exponential_time_example(n - 2)  # O(2^n)
print(exponential_time_example(5))  # Output: 5

def factorial_time_example(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i  # O(n!)
    return result
print(factorial_time_example(5))  # Output: 120

def polynomial_time_example(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
print(arr[i], arr[j], arr[k])  # O(n^3)
polynomial_time_example([1, 2, 3]) # Output: 1 1 1, 1 1 2, 1 1 3, ..., 3 3 3

def exponential_time_with_constant_base_example(n):
    if n == 0:
        return 1
    result = 1
    for i in range(n):
        result *= 2  # O(2^n)
    return result
print(exponential_time_with_constant_base_example(5))  # Output: 32

def super_exponential_time_example(n):
    if n == 0:
        return 1
    result = 1
    for i in range(n):
        result *= n  # O(n^n)
    return result
print(super_exponential_time_example(5))  # Output: 3125

def double_logarithmic_time_example(n):
    if n <= 1:
        return 0
    return double_logarithmic_time_example(n // 2) + 1  # O(log log n)
print(double_logarithmic_time_example(16))  # Output: 2

def square_root_time_example(n):
    for i in range(1, int(n**0.5) + 1):
        print(i)  # O(sqrt(n))
square_root_time_example(16)  # Output: 1 2 3 4

def polynomial_time_with_constant_exponent_example(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                print(arr[i], arr[j], arr[k])  # O(n^3)
polynomial_time_with_constant_exponent_example([1, 2, 3]) # Output: 1 1 1, 1 1 2, 1 1 3, ..., 3 3 3

def exponential_time_with_variable_base_example(n):
    if n == 0:
        return 1
    result = 1
    for i in range(n):
        result *= n  # O(n^n)
    return result
print(exponential_time_with_variable_base_example(5))  # Output: 3125

def fibbonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # O(2^n)
print(fibonacci(5))  # Output: 5
'''