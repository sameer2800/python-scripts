import facebook
import requests
import traceback

#get token from here : https://developers.facebook.com/tools/access_token/
#or here : https://developers.facebook.com/tools/explorer/145634995501895/

token = 'EAACEdEose0cBALeEfAeNW2jBmndwtbBfXxZBHCjiJR1VyMez3ZAHfOttYOxZA2deo9HBETReeu8XHx8F6wfXd6yQTo91nPJEymEYSLhl4nUuZBoiJpEcZC30ZARVoUiqHtsTZBRGvvCafOm2R9tfZBmXh1cWb9s1VBzDXSKP7aLZAiAZDZD'
bday_date= "2015-08-16"

def slice_date(post):
	date = post['created_time']
	return date[:10]

graph = facebook.GraphAPI(token)

friends = graph.get_connections(id='me', connection_name='friends')
#print friends

posts = graph.get_connections(id='me', connection_name='posts')
#print posts


def process_post(post):
	
	bday_comment = "Thank you :) "
	
	if(slice_date(post) == bday_date):
		p_id = post['id']			
		#print post
		#graph.put_like(p_id)
		#graph.put_comment(p_id,bday_comment)
			
		if 'story' in post :
			print "liking & commenting " + post['from']['name'] + " post. " + post['story']

		if 'message' in post:
			print "liking & commenting " + post['from']['name'] + " post. " + post['message']



def process_feed(user) :
	
	feed = graph.get_connections(id=user, connection_name='feed')
	print "hello world"

	while 1 :
		try :
			for post in feed['data']:
			   process_post(post)

			feed = requests.get(feed['paging']['next']).json()			
		except Exception :
			print(traceback.format_exc())
			break		   



process_feed("me")

