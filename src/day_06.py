import os
import re

from pprint import pprint
from functools import reduce

with open(f"data/day_06{os.getenv('DEV', '')}.txt") as f:
    data = f.read().splitlines()

data = [
    re.sub("\s+", " ", line.strip()).split(" ")
    for line in data # [::-1]
]

# Transpose matrix
data = list(zip(*data))
results = []
for row in data:
    operator = row[-1]
    numbers = [int(i) for i in row[:-1]]
    if operator == "*":
        result = reduce(lambda x, y: x * y, numbers)
    elif operator == "+":
        result = reduce(lambda x, y: x + y, numbers)
    else:
        raise Exception("Bug")
    results.append(result)

print(sum(results))

pprint(data)
