import requests, subprocess

def download_file(url, destination):
    resp= requests.get(url)
    with open (destination, 'wb') as output:
        output.write(resp.content)

        