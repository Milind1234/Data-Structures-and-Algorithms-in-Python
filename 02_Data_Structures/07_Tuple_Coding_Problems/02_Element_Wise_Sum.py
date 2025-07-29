# Question:
# Create a function that takes two tuples and returns a tuple containing 
# the element-wise sum of the input tuples.
#
# Example:
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple)  # Expected output: (5, 7, 9)


# Approach to Solve:
# 1. Both tuples are of the same length.
# 2. Pair elements at the same index using zip().
# 3. Add corresponding elements.
# 4. Store results in a tuple.
# 
# Two ways to implement:
# - Using a for loop (manual addition)
# - Using map() with sum() (more Pythonic)


# Approach 1: Using zip() and for loop
def tuple_elementwise_sum_loop(tuple1, tuple2):
    result = []
    for a, b in zip(tuple1, tuple2):
        result.append(a + b)
    return tuple(result)


# Approach 2: Using map() and sum()
def tuple_elementwise_sum_map(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))


# Sample Test Case
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print("Using Loop:", tuple_elementwise_sum_loop(tuple1, tuple2))  # Expected: (5, 7, 9)
print("Using map+sum:", tuple_elementwise_sum_map(tuple1, tuple2))  # Expected: (5, 7, 9)
