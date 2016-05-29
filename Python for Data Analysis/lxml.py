from lxml import etree

root = etree.Element("root", interesting="totally")
etree.tostring(root)
root.set("hello", "Huhu")
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")

for name, value in sorted(root.items()):
    print ('%s = %r' %(name, value))
    
root[0].getnext().tag    
root.set('test','ter')

attributes = root.attrib
attributes["hello"] = "Guten Tag"
print(attributes["hello"])
attributes['hello']='yowazzup'

dictionaryattribute = dict(root.attrib)
dictionaryattribute['hello']='changed?'
print root.attrib

root1 = etree.Element('root1')
root1.text = 'TEXT'
print root1.text
etree.tostring(root1)

html = etree.Element('html')
body = etree.SubElement(html,"body")
body.text='TEXT'
etree.tostring(html)

html.xpath('//text()')
html.xpath('string()')

br = etree.SubElement(body,'br')
br.tail='TAIL'
etree.tostring(html)

etree.tostring(br)
etree.tostring(br,with_tail=False)
etree.tostring(html,method="text")

etree.SubElement(root, 'another').text='another day'
for element in root.iter('child2'):
    print element.tag, element.text

root = etree.XML('<root><a><b/></a></root>')
print etree.tostring(root,encoding = 'iso-8859-1')
print etree.tostring(root, pretty_print=True)

root=etree.XML('<html><head/><body><p>Hello<br/>World</p></body></html>')
print etree.tostring(root,method='html', pretty_print=True)
etree.tostring(root,method='text')

br=next(root.iter('br'))
br.tail=u'W\xf6rld'
etree.tostring(root, method='text',encoding='UTF-8')

##############################################################################

root = etree.XML('''\
<?xml version="1.0"?>
<!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]>
<root>
    <a>&tasty;</a>
</root>
''')

print etree.tostring(root,pretty_print=True)

tree=etree.ElementTree(root)
print(tree.docinfo.doctype)
print(tree.docinfo.xml_version)

tree.docinfo.xml_version
tree.docinfo.public_id = '-//W3C//DTD XHTML 1.0 Transitional//EN'
tree.docinfo.system_url = 'file://ocal.dtd'
print tree.docinfo.doctype
print(etree.tostring(tree)) 

##############################################################################
some_xml_data = "<root>data</root>"
root = etree.fromstring(some_xml_data)
print etree.tostring(root)

###############################################################################
root = etree.XML("<root>data</root>")
print(root.tag)
###############################################################################
some_file_like_object = BytesIO("<root>data</root>")
tree=etree.parse(some_file_like_object)
etree.tostring(tree)
###############################################################################
parser = etree.XMLParser(remove_blank_text=True)
root = etree.XML("<root>  <a/>   <b>  </b>                 </root>", parser)
for element in tree.iter("*"):
    if element.text is not None and not element.text.strip():
        print element.text
        element.text = None