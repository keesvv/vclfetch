import urllib.request as urllib

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

