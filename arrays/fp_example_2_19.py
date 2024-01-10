from array import array
from random import random
from time import perf_counter

# Create an array of double-precision floats (typecode 'd')
# from generator expression:
t0 = perf_counter()
floats = array("d", (random() for _ in range(10**7)))
print(f"Array created in {perf_counter()-t0:.4f} s")

# Inspect the last number in the array:
t0 = perf_counter()
print(floats[-1])
print(f"Access last element in {perf_counter()-t0:.8f} s")

# Save the array to a binary file:
t0 = perf_counter()
fp = open("floats.bin", "wb")
floats.tofile(fp)
fp.close()
print(f"Save the array to a binary file in {perf_counter()-t0:.4f} s")

# Create empty array of doubles and read 10**7 numbers from file:
t0 = perf_counter()
floats2 = array("d")
fp = open("floats.bin", "rb")
floats2.fromfile(fp, 10**7)
fp.close()
print(f"Read 10**7 numbers from file in {perf_counter()-t0:.4f} s")

print(f"floats == floats2: {floats == floats2}")
