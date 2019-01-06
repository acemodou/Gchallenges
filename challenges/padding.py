"""Implement a function that takes two arguments: first an integer,
block_size, and second, an arbitrarily long string.
It outputs a string where the string’s length is always a multiple of block_size.
It should do this by appending a "padding" to the end of the string.
All characters in the padding should be the same.
The character to use should be the length of the padding, e.g. "1", "22," "333," and so on.
If the input string's length is already a multiple of block_size,
append a new block completely consisting of padding.
"""


def padding(block_size, input):
    if block_size <= 0:
        return "Block size can't be less than or equal to 0 but is {}".format(block_size)
    result = len(input) % block_size
    output = (block_size - result)
    for x in range(output):
        input +=str(output)
    return input

def cryptography(b_s,input):
    pad_len = b_s - len(input) % b_s
    return input + str(pad_len) * pad_len



str1 = cryptography(4, 'hello')
print(str1)