from pyquery import PyQuery as pq
import csv
import requests
from os import path
itemSelector = '.product-item'
nameSelector = '.product-name'
priceSelector = '.price-box'
descSelector = '.desc'
from bs4 import BeautifulSoup
from urlparse import urlparse
import re
#https://www.made.com/outdoor-and-garden/garden-rattan-furniture
#urls = ['http://demo-acm2.bird.eu/promotions/tees-all.html']
urls = ['https://www.made.com/outdoor-and-garden/garden-rattan-furniture']
lst = []

for url in urls:
    #d = pq(url)
    #lst.append(['URL->',url.encode('utf8')])
    d = requests.get(url).content;
    # print(d)
    soup = BeautifulSoup(d, "html.parser")
    items = soup.find_all("", "product-item")
    parse_object = urlparse(url)
    print(items);
   # buyers = tree.xpath('//div[@title="buyer-name"]/text()')
    for item in items:
        print(item)

        site = parse_object.netloc

        try:
            product_title = re.sub(' +',' ',item.find("", lambda x: x == 'product-name' or x=='product-item-name').text.encode('utf-8').replace("\r","").replace("\n","").strip())
        except (TypeError, KeyError, AttributeError), e:
            product_title = ""
        try:
            product_price = re.sub(' +',' ',item.find("", lambda x: x == 'price-box' or x=='price').text.encode('utf-8').replace("\r","").replace("\n","").strip())
        except (TypeError, KeyError, AttributeError), e:
            product_price = ""
        try:
            product_url = item.find("a")["href"].strip()
        except (TypeError, KeyError, AttributeError), e:
            product_url = ""
        try:
            product_img = item.find("img")["src"].strip()
        except (TypeError, KeyError, AttributeError), e:
            product_img = ""
        product_path_category = parse_object.path
        print "{} is selling for {} with path {} at {}, img {}".format(product_title, product_price, product_path_category, product_url, product_img)
        #tempLst = [item(nameSelector).text().replace('\n',' ').encode("utf-8"), item(priceSelector).text().replace('\n',' ').encode("utf-8"), item(descSelector).text().replace('\n',' ').encode("utf-8")]
        lst.append([site,product_title,product_price,product_path_category,product_img, product_url])


if(path.exists('output.csv')):
    with open('output.csv', 'ab') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(lst)
else:
    with open('output.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["site","product_title", "product_price", "product_path_category", "product_img", "product_url"])
        writer.writerows(lst)

