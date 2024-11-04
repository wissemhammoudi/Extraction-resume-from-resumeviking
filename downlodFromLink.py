import requests
import os
# Define the path to your text file
url_file = 'resume_templates.txt'
# Define the directory to save the downloaded files
download_dir = 'downloads'
# Create the download directory if it doesn't exist
os.makedirs(download_dir, exist_ok=True)
# Read the URLs from the file
with open(url_file, 'r') as file:
    urls = file.readlines()
# Download each file
for url in urls:
    url = url.strip()  # Remove any leading/trailing whitespace
    if url:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for request errors
            # Extract the filename from the URL
            filename = url.split('/')[-1]
            file_path = os.path.join(download_dir, filename)
            # Save the PDF file
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f'Downloaded: {filename}')
        except requests.RequestException as e:
            print(f'Failed to download {url}: {e}')
