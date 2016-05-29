from lxml import html
import requests
from lxml import etree

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

print etree.tostring(tree, pretty_print=True)
#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

testtree = tree.xpath('/body/*')

buyers = tree.xpath('//div[@title="buyer-name"]')
prices = tree.xpath('//span["item-price"<10].text()')
prices1 = tree.xpath('//span[@class="item-price"]')

textprices = tree.xpath('self::text()')