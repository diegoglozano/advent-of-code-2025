import os
import re
import itertools as it

from pprint import pprint
from functools import reduce

with open(f"data/day_06{os.getenv('DEV', '')}.txt") as f:
    data = f.read().splitlines()

data = [
    re.sub(r"\s+", " ", line.strip()).split(" ")
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

with open(f"data/day_06{os.getenv('DEV', '')}.txt") as f:
    data = f.read().splitlines()
    data = it.zip_longest(*data, fillvalue="")

OPERATORS = ("*", "+")
current_operator = None
total = []
current_numbers = []
for line in data:
    if all([l == " " for l in line]):
        if current_operator == "*":
            block_result = reduce(
                lambda x, y: x * y,
                current_numbers
            )
        elif current_operator == "+":
            block_result = reduce(
                lambda x, y: x + y,
                current_numbers
            )
        else:
            raise Exception("Bug")
        total.append(block_result)
        current_numbers = []
        continue
    if line[-1] in OPERATORS:
        current_operator = line[-1]
    numbers = int("".join(line[:-1]))
    current_numbers.append(numbers)

# For the last block. Ugly
if current_operator == "*":
    block_result = reduce(
        lambda x, y: x * y,
        current_numbers
    )
elif current_operator == "+":
    block_result = reduce(
        lambda x, y: x + y,
        current_numbers
    )
else:
    raise Exception("Bug")
total.append(block_result)

print(sum(total))
