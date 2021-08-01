import xml
from xml.dom import minidom


# parse an xml file by name
# path = r'C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\pythonXml\items.xml'
# mydoc = minidom.parse(path)

# items = mydoc.getElementsByTagName('item')


# print('Item #2 attribute:',items[1].attributes['name'].value)# one specific item attribute
# for it in items:
#     print(it.firstChild.data)

"""
dir(item)
['ATTRIBUTE_NODE', 'CDATA_SECTION_NODE', 'COMMENT_NODE', 'DOCUMENT_FRAGMENT_NODE', 'DOCUMENT_NODE', 'DOCUMENT_TYPE_NODE', 'ELEMENT_NODE', 'ENTITY_NODE', 
'ENTITY_REFERENCE_NODE', 'NOTATION_NODE', 'PROCESSING_INSTRUCTION_NODE', 'TEXT_NODE', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', 
'__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
'__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', 
'__weakref__', '_attrs', '_attrsNS', '_call_user_data_handler', '_child_node_types', '_ensure_attributes', '_get_attributes', '_get_childNodes', '_get_firstChild', 
'_get_lastChild', '_get_localName', '_get_tagName', '_localName', '_magic_id_nodes', 'appendChild', 'attributes', 'childNodes', 'cloneNode', 'firstChild', 
'getAttribute', 'getAttributeNS', 'getAttributeNode', 'getAttributeNodeNS', 'getElementsByTagName', 'getElementsByTagNameNS', 'getInterface', 'getUserData', 
'hasAttribute', 'hasAttributeNS', 'hasAttributes', 'hasChildNodes', 'insertBefore', 'isSameNode', 'isSupported', 'lastChild', 'localName', 'namespaceURI', 
'nextSibling', 'nodeName', 'nodeType', 'nodeValue', 'normalize', 'ownerDocument', 'parentNode', 'prefix', 'previousSibling', 'removeAttribute', 
'removeAttributeNS', 'removeAttributeNode', 'removeAttributeNodeNS', 'removeChild', 'replaceChild', 'schemaType', 'setAttribute', 'setAttributeNS', 
'setAttributeNode', 'setAttributeNodeNS', 'setIdAttribute', 'setIdAttributeNS', 'setIdAttributeNode', 'setUserData', 'tagName', 'toprettyxml', 'toxml', 
'unlink', 'writexml']

dir(firstChild)
['ATTRIBUTE_NODE', 'CDATA_SECTION_NODE', 'COMMENT_NODE', 'DOCUMENT_FRAGMENT_NODE', 'DOCUMENT_NODE', 'DOCUMENT_TYPE_NODE', 'ELEMENT_NODE', 'ENTITY_NODE', 
'ENTITY_REFERENCE_NODE', 'NOTATION_NODE', 'PROCESSING_INSTRUCTION_NODE', 'TEXT_NODE', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
'__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', 
'__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', 
'__weakref__', '_call_user_data_handler', '_data', '_get_childNodes', '_get_data', '_get_firstChild', '_get_isWhitespaceInElementContent', '_get_lastChild', 
'_get_length', '_get_localName', '_get_wholeText', '_set_data', 'appendChild', 'appendData', 'attributes', 'childNodes', 'cloneNode', 'data', 'deleteData', 
'firstChild', 'getInterface', 'getUserData', 'hasChildNodes', 'insertBefore', 'insertData', 'isSameNode', 'isSupported', 'isWhitespaceInElementContent', 
'lastChild', 'length', 'localName', 'namespaceURI', 'nextSibling', 'nodeName', 'nodeType', 'nodeValue', 'normalize', 'ownerDocument', 'parentNode', 'prefix', 
'previousSibling', 'removeChild', 'replaceChild', 'replaceData', 'replaceWholeText', 'setUserData', 'splitText', 'substringData', 'toprettyxml', 'toxml', 'unlink', 
'wholeText', 'writexml']
"""


# # all item attributes
# print('\nAll attributes:')
# for elem in items:
#     print(elem.attributes['name'].value)

# # one specific item's data
# print('\nItem #2 data:')
# print(items[1].firstChild.data)
# print(items[1].childNodes[0].data)

# # all items data
# print('\nAll item data:')
# for elem in items:
#     print(elem.firstChild.data)

import xml.etree.ElementTree as ET
path2 = r'C:\Users\USER\Documents\GitHub\cofico\cofico\FROM BIM MASTER TEMP 210412\Python\pythonXml\Out\items2.xml'
# create the file structure
data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item2 = ET.SubElement(items, 'item')
item1.set('name','item1')
item2.set('name','item2')
item1.text = 'item1abc'
item2.text = 'item2abc'

# create a new XML file with the results
mydata = ET.tostring(data).decode("utf-8")
with open(path2, "w") as myfile:
    myfile.write(mydata)