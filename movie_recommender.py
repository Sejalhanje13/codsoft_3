import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movie data
movies = pd.read_csv("C:/Users/Admin/Desktop/CODSOFT/Task 3/movies.csv")

# Fill missing values
movies["description"] = movies["description"].fillna("")
movies["genre"] = movies["genre"].fillna("")
movies["industry"] = movies["industry"].fillna("")

# TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(movies["description"])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def more_like_this(base_title, exclude_list, num_recommendations=5):
    try:
        base_index = movies[movies["title"].str.lower() == base_title.lower()].index[0]
    except IndexError:
        print("❌ Could not find the movie in dataset.")
        return []

    sim_scores = list(enumerate(cosine_sim[base_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for idx, score in sim_scores:
        candidate_title = movies.iloc[idx]["title"]
        if candidate_title.lower() != base_title.lower() and candidate_title not in exclude_list:
            recommendations.append(candidate_title)
        if len(recommendations) == num_recommendations:
            break

    if recommendations:
        print(f"\n🧠 More movies like *{base_title}*:\n")
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")
    else:
        print("No more similar movies found.")
    return recommendations

def recommend_by_industry_genre(industry_filter, genre_filter, num_recommendations=5):
    filtered_movies = movies[
        (movies["industry"].str.lower() == industry_filter.lower()) &
        (movies["genre"].str.lower().str.contains(genre_filter.lower()))
    ].reset_index()

    if filtered_movies.empty:
        print("\n❌ No movies found for your selected industry and genre.")
        return []

    base_original_index = random.choice(filtered_movies["index"].tolist())
    sim_scores = list(enumerate(cosine_sim[base_original_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for idx, score in sim_scores:
        movie = movies.iloc[idx]
        if idx != base_original_index and \
            movie["industry"].lower() == industry_filter.lower() and \
            genre_filter.lower() in movie["genre"].lower():
            recommendations.append(movie["title"])
        if len(recommendations) == num_recommendations:
            break

    print("\n✅ Recommended movies for your preferences:\n")
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec}")
    return recommendations

# Main Program
if __name__ == "__main__":
    print("🎬 Welcome to the Movie Recommender!")

    while True:
        industry_input = input("\n👉 Choose Industry (Bollywood / Hollywood): ").strip()
        genre_input = input("🎭 Choose Genre (e.g., Action, Romance, Thriller, Drama, Comedy): ").strip()

        exclude_list = []
        depth = 0

        last_recommendations = recommend_by_industry_genre(industry_input, genre_input)
        exclude_list.extend(last_recommendations)

        while last_recommendations and depth < 2:
            print("\n  Want more like one of these? Type number (1–5) or 'no' to stop:")

            user_input = input("🎬 Your choice: ").strip()

            if user_input.lower() == "no":
                break

            if not user_input.isdigit() or not (1 <= int(user_input) <= len(last_recommendations)):
                print("⚠️ Please choose a valid number from the list.")
                continue

            selected_title = last_recommendations[int(user_input) - 1]
            last_recommendations = more_like_this(selected_title, exclude_list)
            exclude_list.extend(last_recommendations)
            depth += 1

        print("\n🔁 Do you want to try a different industry or genre? (yes/no)")
        again = input("🔄 Your choice: ").strip().lower()
        if again != "yes":
            print("👋 Thanks for using the Movie Recommender!")
            break
