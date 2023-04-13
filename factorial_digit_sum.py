# Problem 20
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

# Calculate 100 factorial
fact = 1
for i in range(2, 101):
    fact *= i

# Find sum of digits
digit_sum = 0
while fact > 0:
    digit_sum += fact % 10
    fact //= 10

# Print result
print(digit_sum)

