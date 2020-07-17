
import  xml.etree.ElementTree as ET

import gensim
import nltk
from nltk import word_tokenize, pos_tag, WordNetLemmatizer
from sphinx.util import stemmer

# xmlstring=r'D:\college\sem2\Text Mining\Assignment_Blog_topic\Assignment2BlogData\blogs\5114.male.25.indUnk.Scorpio.xml'
import sys
import time
def remove_stop_symols(word):

    a12=word.replace("blog"," ")
    a13=a12.replace("date", " ")
    a14=a13.replace("post"," ")
    a16=a14.replace("like"," ")
    a17 = a16.replace("know", " ")
    a18 = a17.replace("time", " ")
    a19 = a18.replace("think", " ")
    a20 = a19.replace("thing", " ")
    a21= a20.replace("urllink"," ")
    a22=a21.replace("nbsp"," ")
    a23=a22.replace("'"," ")
    stop_symbols=".,-!?\"()<>/*\\".split()
    stop_word=['1','2','3','4','5','6','7','8','9','0','=']

    a15=""
    for i in a22:
        if(i not in stop_word and i not in stop_symbols):

            a15+=i
    return a15

start=time.time()
from lxml import etree
import io
mypath=r'D:\college\sem2\Text Mining\Assignment_Blog_topic\Assignment2BlogData\blogs'
from os import listdir
from os.path import isfile,join
onlyfiles=[f for f in listdir(mypath) if isfile(join(mypath,f))]
female_no=[]
male_no=[]
al_20=[]
au_20=[]
all_no=[]
# sys.setdefaultencoding('ANSI')

i=0

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

print("hello")

def selectDemographyData(demtype):
    print(demtype)
    if(demtype=="male"):
        return male_no
        print("male")
    elif(demtype=="female"):
        return female_no
        print("female is found")
    elif(demtype=="under20"):
        return al_20
    elif(demtype=="above20"):
        return au_20
    # else(demtype=="all"):
    else:
        return all_no

def readFileData(demotype):
 i=0
 data_al20 = []
 # print(demotype)

 for file in selectDemographyData(demotype):
  xmlstring=r'D:\college\sem2\Text Mining\Assignment_Blog_topic\Assignment2BlogData\blogs'
  joinstring='/'
  a=[]
  with open(xmlstring+joinstring+file ,'r',encoding="ANSI") as f:
   a=f.read()
  data_al20.append(a.lower())
  f.close()
  i+=1
  if(i==200):
     break
 return data_al20

######Data Pre-processing #############
def lemmatize_stemming(text):
    wnl=WordNetLemmatizer()
    return wnl.lemmatize(word=text)
def preprocess(text):
    result = []
    garbage_word = ['july', 'august','people','today','june','year','week','night','january','feburary','march','april','may','september','october','november','december','anyways','haha']
    # deslist = ['NN', 'NNS', 'NNP', 'NNPS', 'VBD', 'VBN', 'VBP', 'VBZ']
    deslist = ['NN', 'NNS', 'NNP', 'NNPS']
    for token,des in nltk.pos_tag(nltk.word_tokenize(text)):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            if des in deslist and token not in garbage_word:
             result.append(lemmatize_stemming(token))

    return result

print("hello")




def processTheData(textFile):
 pre_al20 = []
 for xyz in readFileData(textFile):
  pre_al20.append(remove_stop_symols(xyz))
 print("hello")
 pre_al21=[]
 for xyz in pre_al20:
  pre_al21.append(preprocess(xyz))
 return pre_al21

from gensim import corpora
import pickle
print("hello")

def createCorpusAndDictionary(textFile,demograpy="female"):
 finalData=processTheData(textFile)
 dictionary = corpora.Dictionary(finalData)
 corpus = [dictionary.doc2bow(text) for text in finalData]
 pickle.dump(corpus, open('corpus'+demograpy+'.pkl', 'wb'))
 dictionary.save('dictionary'+demograpy+'.gensim')

print("hello")


def centreControl(demography):
    createCorpusAndDictionary(readFileData(demography),demography)


centreControl("male")
print(time.time()-start)



def findNounAndVerb(textFile,wordlist):
 texttagged=nltk.pos_tag(nltk.word_tokenize(textFile))
 for i,(word,pos) in enumerate(texttagged):
  deslist = ['NN', 'NNS', 'NNP', 'NNPS', 'VBD', 'VBN', 'VBP', 'VBZ']
  if(word in wordlist):
    print('Nouns/Verb before and After the word:',word)
    nvBefore=[]
    nvAfter=[]
    for j in range(i-1,0,-1):
     # print(texttagged)
     if(texttagged[j][1] in deslist):
      nvBefore.append(texttagged[j][0])
      if(len(nvBefore)==2):
       break
    print ('Cluster Before:',nvBefore)
    for j in range(i+1,len(texttagged)):
     if (texttagged[j][1] in deslist):
      nvAfter.append(texttagged[j][0])
      if (len(nvAfter) == 2):
       break
    print('Cluster After:',nvAfter)