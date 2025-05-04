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

    #Add password length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")




