import codecs
from  nltk import stem, word_tokenize
from nltk.corpus import stopwords
import os
import string
import sys
import unicodedata
from paths import TEXT, TOKENS

# Creates tokens of a given text after normalziing, removing punctuations
# and stemming using the porter stemmer
#       @args   text the text of which tokens are needed
#       @return A list of tokens
def tokenize(text):
    porter = stem.porter.PorterStemmer()
    if isinstance(text,unicode):
        r = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')    
    else:
        r = text
    r = r.translate(None, string.punctuation)
    t = word_tokenize(r)

    t = [porter.stem(tok).lower() for tok in t]
    t = [tok for tok in t if tok not in stopwords.words('english')]

    return t

def main():
    base = TEXT
    os.chdir(base)

    listdir = os.listdir(base)

    for fil in listdir:
        print "Trying for file: " + fil + "\n\n"
        os.chdir(base)
        f = codecs.open(fil, 'r', encoding='utf8')
        

        retval = "lis = " + str(tokenize(f.read()))
        f.close()
        os.chdir(TOKENS)
        w = open(fil, 'w')
        w.write(retval)
        w.close()


if __name__ == '__main__':
    main()