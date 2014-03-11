# Problem #5

# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?

i = 2520
# found = False
while True:

  found = True

  for j in xrange(11, 21):
    if i % j != 0:
      found = False
      break

  if found:
    print i
    break
  i+= 2520
