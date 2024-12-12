# SimpleStorage Smart Contract

A basic Ethereum smart contract built with Solidity for storing and retrieving salary values and managing employee data. This repository includes a Python deployment script using `web3.py` to interact with the contract and deploy it to a local blockchain.

## Features
- Store and retrieve a single numeric value (`Salary`).
- Add employee records (name and salary).
- Retrieve employee salary using their name.

## Contents
- `SimpleStorage.sol`: The Solidity smart contract.
- `deploy.py`: Python script to deploy and interact with the contract.
- `.env`: File for storing sensitive information like private keys (not included in the repository).
- `requirements.txt`: Python dependencies for running the script.

## Prerequisites
- Python 3.8+
- Node.js (for Ganache)
- Solidity Compiler (`solc`)
- Ganache (local blockchain)

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/web3_simple_storage.git
cd web3_simple_storage
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Add a .env File

Create a .env file in the project root and add your private key:
```bash
PRIVATE_KEY=your_private_key_here
```
### 5. Start Ganache

Run Ganache on your local machine:
```bash
ganache-cli
```
### 6. Deploy the Contract

Run the deploy.py script to compile, deploy, and interact with the contract:
```bash
python deploy.py
```

### Expected Output
	•	Contract deployed at <contract_address>
	•	Initial stored value retrieved: 0
	•	Updated stored value retrieved: 38

## Smart Contract Overview

### SimpleStorage.sol

This contract includes:

	•	Public variable: Salary to store a single value.
	•	Struct: Employee with name and salary.
	•	Array: employees to store a list of Employee records.
	•	Mapping: nameToSalary for quick salary lookups by name.
	•	Functions:
	•	store(uint256 _Salary): Update the Salary.
	•	retrieve(): Retrieve the stored Salary.
	•	addPerson(string memory _name, uint256 _Salary): Add an employee record.

## Python Script Overview

### deploy.py

This script:

	1.	Compiles SimpleStorage.sol using solcx.
	2.	Deploys the contract to a local blockchain (Ganache).
	3.	Interacts with the deployed contract:
	-	Calls retrieve() to fetch the current salary.
	-	Calls store() to update the salary.

Dependencies

	-	web3.py: Interact with Ethereum nodes.
	-	python-dotenv: Load environment variables from .env.
	-	py-solc-x: Compile Solidity contracts.

