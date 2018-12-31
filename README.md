# vclfetch
![VCL Logo](https://www.vcl-school.nl/Portals/_default/Skins/VCL/images/logo_vcl.png)

🐬 A tiny Python script for fetching the latest news from [vcl-school.nl](https://www.vcl-school.nl/) (Vrijzinnig-Christelijk Lyceum).

# Getting started
If you run `./vclfetch.py`, you'll get a result which looks like this:
```
{
    "agenda": [
        {
          "date": null,
          "name": "(...)"
        }
    ],
    "messages": [
        {
            "category": "(...)",
            "date": {
                "day": "(...)",
                "fullDate": "(...)",
                "month": "(...)",
                "year": "(...)"
            },
            "summary": "(...)",
            "thumbnail": "(...)",
            "title": "(...)",
            "url": "(...)"
        }
    ],
    "news": [
        {
            "category": "(...)",
            "date": {
                "day": "(...)",
                "fullDate": "(...)",
                "month": "(...)",
                "year": "(...)"
            },
            "summary": "(...)",
            "thumbnail": "(...)",
            "title": "(...)",
            "url": "(...)"
        }
    ]
}
```

This is the JSON output that `vclfetch` will return. To use or process these values in your own applications, you can pipe specified property values to any program. In this case, we'll use the program `jq` to get the values from properties.
> `jq` can be installed using `sudo apt install jq` on Debian-based systems.

# Examples
Get an array of news items:
```
./vclfetch.py | jq -r .news
```

Get all news headlines/titles:
```
./vclfetch.py | jq -r .news[].title
```

Get the summary of the first message:
```
./vclfetch.py | jq -r .messages[0].summary
```

Download the thumbnail of a specified news item:
```
wget -O thumb.jpg --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0)" $(./vclfetch.py | jq -r .news[0].thumbnail)
```
The reason for the `--user-agent` argument is because of a `HTTP Error 999: No Hacking` that is being returned from the server if it detects that the connection hasn't been established using a web browser (a.k.a. spam/bot protection).
