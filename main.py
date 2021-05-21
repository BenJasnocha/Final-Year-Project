import os
import json
import requests
from bs4 import BeautifulSoup
from skimage import io
import matplotlib.pyplot as plt

GOOGLE_IMAGES = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&"

usr_agent = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
	"Accept": "text/html,application/xhtml.application/xml;q=0.9*/*;q=0.8",
	"Accept-Charset": "ISO-8859-1,utf-8;q=0.7, *;q=0.3",
	"Accept-Encoding": "none",
	"Accept-Language": "en-US,en;q=0.8",
	"Connection": "keep-alive",
}


def main():
	download_images()


def download_images():
	data = input('What are you looking for? ')
	data = data.replace(" ", "+")

	# creates a new folder for each search unless the same search has been done before
	SAVE_FOLDER = "images "
	if not os.path.exists(SAVE_FOLDER + data):
		os.mkdir(SAVE_FOLDER + data)
		SAVE_FOLDER = SAVE_FOLDER + data
	n_images = int(input('How many images do you want download? '))

	print('Start searching.....')
	searchurl = GOOGLE_IMAGES + 'q=' + data

	# request url, without usr_agent, the permission gets denied
	response = requests.get(searchurl, headers=usr_agent)

	# find all divs where class='rg_meta'
	soup = BeautifulSoup(response.text, 'html.parser')
	results = soup.findAll('img', {'class': 'rg_i Q4LuWd'})
	print(results)
	# gathering requested number of list of image links with data-src attribute
	# continue the loop in case query fails for non-data-src attributes
	count = 0
	links = []
	for res in results:
		try:
			link = res['data-src']
			links.append(link)
			count += 1
			if (count >= n_images): break

		except KeyError:
			continue

	print(f'Downloading {len(links)} images....')

	# Access the data URI and download the image to a file
	j = 0
	for i, link in enumerate(links):
		response = requests.get(link)

		image = io.imread(link)
		plt.imshow(image)
		plt.show(block=False)#
		plt.pause(1)
		inp = input("c - keep, x - discard:")
		plt.close()
		if inp == "c":
			j += 1
			image_name = SAVE_FOLDER + '/' + data + str(j) + '.jpg'
			with open(image_name, 'wb') as fh:
				fh.write(response.content)


if __name__ == "__main__":
	main();
