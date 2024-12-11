# text_tools_project

## Topic
**Sentiment analysis of comments on trailers posted on YouTube**

I have three main scripts for this project:

1. Python script using Google's YouTube API to extract 100 most recent comments per video in a text file. (comments.py)

2. Shell script to iterate over extracted text file and clean and tokenize it. (cleanscript.sh)

3. Python script for sentiment analysis of cleaned text files using nltk library. (sentimentanalysis.py)

Output using video IDs listed in dictionary in comments.py in Resources folder.

Resources folder also contains the list of stop words I used to filter in cleanscript.sh

I have also included an example unclean and clean comment data txt file as an example of the output of comments.py and cleanscript.sh
