import binascii

# Starting with a hex string you can unhexlify it to bytes
deadbeef = binascii.unhexlify("DEADBEEF")
print(deadbeef, len(deadbeef))
print(deadbeef.hex())

# Given raw bytes, get an ASCII string representing the hex values
hex_data = binascii.hexlify(b"\x00\xff")  # Two bytes values 0 and 255
print(hex_data, len(hex_data))

# The resulting value will be an ASCII string but it will be a bytes type
# It may be necessary to decode it to a regular string
text_string = hex_data.decode("utf-8")  # Result is string "00ff"
print(text_string)
