from backend.utils.hex_to_binary import hex_to_binary_string

def test_hex_to_binary():
    original_num = 786
    hex_number = hex(original_num)[2:]
    binary_num = hex_to_binary_string(hex_number)
    assert int(binary_num, 2) == original_num