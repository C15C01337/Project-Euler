# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
import numpy
import time
st = time.time()


# listing = [2]
n = 3
sum = 2
while n < 2000000:
    a = 2
    for a in range(2, int(n**0.5+1)):
        if n % a == 0:
            break
    if n % a != 0:
        sum = sum + n
        # listing.append(n)
    n += 2
     
# print(listing)
# print(numpy.sum(listing))

print(sum)
et = time.time()
print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds') 