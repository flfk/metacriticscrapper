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

# #scrape the critic scores
# for x in soup.find_all("div", attrs={"class": "metascore_w small release positive"}):
# 	criticscores.append(x.text)

#Scrape the album names. Note that the way the data exists in the HTML is with long spaces, so need to strip data
# for x in soup.find_all("div", attrs={"class": "basic_stat product_title"}):
# 	albumnames.append((x.text).strip())

# for the band names, user scores and release dates they are all included in a list so need to find "data" span which is second list item

# scrape the band names
for x in soup.find_all("li", attrs={"class": "stat product_artist"}):
	y = x.find("span", attrs={"class": "data"}).text
	bandnames.append(y)

# scrape the user scores
for x in soup.find_all("li", attrs={"class": "stat product_avguserscore"}):
	y = x.find("span", attrs={"class": "data"}).text
	userscores.append(y)

# scrape the release dates
for x in soup.find_all("li", attrs={"class": "stat release_date"}):
	y = x.find("span", attrs={"class": "data"}).text
	releasedates.append(y)



# 	for y in x.find_all("span", attrs={"class": "data"}):
# 		albumnames.append(y)

# print bandnames

# <li class="stat product_artist">
#                     <span class="label">Artist:</span>
#                     <span class="data">King Gizzard &amp; the Lizard Wizard</span>
#                 </li>

# <span class="data textscore textscore_favorable">7.6</span>

#scrape the band names

#scrape the user scores

#scrape the release dates


