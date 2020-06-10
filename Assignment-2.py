import  xml.etree.ElementTree as ET
xmlstring=r'C:\Users\udit sharma\Desktop\Aut\Text Mining\Assignment2BlogData\blogs\5114.male.25.indUnk.Scorpio.xml'

import time
# import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding="utf-8")
tree = ET.fromstring(xmlstring, parser=parser)

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
# parser = etree.XMLParser(ns_clean=True)
# tree   = etree.parse(io.StringIO(tree), parser)
# print(etree.tostring(tree.getroot()))
# import xml.etree.ElementTree as ET
# parser = ET.XMLParser(encoding="utf-8")
# tree = ET.fromstring(xmlstring, parser=parser)
start=time.time()
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


count=0
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
 a=[]
 # print(file)
 xmlstring=r'C:\Users\udit sharma\Desktop\Aut\Text Mining\Assignment2BlogData\blogs'
 joinstring='/'
 count += 1
 try:
  with open(xmlstring+joinstring+file ,'r',encoding="ANSI") as f:
    a=f.read()

  f.close()
  x=a.replace("&"," ")
  cleanx = x.replace("<3", " ")
  cleanx2 = cleanx.replace("<>", " ")
  cleanx1= cleanx2.replace("< "," ")
  parser = ET.XMLParser(encoding="ANSI")
  tree = ET.fromstring(cleanx1, parser=parser)


 except Exception as e:
     print(count)
     print(e)
     print(file)
     try:
      with open(xmlstring + joinstring + file, 'r', encoding="utf-8") as f:
          a = f.read()

      f.close()
      x = a.replace("&", " ")
      cleanx=x.replace("<3"," ")
      cleanx2 = cleanx.replace("<>", " ")
      cleanx1 = cleanx2.replace("< ", " ")
      parser = ET.XMLParser(encoding="utf-8")
      tree = ET.fromstring(cleanx1, parser=parser)
     except Exception as e:
         print(e)
         print(file)
         exit()

print(count)
end=time.time()



