import helper
from io import StringIO
from lxml import etree
from lxml.cssselect import CSSSelector

def parse(rawHtml):
    parser = etree.HTMLParser()
    document = etree.parse(StringIO(rawHtml), parser)
    return document

def parseNews(rawHtml):
    document = parse(rawHtml)
    container = CSSSelector("div.pubItems")(document)[0]
    articleList = list()

    for newsItem in container:
        for prop in newsItem:
            if prop.get("class") == "pubThumbnail":   thumbnail = helper.getThumbnail(prop)
            elif prop.get("class") == "pubDate":      date      = helper.getDateFormat(prop.text)
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

def parseMessages(rawHtml):
    document = parse(rawHtml)
    container = CSSSelector("div.pubItems")(document)[0]
    messageList = list()

    for messageItem in container:
        for prop in messageItem:
            if prop.get("class") == "pubThumbnail":  thumbnail = helper.getThumbnail(prop)
            elif prop.get("class") == "pubDate":     date      = helper.getDateFormat(prop.text)
            elif prop.get("class") == "pubCategory": category  = prop.text
            elif prop.get("class") == "pubTitle":    title     = prop.text
            elif prop.get("class") == "pubSummary":  summary   = prop.text
            elif prop.get("class") == "pubLink":     url       = prop.get("href")

        message = {
            "thumbnail": thumbnail,
            "date": date,
            "category": category,
            "summary": summary,
            "title": title,
            "url": url
        }

        messageList.append(message)

    return messageList

