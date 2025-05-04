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

    #Add check for uppercase and lowercase characters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include both uppercase and lowercase letters.")

    #Add digit check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should include at least one digit.")

    #Add special character check
    if any(char in punctuation for char in password):
        score += 1
    else:
        feedback.append("Password should include at least one special character (!, @, #, etc.).")

    # Add dictionary word check to avoid common words
    lower_password = password.lower()
    if any(word in dictionary_words for word in re.split(r'\W+', lower_password)):
        feedback.append("Password should not contain common dictionary words.")
    else:
        score += 1

    #Add strength evaluation logic
    if score == 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

#Add user interaction for input/output
print("Welcome to the Password Strength Checker!")
password = input("Enter your password: ").strip()

strength, feedback = password_strength(password)
print(f"\nPassword Strength: {strength}")

if feedback:
    print("\nSuggestions to improve your password:")
    for suggestion in feedback:
        print(f"- {suggestion}")











