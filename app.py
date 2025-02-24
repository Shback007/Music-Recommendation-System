import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# 🔹 Spotify API Credentials
CLIENT_ID = "533d956b570c4be0b08624456027a566"
CLIENT_SECRET = "b86190c669c94eedadb04979013bf970"

# 🔹 Initialize Spotify Client
client_Credentials_Manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_Credentials_Manager)

# 🔹 Load Pickle Files
try:
    music = pickle.load(open('df.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Missing 'df.pkl' or 'similarity.pkl'. Please check your files.")
    st.stop()

# 🔹 Function to Get Album Cover
def get_song_album_cover_url(song_name, artist_name):
    query = f"{song_name} {artist_name}"
    results = sp.search(q=query, type="track", limit=1)

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        return track["album"]["images"][0]["url"]
    else:
        return 'https://i.postimg.cc/0QNxYz4V/social.png'  # Default image

# 🔹 Recommendation Function
def recommend(song):
    if song not in music['song'].values:
        return [], []

    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_music_names = []
    recommended_music_posters = []

    for i in distances[1:6]:  # Top 5 recommendations
        artist = music.iloc[i[0]].artist
        song_name = music.iloc[i[0]].song
        recommended_music_names.append(song_name)
        recommended_music_posters.append(get_song_album_cover_url(song_name, artist))

    return recommended_music_names, recommended_music_posters

# 🔹 Streamlit UI with Colors
st.markdown("<h1 style='color: #1DB954;'>🎵 Music Recommender System</h1>", unsafe_allow_html=True)
st.write("Type or select a song from the dropdown:")

music_list = music['song'].values
selected_song = st.selectbox("Select a song", music_list)

if st.button('🔥 Show Recommendation'):
    recommended_music_names, recommended_music_posters = recommend(selected_song)

    if recommended_music_names:
        cols = st.columns(5)  # Creates 5 columns dynamically
        for col, name, img in zip(cols, recommended_music_names, recommended_music_posters):
            with col:
                st.text(name)
                st.image(img)
    else:
        st.warning("No recommendations found. Try another song.")
