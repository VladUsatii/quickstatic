# quickstatic

Ever wanted to generate quick HTML from tags using Python and see your result displayed in the browser? Ever wanted to make web coding more like PyQt, with templates and such? You've come to the right place. Read on to learn how to make fast static sites that actually look really good (we found a medium between too simplistic and too 1990's-style).

## Installation

Firstly, ```git clone https://github.com/VladUsatii/quickstatic.git```. Put it in the project folder of the website you want to make, because it is as simple as importing classes.

Install ```requirements.txt``` by writing ```pip install requirements.txt```.

## Your First Website

Make your first website by doing the following:

```python3
#!/usr/bin/env python3
import sys, os # optionally get the os environment user

from quickstatic import Template
temp = Template() # init

# create a page
temp.create_page(title="My First Site!", author="os.environ.get("USER")", save_to="your/project/directory.html")

# add a header "<h1>" tag (we go by pixels)
temp.h1("Test Site", size=32, color="black", center=True, font="BlinkMacSystemFont")

for x in range(0, 5):
	temp.div(color="gray", padding=25, center=True)

temp.open()
```

We import Template, we initialize the library as a smaller variable, we create a page with a title and author and location, then add a header and 5 divs to it, colored gray. Everything is centered. Then, we run ```open()``` from the Template class and when running the Python script, it will open a new web browser window with your static page.

It is that easy.

Now, if you want to add more and you want to make this fully animated and/or accessible by others, read our documentation.

## Documentation

You can find our Docs here:

<insert link here>

## Contribute

We gladly accept contributions and help with this idea. It was originally created to make HTML less boring and more script-oriented. If you think about it, it is very similar to PyQt's concept of stylesheets and tags. If you can make it more user-friendly, a pull-request would be amazing.
