from pytube import YouTube, Playlist


link = "https://www.youtube.com/watch?v=o0mfoebuL3M"


def download_video(link):
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    print(yt.streams)
    yt.streams.get_highest_resolution().download("videos")


def download_playlist(link):
    playlist = Playlist(link)
    for video in playlist.videos:
        video.streams.get_highest_resolution().download("videos")


def download():
    link = input("Enter a link")
    content_type = input("Type 1 for video 2 for playlist")
    if content_type == "1":
        download_video(link)
    elif content_type == "2":
        download_playlist(link)
    else:
        print("Unknown option")

download()



