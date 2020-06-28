import gensim
import pickle
from gensim import corpora
def FindMaxValue(corpus,demographicType):
 maxvalue={}
 dictionary = corpora.Dictionary.load('dictionary' + demographicType+ '.gensim')
 for doc in corpus:
  for words,freq in doc:
   if(words in maxvalue):
    maxvalue[words]+=freq
   else:
    maxvalue[words]=freq
 newdict={k: v for k, v in sorted(maxvalue.items(), key=lambda item: item[1],reverse=True)}
 i=0
 for word in newdict:
  i+=1
  if(i==3):
   break
 print(dictionary[word],newdict[word])

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


# from Assignment_2 import dictionary
from gensim import corpora, models
def runtfidf(n_top=2,demographicType="all"):
 corpus = pickle.load(open('corpus' + demographicType + '.pkl', 'rb'))
 dictionary=corpora.Dictionary.load('dictionary'+demographicType+'.gensim')
 tfidf = models.TfidfModel(corpus)
 corpus_tfidf = tfidf[corpus]
 FindMaxValue(corpus)
 ldamodel = gensim.models.ldamodel.LdaModel(corpus_tfidf, num_topics=2)
 ldamodel.save('modeltf' + demographicType + '.gensim')
 dictionary = corpora.Dictionary.load('dictionary' + demographicType + '.gensim')
 max_tif=0
 num=0
 count=0
 topics = ldamodel.print_topics(num_words=4)
 tops = 0
 for n, topic in enumerate(topics):
  print("Cluster NUmber:", n)
  # print(topic[1][1])
  for i, val in enumerate(topic[1]):
   # print(topic)

   if (val == '*'):
    top = int(topic[1][i + 2])
    # print(top)
    for k in range(3, 10):
     # print(topic[1][i+k])
     if (topic[1][i + k].isdigit()):
      top = top * 10 + int(topic[1][i + k])
      # print(top)
     else:
      break
    # print(top)
    print(dictionary[top])


 for doc in corpus_tfidf:


  if(max_tif>doc[1][1]):
    num.append(dictionary[doc[1][0]])
    max_tif=doc[1][1]
 print(dictionary[num])

runtfidf(2,'female')
import nltk

# text='Hi my name is Udit Sharma. I am a Student at AUT. Aut stands for Auckland University of Technology'


# findNounAndVerb(text)
#
#

