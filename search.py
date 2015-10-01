# This script is used for the actual searching, the script first
# tokenizes and lemetizes the query and converts it into a vector
# then finds the angle with all the other vectors. The results
# are showed in the ascending order of angles(smaller the angle
# more relevant the result).


from  nltk import stem, word_tokenize
from nltk.corpus import stopwords
import string
import unicodedata
import math
import os
try:
    from Data.vector_mod import vector_mod
except:
    print "Mod Vector doesn't exist"
from paths import *
from tokenizer import tokenize
from tokenizer import main as tokenizer
from counter import main as counter
from score import main as score
from mod import main as mod
import sys

# Goes through the list of results, sorts them and outputs
# the top 10.


def results(ranks):
    ranks = sorted(ranks,key=lambda tup: tup[1])
    i = 0
    for x in ranks:
        i = i + 1
        print TEXT + str(x[0][:-3]) + ".txt"
        if i%10==0:
            f = raw_input("press y for more")
            if f == "y" or f == "Y":
                continue
            else:
                break

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = midpoint
        else:
          if item < alist[midpoint]:
              last = midpoint-1
          else:
            first = midpoint+1

    return found


# Makes the vector of the tokens
# @args tokens The Tokens of the query.
# @return vector The vector for the given query.
# @return mod The modulus of the vector

def create_query_vector(tokens):
    print "Creating Vector From Tokens .."
    vector = []
    interesting_indices = []
    sorted_list = os.listdir(INDICES)
    sorted_list = [x for x in sorted_list if ".pyc" not in x and "__init__" not in x]
    sorted_list.sort()
    total_docs = len(os.listdir(TEXT))
    os.chdir(DATA_PATH)
    vector = [0]*len(sorted_list)
    mod = 0
    for index in tokens:
        position = binarySearch(sorted_list, "nn" + index  + ".py")
        if not position:
            continue
        exec("from Data.indices.nn" + index + " import *")
        ii = ii or []
        df = len(ii)
        if df == 0:
            continue
        idf = float(total_docs)/df
        idf = (math.log(idf))
        tf = 0
        for word in tokens:
            if word == index:
                tf = tf + 1
        tf = math.log(1+tf,2)
        vector[position] = tf*idf
        mod = mod + tf*idf*tf*idf
        interesting_indices.append(position)
    mod = math.sqrt(mod)
    return vector, mod, interesting_indices

# Uses the query vector created, compares to other vectors
# and finds the angles between the vectors and appends
# scores to a list called ranks.
# @args query_vector and query_mod, outputs of create query vector

def search(query_vector,query_mod, interesting_indices):
    os.chdir(DATA_PATH)
    ranks = []
    for score_file in os.listdir(SCORES):
        if ".pyc" in score_file or "__init__" in score_file:
            continue
        exec("from Data.doc_vector." + score_file[:-3] + " import vect")
        found = False
        for index in interesting_indices:
            if vect[index] != 0:
                found = True
                break
        if not found:
            continue
        mod_vector  = vector_mod[score_file[:-3]]
        dotproduct = 0
        for i in xrange(0,len(vect)):
            dotproduct = dotproduct + vect[i]*query_vector[i]
        angle = math.acos(dotproduct/(mod_vector*query_mod))
        ranks.append((score_file,angle))
    return ranks


def banner():
    while True:
        print "1. Press 1 for running the tokenizer usually"
        print "2. Press 2 for creating the inverted index"
        print "3. Press 3 for creating the vectors for the documents"
        print "4. Press any other number to search"
        choice =  int(raw_input("$ "))
        if not os.path.exists(TEXT):
            print "No Data at All. No Valid Corpus. Please add something to\n" + str(TEXT)
        if not os.path.exists(DATA_PATH):
            print "No Data Existed, Path Created"
            os.mkdir(DATA)
        if not os.path.exists(TOKENS) or choice == 1:
            print "Creating tokens as they don't exist/You Chose To"
            os.mkdir(TOKENS)
            tokenizer()
        if not os.path.exists(INDICES) or choice == 2:
            print "Creating indices as they don't exist"
            os.mkdir(INDICES)
            counter()
        if not os.path.exists(SCORES) or choice == 3:
            print "Creating Vectors as they don't exist"
            os.mkdir(SCORES)
            score()
            mod()
        if choice > 3 or choice == 0:
            print "Search begins"
            break
# The main function that uses all the above functions to take queries
# and output results.
def main():
    banner()
    while True:
        query = raw_input("Enter Your Query Here or Press Q to Exit\n$ ")
        if query == "Q" or query == "q":
            print "Thank You"
            break
        print "Tokenizing"
        t = tokenize(query)
        print "Tokens : " + str(t)
        query_vector, query_mod, interesting_indices = create_query_vector(t)
        if query_mod == 0:
            print "No Match Found"
            continue
        print "Comparing this vector with all other vectors"
        ranks = search(query_vector,query_mod, interesting_indices)
        print ranks
        results(ranks)

if __name__ == "__main__":
    main()