import string

alphabet = " " + string.ascii_lowercase
positions = {alphabet[i] : i for i in range(27)}
print(positions["n"])
message = "hi my name is caesar"
def encode(message, key):
    return ''.join([alphabet[(positions[c] + key) % 27] for c in message])
print(encode(message, 3))
decoded_message = encode(encode(message, 3),-3)
print(decoded_message)