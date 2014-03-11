# Problem #1

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0
j = 0
for j in xrange(1, 1000):
  if (j % 3 == 0 or j % 5 == 0):
    sum += j

print sum
