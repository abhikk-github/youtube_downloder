from pytube import YouTube
import os
import sys


def argmt_rtn():
    try:
        filename = sys.argv[1]
        print(sys.argv[1])
    except IndexError:
        print("IndexError: No Argument Found")
        exit(0)
    return filename

def youtube_download(link):

    SAVE_PATH="D:/Download/Youtube"
    yt = YouTube(link)
    print("Title: ",yt.title)
    print("Number of views: ",yt.views)
    print("Rating of video: ",yt.rating)
    ys = yt.streams.get_highest_resolution()
    print("Downloading...")
    ys.download(SAVE_PATH)
    print("Download completed!!")

if __name__ == "__main__":

    url = argmt_rtn()
    youtube_download(url)




    
