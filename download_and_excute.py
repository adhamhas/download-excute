import requests
import os

def download_file(url, destination):
    try:
        with requests.get(url, stream=True, timeout=10) as resp:
            resp.raise_for_status()

            total_size = int(resp.headers.get('content-length', 0))
            content_type = resp.headers.get('Content-Type', 'unknown')
            print(f"[+] Downloading from: {url}")
            print(f"[+] Content-Type: {content_type}")
            print(f"[+] Saving to: {destination} ({total_size} bytes)")

            with open(destination, 'wb') as output:
                for chunk in resp.iter_content(chunk_size=8192):
                    if chunk:
                        output.write(chunk)

            print("[✓] Download completed successfully.")

    except requests.exceptions.RequestException as e:
        print(f"[✗] Download failed: {e}")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
