import os
import urllib2
import cookielib
from getpass import getpass
from urllib import urlencode

print "hello sam -sending Way2SMS message : "

def Login(user,passw,opener,cj):
	
	url="http://site21.way2sms.com/Login1.action"
	url_data = urlencode({
                            'username':user,
                            'password':passw,
                            })
  	# debug message
  	print url_data

  	

  	try:
  		sock = opener.open(url, url_data)	
  		
  		cooki = "hey" #only one cookie in cj
  		for cookies in cj:
   				cooki = cookies.value
  		

  		#print cookies
  		# debug message
  		#print usock.read()
  	except IOError:
  		return "CONNECTION_ERROR"
 	return cooki


def Message(opener,token) :
	mobile = raw_input("receiver mobile no : ")
	message = raw_input("enter message :")

	url="http://site21.way2sms.com/smstoss.action"

	url_data = urlencode({
                            'ssaction':'ss',
                            'mobile':mobile,
                            'message': message,
                            'msgLen' : 140-len(message),
                            'Token' : token
                            })

	opener.addheaders=[('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
)]
	opener.addheaders = [('User-Agent','Mozilla/5.0 (Ubuntu; X11; Linux x86_64; rv:8.0) Gecko/20100101 Firefox/8.0')]

	opener.addheaders = [('Accept-Encoding', 'gzip, deflate'
)]
	opener.addheaders = [('Cookie', 'JSESSIONID=A02~'+ token+'; _gat=1; _ga=GA1.2.1393827013.1466941873')]
	opener.addheaders= [('Referer','http://site21.way2sms.com/sendSMS?Token='+token)]
	opener.addheaders = [('Upgrade-Insecure-Requests',1)]
	print 'http://site21.way2sms.com/sendSMS?Token='+token
	
	print url_data
	req = urllib2.Request(url, url_data)
	response = opener.open(url,url_data)
	#print response.read()


  	
user = raw_input("Enter username: ")
passw = getpass()


cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# To fool the website as if a Web browser is visiting the site
opener.addheaders = [('User-Agent','Mozilla/5.0 (Ubuntu; X11; Linux x86_64; rv:8.0) Gecko/20100101 Firefox/8.0')]

Output = Login(user,passw,opener,cj)

if(Output == "CONNECTION_ERROR"):
	print "Check your connection || network traffic"
else:
	print Output[4:]
	Message(opener,Output[4:])
	#Message(opener)	
		

