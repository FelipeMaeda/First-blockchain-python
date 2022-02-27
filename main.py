from datetime import datetime
from hashlib import sha256

# Definition of the Block class
class Block():
    """Main CLass of the Block. Here is where the block is created."""
    def __init__(self):
        """The data and metadata that the Block must contain."""
        self.transactions = transactions
        self.previus_hash = previus_hash
        self.nonce - 0
        self.timestamp = datetime.now()
        self.hash = self.generate_hash()

    def print_content(self):
        """Print of data and metadata of the Block."""
        print(f'Timestamp: {self.timestamp}'
              f'Transactions: {self.transactions}'
              f'Current Hash: {self.hash}'
              f'Previous Hash: {self.previus_hash}'
              )

    def generate_hash(self):
        """Generate unique Hash for the Block."""
        block_contents = str(self.timestamp) + str(self.transactions) + str(self.previus_hash) + str(self.nonce)
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()

# Definition of the Blockchain class
class Blockchain():
    def __init__(self):
        self.chain = []
        self.all_transaction = []
        self.genesis_block()

    def genesis_block(self):
        transactions = []
        previous_hash = 0
        self.chain.append(Block(transactions, previous_hash))

    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print(f'Block {i} {current_block}')
            current_block.print_content()

    def add_block(self, transactions):
        previous_block_hash = self.chain[len(self.chain)-1].hash
        new_block = Block(transactions, previous_block_hash)
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1,len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.generate_hash():
                print(f'The current hash of the block does not equal the generated hash of the block.')
                return False
            if previous.hash != previous.generate_hash():
                print(f'The previous block\'s hash does not equal the previous hash value stored in the current block.')
                return False
        return True

        def proof_of_work(self, block, difficulty=2):
            proof = block.generate_hash()
            while proof[:difficulty] != '0'*difficulty:
                block.nonce += 1
                proof = block.generate_hash()
            block.nonce = 0
            return proof
