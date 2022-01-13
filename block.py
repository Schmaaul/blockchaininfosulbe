
from hashlib import sha256
import json

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

    def to_string(self):
        returnString = ""
        returnString += "INDEX  : " +str(self.index) +"\n"
        returnString += "TRANS  : "
        if len(self.transactions) == 0: 
            returnString += "NONE\n"
        else: 
            returnString += "\n"
        index = 1
        for transaction in self.transactions:
            returnString += "      " + str(index) +". " +str(transaction)
            index += 1
        returnString += "TIME   : " + str(self.timestamp) +"\n"
        returnString += "PREHASH: " + self.previous_hash +"\n"
        returnString += "NONCE  : " + str(self.nonce) +"\n"
        returnString += "HASH   : " + self.compute_hash()
        
        return returnString

