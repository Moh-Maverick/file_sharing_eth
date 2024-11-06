from web3 import Web3
import json

#Set up Infura URL for Ethereum (e.g., Goerli testnet)
INFURA_URL = 'https://goerli.infura.io/v3/28d01c2d4cc3439db97c3cc5c1704049'  # Replace with your Infura project ID
ACCOUNT = '0x723Ead59341dA4cd907067497034B5EB8b788d15'  # Replace with your Ethereum account address
PRIVATE_KEY = '0x692f6ae10c4ec511e69b81e846d71485181bd4cc12941ee97d7110c51defc6a8'  # Replace with your Ethereum private key

#Connect to Ethereum via Infura
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

#Ensure connection is successful
if web3.isConnected():
    print("Connected to Ethereum network via Infura!")

def store_file_metadata(cid, filename):
    """
    Stores file metadata (CID and filename) in a simple Ethereum transaction.
    """
    # Encode the metadata into a JSON string
    metadata = json.dumps({"cid": cid, "filename": filename})

    # Build the transaction
    nonce = web3.eth.get_transaction_count(ACCOUNT)
    txn = {
        'to': ACCOUNT,  # Sending transaction to the same account (just as an example)
        'value': 0,  # No Ether involved
        'data': web3.toHex(text=metadata),  # Attach metadata as hex data
        'gas': 2000000,
        'gasPrice': web3.toWei('20', 'gwei'),
        'nonce': nonce,
    }

    # Sign the transaction
    signed_txn = web3.eth.account.sign_transaction(txn, PRIVATE_KEY)

    # Send the transaction
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

#Wait for the transaction receipt
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    print("Metadata stored on Ethereum with transaction hash:", tx_receipt.transactionHash.hex())
    return tx_receipt.transactionHash.hex()