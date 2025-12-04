import os
from copy import copy


SYMBOL = "@"
MAX_ROLLS = 4

with open(f"data/day_04{os.getenv('DEV', '')}.txt") as f:
    data = f.read().splitlines()
    data = [list(line) for line in data]

n_rows = len(data)
n_cols = len(data[0])
# pprint(data)

def look_around_and_count(data: list[list[str]], i: int, j: int):
    total = 0
    # TOP-
    if i - 1 >= 0:
        if data[i - 1][j] == SYMBOL:
            total += 1
    # TOP-LEFT
    if i - 1 >= 0 and j - 1 >= 0:
        if data[i - 1][j - 1] == SYMBOL:
            total += 1
    # -LEFT
    if j - 1 >= 0:
        if data[i][j - 1] == SYMBOL:
            total += 1
    # BOTTOM-LEFT
    if i + 1 < n_rows and j - 1 >= 0:
        if data[i + 1][j - 1] == SYMBOL:
            total += 1
    # BOTTOM-
    if i + 1 < n_rows:
        if data[i + 1][j] == SYMBOL:
            total += 1
    # BOTTOM-RIGHT
    if i + 1 < n_rows and j + 1 < n_cols:
        if data[i + 1][j + 1] == SYMBOL:
            total += 1
    # -RIGHT
    if j + 1 < n_cols:
        if data[i][j + 1] == SYMBOL:
            total += 1
    # TOP-RIGHT
    if i - 1 >= 0 and j + 1 < n_cols:
        if data[i - 1][j + 1] == SYMBOL:
            total += 1

    # print(f"({i=},{j=}):{total=}")
    return total

rolls = 0
for i, row in enumerate(data):  # rows
    for j, col in enumerate(row):  # cols
        if data[i][j] == SYMBOL:
            total = look_around_and_count(data, i, j)
            if total < MAX_ROLLS:
                # print(f"Add position {i}, {j}")
                rolls += 1

print(rolls)

def reduce_rolls(data):
    rolls = 0
    positions = []
    for i, row in enumerate(data):  # rows
        for j, col in enumerate(row):  # cols
            if data[i][j] == SYMBOL:
                total = look_around_and_count(data, i, j)
                if total < MAX_ROLLS:
                    # print(f"Add position {i}, {j}")
                    rolls += 1
                    positions.append((i, j))
    return rolls, positions


def update_data(data, positions):
    new_data = copy(data)
    for i, j in positions:
        new_data[i][j] = "."
    return new_data


total_rolls = 0
while True:
    rolls, positions = reduce_rolls(data)
    total_rolls += rolls
    if rolls == 0:
        break
    data = update_data(data, positions)

print(total_rolls)
