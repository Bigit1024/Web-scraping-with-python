
from bs4 import BeautifulSoup
import requests

url = "https://news.google.com/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('h3', class_="ipQwMb ekueJc RD0gLb")

for list in lists:
    news =  list.find('a', class_="DY5T1d RZIKme").text

    print(news)
    print("\n")
