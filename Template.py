#!/usr/bin/env python3
import webbrowser
import sys, os
from requests import get
import hashlib
import datetime
from pathlib import Path
from selenium import webdriver
import subprocess

class Template(object):
	def __init__(self):
		# identify the init
		self.identifier = str(os.environ.get("USER") + "\'s Page")
		# identify the user's IP for safety reasons
		self.ip = get('https://api.ipify.org')
		# get the author name
		self.author = os.environ.get("USER")
		# get the last edit date
		self.edit_date = f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S%z}'

	# Gen page (2)

	def create_page(self, title: str, author: str, save_to: str):
		try:
			Path(save_to).touch(exist_ok=False)
		except FileExistsError:
			print("The file path name already exists. Please rename your file to something else.")
		print(f"Success. Touched HTML file at {save_to}.")
		with open(save_to, "w") as file:
			file.write("""<!DOCTYPE html>
  <html>
    <head>
      <title>{titleHTML}</title>
      <meta name="author" content="{authorHTML}">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
    </body></html>""".format(titleHTML=title, authorHTML=author))
		print("Success. Your page has been generated with title and author tags.")

	# Elements

	def h1(self, title: str, size: int, color: str, center: bool, font: str, save_to: str):
		size = str(size)
		if center == True:
			center = "center"
		else:
			center = "left"
		lines = open(save_to).read().splitlines()
		lines[-1] = f"<h1 style='font-size:{size}px;color:{color};text-align:{center};font-family:\"{font}\", sans-serif;'>{title}</h1>\n</body></html>"
		open(save_to, 'w').write('\n'.join(lines))
		open(save_to).close()
		print(f"Successfully wrote an <h1> tag with title '{title}'.")

	def h2(self, title: str, size: int, color: str, center: bool, font: str, save_to: str):
		size = str(size)
		if center == True:
			center = "center"
		else:
			center = "left"
		lines = open(save_to).read().splitlines()
		lines[-1] = f"<h2 style='font-size:{size}px;color:{color};text-align:{center};font-family:\"{font}\", sans-serif;'>{title}</h2>\n</body></html>"
		open(save_to, 'w').write('\n'.join(lines))
		open(save_to).close()
		print(f"Successfully wrote an <h2> tag with title '{title}'.")

	def h3(self, title: str, size: int, color: str, center: bool, font: str, save_to: str):
		size = str(size)
		if center == True:
			center = "center"
		else:
			center = "left"
		lines = open(save_to).read().splitlines()
		lines[-1] = f"<h3 style='font-size:{size}px;color:{color};text-align:{center};font-family:\"{font}\", sans-serif;'>{title}</h3>\n</body></html>"
		open(save_to, 'w').write('\n'.join(lines))
		open(save_to).close()
		print(f"Successfully wrote an <h3> tag with title '{title}'.")

	def h4(self, title: str, size: int, color: str, center: bool, font: str, save_to: str):
		size = str(size)
		if center == True:
			center = "center"
		else:
			center = "left"
		lines = open(save_to).read().splitlines()
		lines[-1] = f"<h4 style='font-size:{size}px;color:{color};text-align:{center};font-family:\"{font}\", sans-serif;'>{title}</h4>\n</body></html>"
		open(save_to, 'w').write('\n'.join(lines))
		open(save_to).close()
		print(f"Successfully wrote an <h2> tag with title '{title}'.")

	def h5(self, title: str, size: int, color: str, center: bool, font: str, save_to: str):
		size = str(size)
		if center == True:
			center = "center"
		else:
			center = "left"
		lines = open(save_to).read().splitlines()
		lines[-1] = f"<h5 style='font-size:{size}px;color:{color};text-align:{center};font-family:\"{font}\", sans-serif;'>{title}</h5>\n</body></html>"
		open(save_to, 'w').write('\n'.join(lines))
		open(save_to).close()
		print(f"Successfully wrote an <h5> tag with title '{title}'.")

	def h6(self, title: str, size: int, color: str, center: bool, font: str, save_to: str):
		size = str(size)
		if center == True:
			center = "center"
		else:
			center = "left"
		lines = open(save_to).read().splitlines()
		lines[-1] = f"<h6 style='font-size:{size}px;color:{color};text-align:{center};font-family:\"{font}\", sans-serif;'>{title}</h6>\n</body></html>"
		open(save_to, 'w').write('\n'.join(lines))
		open(save_to).close()
		print(f"Successfully wrote an <h6> tag with title '{title}'.")

	# ///////////////////////////////////////////////////////////////////////////////////


	#TODO: Figure out how to put elements in div programmatically
	"""

	DIV(x, y, width, height, hex) -> str (all are strings)

	x is the left position for HTML
	y is the top position for HTML
	width is the width of the HTML element
	height is the height of the HTML element
	hex is the #EXAMPL coloration

	"""

	def div(self, x: str, y: str, width: str, height: str, hex: str):
		pass

	# ///////////////////////////////////////////////////////////////////////////////////
	# ACTIVATE OPTIONS

	"""

	OPEN/NEWWINDOW(saved_to) -> WebView

	saved_to is the local/public path to the html file (static)

	OPEN requires Google Chrome or a default web browser. It opens static page to the internet.
	NEWWINDOW requires G. C. or def. web, and opens in new window (tabless).

	"""

	def open(self, saved_to: str):
		webbrowser.open('file://' + os.path.realpath(saved_to))
		print("Success. Opened your file in your default browser.")

	def tablesswindow(self, saved_to: str): # must have chrome stable (terminal)
		import platform
		if platform.system() == "Darwin":
			saved_to = os.path.abspath(saved_to)
			subprocess.Popen(f"/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --new-window --app=file://{saved_to}", shell=True, stdout=subprocess.PIPE)
			print("Successfully opened in tabless window.")
		else:
			print("Not on a supported system.")


	"""

	SCREENSHOT(save_to, save_image_to) -> Array

	save_to is the local/public path to the html file from localhost or the internet (static)
	save_image_to is the path to the directory where the screenshot should be stored

	SCREENSHOT requires Selenium webdriver Google Chrome

	SCREENSHOT takes a picture of your static page on first frame load and saves to path

	"""

	def screenshot(self, save_to: str, save_image_to: str):
		# DEF
		DRIVER = 'chromedriver' # assert chrome

		driver = webdriver.Chrome(DRIVER)
		driver.get("file://" + os.path.abspath(save_to))
		screenshot = driver.save_screenshot(save_image_to)
		driver.quit()

class UnitTest(object):
	def __init__(self):
		pass




