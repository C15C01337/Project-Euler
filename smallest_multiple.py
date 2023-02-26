# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import time
st = time.time()

n = 2520
while n > 0:
    if all(n % i == 0 for i in range(11, 21)):
        print(n)
        break
    else:
        n += 2520

et = time.time()
print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds')
