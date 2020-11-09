
def encode_binary_string(s):
    return(' '.join(format(x, 'b') for x in bytearray(s, 'utf-8')))
    

def decode_binary_string(s):
    return ("".join([chr(int(binary, 2)) for binary in s.split(" ")]))




