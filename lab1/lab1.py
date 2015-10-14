from nltk.book import *
import nltk



# problem 1

from nltk.draw.dispersion import dispersion_plot
p1_words = ['Elinor', 'Marianne', 'Edward', 'Willoughby']
dispersion_plot(text2, p1_words)

# problem 2
V = set(text5)
wordsBeginWithT = [w for w in V if (len(w) == 5) and ((w[0] == 't') or (w[0] == 'T'))]
print(sorted(wordsBeginWithT))

from nltk import FreqDist

fdist = FreqDist(w for w in text5 if len(w) == 5)
print(fdist.most_common())

# problem 3
lista = sorted(w for w in set(text2) if w.endswith('er'))
listb = sorted(w for w in set(text2) if 'm' in w)
listc = sorted(w for w in set(text2) if 'ph' in w)
listd = sorted(w for w in set(text2) if w.istitle())
listall = lista + listb + listc + listd
print(listall)