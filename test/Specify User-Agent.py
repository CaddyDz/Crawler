# Polite crawlers identify themselves with the User-Agent http header
import  urllib
request = urllib.Request('http://python.org/')
request.add_header("User-Agent", "My Python Crawler")
opener = urllib.build_opener()
response = opener.open(request)
html = response.read()
