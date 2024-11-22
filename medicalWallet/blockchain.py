from block import Block
from zkp import zero_knowledge_proof
from user import User
import time
from cryptography.fernet import Fernet

class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.users = {}
        self.difficulty = difficulty
        self.create_genesis_block()
        self.key = Fernet.generate_key()  # For encrypting medical data
        self.cipher_suite = Fernet(self.key)

    def create_genesis_block(self):
        genesis_block = Block(0, "0", "Genesis Block")
        self.chain.append(genesis_block)

    def add_user(self, user_id, name, role):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, name, role)
        else:
            print("User already exists.")

    def createBlock(self, data, verification_data):
        if not self.verifyTransaction(verification_data):
            print("Transaction verification failed.")
            return None
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, data)
        self.mineBlock(new_block)
        self.chain.append(new_block)
        return new_block

    def mineBlock(self, block):
        while not block.hash.startswith('0' * self.difficulty):
            block.timestamp = time.time()
            block.hash = block.compute_hash()
        print(f"Block mined: {block.hash}")

    def verifyTransaction(self, x):
        return zero_knowledge_proof(x)

    def encrypt_data(self, data):
        return self.cipher_suite.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        return self.cipher_suite.decrypt(encrypted_data).decode()

    def viewUser(self, user_id):
        return [block.data for block in self.chain if 'user_id' in block.data and block.data['user_id'] == user_id]

    def log_access(self, transaction, user_id, action):
        access_entry = {
            "accessed_by": user_id,
            "timestamp": time.time(),
            "action": action
        }
        transaction["access_logs"].append(access_entry)

    def authorize_user(self, transaction, user):
        return user.user_id in transaction["permissions"]

    def filter_records(self, user_id=None, record_type=None, status=None):
        return [
            block.data for block in self.chain
            if (not user_id or block.data.get("user_id") == user_id) and
               (not record_type or block.data.get("record_type") == record_type) and
               (not status or block.data.get("status") == status)
        ]
