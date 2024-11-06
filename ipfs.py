import ipfshttpclient

client = ipfshttpclient.connect("https://ipfs.infura.io:5001/api/v0")

def upload_to_ipfs(filepath):
    """
    Uploads a file to IPFS via Infura and returns the CID.
    """
    try:
        res = client.add(filepath)
        print("File uploaded to IPFS with CID:", res['Hash'])
        return res['Hash']
    except Exception as e:
        print("An error occurred during upload:", e)
        return None

def download_from_ipfs(cid, output_path):
    """
    Downloads a file from IPFS given its CID and saves it to the specified path.
    """
    try:
        client.get(cid, target=output_path)
        print("File downloaded from IPFS to:", output_path)
    except Exception as e:
        print("An error occurred during download:", e)