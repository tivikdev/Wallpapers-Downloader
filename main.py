from downloader import Downloader
import configparser
import json
import os

# I think that there is nothing comment on...
if not os.path.isfile("config.ini"):
    input("Download config.ini from the repository before we start")
    exit(0)
config = configparser.ConfigParser()
config.read("config.ini")
dl = Downloader(json.loads(config.get("default", "tags")), config.get("default", "resolution"), config.getint("default", "pages_value"))
print("Loading, please wait...")
dl.get_images()
input("All images downloaded successfully. Press ENTER to exit. ")