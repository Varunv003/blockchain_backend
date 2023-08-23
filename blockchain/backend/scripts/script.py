from backend.blockchain.blockchain import Blockchain
from backend.blockchain.block import Block 
import time
from backend import config
blockchain = Blockchain()
timer = []
mine_rate = 0
for i in range(100):
    start_time = time.time_ns()
    blockchain.addblock(i)
    end_time = time.time_ns()
    time_to_mine = (end_time - start_time)/config.SECOND
    timer.append(time_to_mine)
    average_mine_rate = sum(timer)/len(timer)
    last_block = blockchain.chain[-1]
    print(
        f"difficulty-{last_block.difficulty}\n"
        f"time_to_mine-{time_to_mine}\n"
        f"average_mine_rate-{average_mine_rate}")
