
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
import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\udit sharma\Desktop\Aut\Text Mining\Assignment2BlogData\blogs\5114.male.25.indUnk.Scorpio.xml')
root = tree.getroot()
print(root)
