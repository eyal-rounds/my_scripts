#!/usr/bin/env python

import sys
import os
import os.path
from xml.dom.minidom import parse
import xml.dom.minidom


def stringsXml2Dict(xmlfile):
	strings_dict = {}
	doc = parse(xmlfile)
	stringsElem = doc.getElementsByTagName("string")
	for elem in stringsElem:
		name = elem.attributes['name'].value
		value = getTextFromNode(elem)
		strings_dict[name] = value
	return strings_dict

def getTextFromNode(node):
	result = ''
	if node != None:
		for item in node.childNodes:
			if item.nodeType == node.TEXT_NODE:
				result = result + item.data
	return result;

def cmpAtoB(a,b):
	aHasButbNot=[]
	keydiff = []
	for key in a.keys():
		if key not in b.keys():
			aHasButbNot.append(key)
		elif a[key] != b[key]:
			keydiff.append(key)
	return (aHasButbNot, keydiff)


if len(sys.argv) < 2:
	print(sys.argv[0] + " [fileA] [fileB]")
	exit(1)

aExtraKeys=[]
bExtraKeys=[]
keysWithDiff=[]

xmlA = stringsXml2Dict(sys.argv[1])
xmlB = stringsXml2Dict(sys.argv[2])

aExtraKeys, keysWithDiff = cmpAtoB(xmlA, xmlB)
bExtraKeys, keysWithDiff = cmpAtoB(xmlB, xmlA)

print("extra keys in " + sys.argv[1] + ":")
for item in aExtraKeys:
	print(key)

print("extra keys in " + sys.argv[2] + ":")
for item in abxtraKeys:
	print(key)

print("keys in which there is a diff:")
for item in keysWithDiff:
	print(key)
