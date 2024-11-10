import subprocess
import requests
import os

# Constants
LINPEAS_URL = "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh"
LINPEAS_SCRIPT = "linpeas.sh"
OUTPUT_FILE = "linpeas_output.txt"

def download_linpeas():
    """Download the latest LinPEAS script."""
    print(f"Downloading LinPEAS from {LINPEAS_URL}...")
    response = requests.get(LINPEAS_URL, stream=True)
    if response.status_code == 200:
        with open(LINPEAS_SCRIPT, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        # Make the script executable
        os.chmod(LINPEAS_SCRIPT, 0o755)
        print(f"Downloaded and saved as {LINPEAS_SCRIPT}")
    else:
        print(f"Failed to download LinPEAS. Status code: {response.status_code}")

def run_linpeas():
    """Execute LinPEAS script and save the output to a file."""
    print(f"Running LinPEAS and saving output to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w') as output_file:
        # Run LinPEAS
        subprocess.run(["./" + LINPEAS_SCRIPT], stdout=output_file, stderr=subprocess.PIPE, text=True)
    print(f"LinPEAS output saved to {OUTPUT_FILE}")

def main():
    download_linpeas()
    run_linpeas()

if __name__ == "__main__":
    main()
