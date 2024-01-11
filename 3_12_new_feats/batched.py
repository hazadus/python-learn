from itertools import batched

for batch in batched([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2):
    print(batch)
