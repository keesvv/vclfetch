import re
from io import StringIO
from lxml import etree
from lxml.cssselect import CSSSelector

def parseNews(rawHtml):
    parser = etree.HTMLParser()
    document = etree.parse(StringIO(rawHtml), parser)
    container = CSSSelector("div.pubItems")(document)[0]
    articleList = list()

    for newsItem in container:
        for prop in newsItem:
            if prop.get("class") == "pubThumbnail":
                rawStyle = prop.get("style")
                regex = re.compile("'(.*)'")
                thumbnail = regex.search(rawStyle).group(1)

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

