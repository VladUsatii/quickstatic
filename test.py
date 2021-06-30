#!/usr/bin/env python3
from Template import Template

# 4 lines of code made this!

t = Template()
t.create_page("Test Page", "Vlad U", "testpage.html")
t.h1('Example', 32, 'black', True, 'BlinkMacSystemFont', 'testpage.html')
# t.open("testpage.html")
# t.startserver()
t.tablesswindow("testpage.html")
