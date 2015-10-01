import os
import math
from paths import *

# Goes through the inverted indices and creates a score
# vector for every document.
def main():
    os.chdir(DATA_PATH)
    listdir = os.listdir(TOKENS)
    total_docs = len(listdir)

    for d in listdir:
        if d == "__init__.py" or ".pyc" in d:
                continue
        doc = []
        listd = os.listdir(INDICES)
        listd.sort()
        for tok in listd:
            if tok == "__init__.py" or ".pyc" in tok:
                continue
            exec("from Data.indices." + tok[0:-3] + " import *")
            ii =  ii or []
            df = len(ii)
            if df == 0:
                idf = 0
            else:
                idf = math.log(float(total_docs)/df)
            tf = 0
            for tup in ii:
                print tup, d
                if tup[0][:-3] == d[:-3]:
                    tf = math.log(1 + tup[1],2)
                    break
            print tf,df
            score = tf * idf
            doc.append(score)
            print tok
        os.chdir(SCORES)
        f = open(d,"w")
        f.write("vect = " + str(doc))
        f.close()


if __name__ == '__main__':
    main()
