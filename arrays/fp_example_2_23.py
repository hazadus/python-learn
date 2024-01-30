# Fluent Python ex.2.10
# Working with a `deque`
from collections import deque

# The optional maxlen argument sets the maximum number of items allowed
# in this instance of `deque`:
dq = deque(range(10), maxlen=10)
print(f"{dq=}")

# Rotating with n > 0 takes items from the right end and prepends them to the
# left; when n < 0 items are taken from left and appended to the right:
dq.rotate(3)
print(f"{dq=}")

dq.rotate(-6)
print(f"{dq=}")

# Appending to a deque that is full discards items from the other end:
dq.appendleft(-1)
print(f"{dq=}")

# Adding three items to the right pushes out the leftmost -1, 1, and 2:
dq.extend([11, 22, 33])
print(f"{dq=}")

# Note that `extendleft(iter)` works by appending each successive item of the
# `iter` argument to the left of the deque, therefore the final position of the
# items is reversed:
dq.extendleft([10, 20, 30, 40])
print(f"{dq=}")
