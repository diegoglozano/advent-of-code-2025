import os
import math

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
total = 0
for idx, fresh_range in enumerate(ingredients, start=1):
    print(f"{idx}/{len(ingredients)}")
    min_fresh, max_fresh = fresh_range.split("-")
    min_fresh = int(min_fresh)
    max_fresh = int(max_fresh)
    total += len(range(min_fresh, max_fresh + 1))

print(total)


ranges_to_check = []
for idx, fresh_range in enumerate(ingredients, start=1):
    print(f"{idx}/{len(ingredients)}")
    min_fresh, max_fresh = fresh_range.split("-")
    min_fresh = int(min_fresh)
    max_fresh = int(max_fresh)
    for range_to_check in ranges_to_check:

        ranges_to_check.append(
            (min_fresh, max_fresh),
        )
print(ranges_to_check)
