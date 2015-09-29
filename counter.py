import os
from paths import *
from collections import Counter

#Goes through all the files and finds occurances of tokens
#after this creates an index file for every token. 
def create_index():
    listdir = os.listdir(TOKENS)

    ans = {}
    os.chdir(TOKENS)
    for token_file in listdir:
        if token_file == "index.py" or token_file == "__init__.py" or ".pyc" in token_file:
            continue

        r = open(token_file, 'r').read()
        c  = Counter()

        for line in r.splitlines():
        	c.update(line.split())

        exec("from Data.tokens." + token_file[:-3] + " import lis as tokens")

        for tok in tokens:
            if ans.get(tok) is None:
                ans[tok] = [(token_file,c[tok])]
            else:
                ans[tok] += [(token_file,c[tok])]

    os.chdir(INDICES)
    for key, value in ans.items():
	    w = open("nn" + str(key) + ".py", 'w')
        w.write("ii = " + str(value))
	    w.close()


def main():
	create_index()
    

if __name__ == '__main__':
    main()
