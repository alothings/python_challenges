import urlparse
import urllib
from bs4 import BeautifulSoup

# url = "http://nytimes.com"
url = "http://www.mileycyrus.com/"

# stack for visited and want to visit
# to not visit pages twice
# need total of pages
# need historial list of visited pages
urls = [url]        # stack of urls to scrape
visited = [url]     #historic record of urls
f1 = open('testfile.txt', 'w+')

while len(urls) > 0:
    try:
        htmltext = urllib.urlopen(urls[0]).read() #using queue (like dominos)
    except:
        print urls[0]
    soup = BeautifulSoup(htmltext, "html5lib")

    urls.pop(0)
    print len(urls)

    # print soup.findAll('a', href=True)
    for tag in soup.findAll('a', href=True):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        if url in tag['href'] and tag['href'] not in visited:
            urls.append(tag['href'])
            visited.append(tag['href'])

    print visited
        # f1.write(str(tag))

    f1.close()


