# urllib2 library
# http://docs.python.org/library/urllib2.html

import urllib
response = urllib.urlopen('http://python.org')
html = response.read()

print(html.split('\n')[0])