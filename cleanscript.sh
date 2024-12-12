#!/bin/bash

#iterate over each txt file in this directory and clean/tokenize it.

## TODO ##

#remove stopwords done
#remove content inside HTML tags done
#remove non-alpha chars done
#tokenize, one word per line done
#save each txt file as clean version separate from unclean done
#delete duplicates

stop_words="$HOME/Desktop/MSU/YoutubeComments/Resources/stopwords.txt"

commentdir="$HOME/Desktop/MSU/YoutubeComments"

#to prevent duplicate _clean files on subsequent runs
if [ -n "$(ls "$commentdir"/*_clean.txt)" ]; then
    rm "$commentdir"/*_clean.txt
fi

#clean/tokenize
for file in "$commentdir"/*.txt; do

    fragment=$(basename "$file" .txt)

    cleanfile="./${fragment}_clean.txt"

    sed -e 's/<[^<>]*>//g' $file | sed "s/&#39;/'/" | tr '[:upper:]' '[:lower:]' | tr -sc "a-z'" "\n" | grep -vw -f "$stop_words" | sort | uniq > "$cleanfile"

done