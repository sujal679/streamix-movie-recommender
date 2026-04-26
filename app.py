import streamlit as st
from model import recommend, movies
import base64
import requests

# 🔑 ADD YOUR TMDB API KEY HERE
API_KEY = "3dc79154354b27de6458fe5f67dcb030"

# 🔥 Convert background image
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("background.jpeg")

# 🎬 Fetch movie poster
import requests
import re 

def fetch_poster(movie_title):
    try:
        # 🔥 Step 1: clean title properly
        movie_title = re.sub(r"\(\d{4}\)", "", movie_title)  # remove year
        movie_title = movie_title.split(":")[0]             # remove subtitle
        movie_title = movie_title.strip()

        # 🔥 Step 2: call API
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": API_KEY,
            "query": movie_title
        }

        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        # 🔥 Step 3: check results properly
        if data.get("results"):
            for movie in data["results"]:
                if movie.get("poster_path"):
                    return f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"

        # 🔥 fallback image
        return "https://via.placeholder.com/300x450?text=No+Image"

    except Exception as e:
        print("ERROR:", e)
        return "https://via.placeholder.com/300x450?text=Error"
# 🎨 Page config
st.set_page_config(page_title="Streamix", page_icon="🎬", layout="wide")

# 🎨 Styling
st.markdown(f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Poppins:wght@300;500;700&display=swap');

/* 🌊 Background */
[data-testid="stAppViewContainer"] {{
    background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.95)),
                url("data:image/jpeg;base64,{bg}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

[data-testid="stHeader"] {{
    background: transparent;
}}

/* 🌐 Font */
html, body, [class*="css"] {{
    font-family: 'Poppins', sans-serif;
}}

/* 🎬 Title */
.title {{
    font-family: 'Bebas Neue', sans-serif;
    font-size: 80px !important;
    text-align: center;
    color: #E50914;
}}

/* 🔍 Label */
.label {{
    font-size: 22px;
    color: #ccc;
}}

/* 🔎 Input */
input {{
    background-color: #1c1c1c !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 10px !important;
}}

/* 🎯 Selectbox */
div[data-baseweb="select"] > div {{
    background-color: #1c1c1c !important;
    border-radius: 12px !important;
    padding: 10px !important;
    font-size: 16px !important;
    border: 1px solid #333 !important;
}}

div[data-baseweb="select"] span {{
    color: white !important;
}}

/* 🚀 Button */
.stButton > button {{
    background-color: #E50914;
    color: white;
    border-radius: 10px;
    padding: 10px 25px;
    font-size: 18px;
    border: none;
}}

.stButton > button:hover {{
    background-color: #ff1a1a;
    transform: scale(1.05);
}}

</style>
""", unsafe_allow_html=True)

# 🎬 Title
st.markdown('<p class="title">STREAM<span style="color:white;">IX</span></p>', unsafe_allow_html=True)

movie_list = movies['title'].values

# 📐 Layout center
col1, col2, col3 = st.columns([2,2,2])

with col2:

    # 🔍 SEARCH (FIXED VERSION)
    st.markdown('<p class="label">🎥 Search your movie</p>', unsafe_allow_html=True)

    search_query = st.text_input("", placeholder="Type movie name...")

    # Default = what user typed
    selected_movie = search_query

    # Show suggestions
    if search_query:
        filtered_movies = [m for m in movie_list if search_query.lower() in m.lower()]
        
        if filtered_movies:
            selected_movie = st.selectbox("Suggestions", filtered_movies)

    # Fallback
    if not search_query:
        selected_movie = st.selectbox("Or pick a movie", movie_list)

    # 🚀 Recommend
    if st.button("🚀 Recommend"):

        if selected_movie == "":
            st.warning("Please type or select a movie first!")
        else:
            names = recommend(selected_movie)

            st.subheader("✨ Recommended Movies")

            cols = st.columns(5)

            for i in range(len(names)):
                with cols[i % 5]:
                    st.image(fetch_poster(names[i]))
                    st.caption(names[i])