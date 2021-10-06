import requests
import json
from bs4 import BeautifulSoup
import string

r = requests.get("https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3")
soup = BeautifulSoup(r.content, 'html.parser')
articles = soup.find_all("a", "c-card__link u-link-inherit")

urls = []
saved = []
for article in articles:
    urls.append("https://www.nature.com{}".format(article.get('href')))

for url in urls:
    a = requests.get(url)
    soup_a = BeautifulSoup(a.content, 'html.parser')

    if soup_a.find("span", "c-article-identifiers__type") and soup_a.find("span", "c-article-identifiers__type").text == "NEWS":
        name = soup_a.find("h1", "c-article-magazine-title").text
        filename = name.translate(str.maketrans(' ', '_', string.punctuation + "’"))
        filename = filename + ".txt"
        content = soup_a.find("div", "c-article-body u-clearfix").text.encode('utf-8')

        file = open(filename, 'wb')
        file.write(content)
        file.close()
        saved.append(filename)

print("Saved articles:")
print(saved)

# print(is_news)
# print(urls)


