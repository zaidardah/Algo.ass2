import time

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

#In Python, the int type automatically supports arbitrary precision, meaning you can use it for very large integers (essentially like long long in C/C++).
x = int(input("Enter a number to calculate its factorial: "))

start_time_iter = time.perf_counter()
iterative_result = factorial_iterative(x)
end_time_iter = time.perf_counter()
start_time_recur = time.perf_counter()
recursive_result = factorial_recursive(x)
end_time_recur = time.perf_counter()
iterative_time_ms = (end_time_iter - start_time_iter) * 1000
recursive_time_ms = (end_time_recur - start_time_recur) * 1000

print("=" * 50)
print(f"Factorial Calculation for: {x}")
print("-" * 50)
print(f"Iterative Method:")
print(f"  Result: {iterative_result}")
print(f"  Execution Time: {iterative_time_ms:.3f} ms")
print("-" * 50)
print(f"Recursive Method:")
print(f"  Result: {recursive_result}")
print(f"  Execution Time: {recursive_time_ms:.3f} ms")
print("=" * 50)
