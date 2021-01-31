from pytube import YouTube, Playlist

def download_highest_resolution(vid,location):
    #get video that has highest resolution that has both audio and video codec
    ys = vid.streams.filter(progressive=True).get_highest_resolution()
    #download video to folder specified in parameter 'location'
    ys.download(location)

type = input("Downloading a playlist or individual video(s)? Answer P for playlist, L for link(s). ")

while type != "P" and type != "L":
    type = input("Invalid input, answer P for playlist, L for individual video(s). ")

if type == "P":
    while True:
        try:
            numPlaylists = int(input("Number of playlists you would like to download: "))
            break
        except ValueError:
            print("Please enter integer")
    playlists = []
    for x in range(numPlaylists):
        link = input("Enter link of playlist "+str(x+1)+": ")
        playlists.append(link)
    for pLink in playlists:
        pl = Playlist(pLink)
        vidNum = 1
        print("Playlist " + pl.title + " download started...")
        for video in pl.videos:
            print(video.title+" download in progress...")
            download_highest_resolution(video, pl.title)
            print(video.title + " download complete")
            vidNum += 1
        print("Playlist "+pl.title+" download completed, playlist located in folder "+pl.title)
    print("all playlists downloaded")


if type =="L":
    while True:
        try:
            numVids = int(input("Number of videos you would like to download: "))
            break
        except ValueError:
            print("Please enter integer")
    vids = []
    for x in range(numVids):
        link = input("Enter link of video "+str(x+1)+": ")
        vids.append(link)
    vidCount = 1
    for vid in vids:
        yt = YouTube(vid)
        print("Downloading "+yt.title+"...")
        download_highest_resolution(yt, yt.author)
        print(yt.title+" download complete, video located in folder "+yt.author)
        vidCount+=1
