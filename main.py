from pytube import Playlist
def downloadplaylist(playlistid):
    savepath = 'E:\youtubefolder'
    p = Playlist("https://www.youtube.com/playlist?list="+playlistid)#'https://www.youtube.com/playlist?list=PL6mx5D4YlhnTVgee_9pu6snpAQoB0viuD'
    print(f'Downloading: {p.title}')
    for audio in p.videos:
        print(audio.title)
        audio.streams.get_by_itag(250).download(savepath)


