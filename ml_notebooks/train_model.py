import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Load your product data
products_df = pd.read_csv('../data/sample_products.csv')

# Feature extraction using product tags
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(products_df['tags'])

# Compute similarity matrix (cosine similarity)
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Save the model and vectorizer
joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.joblib')
joblib.dump(cosine_sim, 'cosine_similarity_matrix.joblib')
