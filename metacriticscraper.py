import urllib2, sys
from bs4 import BeautifulSoup

#create the soup
site= "http://www.metacritic.com/browse/albums/release-date/new-releases/date"
#metacritic showed a 403 error without 'user-agent' data, likely because it is checking to ensure the user agent is from a common browser
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(site, headers=hdr)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page, "lxml")

# print soup

#create seperate lists for all the critic scores, album names, band names, user scores and release dates
criticscores=[]
albumnames=[]
bandnames=[]
userscores=[]
releasedates=[]

links=[]

for link in soup.find_all("div", attrs={"class": "metascore_w small release positive"}):
	links.append(link.text)

print links


#find all the information and populate the lists

# for criticscore in soup.find_all('div', attrs={"class":"metascore_w small release positive"}):
# 	criticscores.append(criticscore)
# for criticscore in soup.find_all('a'):
# 	print criticscore

# print criticscores

#create a list with all the band names




# #selenium required to scrape given that there is javascript that isn't included in the source code
# from selenium import webdriver
# from bs4 import BeautifulSoup

# #set the path to the raw path of the driver to be used
# chrome_path = r'/Users/FelixKramer/Desktop/Coding/Chromedriver/chromedriver'
# driver = webdriver.Chrome(chrome_path)

# #set the url and run selenium get function
# url = "http://www.metacritic.com/browse/albums/release-date/new-releases/date"
# driver.get(url)

# #get the html code for the page that was opened using selenium
# html = driver.page_source

# #run the html collected from selenium through BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')

# print soup