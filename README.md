# MovieRec: Content-Based Movie Recommender

Discover new movies based on your favorites! MovieRec is a deployed web application that uses content-based filtering to recommend movies similar to the one you select.

## How does it work?
MovieRec combines information from genre, cast, director, and storyline for each movie, creating a unique textual representation. This representation is vectorized using TF-IDF, and cosine similarity is calculated between all movies. When you select a movie, the system returns the 5 most similar titles.

## Features
- Select a movie from the list
- Get 5 recommended movies based on content similarity
- Simple and intuitive Streamlit interface

## Getting Started
1. Clone this repository
2. Place your `movies.csv` file in the project root
3. Run the notebook `MovieRec_Recommendation_Engine.ipynb` to generate `movies.pkl` and `similarity.pkl`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   streamlit run app.py
   ```

## Deployment
You can deploy this app for free on [Streamlit Community Cloud](https://streamlit.io/cloud). Just upload your code and data files.

## Example
![App Screenshot](screenshot.png)

## Live Demo
[Add your Streamlit Cloud link here]

---

**How recommendations are made:**
Content-based filtering using TF-IDF and cosine similarity on combined movie features (genre, cast, director, storyline).

---

Feel free to contribute or reach out for questions!
