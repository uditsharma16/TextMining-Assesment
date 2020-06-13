
import  xml.etree.ElementTree as ET

import gensim
import nltk
from nltk import word_tokenize, pos_tag, WordNetLemmatizer
from sphinx.util import stemmer

# xmlstring=r'D:\college\sem2\Text Mining\Assignment_Blog_topic\Assignment2BlogData\blogs\5114.male.25.indUnk.Scorpio.xml'
import sys
import time
def remove_stop_symols(word):
    a1=word.replace("."," ")
    a2=a1.replace(",", " ")
    a3=a2.replace("-", " ")
    a4=a3.replace("!", " ")
    a5 = a4.replace("?", " ")
    a6 = a5.replace("\"", " ")
    a7 = a6.replace("("," ")
    a8= a7.replace(")"," ")
    a9 = a8.replace("<"," ")
    a10 = a9.replace(">"," ")
    a11 = a10.replace("/"," ")
    return a11
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

female_no=[]
male_no=[]
al_20=[]
au_20=[]
all_no=[]
# sys.setdefaultencoding('ANSI')



for file in onlyfiles:
 fileinfo=file.split('.')
 if(fileinfo[1]=="female"):
   female_no.append(file)
 elif(fileinfo[1]=="male"):
    male_no.append(file)
 if(int(fileinfo[2])<=20):
    al_20.append(file)
 elif(int(fileinfo[2])>20):
    au_20.append(file)
 all_no.append(file)
#print(al_20)

file=al_20[0]
data_al20=[]
for file in al_20:
 xmlstring=r'D:\college\sem2\Text Mining\Assignment_Blog_topic\Assignment2BlogData\blogs'
 joinstring='/'
  # count += 1
 a=[]
 with open(xmlstring+joinstring+file ,'r',encoding="ANSI") as f:
  a=f.read()
 data_al20.append(a)
 f.close()


# abc=a.split(' ')
#data_al20.append(a)



#print(data_al20)
######Data Pre-processing #############
def lemmatize_stemming(text):
    wnl=WordNetLemmatizer()
    return wnl.lemmatize(word=text)
def preprocess(text):
    result = []
    for token in nltk.word_tokenize(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:

            result.append(lemmatize_stemming(token))

    return result

print("hello")

# words_al20=[]
pre_al20=[]
# # for words in data_al20.split(''):
# #     words_al20.append(words)
for xyz in data_al20:
 pre_al20.append(remove_stop_symols(xyz))
#print(pre_al20)
# words =[]
# for word in pre_al20.split(' '):
#     words.append(word)
print("hello")
pre_al21=[]
for xyz in pre_al20:
 pre_al21.append(preprocess(xyz))
print(pre_al20)

print("hello")
print(pre_al21)
from gensim import corpora
dictionary = corpora.Dictionary(pre_al21)
corpus = [dictionary.doc2bow(text) for text in pre_al21]
#print(corpus)
import pickle
pickle.dump(corpus, open('corpus.pkl', 'wb'))
dictionary.save('dictionary.gensim')

print("hello")
num_topics=2
ldamodel=gensim.models.ldamodel.LdaModel(corpus,num_topics=num_topics)
ldamodel.save('model2.gensim')

topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)

