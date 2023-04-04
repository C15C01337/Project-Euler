import inflect
import re

p = inflect.engine()

count = sum(len(re.sub(r'\W', '', p.number_to_words(i))) for i in range(1, 1001))
print(count)
