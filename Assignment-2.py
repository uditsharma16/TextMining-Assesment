
xmlstring=r'C:\Users\udit sharma\Desktop\Aut\Text Mining\Assignment2BlogData\blogs\5114.male.25.indUnk.Scorpio.xml'
# import xml.etree.ElementTree as ET
# parser = ET.XMLParser(encoding="utf-8")
# tree = ET.fromstring(xmlstring, parser=parser)
# import io
# from xml.etree import ElementTree as ET
#
# with io.open(xmlstring, 'r', encoding='utf-8-sig') as f:
#     contents = f.read()
#     tree = ET.fromstring(contents)

# from lxml import etree
# # import xml.etree.cElementTree as etree
# parser = etree.XMLParser(recover=True)
# abc=etree.fromstring(xmlstring, parser=parser)
# tree = etree.XML(xmlstring, parser)
# print(tree)
# # root=etree.getElementByTag("post")
# print(abc)
# # import xml.etree.cElementTree as etree
# import xml.etree.ElementTree as ET
# tree = ET.parse(r'C:\Users\udit sharma\Desktop\Aut\Text Mining\Assignment2BlogData\blogs\5114.male.25.indUnk.Scorpio.xml')
# root = tree.getroot()
# print(root)
from lxml import etree
import io
mypath=r'C:\Users\udit sharma\Desktop\Aut\Text Mining\Assignment2BlogData\blogs'
from os import listdir
from os.path import isfile,join
onlyfiles=[f for f in listdir(mypath) if isfile(join(mypath,f))]
count=0
female_no=[]
male_no=[]
al_20=[]
au_20=[]
all_no=[]



for file in onlyfiles:
 fileinfo=file.split('.')
 if(fileinfo[1]=="female"):
   female_no.append(fileinfo[0])
 elif(fileinfo[1]=="male"):
    male_no.append(fileinfo[0])
 if(int(fileinfo[2])<=20):
    al_20.append(fileinfo[0])
 elif(int(fileinfo[2])>20):
    au_20.append(fileinfo[0])
 all_no.append(fileinfo[0])
print(len(female_no))
print(len(male_no))
# for tree in files:
#  print(counttree)

# parser = etree.XMLParser(ns_clean=True)
# tree   = etree.parse(io.StringIO(tree), parser)
# print(etree.tostring(tree.getroot()))
