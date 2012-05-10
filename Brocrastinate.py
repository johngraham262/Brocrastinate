############################################################
###                   ImgurDownloader                    ###
###             Venmo Hackathon - May 2012               ###
############################################################

### A simple app to scrape all the links on the front page
### of wwww.imgur.com and open them up in a new browser
### tab. Tabs can be quickly viewed (and closed) with cmd+w.
### Procrastination efficiency is thus improved. Profit.

from sys import argv
import requests
import webbrowser
from BeautifulSoup import BeautifulSoup

### Check number of tabs limit.
max_tabs = 5
if len(argv) > 1 and argv[1].isdigit():
    max_tabs = int(argv[1])

### Make imgur request and convert response.
r = requests.get('http://www.imgur.com/gallery')
soup = BeautifulSoup(r.content)

links = []

### Find all front page links.
count = 0
for blob in soup.findAll('div', {'class': 'post'}):
    if count == max_tabs:
        break
    if blob.a.has_key('href'):
        links.append(blob.a['href'])
        count += 1

### Open links in new tab.
for l in links:
    url = "http://www.imgur.com%s" % l
    webbrowser.open_new_tab(url)

