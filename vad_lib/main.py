import requests as rq
from tqdm import tqdm

def main():

    url = "https://drive.usercontent.google.com/download?id=1-DBKQE781Srff7_mjManONfDNU2_UplL&export=download&confirm=t&uuid=c69f5bc5-2fdf-418d-b421-6f9eb333ba9c&at=APZUnTVIhFUteDEZnPOH5dCRMBdH%3A1708075075180"

    resp = rq.get(url, stream=True)

    # Check if the request was successful
    if resp.status_code == 200:
        file_size = int(resp.headers.get('content-length', 0))

        # Initialize the progress bar with the total file size
        progress = tqdm(total=file_size, unit='B', unit_scale=True)

        with open("DeepForest_Model", "wb") as file:
            for chunk in resp.iter_content(chunk_size=1024):
                # Write each chunk of data to the file
                file.write(chunk)
                # Update the progress bar with the size of the current chunk
                progress.update(len(chunk))

        progress.close()
        print("Download complete")
    else:
        print("Failed to download file. Status code:", resp.status_code)