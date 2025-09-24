# In this file, we are going to implement a simple function "is_power_of(num, n)" that checks if a number num is a power of n using recursion.
# For example, is_power_of(27, 3) should return True because 3^3 = 27, while is_power_of(10, 2) should return False because 10 is not a power of 2.
# An important note is that we are not allowed to use loops in this implementation.
# Your function should check for the following conditions:
# 1. If num is less than 1, return False.
# 2. If n is less than 2, return False.
# 3. If num is equal to 1, return True (since any number to the power of 0 is 1).
# 4. If num is equal to n, return True (since n^1 = n).
# 5. If num is not divisible by n, return False.
# 6. If num or n are outside the range of 1 to 1,000,000 for num and 2 to 10 for n, return False.

# Your code will be tested by auto grader inside the helper code.
# If your implementation is correct, you will see "All tests passed!" message at the end of the output.

def is_power_of(num, n):
    if num < 1 or num > 1000000: #condition 1 & 6
        return False
    if n < 2 or n > 10: #condition 2 & 6
        return False
    if num == 1: #condition 3
        return True
    if num == n: #condition 4
        return True
    if num % n != 0: #condition 5
        return False
    return is_power_of(num/n, n)



# do not change the code below this line.
if __name__ == "__main__":
    examples = [
        ((27, 3),True),  # True, because 3^3 = 27
        ((10, 2),False),  # False, because 10 is not a power of 2
        ((16, 4),True),  # True, because 4^2 = 16
        ((81, 3),True),  # True, because 3^4 = 81
        ((20, 5),False),  # False, because 20 is not a power of 5
        ((1, 2),True),   # True, because any number to the power of 0 is 1
        ((0, 2),False),   # False, because no positive power of 2 is 0
        ((9, 3),True),   # True, because 3^2 = 9
        ((25, 5),True),  # True, because 5^2 = 25
        ((14, 7),False),   # False, because 14 is not a power of 7
        ((0, 5),False),    # False, because no positive power of 5 is 0
        ((1, 5),True),    # True, because any number to the power of 0 is 1
        ((279936, 6),True),  # True, because 6^6 = 279936
        ((1000000, 9),False),  # False, because 9^6 is not 1000000
        ((10000000, 10),False),  # boundary case, should return False
        ((144, 12),False)  # boundary case, should return False
    ]

    error_count = 0
    for (num, n), expected in examples:
        result: bool = is_power_of(num, n)
        if result == expected:
            print(f"is_power_of({num}, {n}) = {result}")
        else:
            # Print failed cases in red
            print(f"\033[91mTest failed for input: ({num}, {n}) - got {result}, expected {expected}\033[0m")
            error_count += 1
    print("Testing complete!")
    if error_count == 0:
        print("\033[92mAll tests passed!\033[0m")
    else:
        print("\033[91mSome tests failed.\033[0m")
        print(f"Total errors: {error_count}")