# #  a=[]
# #  # print(file)
# #  xmlstring=r'C:\Users\udit sharma\Desktop\Aut\Text Mining\Assignment2BlogData\blogs'
# #  joinstring='/'
# #  count += 1
# #
# #  try:
# #   with open(xmlstring+joinstring+file ,'r',encoding="ANSI") as f:
# #     a=f.read()
# #
# #   f.close()
# #   # x=a.replace("&"," ")
# #   # cleanx = x.replace("<3", " ")
# #   # cleanx2 = cleanx.replace("<>", " ")
# #   # cleanx1= cleanx2.replace("< "," ")
# #   # parser = ET.XMLParser(encoding="ANSI")
# #   # tree = ET.fromstring(cleanx1, parser=parser)
# #
# #
# #  except Exception as e:
# #      print(count,"errornum")
# #      print(e)
# #      print(file)
# #      try:
# #       with open(xmlstring + joinstring + file, 'r', encoding="utf-8") as f:
# #           a = f.read()
# #
# #       f.close()
# #
# #       # x = a.replace("&", " ")
# #       # cleanx=x.replace("<3"," ")
# #       # cleanx2 = cleanx.replace("<>", " ")
# #       # cleanx1 = cleanx2.replace("< ", " ")
# #       # parser = ET.XMLParser(encoding="utf-8")
# #       # tree = ET.fromstring(cleanx1, parser=parser)
# #      except Exception as e:
# #
# #          print(e)
# #          print(file)
# #          exit()
# xmlstring=r'C:\Users\udit sharma\Desktop\Aut\Text Mining\Assignment2BlogData\blogs'
# joinstring='/'
#   # count += 1
#
# file=onlyfiles[0]
# with open(xmlstring+joinstring+file ,'r',encoding="ANSI") as f:
#     a=f.read()
#
# f.close()
# max_occur=0
# counts=dict()
# abc=remove_stop_symols(a)
# abx=abc.split()
# for i,word in enumerate(list(set(abx))):
#     # print(word)
#     if(word in counts):
#         counts[word]+=1
#     else:
#         counts[word]=1
# top=[]
# for word in counts:
#     if(counts[word]>max_occur):
#         max_occur=counts[word]
#         top.append(word)
#
# print(counts[top[len(top)-1]])
# print("Hello")
#
# end=time.time()


# from lxml import etree
# import io
# import gensim
# from gensim.utils import simple_preprocess
# from gensim.parsing.preprocessing import STOPWORDS,remove_stopwords
# from nltk.stem import WordNetLemmatizer, SnowballStemmer
# import numpy as np
# from nltk.stem.porter import *
# 
# mypath=r'C:\Users\udit sharma\Desktop\Aut\Text Mining\Assignment2BlogData\blogs'
# from os import listdir
# from os.path import isfile,join
# onlyfiles=[f for f in listdir(mypath) if isfile(join(mypath,f))]
# 
# female_no=[]
# male_no=[]
# al_20=[]
# au_20=[]
# all_no=[]
# # sys.setdefaultencoding('ANSI')
# 
# 
# 
# for file in onlyfiles:
#  fileinfo=file.split('.')
#  if(fileinfo[1]=="female"):
#    female_no.append(file)
#  elif(fileinfo[1]=="male"):
#     male_no.append(file)
#  if(int(fileinfo[2])<=20):
#     al_20.append(file)
#  elif(int(fileinfo[2])>20):
#     au_20.append(file)
#  all_no.append(file)
# ####################Reading all the files in under 20 category
# print(al_20)
# count=0
# data_al_20=[]
# for file in al_20:
#  xmlstring=r'C:\Users\udit sharma\Desktop\Aut\Text Mining\Assignment2BlogData\blogs'
#  joinstring='/'
#  count+=1
#  a=[]
#  try:
#   with open(xmlstring+joinstring+file ,'r',encoding="ANSI") as f:
#     a=f.read()
# 
#  except Exception as e:
#      print(count, "errornum")
#      print(e)
#  data_al_20.append(a)
#  f.close()
# 
# def lemmatize_stemming(text):
#     return SnowballStemmer.stem(WordNetLemmatizer().lemmatize(text,pos='v'))
# def preprocess(text):
#     result=[]
#     for token in gensim.utils.simple_preprocess(text):
#         if token not in gensim.parsing.preprocessing.STOPWORDS and len(token)>3:
#             result.append(lemmatize_stemming(token))
#     return result
# words_al20=[]
# for words in data_al_20.split(' '):
#     words_al20.append(words)
# pre_al20=preprocess(words_al20)
# 
# num_topics=2
# ldamodel=gensim.models.ldamodel.LdaModel(pre_al20,num_topics=num_topics)
# 
# topics=ldamodel.print_topics
