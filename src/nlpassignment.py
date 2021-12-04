import PyPDF2


reader = PyPDF2.PdfFileReader("C:\\Users\\ntlg4\\Documents\\COVID19 Misinformation Articles\\BLT.20.276782.pdf")
pageObj = reader.getNumPages()
corpus = []
for page_count in range(pageObj):
    page = reader.getPage(page_count)
    page_data = page.extractText()
    corpus.append(page_data)

reader = PyPDF2.PdfFileReader('C:\\Users\\ntlg4\\Documents\\COVID19 Misinformation Articles\\S0007114520002950a.pdf')
pageObj = reader.getNumPages()
for page_count in range(pageObj):
    page = reader.getPage(page_count)
    page_data = page.extractText()
    corpus.append(page_data)

reader = PyPDF2.PdfFileReader("C:\\Users\\ntlg4\\Documents\\COVID19 Misinformation Articles\\COVID Misinformation Is Killing People - Scientific American.pdf")
pageObj = reader.getNumPages()
for page_count in range(pageObj):
    page = reader.getPage(page_count)
    page_data = page.extractText()
    corpus.append(page_data)

# print(corpus)

sample_corpus = ' '.join(corpus)

import nltk
from nltk.tokenize import word_tokenize as wtoken
tokenize_corpus = wtoken(sample_corpus)
tokenize_corpus = ' '.join(tokenize_corpus)



#Remove stop words
from nltk.corpus import stopwords
sw_l = stopwords.words('english')
corpus_drop_stopwords = [word for word in tokenize_corpus.split() if word not in sw_l]
corpus_drop_stopwords = ' '.join(corpus_drop_stopwords)
# print(corpus_drop_stopwords)

from nltk import wordpunct_tokenize
corpus_wordpunct = wordpunct_tokenize(corpus_drop_stopwords)
corpus_wordpunct = ' '.join(corpus_wordpunct)
# print(corpus_wordpunct)
#
#Regex

from nltk import regexp_tokenize
patn = '\w+|[!,\-,]'
# try patn = '\w+|[!,\-,]'
corpus_final = regexp_tokenize(corpus_wordpunct,patn)
# print(corpus_final)

#Frequency distribution

frequency_dist = nltk.FreqDist(corpus_final)
print(sorted(frequency_dist, key=frequency_dist.__getitem__,reverse=True)[0:18])

from matplotlib import pyplot as plt

frequency_dist.plot(50,cumulative=False)
plt.show()



