# 🎬 Streamix Movie Recommender

A smart movie recommendation system built using **Python** and **Streamlit** that suggests movies based on user preferences. This project uses data-driven techniques to provide personalized recommendations in a clean and interactive UI.

---

## 🚀 Features

* 🎯 Personalized movie recommendations
* 📊 Uses real movie datasets (movies + ratings)
* ⚡ Fast and simple recommendation engine
* 💻 Interactive UI using Streamlit
* 📁 Clean and modular code structure

---

## 🧠 How It Works

The system uses **content-based filtering** to recommend movies.

* Movies are processed and cleaned using `clean_data.py`
* A similarity model is built in `model.py`
* Based on user input, similar movies are suggested
* Results are displayed using a Streamlit interface

---

## 🛠️ Tech Stack

* Python
* Pandas & NumPy
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

```
streamix-movie-recommender/
│
├── app.py                # Streamlit app (UI)
├── model.py              # Recommendation logic
├── clean_data.py         # Data preprocessing
├── movies.csv            # Movie dataset
├── ratings.csv           # Ratings dataset
├── movies_clean.csv      # Processed movies data
├── ratings_clean.csv     # Processed ratings data
├── background.jpeg       # UI background
├── .gitignore            # Ignored files
└── README.md             # Project documentation
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/sujal679/streamix-movie-recommender.git
cd streamix-movie-recommender
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 📸 Demo

*(Add a screenshot here of your app UI — this makes a BIG difference for recruiters)*

---

## 💡 Future Improvements

* Add collaborative filtering
* Improve recommendation accuracy
* Deploy online (Streamlit Cloud / Render)
* Add user login system
* Enhance UI/UX

---

## 👨‍💻 Author

**Sujal Thekkatte**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it helps!
