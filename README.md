# Twitter-Vaccine-Surveillance
Created a Twitter-based vaccine hesitancy surveillance system (Using Tweepy)

The underlying idea is that by monitoring the number of tweets that describe vaccine hesitancy issues or related consequences it is possible to monitor trends at the Provence- or Country-level. This is particularly important given the current need to vaccinate a large portion of the Canadian population to protect against COVID-19.

The Project had two phases: 
1) Tweet Labelling
2) Developing the surveillance system





PHASE 1


Using Tweepy after setting up an API keys from Twitter Developers account to collect both short and long tweets: to create a large pool of training dataset.

For this task, we made a function called <a href= "https://github.com/smridh99/Twitter-Vaccine-Surveillance/blob/main/twitter_streaming.py">twitter_streaming</a>.



ONCE ENOUGH TWEETS HAVE BEEN CAPTURES, STOP THE CODE (cmd + c)






PHASE 2


Labelled the collected tweets with TWO possible labels: 
POSITIVE, when the tweet is deemed related to vaccine hesitancy, and 
NEGATIVE when the tweet is deemed to be not related.

Refered to the codebook <a href="https://www. ncbi.nlm.nih.gov/pmc/articles/PMC6004971/.">Blankenship et. al (2018)</a> to establish ground truth definition for our dataset:

1. Pro-vaccine, e.g. “Equine #Influenza #Vaccine Remains Effective Against Mutated Virus Study Shows - TheHorse.com : http://bit.ly/c4eRWu”
   
2. Neutral, e.g. “#H1N1 #vaccine still available recommended - Zanesville Times Recorder: http://bit.ly/aJQyIY”
   
3. Anti-vaccine, e.g. “RT @bengoldacre ”Give children #vaccine that we said would kill them”: Daily Mail joy by @PrimlyStable http://dlvr.it/DKJRm #health”

Pro-vaccine and Neutral tweets: 'NEGATIVE'
Anti-vaccine tweets: 'POSITIVE'


PHASE 3

Created an actual surveillance system coded in python file called twitter_surveillance.py

-> loads a trained classifier from file called twitter_classifier.pkl
-> Reads tweets file named tweets.txt and calssify each one as either positive or negative
-> Assign each tweet corressponding lables and store them in different file called labels.txt
-> Save a plot of daily percentages of positive tweets to a file called plot.png




