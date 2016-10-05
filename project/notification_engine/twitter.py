consumer_key= "7AUALPGWUSr7rdxtoWpnukIwX"
consumer_secret = "vxdAt3fNNE1MluTUfApeX9G7OxqP9ISKqcwSG2DchCBdaXbko6"
access_token = "782476396127932416-jxUu7tNCEMrCjHITG3BVtahkEE4Ajq3"
access_secret = "c2ThkY7vuzsmKBIrZ9Zrv00r1pL6CSBtxLixfhgMPqITX"
import time 
import twitter
import random
api = twitter.Api()
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_secret)
constant_str = ['@google','@AdSense','@YouTube']
str_list = ['#Sad','#Disappointed','#RevokeAdSenseBan','#NoWarning','Will you reply?','Why banned','#Fraud?','#WTF','#Unfair',
          'NoIntensionalHits','#FakeAlgorithm','#StartAdSense','#Shit']
count=0
while(True):
    print count
    str_1 = random.sample(constant_str,2)
    str_2 = random.sample(str_list,4)
    str_1 = ' '.join(str_1)
    str_2 = ' '.join(str_2)
    tweet_str = str_1+' '+str_2
    status = api.PostUpdate(tweet_str)
    print(status.text)
    count=count+1
    time.sleep(120)