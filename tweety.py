import tweepy 
from tweepy import OAuthHandler
import time

auth = OAuthHandler(consumer_api, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

file_name = 'last_seen.txt'

def retrieve(filename) :
    f_read = open(filename, 'r')
    id = int(f_read.read().strip())
    f_read.close()
    return id

def store(id, filename) :
    f_write = open(file_name, 'w')
    f_write.write(str(id))
    f_write.close()
    return 

def reply() :
    last_id = retrieve(file_name)
    mentions = api.mentions_timeline(last_id, tweet_mode = 'extended')
    for mention in reversed(mentions):
            print(str(mention.id) + ' - ' + mention.full_text)
            last_seen_id = mention.id
            store(last_seen_id, file_name)
            if 'hello friend' in mention.full_text.lower():
                print('found a friend')
                print('saying hi')
                api.update_status(' Hello there, @' + mention.user.screen_name +
                    ' how are you doing', mention.id)
            if  'you are breathtaking' in mention.full_text.lower():
                print('found keanu!')
                print('responding with love')
                api.update_status(' NO, YOU ARE BREATHTAKING @' + mention.user.screen_name +
                    '!', mention.id) 
            if  '#helloworld' in mention.full_text.lower():
                print('found hello world')
                print('responding back')
                api.update_status("Hello to you too  @"+ mention.user.screen_name +
                    '!', mention.id)     

while True:
    reply()
    time.sleep(15)                            

#    