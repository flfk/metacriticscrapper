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
for x in soup.find_all("div", attrs={"class": "metascore_w small release positive"}):
	criticscores.append(x.text)

#Scrape the album names. Note that the way the data exists in the HTML is with long spaces, so need to strip data
for x in soup.find_all("div", attrs={"class": "basic_stat product_title"}):
	albumnames.append((x.text).strip())

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

#find the elements that are interesting - if the user score is 7.8 or higher

#given a lot of scores are "tbd" need to test
def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

#use a counter to track which element in the list it is - note start at -1 since we want the first count to start at 0
counter = -1
#create a list in which to output the indeces of list elements that are selected
topelementindeces = []

#loop through user scores and select relevant elements
for x in userscores:
	#add to counter
	counter = counter + 1
	#use defined function to test if it is a number first
	if is_number(x) == True:
		if float(x) > 7.8:
			topelementindeces.append(counter)

#create a list which outputs all the information for relevant aalbums
bestalbums = []

for i in topelementindeces:
	bestalbums.append([userscores[i],bandnames[i],albumnames[i],releasedates[i]])

#print output
for album in bestalbums:
	print album
