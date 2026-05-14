import urllib.request
import re
import zipfile

url = "https://nightly.link/packwiz/packwiz/workflows/go/main"
print("Fetching nightly.link HTML...")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode()

match = re.search(r'href="(.*?Windows.*?\.zip)"', html, re.IGNORECASE)
if match:
    download_url = match.group(1)
    print("Found URL:", download_url)
    urllib.request.urlretrieve(download_url, "packwiz.zip")
    with zipfile.ZipFile("packwiz.zip", 'r') as z:
        z.extractall(".")
    print("Packwiz successfully downloaded and extracted.")
else:
    print("Could not find Windows zip link.")
