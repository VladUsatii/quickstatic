#!/usr/bin/env python3
import webbrowser
import sys
import os
import subprocess
from requests import get
import hashlib
import datetime
from pathlib import Path
import time
from webscreenshot.webscreenshot import *
import argparse

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

	def div(self, x: str, y: str, height: str, width: str, className: str, save_to: str):
		lines = open(save_to).read().splitlines()
		lines[-1] = f"<div style='left:{x};top:{y};height:{height};width:{width};' class=\"{className}\"></div>\n</body></html>"
		open(save_to, 'w').write('\n'.join(lines))
		open(save_to).close()
		print(f"Successfully wrote a <div> tag.")


	# ///////////////////////////////////////////////////////////////////////////////////
	# INTERACTIVE STATIC

	def classreload(self, tagclass: str, newContent: str, reloadtime: int, save_to: str):
		reloadtime = str(reloadtime)
		lines = open(save_to).read().splitlines()
		lines[-1] = "<script>\nfunction updateDiv() { var d = document.document.getElementsByClassName(\"" + tagclass + "\")[0];d.innerHTML = \"" + newContent + "\";}setInterval(updateDiv, " + reloadtime + "000);</script>\n</body></html>"
		open(save_to, 'w').write('\n'.join(lines))
		open(save_to).close()
		print(f"Successfully wrote a classreload in JavaScript with reload time of '{reloadtime}'.")


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

	def startserver(self):
		ask = input("Is quickstatic in the same directory as your html document? Please answer honestly. If you move html file from the folder, this process won't run (" + u"\u001b[32my\u001b[0m or \u001b[31mn\u001b[0m).")
		if ask == 'y':
			try:
				subprocess.run(['http-server'])
				print("To view your HTML file, click on the name of your saved_to file in the directory found at your HTTP localhost location.")
			except KeyboardInterrupt:
				pass
		else:
			pass

	"""

	SCREENSHOT(save_to, save_image_to) -> Array

	save_to is the local/public path to the html file from localhost or the internet (static)
	save_image_to is the path to the directory where the screenshot should be stored

	SCREENSHOT requires Selenium webdriver Google Chrome (NOT Chromium Stable or others)

	SCREENSHOT takes a picture of your static page on first frame load and saves to path
	Note: USE only AFTER declaring site headers and content

	"""

	def screenshot(self, save_to: str, save_image_to: str):
		# init for screenshot
		path = Path(__file__).parent.resolve()
		save_to = str(path) + f"/{save_to}"
		url = [f"file://{save_to}"]
		save_image_to = str(path) + f"/{save_image_to}"
		print(path, save_to, url, save_image_to)

		options = argparse.Namespace(URL=None, ajax_max_timeouts='1400,1800', cookie=None, crop=None, custom_js=None, format='png', header=None, http_password=None, http_username=None, imagemagick_binary=None, input_file=None, label=False, label_bg_color='NavajoWhite', label_size=60, log_level='DEBUG', multiprotocol=False, no_error_file=False, no_xserver=False, output_directory=f'{save_image_to}', port=None, proxy=None, proxy_auth=None, proxy_type=None, quality=75, renderer='phantomjs', renderer_binary=None, single_output_file=None, ssl=False, timeout=30, verbosity=2, window_size='1200,800', workers=4)

		take_screenshot(url, options)

class UnitTest(object):
	def __init__(self):
		pass




