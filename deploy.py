import json
from web3 import Web3
from solcx import compile_standard, install_solc
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read the Solidity file
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Install Solidity compiler
install_solc("0.6.0")
print("Solidity compiler installed.")

# Compile the Solidity contract
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)

# Save the compiled contract to a JSON file
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# Extract Bytecode and ABI
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# Connect to local blockchain (Ganache)
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
address = "0x85145D9E28FB228E2be58F2231eE85e4CA05c8B8" 
private_key = os.getenv("PRIVATE_KEY")  

# Print private key for debugging
print(f"Using private key: {private_key}")

# Create the contract object
SimpleStorage = web3.eth.contract(abi=abi, bytecode=bytecode)

# Get the latest transaction count (nonce)
nonce = web3.eth.get_transaction_count(address)

# Build the transaction to deploy the contract
transaction = SimpleStorage.constructor().build_transaction(
    {
        "chainId": chain_id,
        "gasPrice": web3.eth.gas_price,
        "from": address,
        "nonce": nonce,
    }
)

# Sign the transaction
signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)

# Send the transaction
print("Deploying Contract...")
tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
print("Waiting for transaction to finish...")
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Done! Contract deployed at {tx_receipt.contractAddress}")

# Interact with the deployed contract
simple_storage = web3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# Retrieve the initial stored value
print(f"Initial Stored Value: {simple_storage.functions.retrieve().call()}")

# Build a transaction to store a new value
greeting_transaction = simple_storage.functions.store(38).build_transaction(
    {
        "chainId": chain_id,
        "gasPrice": web3.eth.gas_price,
        "from": address,
        "nonce": nonce + 1,
    }
)

# Sign and send the transaction
signed_greeting_txn = web3.eth.account.sign_transaction(greeting_transaction, private_key=private_key)
tx_greeting_hash = web3.eth.send_raw_transaction(signed_greeting_txn.raw_transaction)

print("Updating stored value...")
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_greeting_hash)

# Retrieve the updated value
updated_value = simple_storage.functions.retrieve().call()
print(f"Updated Stored Value: {updated_value}")