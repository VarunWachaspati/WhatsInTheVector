The directory has the following structure:

|-- Data
|   |-- doc_vector
|   |-- corpus
|   |-- __init__.py
|   |-- tokens
|   |-- vector_mod.py
|   `-- indices
|-- counter.py
|-- mod.py
|-- tokenizer.py
|-- score.py
|-- __init__.py
|-- README.txt
|-- search.py
`-- paths.py

You can run the search.py file directly and it will prompt you in case there isn't an existing tokens, indices, corpus or doc_vector directory. The corpus used is the litereature corpus in which we are using a 120 Mb, 154
file corpus that has literature between 1830 and 1839. Search.py can be used to run tokenizer, counter score and
mod but you can run them individually as well.

Other wise you can run the files in the following order:
    tokenizer.py - Creates tokens of the words in documents and stores document per file in individual files in
    Data/tokens.(154 files)

    counter.py - Uses the created tokens to create an inverted index inwhich token links to a list of tuples. The tuples
    contain the file name followed by the term frequency. A different file is created for every token, as importing
    a big dictionary takes much more memory and time then importing a single file.
        data/indices/Brutus.py (about 2,000,00 files)
            ii = [("filename",5),("file2",6)]

    score.py - Uses the inverted indices in data/indices to create a 1xN(number of tokens) vector of scores using the weighting function given in the documentation.
        data/doc_vector/Doc.py (about 154 files)
            vect = [1,2,4,5,124 ...]
    mod.py - Goes through all the vectors and stores the modulus in a dictionary.(1 file created)

    search.py - Takes the query and outputs the results, prompts incase something is missing.

    Test Cases:
    1) Query - "Knapp"
        First 5 Retrieved Results - MartHRW.txt, ThomGLG.txt, GrimSlE.txt, RennJIT.txt, CrokTPS.txt
        Precision - 1
        Recall - .78
    2) Query - "walt whitman"
        First 5 Retrieved Results - CoolWHM.txt, WheeJPT.txt
        Precision - 1
        Recall - .66
    3) Query - "paliuri raiko zitza"
    	Precision - 1
    	Recall - .75