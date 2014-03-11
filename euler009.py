# Problem #9

# A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

done = False
for a in xrange(1, 501):
  for b in xrange(a, 501):
    for c in xrange(b, 501):
      if (a + b + c == 1000):
        if ((a ** 2) + (b ** 2) == (c ** 2)):
          print a * b * c
          done = True
          break
    if done:
      break
  if done:
    break
