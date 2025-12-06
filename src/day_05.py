import os
import itertools as it

with open(f"data/day_05{os.getenv('DEV', '')}.txt") as f:
    data = f.read().splitlines()
    to_split = data.index("")
    ingredients = data[:to_split]
    available_ingredients = data[to_split + 1:]


# Part I
total = 0
for available_ingredient in available_ingredients:
    for fresh_range in ingredients:
        min_fresh, max_fresh = fresh_range.split("-")
        min_fresh = int(min_fresh)
        max_fresh = int(max_fresh)
        if int(available_ingredient) in range(
            min_fresh, max_fresh + 1
        ):
            total += 1
            break

print(total)

# Part II
def ranges_union(
    range_base,
    range_to_check,
):
    if range_to_check[0] not in range(range_base[0], range_base[1] + 1) and range_to_check[1] not in range(range_base[0], range_base[1] + 1):
        return None
    elif range_to_check[0] in range(range_base[0], range_base[1] + 1) and range_to_check[1] in range(range_base[0], range_base[1] + 1):
        return range_base
    elif range_to_check[0] in range(range_base[0], range_base[1] + 1) and range_to_check[1] > range_base[1]:
        return (range_base[0], range_to_check[1])
    elif range_to_check[0] < range_base[0] and range_to_check[1] in range(range_base[0], range_base[1] + 1):
        return (range_to_check[0], range_base[1])
    elif range_to_check[0] < range_base[0] and range_to_check[1] > range_base[1]:
        return None
    else:
        return None


ranges = [
    tuple(map(int, block.split("-")))
    for block in ingredients
]
ranges = sorted(
    ranges,
    key=lambda x: x[0],
)

changed = True
for i in it.count(1):
    print(f"Iteration: {i}")
    print(f"{ranges=}")
    changed = False
    combinations = (
        it
        .combinations(
            ranges,
            r=2,
        )
    )
    for combination in combinations:
        union = ranges_union(
            combination[0],
            combination[1],
        )
        if union is not None:
            changed = True
            ranges.remove(combination[0])
            ranges.remove(combination[1])
            ranges.append(union)
            break
    if not changed:
        print("Converged")
        break
print(
    sum(
        len(range(block[0], block[1] + 1))
        for block in ranges
    )
)
