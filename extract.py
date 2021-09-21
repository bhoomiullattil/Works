# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count =input('Enter count')
positio=input('Enter position')
position=int(positio)
count=int(count)
pos=position-1
for k in range(count):
	links=[]
	l=len(links)
	html = urllib.request.urlopen(url)
	soup = BeautifulSoup(html, 'html.parser')
	for link in soup.findAll('a',attrs={'href':re.compile("^http://")}):
		links.append(link.get('href'))
	l=len(links)
	pos=position-1
	for i in range (l):
		if i==pos:
			url=links[i]
			print('retrieving:',url)