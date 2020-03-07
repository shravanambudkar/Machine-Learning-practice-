from textblob import TextBlob

#sentence = input('enter the sentence to be analysed')

gotit = TextBlob('it is a good day')

print('it is a good day \n')

#analysing sentiment

print(gotit.sentiment)
'''
Polarity is float which lies in the range of [-1,1] where 1 
means positive statement and -1 means a negative statement.
Subjective sentences generally refer to personal opinion,
emotion or judgment whereas objective refers to factual information.
Subjectivity is also a float which lies in the range of [0,1].
'''
