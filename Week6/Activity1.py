### Parse website 
# Load libraries 
from urllib import request 
from bs4 import BeautifulSoup 

# Website to parse
tofugu = 'https://www.tofugu.com/japanese/sensei/'

# Obtain response from website; parse through BeautifulSoup 
response = request.urlopen(tofugu)
html = response.read().decode('utf8')
htmlsoup = BeautifulSoup(html, 'html.parser')

# Get five tags from the parsed website 
site_title = htmlsoup.title 
print(site_title)

site_headers2 = htmlsoup.find_all("h2")
print(site_headers2[0].text)

site_paragraphs = htmlsoup.find_all("p")
print(site_paragraphs[1])

site_lists = htmlsoup.find_all("li")
print(site_lists[10:15])