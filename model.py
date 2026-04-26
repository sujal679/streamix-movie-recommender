import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load LOCAL data
movies_df = pd.read_csv('movies_clean.csv')
ratings_df = pd.read_csv('ratings_clean.csv')

# Merge data
merged_df = pd.merge(ratings_df, movies_df, on="movieId")

# Create matrix
user_movie_matrix = merged_df.pivot_table(index="userId", columns="title", values="rating")

# Fill missing values
user_movie_matrix_filled = user_movie_matrix.fillna(0)

# Compute similarity
item_similarity = cosine_similarity(user_movie_matrix_filled.T)

item_similarity_df = pd.DataFrame(item_similarity,
                                 index=user_movie_matrix.columns,
                                 columns=user_movie_matrix.columns)

# Recommendation function
def recommend(movie_title):
    if movie_title not in item_similarity_df.index:
        return ["Movie not found"]

    similar_movies = item_similarity_df[movie_title].sort_values(ascending=False)
    return similar_movies.drop(movie_title).head(5).index.tolist()

# For app
movies = movies_df