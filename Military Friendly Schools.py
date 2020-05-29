#https://www.youtube.com/watch?v=H8wUYz22joM
# https://www.militaryfriendly.com/schools/?pageresult=2
import urllib
import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase

"""
#Trying to find button
button = 'http://www.militaryfriendly.com/schools/?pageresult=2'
soup.findAll(button)
#nexturl = soup.findAll('div')
#print(soup.find('div',{"id":pager}).text)
#div = (soup.findAll('div'))
#print(div)

for link in soup.findAll('div'):
    for i in (link.get('id')):
        print(link.get('button'))

pager = soup.findAll(id="pager")
print(pager[0].attrs[""])
print(pager)
for findbutton in soup.findAll('div'):
    for finds in findbutton.findAll('button'):

#Save working version
soup = make_soup("https://www.militaryfriendly.com/schools/?pageresult=1")

for record in soup.findAll('tr'):
    tabledata = ""
    for data in record.findAll('td'):
        tabledata= tabledata + "," + data.text
    if len(tabledata) != 0:
        tabledatasaved = tabledatasaved + "\n" + tabledata[1:]
print(tabledatasaved)

#Trying to cycle through pages
for i in range(8):
    soup = make_soup(f"http://www.militaryfriendly.com/schools/?pageresult={page_number}")
    page_number = page_number + 1
    print(make_soup)
"
# make soup function
def make_soup(one):
    url = Request(one, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage,"html.parser", )
    return soupdata

tabledatasaved= ""
page_number = 1

# Go through rows and columns pulling data
for i in range(8):
    soup = make_soup(f"http://www.militaryfriendly.com/schools/?pageresult={page_number}")
    for record in soup.findAll('tr'):
        tabledata = ""
        for data in record.findAll('td'):
            tabledata = tabledata + "," + data.text
        if len(tabledata) != 0:
            tabledatasaved = tabledatasaved.strip() + "\n" + tabledata[1:]
    page_number = page_number + 1
print(tabledatasaved)
file = open(os.path.expanduser("military_friendly.csv"),"wb")
file.write(bytes(tabledatasaved, encoding='ascii', errors='ignore'))