# NLP Day 1 - Learning Summary

## Assignment 1: Text Preprocessing

Text preprocessing is the foundation of any NLP pipeline. Raw text is messy and contains noise that must be cleaned before any analysis or model training. The key steps performed are:

**Lowercasing** converts all characters to lowercase so that words like "Movie" and "movie" are treated identically. **Tokenization** splits a sentence into individual word tokens using NLTK's word_tokenize function. **Punctuation removal** filters out characters like periods, commas, and exclamation marks that carry no analytical value. **Stopword removal** drops very common English words such as "the", "is", "a", and "it" that appear frequently but carry little meaning. Finally, **whitespace filtering** removes any blank or empty tokens produced during tokenization.

The output is a clean list of meaningful keywords for each document. For example, "The movie was absolutely fantastic! I loved the acting." becomes ['movie', 'absolutely', 'fantastic', 'loved', 'acting']. These cleaned tokens serve as input for both TF-IDF and Word2Vec in the subsequent assignments.

## Assignment 2: TF-IDF Vectorization

TF-IDF (Term Frequency - Inverse Document Frequency) converts text into numerical vectors that machines can process. TF measures how often a word appears in a document, while IDF measures how rare that word is across all documents.

A high TF-IDF score means a word is very important to a particular document. It appears frequently in that document but is rare across the rest, making it a distinguishing keyword. IDF is important because without it, common words like "good" or "use" would score high everywhere even though they do not help distinguish documents. IDF penalizes such common words and gives higher weight to unique, distinctive terms.

Using sklearn's TfidfVectorizer, the 20-document dataset was converted into a matrix of shape (20, 94), meaning 20 documents and 94 unique vocabulary words. The top-scoring words per document correctly identified the most distinctive terms, such as "fantastic" and "loved" for a positive movie review, and "terrible" and "broke" for a negative product review.

## Assignment 3: Word2Vec Embeddings

Word2Vec learns dense vector representations of words based on their context in sentences. Unlike TF-IDF which uses word frequency, Word2Vec captures semantic meaning. Words used in similar contexts end up with similar vectors, so "good" and "great" would be close in vector space.

The model was trained using gensim's Word2Vec with a vector size of 50 dimensions, a context window of 3 words, and Skip-gram architecture (sg=1). The most_similar function finds words closest to a target word in vector space.

**Key differences between TF-IDF and Word2Vec:** TF-IDF produces sparse vectors based on frequency while Word2Vec produces dense vectors based on context. TF-IDF vector size grows with vocabulary while Word2Vec uses a fixed size. TF-IDF does not capture semantic similarity between synonyms while Word2Vec is designed for exactly that. TF-IDF works well for search and baseline classification while Word2Vec is better suited for similarity tasks, clustering, and deep learning applications.

**Overall takeaway:** Text preprocessing cleans raw text, TF-IDF converts it to frequency-based numbers, and Word2Vec converts it to meaning-based vectors. Each technique builds on the previous one, moving from raw text to increasingly sophisticated numerical representations that machines can understand and process.
