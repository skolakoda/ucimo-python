import requests

link = "https://api.lyrics.ovh/v1/shakira/waka-waka"
response = requests.get(link)

print response.text
