import time

from blockchain import Blockchain
from user import User

# Initialize blockchain
medical_chain = Blockchain()

# Add users
medical_chain.add_user("user123", "Alice", "Patient")
medical_chain.add_user("doctor_1", "Dr. Smith", "Doctor")

# Encrypt and add a medical record block
medical_data = "Blood glucose level: 5.5 mmol/L"
encrypted_data = medical_chain.encrypt_data(medical_data)

block_data = {
    "user_id": "user123",
    "medical_record_id": "rec456",
    "record_type": "lab_result",
    "description": "Blood test for glucose",
    "data": encrypted_data,
    "timestamp": time.time(),
    "created_by": "doctor_1",
    "status": "Finalized",
    "version": 1,
    "permissions": ["doctor_1"],
    "access_logs": []
}

# Verify and add block to the blockchain
verification_data = 7  # Assume this is the patient's identifier for ZKP
medical_chain.createBlock(block_data, verification_data)

# Display blocks for a specific user
user_blocks = medical_chain.viewUser("user123")
print("\nUser's Blocks:")
for block in user_blocks:
    print(block)

# Attempt to view decrypted data with permission
user = medical_chain.users["doctor_1"]
if medical_chain.authorize_user(block_data, user):
    print("\nAuthorized access. Decrypting data...")
    decrypted_data = medical_chain.decrypt_data(block_data["data"])
    print("Decrypted Data:", decrypted_data)
else:
    print("Unauthorized access. Cannot decrypt data.")
