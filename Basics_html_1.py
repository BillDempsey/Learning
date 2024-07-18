from bs4 import BeautifulSoup

with open("index.html", "r") as f: # r for read mode
    doc = BeautifulSoup(f, "html.parser") # html.parser is an accepted type for this module

# print(doc)
# print(doc.prettify) # unable to spot any real differences in output

# <title> is descendant of <head>
# <P> = New paragraph
# <P> <B color="red">This is a new paragraph!</B>
# <BR> <B><I>This is a new sentence without a pargraph break, in bold italisc.</I></B>
# <HR>
# </BODY>
# </HTML>

# tag = doc.title # will give you the first item with that tag
# print(tag)
# print(tag.string)

# tag.string = "hello"
# print(tag)

# # print all bits which have both a "p" and "b" tag
# tags = doc.find_all("p")[0]
# print(tags.find_all("b"))   
