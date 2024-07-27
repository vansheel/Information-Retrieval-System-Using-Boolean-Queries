import streamlit as st
import nltk
from nltk.stem import PorterStemmer
import re
from collections import defaultdict
from nltk.tokenize import word_tokenize
import doc
nltk.download('punkt')

documents=doc.doc()
# Streamlit app title
st.title("Boolean Retrieval System")

# Initialize the stemmer globally
stemmer = PorterStemmer()

# Sample documents (Replace with the actual documents or a method to upload documents)


# Function to build an inverted index
def build_inverted_index(docs):
    inverted_index = defaultdict(set)
    for doc_id, text in docs.items():
        # Tokenization with normalization (lowercase)
        words = word_tokenize(re.sub(r'\W', ' ', text.lower()))
        for word in words:
            stemmed_word = stemmer.stem(word)
            inverted_index[stemmed_word].add(doc_id)
    return inverted_index

# Function to handle phrase queries and basic Boolean logic
def search(query, inverted_index, docs):
    query = query.lower()
    words = word_tokenize(query)
    op = None
    if 'and' in words:
        op = 'and'
    elif 'or' in words:
        op = 'or'
    elif 'not' in words:
        op = 'not'

    if op:  # If there's an operator in the query, split it based on the operator.
        parts = query.split(op)
        left = [stemmer.stem(word) for word in word_tokenize(parts[0]) if word.isalnum()]
        right = [stemmer.stem(word) for word in word_tokenize(parts[1]) if word.isalnum()] if len(parts) > 1 else []

        left_docs = set.intersection(*(inverted_index.get(word, set()) for word in left))
        right_docs = set.intersection(*(inverted_index.get(word, set()) for word in right)) if right else set()

        if op == 'and':
            final_docs = left_docs & right_docs
        elif op == 'or':
            final_docs = left_docs | right_docs
        elif op == 'not':
            final_docs = left_docs - right_docs
    else:  # Handle as a single word or unrecognized format query
        stemmed_words = [stemmer.stem(word) for word in words]
        final_docs = set.union(*(inverted_index.get(word, set()) for word in stemmed_words))

    return final_docs




# Building the inverted index
inverted_index = build_inverted_index(documents)

# Streamlit user input for queries
user_query = st.text_input("Enter your search query:")

# Search button
if st.button("Search"):
    # Perform search
    result_docs = search(user_query, inverted_index, documents)
    if result_docs:
        st.write("Documents matching the query:")
        for doc_id in result_docs:
            st.write(f"Document {doc_id}: {documents[doc_id]}")
    else:
        st.write("No documents match your query.")
