#Test of getting list of YouTube comments using YouTube API

#setup
#will not work without replacing key variable with your own API key
with open('/users/emily/Desktop/MSU/YoutubeComments/Resources/api.txt', 'r') as file:
    key = file.read()
#key = 'AIzaSyBE-yerg0CMxAyaOq2yVeLIZewVFXRelsM'
from googleapiclient.discovery import build
#from operator import itemgetter

def commentextractor(videoname, id):
    comments = []
    video_id = id
    youtube = build('youtube','v3',developerKey=key)
    video=youtube.commentThreads().list(part='snippet',videoId=video_id, maxResults=100).execute()

    for item in video['items']:

        commentcode = item['snippet']['topLevelComment']
        comment = commentcode['snippet']['textDisplay']
        #likescode = item['snippet']['topLevelComment']
        #likes = likescode['snippet']['likeCount']
        #comments.append((comment,likes))
        comments.append(comment)

    with open (f'{videoname}.txt', 'w+') as file:
        for comment in comments:
            file.write('%s\n' % comment)
    file.close()
    print(f'{videoname} comments extracted successfully')
    
videos_and_ids = {'minecraftmovie': 'PE2YZhcC4NY', #A Minecraft Movie, movie based on video game
                  'overwatchclassic': 'kBj4SCL4PNo', #Overwatch Classic, video game, new game mode
                  'ghostofyotei': '7z7kqwuf0a8', #Ghost of Yōtei, video game
                  'marvelwhatifs3': 'umiKiW4En9g', #Season 3 of Marvel animated show What If?
                  'bornpink': 'nxs0RHpT_Hg', #Blackpink Kpop group new album Born Pink
                  'sheeransubtract':'QaNa2bVG860', #Ed Sheeran's new album Subtract
                  'captainamerica':'1pHDWnXmK7Y', #New Captain America movie: Brave New World
                  'traindragon': '5lzoxHSn0C0', #How to train your dragon live action reboot
                  'squidgame2': 'lQBmZBJCYcY', #Squid game show season 2
                  'thestudio': 'ucgsmqxSJ1c', #Apple TV comedy series
                  'partyneverends': '4hN5iDe8lNA', #juice wrld album trailer
                  'subnautica2': 'WS0vTRl_2PQ'} #Subnautica 2 video game teaser

for video, id in videos_and_ids.items():
    commentextractor(video,id)