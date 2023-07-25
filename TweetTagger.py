import json 

class TweetTagger:
    
    # __init__ intializes an empty object containing tweets and lables
    def __init__(self):
        self.tweets = []
        self.labels = []

    
    # load imports all tweets and corresponsing labels from saved files
    def load (self, tweets_filename, *labels_filename):
        with open(tweets_filename) as f:
            for line in f:
#                 if len(self.objects) >= 35: 
#                     break
                raw_obj = json.loads(line)
                self.tweets.append(raw_obj) # Adding tweets
                self.labels.append("")
        
        if labels_filename:
            label_file = ''.join(labels_filename)
            with open(label_file) as f:
                index = 0
                for line in f:
                    label_info = line.rstrip('\n')
                    self.labels[index] = label_info
                    index += 1        

# provides an input to help label as positive or negative and update labels list
    def label_tweets(self):
        for x in range(len(self.tweets)):
            display_tweet = self.tweets[x]['text']
            opinion = input(f"{display_tweet}: Enter the label => 'pos' or 'neg':")
            self.labels[x] = opinion


    # save features takes a name for naming file conventions and consumes data from self.tweets and self
    # to produce two seperate files for tweets and labels
    
    def save (self, filename):
        with open (f'tweets_{filename}', "w") as f_name:
            for tweets in self.tweets:
                content = json.dumps(tweets)
                f_name.write(f'{content}\n')
                
        with open (f'labels_{filename}', "w") as l_name:
            for labels in self.labels:
                l_name.write(f'{labels}\n')
    

    # counts the number of asked labels: positive or negative
    def count(self, label):
        count_tracker = self.labels.count(label)
        return count_tracker
    

    # merge tweets from another tweets 
    def merge (self, another_tweet_tagger):
        merge_tweets = another_tweet_tagger.tweets # Merge tweet list
        self.tweets.extend(merge_tweets)
        merge_labels = another_tweet_tagger.labels # Merge labels list
        self.labels.extend(merge_labels)


    
    # deletes all non english tweets. secondly, deletes all tweets with their labels == label 
    # whose number is greater than count 
    def trim (self, label, count):
        self.new_tweet = []
        self.new_label = []
        for i in range(len(self.tweets)): 
        # Deletes all non-english tweets
           # if self.objects[i]['metadata']['iso_language_code'] == "en":
            if self.tweets[i]['lang'] == "en":
                self.new_tweet.append(self.tweets[i])
                self.new_label.append(self.labels[i])
        
                    
        ## check if count > label tweets 
        count_label = self.new_label.count(label)
       # print(count_label)
        if not (count > count_label):
            tracker = count_label - count
            #print(tracker)
            
            self.new_tweet2 = []
            self.new_label2 = []  
        
            for i in range(len(self.new_tweet)):
#                 print("loop begins")
#                 print("{A}:this is tracker info", tracker)
#                 print("{A}length of new label list",len(self.new_label2))
#                 print("{B}length of old label list",len(self.new_label))

                if self.new_label[i] == label and tracker > 0:
#                     print("Missed element is " + self.new_label[i])
                    tracker -= 1
                else:
                    self.new_tweet2.append(self.new_tweet[i])
                    self.new_label2.append(self.new_label[i])        

            #Assigning new values:
            self.tweets = self.new_tweet2
            self.labels = self.new_label2
        
        else: # if count > number of lables
            self.tweets = self.new_tweet
            self.labels = self.new_label

