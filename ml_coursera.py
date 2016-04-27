import os
import requests

#requests.get('https://class.coursera.org/ml-005/lecture/download.mp4?lecture_id=7')


def download_file(url,filenm):
    
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    file="/coursera_ml/subtitles/"+filenm
    path=os.getcwd()+file


    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return 



for i in range(1,114):
	download_file('https://class.coursera.org/ml-005/lecture/subtitles?q='+ str(i) +'_en&format=srt','lecture'+str(i) +'.srt')
