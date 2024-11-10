import os

# Constants
LINPEAS_SCRIPT = "linpeas.sh"
OUTPUT_FILE = "linpeas_output.txt"

def cleanup_files():
    """Delete LinPEAS script and output file."""
    try:
        if os.path.exists(LINPEAS_SCRIPT):
            os.remove(LINPEAS_SCRIPT)
            print(f"Deleted {LINPEAS_SCRIPT}")
        else:
            print(f"{LINPEAS_SCRIPT} does not exist.")

        if os.path.exists(OUTPUT_FILE):
            os.remove(OUTPUT_FILE)
            print(f"Deleted {OUTPUT_FILE}")
        else:
            print(f"{OUTPUT_FILE} does not exist.")
    except Exception as e:
        print(f"Error during cleanup: {e}")

cleanup_files()
