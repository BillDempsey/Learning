from bs4 import BeautifulSoup
import re
import requests

# Takes the headlines from KK GAA and prints them out

url = f"https://kilkennygaa.ie/news/"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

#print(doc.prettify())

# Print all the headlines
#div = doc.find_all(class_="post-content py-1 px-2 p-md-3")
# for item in div:
#    # print(item, "\n")
#     #post = doc.find(class_="post-content py-1 px-2 p-md-3")
#     split_1 = str(item).split(">")
#     print(split_1[-4].split("<")[0])


# Next -> find for all pages
# page_text = doc.find(class_="pagination justify-content-center mb-0")
# print(page_text)

for pages in range(1,5):
    url = f"https://kilkennygaa.ie/news/page/{pages}/"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find_all(class_="post-content py-1 px-2 p-md-3")

    for item in div:
     post = doc.find(class_="post-content py-1 px-2 p-md-3")
     split_1 = str(item).split(">")
     print(split_1[-4].split("<")[0])