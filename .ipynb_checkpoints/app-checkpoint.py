import streamlit as st 
import pickle 
import numpy as np 
import pandas as pd 
import streamlit.components.v1 as components

# ------------------- CONFIG -------------------
st.set_page_config(page_title="📚 Book Recommender", layout="wide")

# ------------------- CUSTOM CSS & MODAL -------------------
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
        }
        /* Page background */
        .main {
            background-color: #121212;
        }
        /* Sidebar background */
        .css-1d391kg {
            background-color: #1C1C1C;
        }
        /* Book Card */
        .book-card {
            background: linear-gradient(145deg, #1E1E1E, #2C2C2C);
            padding: 15px;
            border-radius: 14px;
            box-shadow: 0px 3px 6px rgba(0,0,0,0.25);
            text-align: center;
            height: 280px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.3s ease-in-out;
            margin: 10px;
            cursor: pointer;
        }
        .book-card:hover {
            transform: scale(1.08) ;
            box-shadow: 0px 10px 22px rgba(0,0,0,0.55);
            background: linear-gradient(145deg, #2C2C2C, #3A3A3A);
        }
        .book-card img {
            height: 150px;
            width: auto;
            object-fit: contain;
            margin: 0 auto 10px auto;
        }
        .book-title {
            font-weight: bold;
            font-size: 14px;
            color: #f5f5f5;
            min-height: 35px;
            overflow: hidden;
        }
        .book-author {
            font-size: 12px;
            color: #bbb;
        }

        /* Modal background */
        .modal {
            display: none; 
            position: fixed; 
            z-index: 999; 
            padding-top: 80px; 
            left: 0; top: 0;
            width: 100%; height: 100%;
            overflow: auto;
            background-color: rgba(0,0,0,0.75);
            backdrop-filter: blur(8px);
        }
        /* Modal content */
        .modal-content {
            background: rgba(30,30,30,0.9);
            margin: auto;
            padding: 20px;
            border-radius: 14px;
            width: 340px;
            text-align: center;
            color: #fff;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.6);
            animation: fadeIn 0.3s ease-in-out;
        }
        /* Close button */
        .close {
            color: #ff4d4d;
            float: right;
            font-size: 30px;
            font-weight: bold;
            cursor: pointer;
            margin-top: -10px;
        }
        .close:hover {
            color: #fff;
            transform: scale(1.2);
        }
        @keyframes fadeIn {
            from {opacity: 0; transform: scale(0.9);}
            to {opacity: 1; transform: scale(1);}
        }
    </style>

    <script>
        function openModal(title, author, img) {
            document.getElementById("bookModal").style.display = "block";
            document.getElementById("modalTitle").innerText = title;
            document.getElementById("modalAuthor").innerText = author;
            document.getElementById("modalImg").src = img;
        }
        function closeModal() {
            document.getElementById("bookModal").style.display = "none";
        }
    </script>

    <!-- Modal structure -->
    <div id="bookModal" class="modal">
      <div class="modal-content">
        <span class="close" onclick="closeModal()">❌</span>
        <img id="modalImg" src="" style="width:150px; margin-bottom:15px; border-radius:10px;">
        <h3 id="modalTitle"></h3>
        <p id="modalAuthor"></p>
      </div>
    </div>
""", unsafe_allow_html=True)

# ------------------- HEADER -------------------
st.title("📖 Book Recommender System")
st.markdown('''
✨ A personalized book recommendation engine powered by **Collaborative Filtering**.  
Browse the **Top 50 Books** or get **AI-powered book suggestions**.
''')

# ------------------- LOAD MODELS -------------------
popular = pickle.load(open('popular.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb')) 

# ------------------- TOP 50 BOOKS -------------------
st.sidebar.header("🔥 Top 50 Books")
if st.sidebar.button("Show Top Books"):
    st.subheader("📚 Top 50 Most Popular Books")
    cols_per_row = 5
    num_rows = 10
    for row in range(num_rows): 
        cols = st.columns(cols_per_row)
        for col in range(cols_per_row): 
            book_idx = row * cols_per_row + col
            if book_idx < len(popular):
                with cols[col]:
                    st.markdown(f"""
                        <div class="book-card" onclick="openModal(
                            '{popular.iloc[book_idx]['Book-Title']}',
                            '👤 {popular.iloc[book_idx]['Book-Author']}',
                            '{popular.iloc[book_idx]['Image-URL-M']}'
                        )">
                            <img src="{popular.iloc[book_idx]['Image-URL-M']}">
                            <div class="book-title">{popular.iloc[book_idx]['Book-Title']}</div>
                            <div class="book-author">👤 {popular.iloc[book_idx]['Book-Author']}</div>
                        </div>
                    """, unsafe_allow_html=True)

# ------------------- RECOMMEND FUNCTION -------------------
def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x : x[1],
        reverse=True
    )[1:6]
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item) 
    return data

# ------------------- RECOMMENDATION SECTION -------------------
st.sidebar.header("🎯 Book Suggestions")
book_list = pt.index.values
selected_book = st.sidebar.selectbox("Select a book", book_list)

if st.sidebar.button("Recommend Me"):
    st.subheader(f"📌 Because you liked *{selected_book}*...")
    book_recommend = recommend(selected_book)
    cols = st.columns(5)
    for col_idx in range(5):
        if col_idx < len(book_recommend):
            with cols[col_idx]:
                st.markdown(f"""
                    <div class="book-card" onclick="openModal(
                        '{book_recommend[col_idx][0]}',
                        '👤 {book_recommend[col_idx][1]}',
                        '{book_recommend[col_idx][2]}'
                    )">
                        <img src="{book_recommend[col_idx][2]}">
                        <div class="book-title">{book_recommend[col_idx][0]}</div>
                        <div class="book-author">👤 {book_recommend[col_idx][1]}</div>
                    </div>
                """, unsafe_allow_html=True)

# ------------------- SHOW DATA -------------------
books_data = pd.read_csv('Data/Books.csv')
users_data = pd.read_csv('Data/Users.csv')
ratings_data = pd.read_csv('Data/Ratings.csv')

st.sidebar.header("📊 Data Used")
if st.sidebar.button("Show Dataset"):
    st.subheader('📘 Books Data')
    st.dataframe(books_data.head(20))
    st.subheader('⭐ Ratings Data')
    st.dataframe(ratings_data.head(20))
    st.subheader('👤 Users Data')
    st.dataframe(users_data.head(20))
