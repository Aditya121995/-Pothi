from copy import deepcopy
from datetime import *
import threading
from nltk.corpus import stopwords
import string
try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

ACCESS_TOKEN='3277677913-Unwv6MTOoupwZaq4rf1e3Fzh5VKVUi7CYj5Oh0N'
ACCESS_SECRET='oXnDxg0QEJqQuBFySosf7rVFRm341ynaM568mcSVhHs4j'
CONSUMER_KEY='t0qcbeA9KnyYiGs3J0kFRysAs'
CONSUMER_SECRET='3DP2itAWGa6n0hTALmdz0tnbWuabvPuzf1iJ7Rn8I1DdLh2W7M'

oauth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream=TwitterStream(auth=oauth)

keyword=raw_input()

iterator=twitter_stream.statuses.filter(track=keyword,language='en')
punctuation = list(string.punctuation)
stop= stopwords.words('english') + punctuation + ['rt','RT', 'via']
#a list of stopwords 


cache={}
score={}
score1={}
score2={}
cache1={}
cache2={}

def update_score():
    ## a function which update the score after 30 seconds
    threading.Timer(30.0,update_score).start()
    
    t2=datetime.now()# taking the time of execution of function
    m1=t2.minute
    s1=t2.second
    seconds1=m1*60+s1
    for word in cache1:
        t=cache[word]
        seconds=(t.minute)*60 + t.second
        if seconds1-seconds>60:#checking difference of time
            score[word]-=1
            if score[word]==0:#checking if score is 0 or not
                del(score[word])
                del(cache[word])

                

def print_score():
    #a function to print words and their score
    threading.Timer(60.0,print_score).start()
    cache2=cache.copy()
    score2=score.copy()
    
    for word in score2:
        print word + ' >>>' , score2[word]
update_score()
print_score()




for tweet in iterator:
        
    line=json.dumps(tweet)
    tweet=json.loads(line)
        
    if 'text' in tweet:
        x=tweet["text"] # taking text of data of tweet

        t1=datetime.now()

        c=[i for i in x.split() if i not in stop]
        #making list of words in tweet
        #trying to take only meaningfull words
        for word in c:
            if 'http' not in word:
                if word not in cache.keys():
                    cache[word]=t1
                    score[word]=1
                else:
                    cache[word]=t1
                    score[word]+=1
            
     


    
    
    
    
    
    
        




    
    




        
    