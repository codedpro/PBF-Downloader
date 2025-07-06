import os
import requests
from tqdm import tqdm
from itertools import product

# Base URL
BASE_URL = "https://gnaf2.post.ir/tile/layers/group/16/{}/{}.pbf"

# Output directory
OUTPUT_DIR = "pbf_files"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Log file for errors
ERROR_LOG_FILE = "error_log.txt"

# Define the range for the two 5-digit numbers
START, END = 10000, 99999

# Number of parallel threads (adjust based on network capacity)
NUM_THREADS = 10


def download_file(x, y):
    """
    Downloads the PBF file for the given x and y values.
    Saves the file immediately and logs any errors.
    """
    url = BASE_URL.format(x, y)
    file_path = os.path.join(OUTPUT_DIR, f"{x}_{y}.pbf")
    
    # Skip if the file already exists
    if os.path.exists(file_path):
        return f"Skipped: {file_path} (already exists)"
    
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            # Write the response to a file in chunks to avoid memory usage
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:  # Filter out keep-alive chunks
                        file.write(chunk)
            return f"Downloaded: {file_path}"
        else:
            status = f"Failed: {url} - Status Code: {response.status_code}"
            log_status(status)
            return status
    except Exception as e:
        status = f"Error: {url} - {e}"
        log_status(status)
        return status


def log_status(message):
    """
    Writes a status message to the log file immediately.
    """
    with open(ERROR_LOG_FILE, "a") as log_file:
        log_file.write(message + "\n")


def process_combinations(start, end):
    """
    Processes all combinations of x and y in the range using minimal memory.
    """
    total_combinations = (end - start + 1) ** 2
    progress_bar = tqdm(total=total_combinations, desc="Downloading files")
    
    for x, y in product(range(start, end + 1), repeat=2):
        status = download_file(f"{x:05}", f"{y:05}")
        progress_bar.update(1)
        print(status)

    progress_bar.close()


# Start processing
process_combinations(20000, 99999)  # Example subset for testing
