# Task 3 - Movie Recommender 🎬📽️

This is a **content-based movie recommender system** created using Python. It suggests similar movies based on **user-selected genre and industry** (Bollywood / Hollywood) using **TF-IDF vectorization** and **cosine similarity**. The user can also request more recommendations like a specific movie from the list.

---

## 💡 Features

- 🎯 Smart filtering by industry & genre  
- 🎯 "More like this" recommendations on selected movies  
- 🧠 TF-IDF vectorization of movie descriptions  
- 📐 Cosine similarity for finding closeness between plots  
- 💬 Interactive terminal-based experience  
- ♻️ Option to continue exploring recommendations in-depth  

---

## 📁 Files Included

- `movie_recommender.py` – Main Python script  
- `movies.csv` – Dataset containing titles, genres, descriptions, and industries  
- `README.md` – Project overview and usage guide  

---

## ▶️ How to Run

1. Ensure Python is installed (preferably version 3.6+)
2. Install dependencies using:
   ```bash
   pip install pandas scikit-learn
Make sure movies.csv is in the correct path or adjust the file path in the script.

Open terminal or command prompt

Run the recommender using:

bash
Copy
Edit
python movie_recommender.py
💬 Example Conversation
markdown
Copy
Edit
🎬 Welcome to the Movie Recommender!

👉 Choose Industry (Bollywood / Hollywood): Hollywood
🎭 Choose Genre (e.g., Action, Romance, Thriller, Drama, Comedy): Sci-Fi

✅ Recommended movies for your preferences:

1. Interstellar
2. Inception
3. The Matrix
4. Avatar
5. Tenet

  Want more like one of these? Type number (1–5) or 'no' to stop:
🎬 Your choice: 2

🧠 More movies like *Inception*:

1. Tenet
2. Shutter Island
3. The Prestige
4. Interstellar
5. Source Code

🔁 Do you want to try a different industry or genre? (yes/no)
🔄 Your choice: no

👋 Thanks for using the Movie Recommender!
