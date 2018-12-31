import urllib.request as urllib
import re
import datetime

def constructOpener():
    opener = urllib.build_opener()
    opener.addheaders = [('User-Agent', (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3 "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/35.0.1916.47 Safari/537.36"))]

    urllib.install_opener(opener)

def getHtml(url):
    try:
        sock = urllib.urlopen(url)
        html = sock.read()
        sock.close()
        return html.decode()
    except Exception as ex:
        print("Error: {0}".format(ex))
        return None

def getDateFormat(dateStr):
    date = datetime.datetime.strptime(dateStr, '%d-%m-%Y')
    dateInfo = {
        "year": date.strftime("%Y"),
        "month": date.strftime("%-m"),
        "day": date.strftime("%-d"),
        "fullDate": dateStr
    }

    return dateInfo

def getThumbnail(prop):
    rawStyle = prop.get("style")
    regex = re.compile("'(.*)'")
    thumbnail = regex.search(rawStyle).group(1)
    return thumbnail

