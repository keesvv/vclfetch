#!/usr/bin/env python3
import json
import parser
import helper

# The URL to fetch the latest news from
news_url = "https://www.vcl-school.nl/Actueel"

# The data JSON object
data = {
    "news": []
}

# Construct an opener with User-Agent headers
helper.constructOpener()

# Get the raw HTML
result = helper.getHtml(news_url)
if result == None:
    exit()

# Parse the URL and feed raw HTML
data["news"] = parser.parseNews(result)
print(json.dumps(data, indent=4, sort_keys=True))

