#!/usr/bin/env python3
import re
import urllib.request as urllib
from io import StringIO, BytesIO
from lxml import etree
from lxml.cssselect import CSSSelector

# The URL to fetch the latest news from
url = "https://www.vcl-school.nl/Actueel"

# List of thumbnails
thumbs = list()
articles = list()

class Article(object):
    def __init__(self, thumbnail, date, category, summary, title, url):
        self.thumbnail = thumbnail
        self.date = date
        self.category = category
        self.summary = summary
        self.title = title
        self.url = url

def constructOpener():
    opener = urllib.build_opener()
    opener.addheaders = [('User-Agent', (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3 "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/35.0.1916.47 Safari/537.36"))]

    urllib.install_opener(opener)

def getRequest(url):
    req = urllib.Request(
        url, 
        data = None)

    return req

def getHtml(url):
    try:
        req = getRequest(url)
        sock = urllib.urlopen(req)
        html = sock.read()
        sock.close()
        return html
    except Exception as ex:
        print("Error: {0}".format(ex))
        return None

# Construct an opener with User-Agent headers
constructOpener()

# Get the raw HTML
result = getHtml(url)
result = result.decode("utf-8")
if result == None:
    exit()

# Parse the URL and feed raw HTML
print("Parsing url...")
parser = etree.HTMLParser()
document = etree.parse(StringIO(result), parser)
container = CSSSelector("div.pubItems")(document)[0]
for newsItem in container:
    for prop in newsItem:
        if prop.get("class") == "pubThumbnail": thumbnail = prop.get("style")
        elif prop.get("class") == "pubDate":      date      = prop.text
        elif prop.get("class") == "pubCategory":  category  = prop.text
        elif prop.get("class") == "pubTitle":     title     = prop.text
        elif prop.get("class") == "pubSummary":   summary   = prop.text
        elif prop.get("class") == "pubLink":      url       = prop.get("href")

    article = Article(thumbnail, date, category, summary, title, url)
    articles.append(article)

for i in range(0, len(articles)):
    article = articles[i]
    format = "{0}\n{1}\n{2}\n".format(article.date, article.title, article.url)
    print(format)

exit()

# Download thumbnails
print("Downloading thumbs...")
for i in range(0, len(thumbs)):
    print("    [-] Downloading {0} of {1}...".format(i, len(thumbs)))
    thumb = thumbs[i]
    regex = re.compile("'(.*)'")
    result = regex.search(thumb).group(1)
    
    # Retrieve the thumbnail from the server
    urllib.urlretrieve(result, "thumb{0}.jpg".format(i))

print("Done!")

