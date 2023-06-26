def binary_to_string(bits):
    return ''.join([chr(int(i, 2)) for i in bits])

def apply_table(inp, table):
    """
    >>> apply_table("0123456789", list(range(10)))
    '9012345678'
    >>> apply_table("0123456789", list(range(9, -1, -1)))
    '8765432109'
    """
    res = ""
    for i in table:
        res += inp[i-1]
    return res


def left_shift(data):
    """
    >>> left_shift("0123456789")
    '1234567890'
    """
    return data[1:] + data[0]


def xor(a, b):
    """
    >>> xor("01010101", "00001111")
    '01011010'
    """
    res = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            res += "0"
        else:
            res += "1"
    return res


def apply_sbox(s, data):
    row = int("0b" + data[0] + data[-1], 2)
    col = int("0b" + data[1:3], 2)
    return bin(s[row][col])[2:]


def function(expansion, s0, s1, key, message, p4_table):
    left = message[:4]
    right = message[4:]
    temp = apply_table(right, expansion)
    temp = xor(temp, key)
    l = apply_sbox(s0, temp[:4])
    r = apply_sbox(s1, temp[4:])
    l = "0" * (2 - len(l)) + l
    r = "0" * (2 - len(r)) + r
    temp = apply_table(l + r, p4_table)
    temp = xor(left, temp)
    return temp + right


def convert_to_bits(data):
    bits = ""
    for char in data:
        ascii_val = ord(char)
        binary_val = bin(ascii_val)[2:]  # Exclude the "0b" prefix
        bits += binary_val.zfill(8)  # Pad with zeros to ensure each binary representation is 8 bits
    return bits


def convert_to_text(bit_array):
    text = ""
    for i in range(0, len(bit_array), 8):
        byte = "".join(bit_array[i:i + 8])
        decimal_val = int(byte, 2)
        character = chr(decimal_val)
        text += character
    return text


def process_enc(key, message):
    message_bits = format(ord(message), '08b')
    message = message_bits[:8]

    p8_table = [6, 3, 7, 4, 8, 5, 10, 9]
    p10_table = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p4_table = [2, 4, 3, 1]
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    expansion = [4, 1, 2, 3, 2, 3, 4, 1]
    s0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    s1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

    # key generation
    temp = apply_table(key, p10_table)
    left = temp[:5]
    right = temp[5:]
    left = left_shift(left)
    right = left_shift(right)
    key1 = apply_table(left + right, p8_table)
    left = left_shift(left)
    right = left_shift(right)
    left = left_shift(left)
    right = left_shift(right)
    key2 = apply_table(left + right, p8_table)

    # encryption
    temp = apply_table(message, IP)
    temp = function(expansion, s0, s1, key1, temp, p4_table)
    temp = temp[4:] + temp[:4]
    temp = function(expansion, s0, s1, key2, temp, p4_table)
    CT = apply_table(temp, IP_inv)
    return CT



def process_dec(key, message):
    #message_bits = format(ord(message), '08b')
    message = message[:8]

    p8_table = [6, 3, 7, 4, 8, 5, 10, 9]
    p10_table = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p4_table = [2, 4, 3, 1]
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    expansion = [4, 1, 2, 3, 2, 3, 4, 1]
    s0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    s1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

    # key generation
    temp = apply_table(key, p10_table)
    left = temp[:5]
    right = temp[5:]
    left = left_shift(left)
    right = left_shift(right)
    key1 = apply_table(left + right, p8_table)
    left = left_shift(left)
    right = left_shift(right)
    left = left_shift(left)
    right = left_shift(right)
    key2 = apply_table(left + right, p8_table)

    # decryption
    temp = apply_table(message, IP)
    temp = function(expansion, s0, s1, key2, temp, p4_table)
    temp = temp[4:] + temp[:4]
    temp = function(expansion, s0, s1, key1, temp, p4_table)
    PT = apply_table(temp, IP_inv)
    dec=int(PT,2)
    return chr(dec)
    #print("Cipher text is:", CT)

global username,account

def server(cipher):
    data ={
        "IDBI123":500000,
        "IDBI111":450000
    }
    chunk_size = 8
    res = []

    key='1111000010'
    list =str()
    for i in range(0, len(cipher), chunk_size):
     chunk = cipher[i:i+chunk_size]
     list+=process_dec(key, chunk)
    
    if(list[:4]=='IDBI'):
        account=list
        return data[account]
    else:
        username=list 
        return username


      
