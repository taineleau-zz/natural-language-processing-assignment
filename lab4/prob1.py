
import nltk
from nltk import *
from nltk.corpus import brown


# 1a
fdist = FreqDist(brown.words())
for word in set(brown.words()):
    if fdist[word+'s'] > fdist[word]:
        print(word, )
print('\n')

# 1b
cfd = ConditionalFreqDist(brown.tagged_words())
maxword = ''
for word in set(brown.words()):
    if len(cfd[word].items()) > len(cfd[maxword].items()):
        maxword = word
print(maxword)
print('\n')

# 1c
tag_fd = nltk.FreqDist(tag for (word, tag) in brown.tagged_words())
for (tag, freq) in tag_fd.most_common():
    print (tag,)
print('\n')
for (tag, freq) in tag_fd.most_common(20):
    print(tag,)
print('\n')

# 1d
tags = [tag for (word, tag) in brown.tagged_words()]
bgms = bigrams(tags)
bgms = [bgm for bgm in bgms if bgm[0] == 'NN']
fdist = FreqDist(bgms)
print(fdist.most_common(5))
