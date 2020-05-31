#https://www.youtube.com/watch?v=H8wUYz22joM
# https://inquiry.vba.va.gov/weamspub/buildSearchCountryCriteria.do
import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


"""
for tag in soup.find_all(id= "searchInstitutionCriteria.countryName"):
    print(f"string {tag.string}")
    print(tag.name)
    print(tag.attrs)

for tag in soup.find_all(title = "Select a country for search."):
    print(tag.name)

print("THIs")
for i in soup.find_all(id='searchInstitutionCriteria.countryName',name= "option"):
    print(i)
print(soup.find_all(id='searchInstitutionCriteria.countryName',name= "option"))

"""
"""
# Initiate var
tabledatasaved= ""
page_number = 1

# Go through rows and columns pulling data
for i in range(8):
    soup = make_soup(f"https://www.militaryfriendly.com/schools/?pageresult={page_number}")
    #print(f"this is the page we're on {page_number}")
    for record in soup.findAll('tr'):
        tabledata = ""
        for data in record.findAll('td'):
            tabledata = tabledata + "," + data.text
        if len(tabledata) != 0:
            tabledatasaved = tabledatasaved.strip() + "\n" + tabledata[1:]
    page_number += 1

print(tabledatasaved)
#TODO update file names
#file = open(os.path.expanduser("military_friendly.csv"),"wb")
#file.write(bytes(tabledatasaved, encoding='ascii', errors='ignore'))
"""

# make soup function
def make_soup(URL):
    page_request = Request(URL, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    thepage = urllib.request.urlopen(page_request)
    soupdata = BeautifulSoup(thepage,"html.parser", )
    return soupdata

weams = "https://inquiry.vba.va.gov/weamspub/buildSearchCountryCriteria.do"
soup = make_soup(weams)
option_strings =[]

# Make a list of all option strings and derive a list of countries from that list
for tag in soup.find_all(name= "option", attrs={'value': True }):
    print(tag.string)
    print(tag.name)
    print(tag.attrs)
    print(tag.__class__)
    print('\n')
    option_strings.append(tag.string)
print(option_strings)
countries = option_strings[8:]
print(countries)



