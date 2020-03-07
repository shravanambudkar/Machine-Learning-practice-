##printing nouns from sentence

from textblob import TextBlob
from textblob import Word
blob = TextBlob("I am a student from India who loves programming")

nouns = list()

for word, tag in blob.tags:
	if tag == 'NN':
		nouns.append(word)

print(nouns)


##inflection or singularization or pluralization

blob = TextBlob("Google Youtube is a great platform to learn data science. \n It helps community through videos, codes, discussions,etc.")
print (blob.sentences[1].words[1])
print (blob.sentences[1].words[1].singularize())


## lemmatization


w = Word('running')
print(w.lemmatize("v")) ## v here represents verb


##spelling correction


blob = TextBlob('Google Youtube is a gret platfrm to learn data scence')
print(blob.correct())
