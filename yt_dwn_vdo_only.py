#!"E:/stp6/python/python310/python"
print("Content-Type: text/html")
print("\n\n")
import cgi

import sys
import pytube as yt
from pytube.cli import on_progress

from lib.head import *

SAVE_PATH = "" #"E:/" #to_do
frm=cgi.FieldStorage()
vdoId=frm.getvalue("video_id")
if vdoId == None :
    vdoId = ''
    
video_url=f'https://www.youtube.com/watch?v={vdoId}' # l5xBsDsLpms'

def progress_show(chunk, file_handle, bytes_remaining):
    global filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()
    
def dwnloYTVdo():
    if vdoId == '' :
        print(f'<h1 style="color:skyblue;">Please enter video ID like<b style="color:gold;"> l5xBsDsLpms</b></h1>')
    else:
        print(f'<h1 style="color:skyblue;">{video_url}</h1>')
        youtube = yt.YouTube(video_url, on_progress_callback=progress_show)
        # video = youtube.streams.filter(only_video=True, res="360p").first()
        video = youtube.streams.filter(res="480p").first()
        filesize = video.filesize
        video.download(SAVE_PATH)

pg=f'''
<!DOCTYPE html>
<html class="unselectable" oncontextmenu="return false">
{hd}
<body >
<center>
<form method="post" action="yt_download" enctype="multipart/form-data" autocomplete="off">
<input autocomplete="false" name="hidden" type="text" style="display:none;">
<div class="form-group">
<label>Video ID</label>
<input type="text" name="video_id" class="form-control" placeholder="Type video ID ex., l5xBsDsLpms" value="{vdoId}" >
</div>

<div class="form-group">
<button type="submit" name="btn_yt_vdo" id="btlogn">Download video from youtube</button>
</div>
</form>
</center>
</body>
</html>
'''

print(pg)

dwnloYTVdo()



'''
from pytube import YouTube

link="https://www.youtube.com/watch?v=l5xBsDsLpms"
try:
    yt = YouTube(link)
except:
    print("Connection Error")


t = yt.filter(only_video=True).get(mp4files[-1].extension,mp4files[-1].resolution)
yt.set_filename('1 #ارحل_عدو_الله')
print(t)
t.download(SAVE_PATH)
'''

'''
from pytube import YouTube 
  
# where to save 
SAVE_PATH = "E:/" #to_do 
  
# link of the video to be downloaded 
link="https://www.youtube.com/watch?v=l5xBsDsLpms"
  
try: 
    # object creation using YouTube
    # which was imported in the beginning 
    yt = YouTube(link) 
except: 
    print("Connection Error") #to handle exception 
  
# filters out all the files with "mp4" extension 
mp4files = yt.filter('mp4') 
  
#to set the name of the file
yt.set_filename('1 #ارحل_عدو_الله')  
  
# get the video with the extension and
# resolution passed in the get() function 
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
try: 
    # downloading the video 
    d_video.download(SAVE_PATH) 
except: 
    print("Some Error!") 
print('Task Completed!')
'''
