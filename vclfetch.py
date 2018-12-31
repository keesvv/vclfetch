#!/usr/bin/env python3
import re
import json
import urllib.request as urllib
from io import StringIO, BytesIO
from lxml import etree
from lxml.cssselect import CSSSelector

# The URL to fetch the latest news from
news_url = "https://www.vcl-school.nl/Actueel"

# List of data
data = {
    "news": []
}

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

def parse(rawHtml):
    parser = etree.HTMLParser()
    document = etree.parse(StringIO(rawHtml), parser)
    container = CSSSelector("div.pubItems")(document)[0]
    articleList = list()

    for newsItem in container:
        for prop in newsItem:
            if prop.get("class") == "pubThumbnail":
                rawStyle = prop.get("style")
                regex = re.compile("'(.*)'")
                thumbnail = regex.search(styleObj).group(1)

            elif prop.get("class") == "pubDate":      date      = prop.text
            elif prop.get("class") == "pubCategory":  category  = prop.text
            elif prop.get("class") == "pubTitle":     title     = prop.text
            elif prop.get("class") == "pubSummary":   summary   = prop.text
            elif prop.get("class") == "pubLink":      url       = prop.get("href")

        article = {
            "thumbnail": thumbnail,
            "date": date,
            "category": category,
            "summary": summary,
            "title": title,
            "url": url
        }

        articleList.append(article)
    
    return articleList

# Construct an opener with User-Agent headers
constructOpener()

# Get the raw HTML
result = getHtml(news_url)
result = result.decode("utf-8")
if result == None:
    exit()

# Parse the URL and feed raw HTML
data["news"] = parse(result)
print(json.dumps(data, indent=4, sort_keys=True))

