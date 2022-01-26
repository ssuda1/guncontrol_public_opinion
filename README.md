# guncontrol_public_opinion
Text Analysis on real time Twitter streaming data from 3/24/2018 to 3/26/2018 (during and right after mass demonstration on 3/24/2018 for gun control in the wake of 3/14 School shooting in Florida.)

I acquired twitter streaming data using Tweepy library, converted it to dataframe, cleaned up (gettng rid of emojis etc) and manipulated it by pandas.

After tokenized text data with NLTK library and removed stop words, found out the most frequently used word and # hashtags and visualize when each word and # hashtags trended during the demonstration. 

Next step is to figure out if geographic locations (ex. Blue States
vs Red States) affect the attitude toward gun control (positive or negative). (Using Cluster).
