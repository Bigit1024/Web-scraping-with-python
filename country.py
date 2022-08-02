
from bs4 import BeautifulSoup
import requests
# from csv import writer

url = "https://scrapethissite.com/pages/simple/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div' ,class_="col-md-4 country")

for list in  lists:
    country_name = list.find('h3' ,class_="country-name").text.replace('\n\t', '')
    print(country_name)
    print("\n")