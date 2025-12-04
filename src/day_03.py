import os
import itertools as it
from copy import copy


with open(f"data/day_03{os.getenv('DEV', '')}.txt") as f:
    data = f.read().splitlines()


def get_joltage_from_number(
    n: str,
    r: int,
):
    current_n = copy(n)
    numbers = []
    skip = 0
    for i in range(r):
        candidates = current_n[:len(n) - r - skip + 1]
        max_candidate = max(candidates)
        index_max_candidate = candidates.index(max_candidate)
        skip += index_max_candidate
        numbers.append(max_candidate)
        current_n = current_n[index_max_candidate + 1:]
    return int("".join(numbers))

# Part I
joltage = []
for i, line in enumerate(data, start=1):
    print(f"Line {i}/{len(data)}")
    comb = (
        it
        .combinations(
            list(line),
            r=2,
        )
    )
    max_joltage = (
        max(
            int("".join(i))
            for i in comb
        )
    )
    joltage.append(max_joltage)

print(
    sum(joltage)
)

# Part II
# Testing solution from part II for part I
R = 2
print(
    sum(
        [
            get_joltage_from_number(
                n=line,
                r=R,
            )
            for line in data
        ]
    )
)
R = 12
print(
    sum(
        [
            get_joltage_from_number(
                n=line,
                r=R,
            )
            for line in data
        ]
    )
)
