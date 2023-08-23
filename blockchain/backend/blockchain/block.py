import time
from backend.utils.crypto_hash import crypto_hash
from backend.config import MineRate
from backend.utils.hex_to_binary import hex_to_binary_string
genesis_data = {
    "timestamp" : 1, 
    "lasthash" : "0000", 
    "hash" : "genesis_block_hash", 
    "data" : [],
    "difficulty" : 3,
    "nonce" : "gen nonce"
    }
class Block ():
    def __init__(self,timestamp, lasthash, hash, data, difficulty, nonce):
        self.data = data
        self.timestamp = timestamp
        self.lasthash = lasthash
        self.hash = hash
        self.difficulty = difficulty
        self.nonce = nonce
    def __repr__(self):
        return (
                'Block('
                f"timestamp-{self.timestamp}"
                f"lasthash-{self.lasthash}"
                f"hash-{self.hash}"
                f"data-{self.data}"
                f"difficulty-{self.difficulty}"
                f"nonce-{self.nonce}"
                )
    def __eq__(self, others):
        return self.__dict__ == others.__dict__
    def to_json(self):
        return self.__dict__
    
    @ staticmethod
    def mineblock(lastblock, data):
        timestamp = time.time_ns()
        lasthash = lastblock.hash

        hash = crypto_hash(data, timestamp, lasthash)
        difficulty = Block.adjustdifficulty(lastblock, timestamp)
        nonce = 0
        while hex_to_binary_string(hash)[0:difficulty]!='0'*difficulty:
            nonce+=1
            timestamp = time.time_ns()
            difficulty=Block.adjustdifficulty(lastblock,timestamp)
            hash = crypto_hash(data,timestamp,lasthash,difficulty,nonce)

           
        return Block(timestamp, lasthash, hash, data, difficulty, nonce)
    @staticmethod
    def genesis():
        return Block(**genesis_data)
    @staticmethod
    def adjustdifficulty(lastblock, new_timestamp):
        if (new_timestamp- lastblock.timestamp) < MineRate:
            return lastblock.difficulty+1
        if (lastblock.difficulty-1)>0:
            return lastblock.difficulty-1
        return 1
    @staticmethod
    def is_valid(lastblock,mineblock):
        new_hash = crypto_hash(mineblock.timestamp,mineblock.lasthash,mineblock.data,mineblock.difficulty,mineblock.nonce)
        if mineblock.lasthash != lastblock.hash:
            raise Exception('the block last_hash must be correct')
        if hex_to_binary_string(mineblock.hash)[0:mineblock.difficulty] != '0' * mineblock.difficulty:
            raise Exception('the block difficulty must only adjust by 1')
        if abs(mineblock.difficulty-lastblock.difficulty) >1:
            raise Exception('The proof of work requirement is not met')
        if new_hash != mineblock.hash:
            raise Exception('The block hash must be same')

# def main():
#     genesis_block = block.genesis()
#     bad_block = block.mine_block(genesis_block,'Son God-Nika')
#     bad_block.last_hash = 'Galaxy Impact'
#     try:
#         block.is_valid(genesis_block,bad_block)
#     except Exception as e:
#         print(f'is_valid_function: {e}')


# genesis_block = Block.genesis()
# x_var = Block.mineblock(genesis_block, 'vinsmoke')
# print(x_var)
# # @ staticmethod    
# def mineblock(lastblock, data):
#     timestamp = time.time_ns()
#     lasthash = lastblock.hash
#     hash = crypto_hash(data, timestamp, lasthash)
#     return Block(timestamp, lasthash, hash, data)

# @staticmethod
# def genesis():
#     return Block(1,"0000", "genesis_block_hash", [])
# genesis_block = genesis()
# x_var = mineblock(genesis_block, 'vinsmoke')
# print(x_var)
