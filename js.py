import json
import urllib.request, urllib.parse, urllib.error
url=input("Enter Location")
print('Retrieving',url)
links=[]
data = urllib.request.urlopen(url)
dataa=data.read()
info = json.loads(dataa)

for item in info['comments']:
    links.append(item['count'])
links = [int(i) for i in links]
print('Count:',len(links))
print('sum:',sum(links)) 