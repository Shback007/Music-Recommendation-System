# 🎵 Music Recommendation System

This is a content-based Music Recommendation System built using Python. It suggests similar songs based on audio features like acousticness, danceability, energy, and more. The project includes a web interface powered by Streamlit to interactively receive recommendations.

## 📌 Key Features

- Content-based filtering using song features
- Cosine similarity for finding similar tracks
- Interactive UI with Streamlit
- Returns top 10 recommended songs
- Lightweight and easy to deploy

## 📁 Project Structure
```
Music-Recommendation-System/
├── app.py                             # Streamlit app code
├── music-recommendation-system.ipynb # Jupyter notebook for exploration and modeling
├── songs.csv                          # Dataset containing song metadata and audio features
├── requirements.txt                   # List of Python dependencies
└── README.md                          # Project documentation
```

## 📊 How It Works

1. **Data Input**: Uses `songs.csv`, which includes several numerical audio features for each song.
2. **Similarity Calculation**: Uses cosine similarity between feature vectors of songs.
3. **Recommendation Logic**: Given a selected song, recommends the 10 most similar songs.
4. **Web Interface**: Streamlit is used to provide a simple dropdown UI for selecting songs.

### 🔧 Installation

1. **Clone the repository:**

```
git clone https://github.com/Shback007/Music-Recommendation-System.git
cd Music-Recommendation-System

streamlit run app.py
```
2. **Install required libraries:**
```
pip install -r requirements.txt
```
3. **Run the Streamlit app:**
```
streamlit run app.py
```
