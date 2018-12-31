#!/usr/bin/env python3
import json
import parser
import helper

# The URL to fetch the latest news from
root = "https://www.vcl-school.nl"
news_url = f"{root}/Actueel"
messages_url = f"{root}/Mededelingen"
agenda_url = f"{root}/Agenda/Jaaragenda"

# The data JSON object
data = {}

# Construct an opener with User-Agent headers
helper.constructOpener()

# Parse all information
data["news"] = parser.parseNews(helper.getHtml(news_url))
data["messages"] = parser.parseMessages(helper.getHtml(messages_url))
data["agenda"] = parser.parseAgenda(helper.getHtml(agenda_url))

# Print all information in indented JSON format
print(json.dumps(data, indent=4, sort_keys=True))

