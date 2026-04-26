import pandas as pd

# 🟢 STEP 1: Load data
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

print("📊 BEFORE CLEANING\n")

# 🟢 STEP 2: Check null values
print("Missing values in movies:\n", movies.isnull().sum())
print("\nMissing values in ratings:\n", ratings.isnull().sum())

# 🟢 STEP 3: Check duplicates
print("\nDuplicate rows in movies:", movies.duplicated().sum())
print("Duplicate rows in ratings:", ratings.duplicated().sum())

# 🟢 STEP 4: Remove null values
movies = movies.dropna()
ratings = ratings.dropna()

# 🟢 STEP 5: Remove duplicates
movies = movies.drop_duplicates()
ratings = ratings.drop_duplicates()

# 🟢 STEP 6: Clean text (titles)
movies['title'] = movies['title'].str.strip()

# 🟢 STEP 7: Reset index
movies = movies.reset_index(drop=True)
ratings = ratings.reset_index(drop=True)

print("\n📊 AFTER CLEANING\n")

# Check again after cleaning
print("Missing values in movies:\n", movies.isnull().sum())
print("\nMissing values in ratings:\n", ratings.isnull().sum())

print("\nDuplicate rows in movies:", movies.duplicated().sum())
print("Duplicate rows in ratings:", ratings.duplicated().sum())

# 🟢 STEP 8: Save cleaned data
movies.to_csv("movies_clean.csv", index=False)
ratings.to_csv("ratings_clean.csv", index=False)

print("\n✅ Data cleaned successfully and saved as:")
print("movies_clean.csv")
print("ratings_clean.csv")