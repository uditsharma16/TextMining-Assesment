import gensim
import pickle
from gensim import corpora

# from Assignment_2 import dictionary
def runLDA(n_topic=2,demographicType="all"):
 num_topics=n_topic
 corpus=pickle.load(open('corpus'+demographicType+'.pkl','rb'))
 ldamodel=gensim.models.ldamodel.LdaModel(corpus,num_topics=num_topics)
 ldamodel.save('model'+demographicType+'.gensim')
 dictionary=corpora.Dictionary.load('dictionary'+demographicType+'.gensim')
 topics = ldamodel.print_topics(num_words=5)
 tops=[]
 for n, topic in enumerate(topics):
    print("Cluster NUmber:",n)
    #print(topic[1][1])
    for i,val in enumerate(topic[1]):
        # print(topic)

        if(val=='*'):
            top=int(topic[1][i+2])
            # print(top)
            for k in range(3,10):
                # print(topic[1][i+k])
                if(topic[1][i+k].isdigit()):
                 top=top*10+int(topic[1][i+k])
                 # print(top)
                else: break
            # print(top)
            print(dictionary[top])
 maxTerm=1
 num=0
 for xyz in corpus:
   for abc in xyz:
    if(maxTerm<abc[1]):
        num=abc[0]
        maxTerm=abc[1]

runLDA(2,"above20")

# print(corp?us[0][0][1])
#print(corpus[1])
# print(dictionary[corpus[0][0][0]])