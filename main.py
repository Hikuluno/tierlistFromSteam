import requests
import configparser
import os

# Read the configuration file
config = configparser.ConfigParser()
config_file = 'config.properties'

if not os.path.exists(config_file):
    print(f"Configuration file '{
          config_file}' not found. Please create it from 'config.example.properties'.")
    exit(1)

config.read('config.properties')

# Get API key and steamid values from the configuration file
api_key = config.get('DEFAULT', 'key')
steam_id = config.get('DEFAULT', 'steamid')

# URL to get the list of games
games_url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"

# Initial request parameters
params = {
    "key": api_key,
    "steamid": steam_id,
    "include_played_free_games": True,
    "format": "json"
}

# Directory to save images
output_directory = "steam_images"
os.makedirs(output_directory, exist_ok=True)

# Make the initial request to get the list of games
response = requests.get(games_url, params=params)
games_data = response.json()

# Extract appids
appids = [game['appid'] for game in games_data['response']['games']]

# Base URL to get images (replace with the correct URL)
img_url_template = "https://steamcdn-a.akamaihd.net/steam/apps/{appid}/header.jpg"

# Download and save each image
for appid in appids:
    image_url = img_url_template.format(appid=appid)
    image_response = requests.get(image_url, stream=True)

    if image_response.status_code == 200:
        # File name to save the image
        image_path = os.path.join(output_directory, f"{appid}.jpg")
        with open(image_path, 'wb') as image_file:
            for chunk in image_response.iter_content(1024):
                image_file.write(chunk)
        print(f"Image for appid {appid} saved successfully.")
    else:
        print(f"Failed to retrieve image for appid {
              appid}. Status code: {image_response.status_code}")

print("All images downloaded.")
