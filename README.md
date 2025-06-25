

🎬 Movie Recommender System
This is a content-based movie recommendation system that suggests movies based on user-selected industry (Bollywood or Hollywood) and genre (e.g., Action, Romance, Thriller). It uses TF-IDF vectorization and cosine similarity to find and recommend similar films based on movie descriptions.

💡 Features
🎯 Smart filtering by industry & genre

🎯 "More like this" recommendations based on selected movie

🧠 TF-IDF for text vectorization

📐 Cosine similarity to measure closeness of movie plots

📂 Handles user queries interactively in the terminal

🛠️ Tech Stack
Python

pandas

scikit-learn (TF-IDF & Cosine Similarity)

📁 Dataset
The dataset (movies.csv) should contain the following columns:

title: Movie name

description: Short plot/summary

genre: Movie genre(s)

industry: Movie industry (e.g., Bollywood, Hollywood)

🚀 How to Run
Make sure required libraries are installed:

bash
Copy
Edit
pip install pandas scikit-learn
Place movies.csv in the same folder or update the path accordingly in the code.

Run the Python file:

bash
Copy
Edit
python movie_recommender.py
Follow the interactive prompts to get movie recommendations.

📌 Example Interaction
markdown
Copy
Edit
🎬 Welcome to the Movie Recommender!

👉 Choose Industry (Bollywood / Hollywood): Bollywood
🎭 Choose Genre (e.g., Action, Romance, Thriller, Drama, Comedy): Action

✅ Recommended movies for your preferences:

1. War
2. RRR
3. Don
4. Baaghi
5. Simmba

  Want more like one of these? Type number (1–5) or 'no' to stop:
🎬 Your choice: 1

🧠 More movies like *War*:

1. Ek Tha Tiger
2. Bang Bang
3. Pathaan
...