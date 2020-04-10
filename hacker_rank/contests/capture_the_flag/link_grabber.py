import urllib.request
import urllib.parse
import re
import linkGrabber
import string

# links = linkGrabber.Links('https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/qds.html')
# gb = links.find(pretty=True)
# print(gb)
list_links = []
base = 'https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/'
def crawl(url):
    links = linkGrabber.Links(url)
    gb = links.find()
    # gb = links.text
    print(gb, type(gb))
    # print(len(gb))
    if len(gb) <= 0 or url in list_links: return

    for el in gb:
        if el['href']:
            list_links.append(el['href'])
            return crawl(base + el['href'])

    print(list_links)

crawl('https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/qds.html')
# crawl('https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/flhxd.html')
