from bs4 import BeautifulSoup
import re

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.find("option")
# To change the values of the tags, do it like dictionaries
# tag['selected'] = 'false'
# tag['color'] = 'blue'
# print(tag)

tag = doc.find_all('option', string='Undergraduate', value="undergraduate")
print(tag)

# searching for class by name
# Can't use "class" because it's a reserved keyword for defining a class
# Use "class_" instead
#tags = doc.find_all(class_="btn-item")

# n = 2 # arbitrary number of results to give
# tags = doc.find_all(text=re.compile("\$.*"), limit=n) # include the dollar sign and anything which follows it
# for tag in tags:
#     print(tag.strip()) # "strip" the whitespaces

tags = doc.find_all("input", type="text")
for tag in tags:
    tag['placeholder'] = "I changed you!"

with open("changed.html", "w") as file:
    file.write(str(doc)) # write the string of the document's html code into the file