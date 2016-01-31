import nltk

# problem 1

emma = nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)
emma_dins = set(emma)
len(emma_dins)


# problem 2

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

def most_common_50_bigrams_of(text):
	stopwords_and_punctuations = stopwords.words('english')

	

	# deal with punctuations
	stopwords_and_punctuations.append('.')
	stopwords_and_punctuations.append(',')
	stopwords_and_punctuations.append(',"')
	stopwords_and_punctuations.append(',\'')
	stopwords_and_punctuations.append('"')
	stopwords_and_punctuations.append('!')
	stopwords_and_punctuations.append(';')
	stopwords_and_punctuations.append('.--')
	stopwords_and_punctuations.append('!--')
	stopwords_and_punctuations.append('!"')
	stopwords_and_punctuations.append('."')
	stopwords_and_punctuations.append('?"')
	stopwords_and_punctuations.append('--')
	stopwords_and_punctuations.append('-')
	stopwords_and_punctuations.append('\'')


	bigrams = nltk.bigrams(text)
	bigrams_refined = []
	for pairs in bigrams:
		if not (pairs[0].lower() in stopwords_and_punctuations or pairs[1].lower() in stopwords_and_punctuations):
			bigrams_refined.append(pairs)

	#bigrams_refined = [b for b in bigrams if not False in [False for w in b if b in stopwords_and_punctuations]]

	fdist = nltk.FreqDist(bigrams_refined)
	print(fdist.most_common()[:50])


most_common_50_bigrams_of(emma)





