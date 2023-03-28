# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# Once the chain starts the terms are allowed to go above one million.

import time
st = time.time()

def collatz(n):
    k = n
    length = 1
    nList = []
    nList.append(n)
    while n != 1:
        if n not in dict:
            n = collatzRule(n)
            nList.append(n)
            length += 1
        else:
            # we dont need the values but we do need the real length for the for-loop
            nList.extend([None for _ in range(dict[n] - 1)])
            length = (length - 1) + dict[n]
            break

    for seq in nList:
        if seq not in dict:
            dict[seq] = len(nList) - nList.index(seq)

    return length

def collatzRule(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

longestLen = 0
longestNum = 0
dict = {}

for n in range(2, 1000001):
    currentLen = collatz(n)
    if currentLen > longestLen:
        longestLen = currentLen
        longestNum = n

print(f'Starting num is: {longestNum} with the longest chain having: {longestLen} terms.')

et = time.time()
print('Execution time:', float("{:.8f}".format(float(et - st))),'seconds')