import xml.etree.ElementTree as ET
import collections
def reader():
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()
    descriptors_list = root.findall("channel/item/description")
    q =[]
    for i in descriptors_list:
        q.append(i.text)
    print(q)
reader()



