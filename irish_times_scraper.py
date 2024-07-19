# Prints the top 10 headlines form the Irish Times website

from bs4 import BeautifulSoup
import requests

url = f"https://www.irishtimes.com/"
request = requests.get(url).text
doc = BeautifulSoup(request, "html.parser")

div = doc.find_all(class_="c-link font-bold")
counter = 1

for item in div:
    headline = str(item).split(">")[1].split("<")[0]
    if '<' in headline:
        headline = headline.split('<')[0] 
    if counter < 11:
        print(counter, ". ", headline)
        counter += 1
    else:
        break