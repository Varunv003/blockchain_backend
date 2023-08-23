from backend.utils.crypto_hash import crypto_hash
def test_cryptohash():
    assert crypto_hash(3, [4], 5) == crypto_hash(5, [4], 3)
    # assert crypto_hash('x', (5), 10)[0] == "4"

