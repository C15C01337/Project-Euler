# Power digit sum
#  Show HTML problem content 
# Problem 16
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2*1000?

import time
st = time.time()

n = pow(2,1000)
digits = [int(d) for d in str(n)]
print(sum(digits))

et = time.time()
print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds')
