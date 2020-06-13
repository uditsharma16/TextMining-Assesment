abc='xyz'
xyz=[]
tbz=xyz.append(abc)
xyz.append(abc)

# kbz=tbz.append(tbz)
print(type(' '.join(xyz)))

from nltk.stem import WordNetLemmatizer
wnl=WordNetLemmatizer
print(wnl.lemmatize(wnl,word='rocks'))