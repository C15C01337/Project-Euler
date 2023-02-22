# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import time
st = time.time()

listing = []
def prime(n):
    a = 2
    while a <= n:
        if n % a == 0:
            n = n / a
            listing.append(a)
        a = a + 1
    return n
prime(600851475143)
print(list(dict.fromkeys(listing))[len(listing)-1])

et = time.time()
print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds')
