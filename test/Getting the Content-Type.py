# It's helpful to know what type of content was returned
# Typically just search for links in html content
import urllib
response = urllib.urlopen('http://python.org')

Content_type = response.info().get('Content-Type')

print(Content_type)
