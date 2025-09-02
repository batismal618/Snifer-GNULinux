import requests
from bs4 import BeautifulSoup

url = "https://connect.ed-diamond.com/GNU-Linux-Magazine"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links = []
for a in soup.find_all("a", href=True):
    if "/GNU-Linux-Magazine" in a["href"]:
        links.append("https://connect.ed-diamond.com" + a["href"])
else:
    print(links[:10])