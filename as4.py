import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
characters=0
url = input('Enter location:')
print('Retrieving',url)
links=[]
data = urllib.request.urlopen(url)
tree=ET.parse(data)
for line in data:
    characters = characters + len(line)
print('Retrieved',characters,'characters')
counts = tree.findall('.//count')
for item in counts:
    links.append(item.text)
links = [int(i) for i in links]
print('Count:',len(links))
print('sum:',sum(links)) 