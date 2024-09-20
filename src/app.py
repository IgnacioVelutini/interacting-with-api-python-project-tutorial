import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import pandas as pd
import matplotlib.pyplot as plt

# Load environment variables
load_dotenv()

# Get environment variables
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Replace this with your favorite artist's ID
artist_id = "06HL4z0CvFAxyc27GXpf02"  # Example: Taylor Swift

# Fetch the artist's top tracks
top_tracks = sp.artist_top_tracks(artist_id)

# Extract and print song details (name, popularity, duration in minutes)
songs = [{
    "name": track['name'],
    "popularity": track['popularity'],
    "duration_min": track['duration_ms'] / 60000  # Convert duration from ms to minutes
} for track in top_tracks['tracks'][:10]]  # Limit to top 10 tracks

# Convert the list of songs into a DataFrame
df = pd.DataFrame(songs)

# Display the DataFrame
print(df)

# Create a scatter plot: Duration vs Popularity
plt.scatter(df['duration_min'], df['popularity'])
plt.title('Duration vs Popularity')
plt.xlabel('Duration (minutes)')
plt.ylabel('Popularity')
plt.show()
