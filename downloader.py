import requests
from bs4 import BeautifulSoup
import os


class Downloader:
    def __init__(self, tags, resolution, pages_val=5):
        self.resolution = resolution
        self.tags = tags
        self.images = []
        self.pages_val = pages_val
        
    
    def get_images(self):
        for val in range(1, self.pages_val + 1):  # Download images on each page for specific resoluiton
            req = requests.get(f"https://wallpaperscraft.com/all/{self.resolution}/page{val}")
            soup = BeautifulSoup(req.text, features="html.parser")
            result = []
            for wallpaper in soup.find_all("img"):  # Parse all urls on the page
                link = str(wallpaper.get("src"))
                if link.startswith("https://images.wallpaperscraft.com"):
                    result.append(link)
            for url in result:
                for tag in self.tags:  # And now check all tags for equality
                    if tag in url:
                        replaced = url.replace("300x168", self.resolution)  # Replace default resoltion in the URL
                        img = requests.get(replaced, stream=True)
                        if not os.path.exists("saved_images"):  # Create a new folder if it doesn't exists already
                            os.makedirs("saved_images")
                        with open(f"saved_images/{replaced.split('/')[-1:][0]}", "wb") as f: # Save images to the folder
                            for chunk in img:
                                f.write(chunk)
