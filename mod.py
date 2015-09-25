# This script goes through all the vectors, all of them and computes the
# mod for every vector and stores it in the form of a dictionary.
# 	dict = {
# 		"file1" : 52.1,
# 		"file2" : 22.1,
# 	}

import os
import math
from paths import PATH, TOKENS, INDICES, SCORES,DATA_PATH

os.chdir(DATA_PATH)

# Goes through the scores, calculates mod for every
# vector and stores it in a dictionary.

def main():
	f  = open("vector_mod.py","w")

	dic = {}

	lists  = os.listdir(SCORES)

	os.chdir(DATA_PATH)
	for files in lists:
		if ".pyc" in files or "init" in files:
			continue
		exec("from Data.doc_vector." + files[:-3] + " import vect")
		score = 0
		for vector in vect:
			score =  score + vector*vector
		score = math.sqrt(score)
		dic[files[:-3]] = score

	f.write("vector_mod = " + str(dic))
	f.close()

if __name__ == '__main__':
	main()