# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import time
st = time.time()

a = 2
n = 3
listing = [2]

while len(listing) <= 10000:
    if all(n % a != 0 for a in range (a, int(n**0.5+1))): # actor of n that is greater than the square root of n must also have a corresponding factor that is less than the square root of n. 
        listing.append(n)
    n = n + 2
       
print(listing[-1])

et = time.time()
print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds')