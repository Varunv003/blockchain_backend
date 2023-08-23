from backend.utils import crypto_hash
hex_to_binary_conversion_table = {
    "0" : "0000", 
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100", 
    "5"  : "0101",
    "6"  : "0110",
    "7"  : "0111",
    "8"  : "1000", 
    "9"  : "1001",
    "a"  : "1010",
    "b"  : "1011",
    "c"  : "1100",
    "d"  : "1101",
    "e"  : "1110",
    "f"  : "1111",
}
def hex_to_binary_string(hex_string):
    binary_string = ""
    for char in hex_string:
        binary_string += hex_to_binary_conversion_table[char]
    return binary_string

def main():
    number = 451
    hexadecimal_no = hex(number)
    hexadecimal_no=hexadecimal_no[2:]
    print(hexadecimal_no)
    hash = crypto_hash.crypto_hash(hexadecimal_no)
    print(hash)
    print(hex_to_binary_string(hash))
    print(len(hex_to_binary_string(hash)))
    # print(int(hex_to_binary_string(hexadecimal_no),2))

if __name__ == '__main__':
    main()