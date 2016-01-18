#!/usr/bin/env python
import sys
from xml.etree.ElementTree import Element, tostring
import xml.etree.ElementTree
e = xml.etree.ElementTree.parse(sys.argv[1]).getroot()
newdoc=Element(e.tag)
temp=e.getchildren()
sortedtemp=sorted(temp, key=lambda x:x.attrib['name'])
for elem in sortedtemp:
	newdoc.append(elem)

newfile=open(sys.argv[1]+".sorted",'w')
newfile.write(tostring(newdoc, 'utf-8'))
