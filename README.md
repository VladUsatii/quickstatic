# quickstatic

Ever wanted to generate quick HTML from tags using Python and see your result displayed in the browser? Ever wanted to make web coding more like PyQt, with templates and such? You've come to the right place. Read on to learn how to make fast static sites that actually look really good (we found a medium between too simplistic and too 1990's-style).

## Installation

Before anything, get these prerequisites for serving your site locally and rendering screenshots:

```
brew install http-server
brew install phantom-js
```

Firstly, ```git clone https://github.com/VladUsatii/quickstatic.git```. Put it in the project folder of the website you want to make, because it is as simple as importing classes.

Install ```requirements.txt``` by writing ```sudo pip install requirements.txt```. Use ```sudo```!

## Your First Website

Make your first website by doing the following:

```python3
#!/usr/bin/env python3
import sys, os # optionally get the os environment user

from quickstatic import Template
temp = Template() # init

# destination HTML file
save_to = "your/project/directory.html"

# create a page
temp.create_page(title="My First Site!", author="os.environ.get("USER")", save_to=save_to)

# add a header "<h1>" tag (we go by pixels)
temp.h1("Test Site", size=32, color="black", center=True, font="BlinkMacSystemFont")

# adds 4 divs in a row (be creative!)
for x in range(0, 5):
	temp.div(color="gray", padding=25, center=True)

# open in chrome
temp.open(save_to)

# or

# open in a custom tabless chrome window
temp.tablesswindow(save_to)

# or

# even run through HTTP-Server
temp.startserver() # localhost

```

We import Template, we initialize the library as a smaller variable, we create a page with a title and author and location, then add a header and 5 divs to it, colored gray. Everything is centered. Then, we run ```open()``` from the Template class and when running the Python script, it will open a new web browser window with your static page. We even ran a localhost server with your entire folder so that you can go back and forth.

It is that easy.

## Taking Screenshots

We made a oneliner to take screenshots of your website. This was made for simplicity and export reasons. What if a user wants to take a screenshot and use that image somewhere else to showcase how cool their Python quickstatic site is? Had to do it. Here is a basic implementation:

```python3
# yada yada yada imports
# ...

temp.screenshot("myhtmlpage.html", "screenshot.png")

# RESULT:
# [+] 1 Screenshot
# [-] 0 Errors

# SAMPLE OUTPUT:
# Downloads
# ??? Dev
#   ??? quickstatic
#     ??? screenshot
#       ??? screenshot.png

```

## Site Daemon

#### Coming with Stable Release 2
We made a daemon to auto reload portions of your static page every 'n' seconds. This is useful for standalone web apps that rely on reloads for status updates. What if the user is offline? What if a new ad has to reload?

```python3
# yada yada yada imports
# ...

temp.daemon("myhtmlpage.html", "div-or-html-class", 10) # 10 seconds
```

Add your site, your class for the element, and the reload time.

## Documentation

You can find our Docs by simply reading the code. There are multiline comments describing everything.

## Contribute

We gladly accept contributions and help with this idea. It was originally created to make HTML less boring and more script-oriented. If you think about it, it is very similar to PyQt's concept of stylesheets and tags. If you can make it more user-friendly, a pull-request would be amazing.

## TODO:

- Add div entry
- Use stylesheets
- Import fonts
- Preload
- Full Stack Automation

----

Full project created by Vlad Usatii.
