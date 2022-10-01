"""
BMI 500 - Natural Language Processing - 2
Alireza Rafiei - Fall 2022 - HW6
"""

# Importing required libraries
import numpy as np
import nltk
from nltk.corpus import brown
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pickle import dump
from pickle import load


### ........................ Problem #1 ........................ ###


### Part A
print('\nProblem 1 -- Part A\n')

# Opening, reading, and preprocessing by lowercasing of the two provided texts
Text1 = open(r'.\text1').read().lower()
Text2 = open(r'.\text2').read().lower()
print('\nThe preprocessed text 1: {}'.format(Text1))
print('\nThe preprocessed text 2: {}\n'.format(Text2))


### Part B
print('\nProblem 1 -- Part B\n')

# Creating corpus
Corpus = [Text1, Text2]

# Vectorizing corpus
vectorizer = CountVectorizer(ngram_range=(1,3))
Vectorized_corpus = vectorizer.fit_transform(Corpus)

# Vectorized texts
Vect_text1 = Vectorized_corpus[0]
Vect_text2 = Vectorized_corpus[1]

print('\nThe vectorized text 1: {}'.format(Vect_text1))
print('\nThe vectorized text 2: {}\n'.format(Vect_text2))


### Part C
print('\nProblem 1 -- Part C\n')

# Computing the cosine similarity
cosine_similarity = cosine_similarity(Vect_text1, Vect_text2)
print("The cosine similarity is: {}".format(cosine_similarity[0][0]))


### Part D
print('\nProblem 1 -- Part D\n')

# Calculating the jaccard similarity
Vect_text1_arr = Vect_text1.toarray()[0]
Vect_text2_arr = Vect_text2.toarray()[0]
intersection = np.sum(Vect_text1_arr == Vect_text2_arr)
jaccard_similarity = intersection/len(Vect_text1_arr)
print("The jaccard similarity is: {}\n".format(jaccard_similarity))


### ........................ Problem #2 ........................ ###

print("\nproblem #2")


# Loading data
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories="news")

# Splitting data
size = int(len(brown_tagged_sents) * 0.9)
Train = brown_tagged_sents[:size]
Evaluation = brown_tagged_sents[size:]

## unigram tagger
# Training unigram tagger
unigram_tagger = nltk.UnigramTagger(Train)

# Evaluation of the unigram tagger
unigram_performance = unigram_tagger.evaluate(Evaluation)
print("The performance of the unigram tagger is: {}\n".format(unigram_performance))

## bigram tagger
# Training bigram tagger
bigram_tagger = nltk.BigramTagger(Train)

# Evaluation of the bigram tagger
bigram_performance = bigram_tagger.evaluate(Evaluation)
print("The performance of the bigram tagger is: {}\n".format(bigram_performance))


## combined tagger
# Training combined tagger
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(Train, backoff=t0)
t2 = nltk.BigramTagger(Train, backoff=t1)

# Evaluation of the combined tagger
combined_performance = t2.evaluate(Evaluation)
print("The performance of the combined tagger is: {}\n".format(combined_performance))

# Save combined tagger
output = open('combined_tagger.pkl', 'wb')
dump(t2, output, -1)
output.close()

# Loading combined tagger
input = open('combined_tagger.pkl', 'rb')
tagger = load(input)
input.close()

# Tagging text1 with combined tagger
tokens = Text1.split()
tags = tagger.tag(tokens)
print('tagging all the words from Text1 using combined tagger: {}\n'.format(tags))


print('\nQuestion: Can lowercasing affect the performance of the POS tagger?\n')
Ans2 = """Yes, lowercasing can affect the performance of the tagger. Back to Lecture 5, 
lowercasing is not considered for tasks such as comparison of different contents. 
Nevertheless, in the current task, it would result in the elimination of clues that can 
be provided. Take names that are usually in uppercase as the most patently example. 
Therefore, lowercasing can affect the performance of the POS tagger."""
print(Ans2)


### ........................ Problem #3 ........................ ###

print("\nproblem #3")

print('\nQuestion: What are some of the possible NLP components of a Question Answering System?\n')
Ans3 = """Generally, a question answering system (QAS) has three main components:  
question classification, information retrieval, and answer extraction. Question classification 
as a query processing module plays a primary role in a QAS to categorize the question based on 
context using conducting preprocessing on the original input data. It also aims to extract keywords 
and reformulates a question into semantically equivalent multiple questions. Information retrieval 
focuses on extracting applicable answers from the relevant documents. Information retrieval searches 
for information in documents, for documents themselves, for metadata that describes documents, or 
even within databases to find specific pieces of information (keywords) to provide a concise, comprehensible, 
and correct answer. After the precision and ranking of candidate information, the answer extraction module 
gives the top N relevant documents from the retrieval module. It performs a detailed analysis and pinpoints 
the answer to the question. Usually answer extraction module produces a candidate list of answers and ranks 
them according to specific scoring functions. As a result, a QAS provides an answer to the specified question."""
print(Ans3)
