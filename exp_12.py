# -*- coding: utf-8 -*-
"""exp 12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r_VbRO5SfsQCJMYaVZmwYOKrhhLItqs5
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
nltk.download('stopwords')
nltk.download('punkt')

def remove_punctuation(sentence):
  for i in sentence:
    if i in string.punctuation:
      sentence = sentence.replace(i, "")
  return sentence

def remove_stopwords(sentence):
  stop_words = set(stopwords.words('english'))
  word_tokens = word_tokenize(example_sent)
  filtered_sentence = []
  for w in word_tokens:
    if w not in stop_words:
      filtered_sentence.append(w)
  return filtered_sentence

example_sent = """We are learning Natural Language Processing (NLP) as part of
Fundamentals of Machine Learning (FML) course in our second year B.Tech."""

print(f"Original Sentence : \n{example_sent}")

example_sent = remove_punctuation(example_sent)

print(f"\nSentence after removing punctuations : \n{example_sent}")

example_sent = " ".join(remove_stopwords(example_sent))

print(f"\nSentence after removing stopwords : \n{example_sent}")