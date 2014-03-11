# Problem #6

# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

sum_of_squares = reduce(lambda x, y: x + (y * y), xrange(1, 101))
square_of_sums = (reduce(lambda x, y: x + y, xrange(1, 101))) ** 2

print square_of_sums - sum_of_squares
