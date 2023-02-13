# pip install -U pip setuptools wheel
# pip install -U spacy
# python -m spacy download en_core_web_sm

import spacy

nlp = spacy.load('en_core_web_sm')

garden_path_sentences = ["The old man the boat.", "The horse raced past the barn fell.",
                       "The complex houses married and single soldiers and their families.",
                       "The sour drink from the ocean", "Have the students who failed the exam take the supplementary."]

for sentence in garden_path_sentences:
    doc = nlp(sentence)
    print([token.orth_ for token in doc])
    print([(word, word.label_, word.label) for word in doc.ents])
    # The entity recognition doesn't find any words to label for these garden path sentences.
    print("")


# Example to show how entity recognition does work on usual sentences.
sample = "WW1 started in 1914 and lasted a brutal 4 years until 1918, in which time 2 million died."
doc = nlp(sample)
print([(word, word.label_, word.label) for word in doc.ents])

# I found spaCy gave me no entities for these garden-path sentences.
# I expected this as it is quite hard from even a human to understand these sentenes.