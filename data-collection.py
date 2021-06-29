# import libraries
from bs4 import BeautifulSoup
import requests
import os

# Defining the main url
base_url = "https://archives.bulbagarden.net/w/index.php?title=Category:Official_anime_artwork&"

# Defining all the subpages
pages = ["fileuntil=050%0A050Diglett-Alola+SM+anime.png#mw-category-media",
         "filefrom=050%0A050Diglett-Alola+SM+anime.png#mw-category-media",
         "filefrom=108%0A108Lickitung+OS+anime.png#mw-category-media",
         "filefrom=164%0A164Noctowl+OS+anime+2.png#mw-category-media",
         "filefrom=277%0A277Swellow+AG+anime+2.png#mw-category-media",
         "filefrom=382%0A382Kyogre-Primal+XY+anime+3.png#mw-category-media",
         "filefrom=475%0A475Gallade+XY+anime+2.png#mw-category-media",
         "filefrom=571%0A571Zoroark+BW+anime.png#mw-category-media",
         "filefrom=666%0A666Vivillon-Meadow+XY+anime.png#mw-category-media",
         "filefrom=786%0A786Tapu+Lele+SM+anime.png#mw-category-media"]

# Creating a list to stock all image links to be able to go through it later 
images = []

# Changing the working directory to choose where the images are going to be stored
os.chdir("/home/amadios/Documents/Projects/Pokemon-generator/data")



for url in pages:
    # Full url adding the subpage to the main url
    new_url = base_url + url
    # Requesting the page
    page = requests.get(new_url)
    # Turning it into text
    html = page.text
    # Finding all the images ( img tag ) and taking the link ( src attribute )
    soup = BeautifulSoup(html,"html.parser")
    for img in soup.findAll('img'):
        images.append(img.get('src'))
    # There is on each page a useless link which is the last one
    images.pop()

# Going through the links
for i in range(len(images)):
    url = images[i]
    # Reqyest the image
    page = requests.get(url)
    # Open a file with the name of the file on the website
    f = open(url.split('/')[-2], 'wb')
    # Write the content ( which is the image )
    f.write(page.content)
    f.close()
