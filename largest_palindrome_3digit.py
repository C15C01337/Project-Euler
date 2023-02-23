# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import time
st = time.time()

largest_palindrome = 0
one_factor = 0
another_factor = 0

listing = []
def palindromeChecker(n):
    reversed_string = str(n)[::-1]
    return str(n) == reversed_string

for i in range(100, 1000):
    for j in range(100, 1000):
        checkpalindrome = i * j
        if palindromeChecker(checkpalindrome):
            listing.append(checkpalindrome)

listing.sort()
print(listing[-1])

et = time.time()
print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds')

