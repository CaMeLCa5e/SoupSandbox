import bs4
import urllib2
 
webpage = urllib2.urlopen('http://www.reddit.com')
soup = bs4.BeautifulSoup(webpage)
for anchor in soup.find_all('a'):
    print(anchor.get('href', '/'))