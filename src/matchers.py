from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def tfidf_match_score(resume: str, job: str) -> float:
    vect = TfidfVectorizer(stop_words="english", ngram_range=(1,2), min_df=1) # Keeps both uni/bigrams and at least one word occurences
    X = vect.fit_transform([resume, job])
    return float(cosine_similarity(X[0], X[1])[0][0]) # Returns number of 1x1 matrix

def sim_to_score(sim: float) -> int:
    return int(round(sim * 100)) # Converts 0-1 to human-friendly score