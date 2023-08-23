from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import genesis_data
import pytest
def test_blockchain_instance():
    blockchain = Blockchain()
    assert blockchain.chain[0].hash == genesis_data["hash"]
def test_addblock():
    blockchain = Blockchain()
    data = "test_data"
    blockchain.addblock(data)
    assert blockchain.chain[-1].data == data
@pytest.fixture
def blockchain_three_blocks():
    blockchain_three_blocks = Blockchain()
    for i in range(3):
        blockchain_three_blocks.addblock(i)
    return blockchain_three_blocks
def test_is_valid_chain(blockchain_three_blocks):
    Blockchain.is_valid_chain(blockchain_three_blocks.chain)
def test_is_valid_chain_bad_genesis(blockchain_three_blocks):
    blockchain_three_blocks.chain[0].hash = 'celestial_dragon_hash'
    with pytest.raises(Exception, match = 'the Genesis block must be valid'):
        Blockchain.is_valid_chain(blockchain_three_blocks.chain)
def test_replace_chain(blockchain_three_blocks):
    blockchain = Blockchain()
    with pytest.raises(Exception,match='Cannot Replace, the incoming chain must be longer'):
        blockchain_three_blocks.replace_chain(blockchain.chain)
def test_replace_chain_evil_hash(blockchain_three_blocks):
    blockchain = Blockchain()
    blockchain_three_blocks.chain[1].hash = 'evil hash'
    with pytest.raises(Exception, match='cannot replace, the incomming chain is invalid'):
        blockchain.replace_chain(blockchain_three_blocks.chain)
def test_replace_chain_2(blockchain_three_blocks):
    blockchain = Blockchain()
    blockchain.replace_chain(blockchain_three_blocks.chain)
    assert blockchain.chain == blockchain_three_blocks.chain

