import re
import nltk
from nltk.corpus import words
from string import punctuation

# Download the NLTK words corpus
nltk.download('words')
#Load dictionary words into a set for fast lookup
dictionary_words = set(words.words())

#Define the password_strength function structure
def password_strength(password):
    feedback = []
    score = 0




