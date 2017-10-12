import tweepy

#oauth 1.0
consumer_key='69SKsPgAvCs5jXxU9aGVGdNUU'
consumer_secret = 'Op0GTRv7eXIDtcatT7931hu3YoRKVITFO3ux4Lp3yhtYkk5JBA'
access_token = '468616321-r6ElEH4beIce4bfE14ijYxPwmH5YNGITvBqGykAc'
access_token_secret = 'kuyplFEGxSR4TOVBCslptDmjF20TzSNwLioTudA8CetAr'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#input thread author and initial tweet id
thread_start_id = 910815690055143424


#get the thread author
thread_head = api.get_status(id=thread_start_id)

#download all tweets of user since thread initial tweet
tweets = []
for status in tweepy.Cursor(api.user_timeline, user_id=thread_head.user.id, since_id=thread_start_id-1, include_rts=True).items():
  tweets.append(status)
  if status.id == thread_start_id:
    break

#sort tweets in order to build tweets hierarchi
tweets.sort(key=lambda status: status.id)

#filter only thread related tweets
thread = []
for t in tweets:
  if t.id == thread_start_id or any(t.in_reply_to_status_id == th.id for th in thread):
    thread.append(t)

#print and save
file = open('c:/thread_{}.txt'.format(thread_start_id),'w', encoding='utf-8') 
for t in thread:
  print(t.text)
  file.write(t.text + '\n')
file.close

