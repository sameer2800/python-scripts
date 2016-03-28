import os
import requests

for i in range(0,10):
	os.system("ls")

if not os.path.exists("sam"):
	os.system("mkdir sam")
else:
	print "path is already there"
	#os.system("vi sam.c")
	#os.system("mkdir sam")
	os.system("pwd")	

song1 = "Humme hai hero"
#r = requests.get('https://api.github.com/user', auth=('sameer2800', 'pass'))
r1 = requests.get('https://google.com');

with open('sam.txt', 'w') as file_:
    file_.write(r1.text.encode('utf-8').strip())