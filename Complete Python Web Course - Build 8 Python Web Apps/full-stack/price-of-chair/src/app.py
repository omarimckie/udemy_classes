__author__ = 'naptime'

import requests
from bs4 import BeautifulSoup  # imports the BeautifulSoup library from the bs4 file

# this variable is using the requests that we imported and getting the website that we stated
request = requests.get("https://www.johnlewis.com/humanscale-diffrient-world-task-office-chair/black/p4127139")

# taking the website that we got and getting the content
content = request.content

# using the BeautifulSoup, we are going to parse the code of that website
soup = BeautifulSoup(content, "html.parser")

# going to find a specific line of that code using the class/attributes
element = soup.find("p", {"class": "price price--large"})

string_price = element.text.strip() # will get the price

# now need to get it without the symbol in front of the amount
price_without_symbol = string_price[1:]

# converts price on site to a float number and putting it in the price variable
price = float(price_without_symbol)

# prints if you should buy the item depending on price
if (price < 600):
    print("You should buy!")
    print("The current price is {}".format(string_price))
else:
    print("Dont buy yet")

# print(request.content)
