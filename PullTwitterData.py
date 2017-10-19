#Importing libraries
import sys
import os
import jsonpickle
import tweepy

#Pass our consumer key and consumer secret to Tweepy's user authentication handler
auth = tweepy.OAuthHandler("BAE2cipDsFbaqu5VxiRnSk7Ku", "AqIZCnVenGVvIFBYDpOdpEANeOoKeEAAp3SBxpngAY1uo6goT6")

#Pass our access token and access secret to Tweepy's user authentication handler
auth.set_access_token("184149320-lg1A1o0GxPvSD0LQQYaXQGMcFmNch8HuIda5sOA2", "tvLo25DQlrobKETwYGMeSAr5EA6v8ZE7mEfIE7kmDWHlJ")

#Creating a twitter API wrapper using tweepy
#Details here http://docs.tweepy.org/en/v3.5.0/api.html
api = tweepy.API(auth)

#Error handling
if (not api):
    print ("Problem connecting to API")


#This is what we are searching for
#We can restrict the location of tweets using place:id 
#We can search for multiple phrases using OR
searchQuery = 'place:96683cc9126741d1'

#Maximum number of tweets we want to collect 
maxTweets = 1000000

#The twitter Search API allows up to 100 tweets per query
tweetsPerQry = 100

tweetCount = 0

#Open a text file to save the tweets to
with open('sample_data.json', 'w') as f:

    #Tell the Cursor method that we want to use the Search API (api.search)
    #Also tell Cursor our query, and the maximum number of tweets to return
    for tweet in tweepy.Cursor(api.search,q=searchQuery).items(maxTweets) :         

        #Verify the tweet has place info before writing (It should, if it got past our place filter)
        if tweet.place is not None:
            
            #Write the JSON format to the text file, and add one to the number of tweets we've collected
            f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
            tweetCount += 1

    #Display how many tweets we have collected
    print("Downloaded {0} tweets".format(tweetCount))