from ipfs import upload_to_ipfs, download_from_ipfs
from eth import store_file_metadata


def upload_file(filepath):
    """
    Uploads a file to IPFS via Infura, then stores its CID and name on Ethereum.
    """
    # Step 1: Upload file to IPFS
    cid = upload_to_ipfs(filepath)
    if not cid:
        return

    filename = filepath.split('/')[-1]  # Extract the filename from the path

    # Step 2: Store file metadata on Ethereum (using simple transaction with CID and filename)
    tx_hash = store_file_metadata(cid, filename)
    print("File metadata stored on Ethereum with transaction hash:", tx_hash)

    return cid

def download_file(cid, output_path):
    """
    Downloads the file from IPFS using its CID.
    """
    download_from_ipfs(cid, output_path)

#Example usage
if __name__ == "__main__":
    # To upload a file
    upload_file_path = "File/test.txt"
    cid = upload_file(upload_file_path)  # Replace with your file path

    # To download a file using its CID from IPFS
    if cid:
        print("File uploaded successfully with CID:", cid)

        download_file_path = "downloaded_file.txt"

        download_file(cid, download_file_path)
        print("File Succesfully Downloaded to", download_file_path)