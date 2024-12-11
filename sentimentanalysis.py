import nltk
#nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
import glob
from datetime import date

#Since comments.py scrapes the 100 most recent comments on a video, include date in output
cur_date = date.today()

#prepare sentiment analyzer
sentiment = SentimentIntensityAnalyzer()

def sentiment_analysis(file):
    #read file
    with open(file, 'r') as f:
        words = f.read()

    #score
    score = sentiment.polarity_scores(words)
    with open('./Resources/output.txt', 'a') as f:
        print(f'Sentiment values for {file} are: {score} ({cur_date}) \n', file=f)

folder = '/users/emily/Desktop/MSU/YoutubeComments/*_clean.txt'

#iterate over *_clean.txt files
for file in glob.glob(folder):
    sentiment_analysis(file)