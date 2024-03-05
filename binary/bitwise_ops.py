# Some bytes to play with
byte1 = int("11110000", base=2)  # 240
byte2 = int("00001111", base=2)  # 15
byte3 = int("01010101", base=2)  # 85

# Print bit-length, which is the number of binary digits:
print(f"{byte1=:08b}", ", bit length:", byte1.bit_length())
print(f"{byte2=:08b}", ", bit length:", byte2.bit_length())
print(f"{byte3=:08b}", ", bit length:", byte3.bit_length())

# Bitwise NOT (Flip the bits)
print(f"~{byte1:08b} = {~byte1 & 255:08b}")  # NB: `& 255` used to solve sign problem

# AND
print(f"{byte1:08b} & {byte2:08b} =", f"{byte1 & byte2:08b}")

# OR
print(f"{byte1:08b} | {byte2:08b} =", f"{byte1 | byte2:08b}")

# XOR
print(f"{byte1:08b} ^ {byte3:08b} =", f"{byte1 ^ byte3:08b}")

# Shifting right will lose the right-most bit
print(f"{byte2:08b} >> 3 = ", f"{byte2 >> 3:08b}")

# Shifting left will add a 0 bit on the right side
print(f"{byte2:08b} << 1 = ", f"{byte2 << 1:08b}")

# See if a single bit is set
bit_mask = int("00000001", base=2)  # Bit 1
print(bit_mask & byte1)  # Is bit set in byte1?
print(bit_mask & byte2)  # Is bit set in byte2?

# Rotate bits
bit_mask = int("10000000", base=2)
for _ in range(8):
    print(f"{bit_mask:08b}")
    bit_mask >>= 1
