# 🔥Content-Based Recommendation Systems

Welcome to the **Content-Based Recommendation Systems** project! This project is designed to provide recommendations for movies and Indian foods based on user preferences. It utilizes datasets from Kaggle, specifically the [TMDB Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) containing 5000 movies and the [Indian Foods and Its Recipes Dataset](https://www.kaggle.com/datasets/kishanpahadiya/indian-food-and-its-recipes-dataset-with-images) with 4000 Indian foods and recipes.

## Live Demo

Check out the live demo [here](https://akk-content-based-recommendation-systems.streamlit.app/).

## About this Project

### Motivation

Companies like Netflix, Amazon, and others employ recommendation systems to enhance user experience. These systems can be content-based, collaborative, or hybrid. This project focuses on content-based recommendation systems, where users receive suggestions based on their preferences.

### Datasets

1. **TMDB Movies Dataset:** Contains information on 5000+ movies.
2. **Indian Foods and Its Recipes Dataset:** Includes 4000+ Indian foods with recipes.

## Project Development Steps

1. **Download Dataset from Kaggle:** Obtain the necessary datasets for movies and Indian foods.
2. **Preprocessing:** Clean the datasets by handling null values, removing duplicates, unnecessary features, and overall data cleaning.
3. **Create "tags" Feature:** Generate a "tags" feature containing all relevant tags about movies or foods.
4. **Apply Stemming:** Utilize stemming on the "tags" column to consolidate words with similar meanings.
5. **Count Vectorizer:** Use scikit-learn's Count Vectorizer to create vectors containing the most frequent words from the entire dataset.
6. **Cosine Similarity:** Calculate the cosine similarity of each movie or food with all others in the dataset.
7. **Model Deployment:** Import the cosine similarity variable into a binary format and deploy it in a Streamlit app.

## Learning Outcomes

1. **Problem-Solving:** Overcome challenges, errors, and difficulties encountered during the project.
2. **Vectorization:** Create vectors to represent the most frequent words in the dataset.
3. **Cosine Similarity:** Understand and implement the calculation of cosine similarity.
4. **Model Deployment:** Successfully deploy the recommendation model in a Streamlit app.

## How to Run on Your Machine

1. **Clone the Repository:** Download all files and folders from this repository.
2. **Create Virtual Environment:**
   ```bash
   py -3 -m venv virtualEnv
3. **Run this command:**
   ```bash
   pip freeze > requirements.txt
4. **Finally start the streamlit app:**
   ```bash
   streamlit run streamlit_app.py
