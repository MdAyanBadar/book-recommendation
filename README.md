![Banner](assets/banner.png)

# 📚 Book Recommendation System

A **Streamlit-powered Book Recommendation System** that helps users discover new books using machine learning.  
It uses **Content-Based Filtering** and **Cosine Similarity** to recommend books similar to the one selected by the user.

---

## 🌐 Live Demo

Try the live app here:

👉 **[Book Recommendation App](https://book-recommendation-krraqpcvjfhtojsrwtsrxs.streamlit.app/)**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://book-recommendation-krraqpcvjfhtojsrwtsrxs.streamlit.app/)

---

## 🚀 Features

- 🔍 Search & select books with a clean Streamlit UI  
- 🤝 ML-powered recommendations using cosine similarity  
- ⚡ Fast, real-time suggestions  
- 📊 Uses metadata like title, authors, and tags  
- 🌐 Deployed on Streamlit Cloud

---

## 🧠 Tech Stack

**Frontend + Deployment**  
- Streamlit

**Backend / ML**  
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Cosine Similarity  
- Pickle (for similarity matrix)

---

## 📂 Project Structure


│
├── data/
│   ├── books.csv
│   ├── ratings.csv
│   └── users.csv
│
├── models/
│   └── similarity.pkl
│
├── app.py
├── requirements.txt
└── README.md


---

## ⚙️ How It Works

1. Load and clean dataset  
2. Convert book metadata into numerical vectors using TF-IDF / CountVectorizer  
3. Compute cosine similarity matrix between all books  
4. Streamlit UI allows user to select a book  
5. System returns Top N most similar books

---

## ▶️ Run Locally

1. Clone the Repository  
```bash``
git clone <your-repo-url>
cd book-recommendation

pip install -r requirements.txt

streamlit run app.py

🌐 Deploying on Streamlit Cloud

Push your project to GitHub (public repo recommended).

Visit https://share.streamlit.io
 and sign in.

Choose your repo and select app.py as the entrypoint.

Deploy — Streamlit will install packages from requirements.txt and launch the app.

🛠 Troubleshooting (if the live link isn't working)

Check Streamlit app logs on share.streamlit.io — they show errors (missing packages, import errors, file not found).

Ensure requirements.txt contains every dependency (streamlit, pandas, scikit-learn, etc.).

Make app.py the correct entrypoint and commit/push it.

Confirm assets and model files are in the repo (e.g., models/similarity.pkl, book CSVs) or load them from a hosted URL. Large model files may need to be stored elsewhere (GitHub has file-size limits).

Check file paths inside app.py — use relative paths (models/similarity.pkl) not absolute local paths.

If the app builds but shows a runtime error, reproduce locally (streamlit run app.py) — the terminal will show the same traceback. Fix and push.

Private repo: Streamlit Cloud needs read access — link the repo or make it public.

Missing secrets or environment variables: add them under the app settings on Streamlit Cloud.

If you get a 403 or 404 on the share link, re-deploy (there’s a redeploy option) after confirming GitHub HEAD is the branch Streamlit is pointed to.

📌 Future Enhancements

🎯 Add collaborative filtering

🎭 Display book covers/images (use Open Library / Google Books API)

👤 User login + personalized profile

🔮 Deep learning recommendations using embeddings

📱 Improved mobile UI

🤝 Contributing

Contributions are welcome! Fork the repo and open a PR.

🧑‍💻 Author

Ayan Badar
Machine Learning • Streamlit Projects • Full-Stack Development
📬 Open for feedback & collaboration
