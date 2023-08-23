import hashlib
import json
def crypto_hash(*args):
    # stringified_data = json.dumps(data)
    stringified_data = map(lambda data: json.dumps(data), args)
    
    sorted_data = sorted(stringified_data)
    # return hashlib.sha256(sorted_data.encode("utf-8"))
    joined_data = "".join(sorted_data)
    return hashlib.sha256(joined_data.encode("utf-8")).hexdigest()


def main():
    return print(f'hash - {crypto_hash(["absc", 4, 4, 5])}')

main()