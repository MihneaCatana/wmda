import pandas as pd

# Step 1: Load the MovieLens 100K dataset for ratings and movie details
url_ratings = "https://files.grouplens.org/datasets/movielens/ml-100k/u.data"
column_names = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_csv(url_ratings, sep="\t", names=column_names, usecols=["user_id", "movie_id", "rating"])

url_movies = "https://files.grouplens.org/datasets/movielens/ml-100k/u.item"
movies = pd.read_csv(url_movies, sep="|", encoding="latin-1", names=["movie_id", "title"], usecols=[0, 1])

# Step 2: Preprocess the dataset - filter out users who have rated fewer than 10 movies
user_ratings_count = ratings.groupby('user_id').size()
active_users = user_ratings_count[user_ratings_count >= 10].index

# Filter the ratings data to include only active users
filtered_ratings = ratings[ratings['user_id'].isin(active_users)]

# Step 3: Compute the average rating per movie
average_ratings = filtered_ratings.groupby('movie_id')['rating'].mean()

print(average_ratings)

# Step 4: Sort movies based on popularity (average rating)
popular_movies = average_ratings.sort_values(ascending=False)

# Step 5: Merge the movie titles with the average ratings
top_movies = popular_movies.head(5)  # Get the top 5 movies
top_movies_with_titles = pd.merge(top_movies, movies, on="movie_id", how="left")

# Step 6: Display the top 5 recommended movies
print("Top 5 Most Popular Movies Based on User Ratings:")
print(top_movies_with_titles[['title', 'rating']])
