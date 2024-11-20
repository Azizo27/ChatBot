from nltk.corpus import wordnet

# Function to get words related to a lexical field
def get_lexical_field(word):
    related_words = set()
    for synset in wordnet.synsets(word):  # Get synsets for the word
        for lemma in synset.lemmas():    # Get related words (lemmas)
            related_words.add(lemma.name().lower())  # Add the lemma
    return list(related_words)

# Example: Get lexical field for "greeting"
word = 'Goodbye'
lexical_field = get_lexical_field(word)
print("Lexical Field for '" + word +"':", lexical_field)
