with open("data/day_01.txt") as f:
    data = f.read().splitlines()

# Part I
pos = 50
total = 0
for instruction in data:
    l_r, number = instruction[0], instruction[1:]
    number = int(number)
    condition = -1 if l_r == "L" else 1
    pos = (pos + condition * number) % 100
    if pos == 0:
        total += 1
    print(f"{instruction} -> {pos}")

print(f"Password: {total}")
print()

# Part II
pos = 50
total = 0
for instruction in data:
    l_r, number = instruction[0], instruction[1:]
    number = int(number)
    condition = -1 if l_r == "L" else 1
    for _ in range(number):
        pos = (pos + condition * 1) % 100
        if pos == 0:
            total += 1
    print(f"{instruction} -> {pos}")

print(f"Password: {total}")
