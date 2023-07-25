#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
from pandas import Series, DataFrame
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
import json
import nltk
from nltk.corpus import stopwords
import random
import pickle


## Mention Feature extractor again

def tweet_features(tweet):
    tweet_words = set(tweet)
    features = {}
#     pro_vax = set(['effective', 'safe', 'protect','Against', 'recommend', 'H1N1', 'available'])
    anti_vax = set(['dangerous', 'kill', 'death','not', 'disease', 'weak', 'side', 'effect', 'mindless', 'harmful', 'risk','autism','fatalities','seizures'])
    porter = nltk.PorterStemmer()
    porter_stems = [porter.stem(x) for x in anti_vax]
    for x in tweet_words:
        if x in porter_stems:
            features['anti: contains(%s)' % x] = True
        else:
            features['pro: contains(%s)' % x] = True     
    return features

## Load the classifer

with open ('twitter_classifier.pkl', 'rb') as f:
    model = pickle.load(f)
# trainer = pickle.load(open("twitter_classifier.pkl"),'rb')

# Read tweet.txt file and create corresponding lables

with open('tweets.txt', 'r') as tf:
    ttweets = tf.readlines()
ttweets = [json.loads(tweet.strip()) for tweet in ttweets]
llabels = [] 

for x in ttweets:
    tok_it = nltk.word_tokenize(x['text'])
    lower = [tok.lower() for tok in tok_it] #lower case
    nochar = [c for c in lower 
                  if c.isalpha()] ## removes numeric
    porter = nltk.PorterStemmer()
    porter_stems = [porter.stem(x) for x in nochar]
    nostop = set(stopwords.words('english'))
    fil = [s for s in porter_stems 
               if not s in nostop] # remove stopwords
    
    fil = ' '.join(fil)
    x['text'] = fil
    sentiment = model.classify(tweet_features(x))
    llabels.append(sentiment) ## create the labels for the corresponding tweets
#     print(fil)
#     print(llabels)
    
# # Save the lables to a new file

with open('labels.txt', "w") as l:
    for label in llabels:
        l.write(f'{label}\n')

        
### Setup line graph for positive tweets proportion


dd = [] ## array to store time stamps
for tweet in ttweets:
    dd.append(tweet['created_at'])

data = list(zip(dd, llabels))


# Convert the tuple list into dataframe
df = pd.DataFrame(data, columns = ['time', 'label']) 
## df = df[(df.label == 'positive') | (df.label == 'negative')] # filter 


## change the timestamp to python format
df['time'] = pd.to_datetime(df['time'], format="%a %b %d %X %z %Y") 
df['time'] = df['time'].dt.date
df1 = df[df.label == 'positive'] # create another df to store only positives

# Sort the dataframes by date (also avoid settingcopy warning)
df = df.sort_values(by='time')
df1 = df1.sort_values(by='time')

# Count total and pos tweets. Add columns as well
df['total'] = df.groupby('time').transform('count')
df1['pos'] = df1.groupby('time').transform('count')

## To match the length, we filter postives while retaining the total number for each date
df = df[df.label == 'positive']
df['pos'] = df1['pos'].values ## adding column pos from df1

df.drop_duplicates(subset='time',keep='first',inplace=True) # drop duplicates


df['percent'] = (df.pos / df.total) * 100 ## daily positive tweets percentage


## Setup plot

plt.plot(df['time'], df['percent'])
plt.title("Daily Percentage of Positive Tweets")
plt.xlabel("Timeline")
plt.ylabel('Proportion of Positive Tweets')
plt.xticks(rotation=19, ha='right')


## Save the plot
plt.savefig("plot",dpi=300)   


# In[ ]:




