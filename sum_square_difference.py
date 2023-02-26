# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import time
st = time.time()

a = 1;c = 0;d = 0 
while a <=100:
    c = c + pow(a,2)
    d = d + a
    a = a + 1
print(pow(d,2) - c)

et = time.time()
print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds')



