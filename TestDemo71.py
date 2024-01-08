import requests
from clint.textui import progress

url = 'https://www.python.org/ftp/python/3.8.1/python-3.8.1-macosx10.9.pkg'
res = requests.get(url, stream=True)
total_length = int(res.headers.get('content-length'))

with open("py.pkg", "wb") as pypkg:
    for chunk in progress.bar(res.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1, width=100):
        if chunk:
            pypkg.write(chunk)