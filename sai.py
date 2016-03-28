import time
from splinter import Browser

with Browser() as sameer:
    # Visit URL

    for i in range(1,1000000):
    	url = "http://www.iiita.ac.in"
    	sameer.visit(url)
    	time.sleep(300)