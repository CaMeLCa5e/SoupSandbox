import bs4
import urllib2
 
webpage = urllib2.urlopen('http://en.wikipedia.org/wiki/Main_Page')
soup = bs4.BeautifulSoup(webpage)
for anchor in soup.find_all('a'):
    print(anchor.get('href', '/'))