'''
Uses requests to find info on a video card price. Keep in mind: There are websites that have built-in bot protection, such as Amazon, that prevents you from grabbing HTML of a page from a script. Credit to Tech With Tim: https://youtu.be/gRLHr664tXA
'''
from bs4 import BeautifulSoup
import requests

# video card url
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

# 1. set http get request to url
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser") # store request content into result.txt object

'''
HTML tag is like the root of the tree, bs4 reads these files like a tree like structure. For example, the <title></title> is a descendent of the <head></head>, and the <title></title> tag is the parent of the <body></body> tag.
'''
# 2. find prices by looking for specified text '$'
prices = soup.find_all(text="$")
print(prices) # prints prices
print('')
# 3. find parent of price label
parent = prices[0].parent
print(parent) 
print('')
# find the price is located within the strong tag
strong = parent.find("strong")
print(strong)
print('')
print(strong.string) # prints only the text
print('')

print(f'Price: {strong.string}')
