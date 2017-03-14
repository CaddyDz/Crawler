# Output html content to myfile.html
import urllib
response = urllib.urlopen('http://python.org')
html = response.read()
f = open('myfile.html', 'w')
f.write(html)
f.close()
