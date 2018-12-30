import re
import urllib.request as urllib
from html.parser import HTMLParser

opener = urllib.build_opener()
opener.addheaders = [('User-Agent', (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3 "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/35.0.1916.47 Safari/537.36"))]

urllib.install_opener(opener)

url = "https://www.vcl-school.nl/Actueel"
thumbs = list()

class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for i in attrs:
            if i[0] == "class" and i[1] == "pubThumbnail":
                for i in attrs:
                    if i[0] == "style":
                       thumbs.append(i[1])

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        a = None

    def handle_data(self, data):
        #print("Encountered some data  :", data)
        a = None

def getRequest(url):
    req = urllib.Request(
        url, 
        data = None)

    return req

def curl(url):
    try:
        req = getRequest(url)
        sock = urllib.urlopen(req)
        html = sock.read()
        sock.close()
        return html
    except Exception as ex:
        print("Error: {0}".format(ex))
        return None

result = curl(url)
if result == None:
    exit()

result = result.decode("utf-8")

print("Parsing url...")
parser = Parser()
parser.feed(result)

print("Downloading thumbs...")
for i in range(0, len(thumbs)):
    print("    [-] Downloading {0} of {1}...".format(i, len(thumbs)))
    thumb = thumbs[i]
    regex = re.compile("'(.*)'")
    result = regex.search(thumb).group(1)

    urllib.urlretrieve(result, "thumb{0}.jpg".format(i))

