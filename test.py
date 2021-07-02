#!/usr/bin/env python3
from Template import Template
import time
t = Template()
t.create_page("Test Page", "Vlad U", "testpage.html")
t.h1('Example', 32, 'black', True, 'BlinkMacSystemFont', 'testpage.html')
t.div("20px", "100px", "200px", "200px", "testyDiv", "testpage.html")

string = "a"
for x in range(0, 5):
	t.classreload("testyDiv", f"{string}", "5", "testpage.html")
	string = string + "a"
	t.open("testpage.html")
	time.sleep(5)
# t.startserver()
#t.tablesswindow("testpage.html")
