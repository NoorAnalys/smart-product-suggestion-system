import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Example: Load your product data (ensure this file exists)
products_df = pd.read_csv('data/sample_products.csv')

# Example of feature extraction (e.g., using product tags)
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(products_df['product_tags'])

# Compute similarity matrix (cosine similarity)
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Save the model
joblib.dump(cosine_sim, 'ml_service/app/model/model.joblib')
