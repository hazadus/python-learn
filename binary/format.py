a_byte = b"\xff"  # 255
# Format strings require an integer value so the byte will have to be converted to an integer first.
i = ord(a_byte)  # Get the integer value of the byte

bin_ = "{0:b}".format(i)  # binary: 11111111
hex_ = "{0:x}".format(i)  # hexadecimal: ff
oct_ = "{0:o}".format(i)  # octal: 377

print(bin_)
print(hex_)
print(oct_)

# Same output with f-strings:
print(f"{i:b}")
print(f"{i:x}")
print(f"{i:o}")
