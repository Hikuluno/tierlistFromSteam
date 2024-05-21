# Steam Tier List Maker

## Project Overview

The Steam Tier List Maker is a Python script designed to create a tier list based on your Steam library. It downloads images for each game you own on Steam. Then you can generate a tier list using these images on [TierMaker](https://tiermaker.com/).

## How to Use

### 1. Initializing a Virtual Environment and Installing Dependencies

Clone the repository to your local machine and create a virtual environment:

```bash
python3 -m venv myenv
myenv\Scripts\activate
```

Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Creating Your Configuration File

Before running the script, you need to create a config.properties file in the project directory. This file contains your Steam API key and Steam ID. You can obtain your Steam API key by following the instructions here and find your Steam ID by using a service like SteamID Finder.

Here's an example of how your config.properties file should look:

```properties
[DEFAULT]
key=YOUR_STEAM_API_KEY
steamid=YOUR_STEAM_ID
```

### 3. Running the Script

Once you have set up your virtual environment and created the config.properties file, you can run the script:

```bash
python steam_tier_list_maker.py
```

The script will download images for each game in your Steam library and save them to the steam_images directory.
