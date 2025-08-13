import requests
import os

url_file = 'resume_templates.txt'
download_dir = 'downloads'
os.makedirs(download_dir, exist_ok=True)
with open(url_file, 'r') as file:
    urls = file.readlines()
for url in urls:
    url = url.strip()  
    if url:
        try:
            response = requests.get(url)
            response.raise_for_status()  
            filename = url.split('/')[-1]
            file_path = os.path.join(download_dir, filename)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f'Downloaded: {filename}')
        except requests.RequestException as e:
            print(f'Failed to download {url}: {e}')
