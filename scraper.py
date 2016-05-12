from pyquery import PyQuery as pq
from lxml import etree
import urllib
import csv

itemSelector = '.item'
nameSelector = '.product-name'
priceSelector = '.price-box'
descSelector = '.desc'

urls = ['']

lst = []

for url in urls:
	d = pq(url)
	lst.append(['URL->',url.encode('utf8')])	
	for item in d(itemSelector).items():
		tempLst = [item(nameSelector).text().replace('\n',' ').encode("utf-8"), item(priceSelector).text().replace('\n',' ').encode("utf-8"), item(descSelector).text().replace('\n',' ').encode("utf-8")]
		lst.append(tempLst)

with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(lst)

