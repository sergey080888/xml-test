import xml.etree.ElementTree as ET
import collections

def read_xml("newsafr.xml", max_len_word=6, top_words=10)
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse("newsafr.xml", parser)
    root = tree.getroot()
    descriptors_list = root.findall("channel/item/description")