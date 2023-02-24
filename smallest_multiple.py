# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import time
st = time.time()

n = 20
while n > 0:
    if n % 20 == 0 and n % 19 == 0 and n % 18 == 0 and n % 17 == 0 and n % 16 == 0 and n % 15 == 0 and n % 14 == 0 and n % 14 == 0 and n % 13 == 0 and n % 12 == 0 and n % 11 == 0:
        print(n)
        break
    else:
        n = n + 1

et = time.time()
print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds')
