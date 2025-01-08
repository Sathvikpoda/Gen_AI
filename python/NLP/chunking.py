import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, RegexpParser

# Ensure necessary resources are downloaded

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# Sample sentence
sentence = "The quick brown fox jumps over the lazy dog."

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Perform Part-of-Speech (POS) tagging
pos_tags = pos_tag(tokens)

# Define a chunk grammar
chunk_grammar = """
    NP: {<DT>?<JJ>*<NN>}   # Noun Phrase
    VP: {<VB.*><RB>?}      # Verb Phrase
"""

# Create a chunk parser
chunk_parser = RegexpParser(chunk_grammar)

# Parse the POS-tagged tokens
chunk_tree = chunk_parser.parse(pos_tags)

# Display the chunk tree
print(chunk_tree)

# Visualize the chunk tree
chunk_tree.draw()
