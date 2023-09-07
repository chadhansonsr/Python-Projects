import hashlib
import time


class Block:
    def __init__(self, data, previous_hash, next=None):
        self.timestamp = time.gmtime()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = next

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"{self.timestamp}-{self.data}-{self.previous_hash}".encode('utf-8')  # noqa
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self, head=None, next=None):
        self.head = head
        self.next = next

    def add_block(self, data):
        if self.head is None:
            self.head = Block(data, None)
        else:
            current = self.head
            while current.next:
                current = current.next
            previous_hash = current.hash
            current.next = Block(data, previous_hash)

    def print_block(self):
        if self.head is None:
            print("The blockchain is empty.")
            quit()
        else:
            current = self.head
        while current:
            print("Data: ", current.data)
            print("Hash: ", current.hash)
            print("Previous hash: ", current.previous_hash)
            print("Time: ", time.strftime("%a, %d %b %Y %I:%M:%S %p GMT", time.gmtime()))  # noqa
            current = current.next


print("Test 1")

my_blockchain = BlockChain()
my_blockchain.add_block("block1")
my_blockchain.add_block("block2")
my_blockchain.add_block("block3")

print(my_blockchain.print_block())

print("Test 2")

my_blockchain2 = BlockChain()
my_blockchain2.add_block(99 * 99)
my_blockchain2.add_block(99 / 99)
my_blockchain2.add_block(99 % 99)

print(my_blockchain2.print_block())

print("Test 3")

my_blockchain3 = BlockChain()
my_blockchain3.add_block(2)
my_blockchain3.add_block("2")
my_blockchain3.add_block("two")

print(my_blockchain3.print_block())
