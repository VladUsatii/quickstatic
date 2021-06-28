#!/usr/bin/env python3
import webbrowser
import sys, os
from requests import get
import hashlib
import datetime
from pathlib import Path

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
    </body>
  </html>""".format(titleHTML=title, authorHTML=author))
		print("Success. Your page has been generated with title and author tags.")
	def h1(self, title: str, size: int, color: str, center: bool, font: str):
		pass
