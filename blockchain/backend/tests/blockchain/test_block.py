from backend.blockchain.block import Block, genesis_data
from backend.config import MineRate,SECOND
import time
import pytest
genesis = Block.genesis()
def test_block():
    assert isinstance(genesis, Block)
    # for key, value in genesis_data.items():
    #     getattr(genesis, key)== value
    assert genesis.timestamp == genesis_data["timestamp"]
    assert genesis.lasthash == genesis_data["lasthash"]
    assert genesis.hash == genesis_data["hash"]
    assert genesis.data == genesis_data["data"]
def test_mineblock():
    lastblock = Block.genesis()
    data = 'test_data'
    mineblock = Block.mineblock(lastblock, data)
    assert isinstance(mineblock, Block)
    assert mineblock.data == data
    assert mineblock.lasthash == lastblock.hash

# from Backend.BlockChain.block import block, GENESIS_data
# from Backend.config import MINE_RATE,SECONDS
# import time
# import pytest
# from Backend.BlockChain.block import GENESIS_data

# def test_genesis():
#     genesis = block.genesis()
#     assert isinstance(genesis,block)
#     assert genesis.timestamp == GENESIS_data['timestamp']
#     assert genesis.last_hash == GENESIS_data['last_hash']
#     assert genesis.hash == GENESIS_data['hash']
#     assert genesis.data == GENESIS_data['data']
#     for key,value in GENESIS_data.items():
#         getattr(genesis,key)==value

# def test_mine_block():
#     last_block = block.genesis()
#     data = 'Test_data'
#     mined_block = block.mine_block(last_block,data)
#     assert isinstance(mined_block,block)
#     assert mined_block.data == data
#     assert mined_block.last_hash == last_block.hash

def test_quickly_mined_block():
    lastblock = Block.mineblock(Block.genesis(),'10')
    mineblock =Block.mineblock(lastblock,'50')
    assert mineblock.difficulty == lastblock.difficulty +1

def test_slowly_mined_block():
    lastblock = Block.mineblock(Block.genesis(),'10')
    time.sleep(MineRate/SECOND)
    mineblock =Block.mineblock(lastblock,'50')
    assert mineblock.difficulty == lastblock.difficulty -1

def test_mined_block_difficulty_limit_1():
    lastblock = Block(time.time_ns(),'test_last_hash','test_hash','Sukuna',1,0)
    time.sleep(MineRate/SECOND)
    mineblock = Block.mineblock(lastblock,"10")
    assert mineblock.difficulty == 1

@pytest.fixture
def lastblock():
    return Block.genesis()

@pytest.fixture
def mineblock(lastblock):
    mineblock = Block.mineblock(lastblock,'quake quake fruit')
    return mineblock

def test_is_valid(lastblock,mineblock):
    Block.is_valid(lastblock,mineblock)

def test_is_valid_block_bad_last_hash(lastblock,mineblock):
    mineblock.lasthash = 'barbad_hai_hash'
    with pytest.raises(Exception,match='the block last_hash must be correct'):
        Block.is_valid(lastblock,mineblock)
def test_is_valid_bad_Pow(lastblock,mineblock):
    mineblock.hash='fff'
    with pytest.raises(Exception,match="the block difficulty must only adjust by 1"):
        Block.is_valid(lastblock,mineblock)
def test_is_valid_bad_block_hash(lastblock,mineblock):
    mineblock.hash='0000000000abc'
    with pytest.raises(Exception,match='The block hash must be same'):
        Block.is_valid(lastblock,mineblock)
def test_is_valid_block_jumped_difficulty(lastblock, mineblock):
    jumped_difficulty=10
    mineblock.difficulty=jumped_difficulty
    mineblock.hash=f"{'0'*jumped_difficulty}abc"
    with pytest.raises(Exception,match='The proof of work requirement is not met'):
        Block.is_valid(lastblock, mineblock)
                       
                    