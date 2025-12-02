import os

def split_number(n: str):
    n_groups = [
        i
        for i in range(1, len(n) // 2 + 1)
        if len(n) % i == 0
    ]
    for len_group in n_groups:
        yield (
            [
                ''
                .join(item)
                for item
                in zip(*[iter(n)]*len_group)
            ]
        )


with open(f"data/day_02{os.getenv('DEV', '')}.txt") as f:
    data = f.read().splitlines()[0]


# Part I
invalid = []
for _range in data.split(","):
    start_str, end_str = _range.split("-")
    start = int(start_str)
    end = int(end_str)

    # If number of digits is even, we can skip them
    if len(start_str) % 2 != 0:
        if len(start_str) == len(end_str):
            continue
        start = 10 ** len(start_str)

    for n in range(start, end + 1):
        str_n = str(n)
        first = str_n[:len(str_n)//2]
        last = str_n[len(str_n)//2:]
        if first == last:
            invalid.append(n)

print(sum(invalid))

# Part II
invalid = []
for _range in data.split(","):
    start_str, end_str = _range.split("-")
    start = int(start_str)
    end = int(end_str)

    for n in range(start, end + 1):
        str_n = str(n)
        for to_check in split_number(str_n):
            is_invalid = len(set(to_check)) == 1
            if is_invalid:
                invalid.append(n)
                break


print(sum(invalid))
