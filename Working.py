from lxml import etree
import io
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS,remove_stopwords
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import numpy as np
from nltk.stem.porter import *

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
####################Reading all the files in under 20 category
print(al_20)
count=0
data_al_20=[]
for file in al_20:
 xmlstring=r'C:\Users\udit sharma\Desktop\Aut\Text Mining\Assignment2BlogData\blogs'
 joinstring='/'
 count+=1
 a=[]
 try:
  with open(xmlstring+joinstring+file ,'r',encoding="ANSI") as f:
    a=f.read()

 except Exception as e:
     print(count, "errornum")
     print(e)
 data_al_20.append(a)
 f.close()

def lemmatize_stemming(text):
    return SnowballStemmer.stem(WordNetLemmatizer().lemmatize(text,pos='v'))
def preprocess(text):
    result=[]
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token)>3:
            result.append(lemmatize_stemming(token))
    return result
words_al20=[]
for words in data_al_20.split(' '):
    words_al20.append(words)
pre_al20=preprocess(words_al20)

num_topics=2
ldamodel=gensim.models.ldamodel.LdaModel(pre_al20,num_topics=num_topics)

topics=ldamodel.print_topics
