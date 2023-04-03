# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?


import time
st = time.time()

import math

print('''# combinatorics to count the number of paths. 
The number of paths from the top left corner to the bottom right corner of an n x n grid is given by
the central binomial coefficient:

(2n)C(n) = (2n)! / (n! * n!)
For a 20 x 20 grid, this becomes:

 (2 * 20)C(20) = (40!)/(20! * 20!)
''')

print(int(math.factorial(40)/(math.factorial(20)**2)))

et = time.time()
print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds')