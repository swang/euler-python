# Problem #4

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

the_max = float("-inf")

def is_palindrome(num):
  str_num = str(num)
  str_len = len(str_num)
  for i in xrange(0, int(str_len / 2)):
    if str_num[i] != str_num[str_len - 1 - i]:
      return False
  return True


for i in xrange(999, 99, -1):
  for j in xrange(999, 99, -1):
    if i * j > the_max and is_palindrome(i*j):
      the_max = i * j

print the_max
