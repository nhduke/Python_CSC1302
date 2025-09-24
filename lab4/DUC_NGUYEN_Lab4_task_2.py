# Tribonacci Sequence
# Tribonacci numbers are a sequence of numbers similar to Fibonacci numbers but with three initial values, typically 0, 0, and 1. 
# The sequence starts with these three values, and each subsequent number is the sum of the previous three numbers. 
# In mathematical notation, it can be defined as follows:
# T(0) = 0, T(1) = 0, T(2) = 1
# T(n) = T(n-1) + T(n-2) + T(n-3) for n > 2
# Your task is to implement a function tribonacci(n) that returns the nth Tribonacci number using recursion. 
# The function should handle the base cases for n = 0, 1, and 2, and for any n greater than 2, it should recursively calculate the Tribonacci number by summing the three preceding numbers in the sequence.

# Your code will be tested by auto grader inside the helper code.
# If your implementation is correct, you will see "All tests passed!" message at the end of the output.

tribMem = {}

def tribonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n < 0:
        return False
    if n not in tribMem:
        tribMem[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
        return tribMem[n]
    else:
        return tribMem[n]



# Do not change the code below this line.
if __name__ == "__main__":
    examples = [
        (0, 0),  # T(0) = 0
        (1, 0),  # T(1) = 0
        (2, 1),  # T(2) = 1
        (3, 1),  # T(3) = T(2) + T(1) + T(0) = 1 + 0 + 0 = 1
        (4, 2),  # T(4) = T(3) + T(2) + T(1) = 1 + 1 + 0 = 2
        (5, 4),  # T(5) = T(4) + T(3) + T(2) = 2 + 1 + 1 = 4
        (6, 7),  # T(6) = T(5) + T(4) + T(3) = 4 + 2 + 1 = 7
        (7, 13), # T(7) = T(6) + T(5) + T(4) = 7 + 4 + 2 = 13
        (8, 24), # T(8) = T(7) + T(6) + T(5) = 13 + 7 + 4 = 24
        (9, 44), # T(9) = T(8) + T(7) + T(6) = 24 + 13 + 7 = 44
        (10, 81), # T(10)=T(9)+T(8)+T(7)=44+24+13=81
        (20, 35890), # T(20)=T(19)+T(18)+T(17)=19513+10946+5768=35890
        (25, 755476), # T(25)=T(24)+T(23)+T(22)=410,744 + 223,317 + 121,415 = 755,476
        (27, 2555757), # T(27)=2555757 Why this case takes so long? What is your solution?
    ]

    import time
    error_count = 0
    for n, expected in examples:
        start_time = time.time()
        result: int = tribonacci(n)
        end_time = time.time()
        if result == expected:
            print(f"tribonacci({n}) = {result} (Time: {(end_time - start_time)*1000:.3f} milliseconds)")
        else:
            print(f"\033[91mTest failed for input: {n} - got {result}, expected {expected}\033[0m")
            error_count += 1
    print("Testing complete!")
    if error_count == 0:
        print("\033[92mAll tests passed!\033[0m")
        
    else:
        print("\033[91mSome tests failed.\033[0m")
        print(f"Total errors: {error_count}")