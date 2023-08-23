from backend.blockchain.blockchain import Blockchain
from flask import Flask, jsonify
app = Flask(__name__)
blockchain = Blockchain()
for i in range(3):
    blockchain.addblock(i)

@app.route('/test')
def test():
    return 'this is a test'
@app.route('/')
def route_default():
    return "Welcome to blockchain"
@app.route("/blockchain")
def route_blockchain():
    return jsonify(blockchain.to_json())

@app.route("/Blockchain/mine")
def route_mine():
    transaction_data="True Demon Lord"
    blockchain.addblock(transaction_data)
    return jsonify(blockchain.chain[-1].to_json())

app.run(port=5001)


# publishkey = pub-c-2b56007e-fa4a-43fc-ba44-572e0bbd7d33 
# subscribekey = sub-c-95bda9ee-e37d-4a42-aa40-31cd4b3e020e
# userid = varunvij000@gmail.com