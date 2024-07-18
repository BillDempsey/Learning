from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080gaming-oc-10gd/p/N82E16814932459"

# some websites won't allow you to get the html scripts for them
result = requests.get(url)

# print(result.text) # Gibberish

doc = BeautifulSoup(result.text, "html.parser")
# print(doc.prettify)

# .find gives first result
# .find_all gives all results in a list

# find the product price
prices = doc.find_all(text="$")
# print(prices) # find the dollar sign

parent = prices[0].parent
print(parent)  # we see here that the <strong> tag holds the price
strong = parent.find("strong")
print("$",strong.string)

