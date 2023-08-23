from backend.blockchain.block import Block
class Blockchain():
    def __init__(self):
        self.chain = [Block.genesis()]
    def addblock(self, data):
        self.chain.append(Block.mineblock(self.chain[-1], data ))
    def __repr__(self):
        return f"Blockchain - {self.chain}"
    def replace_chain(self, chain):
        if len(chain)<=len(self.chain):
            raise Exception('Cannot Replace, the incoming chain must be longer')
        try:
            Blockchain.is_valid_chain(chain)
        except:
            raise Exception(f'cannot replace, the incomming chain is invalid')
        
        self.chain = chain
    def to_json(self):
        serialized_chain = []
        for block in self.chain:
            serialized_chain.append(block.to_json)
        return serialized_chain
    @staticmethod
    def is_valid_chain(chain):
        if chain[0] != Block.genesis():
            raise Exception("the Genesis block must be valid")
        for i in range (1, len(chain)):
            block = chain[i]
            lastblock = chain[i-1]
            Block.is_valid(lastblock, block)
            
if __name__ == "__main__":
    x = Blockchain()
    x.addblock(5)
    x.addblock(3)  
    x.addblock(4)
    # x.is_valid_chain(x.chain)
    # print(x)
print(f"blockchain.py-__name__-{__name__}")
