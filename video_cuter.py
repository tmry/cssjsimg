#!"E:/stp6/python/python310/python"
print("Content-Type: text/html")
print("\n\n")
import cgi

from moviepy.editor import *
from lib.head import *

SAVE_PATH = "" #"E:/" #to_do
frm=cgi.FieldStorage()
sVdo=frm.getvalue("s_vdo")
if sVdo == None :
    sVdo = ''
tVdo=frm.getvalue("t_vdo")
if tVdo == None :
    tVdo = ''
VdoS=frm.getvalue("vdo_s")
if VdoS == None :
    VdoS = ''
VdoE=frm.getvalue("vdo_e")
if VdoE == None :
    VdoE = ''
    
pg=f'''
<!DOCTYPE html>
<html class="unselectable" oncontextmenu="return false">
{hd}
<body style="background-color:black;color:white;">
<center>
<form method="post" action="home" enctype="multipart/form-data" autocomplete="off">
<input autocomplete="false" name="hidden" type="text" style="display:none;">
<div class="form-group">
<label>Source video</label>
<input type="text" name="s_vdo" class="form-control" placeholder="Type video source name ex., MyVideo1.mp4" value="{sVdo}" >
</div>
<div class="form-group">
<label>Target video</label>
<input type="text" name="t_vdo" class="form-control" placeholder="Type video target name ex., MyVideo2.mp4" value="{tVdo}" >
</div>
<div class="form-group">
<label>Video starting</label>
<input type="text" name="vdo_s" class="form-control" placeholder="Type video starting time ex., 1038" value="{VdoS}" >
</div>
<div class="form-group">
<label>Vdeo Ending</label>
<input type="text" name="vdo_e" class="form-control" placeholder="Type video ending time ex., 1275" value="{VdoE}" >
</div>

<div class="form-group">
<button type="submit" name="btn_cut_vdo" id="btlogn">Cut video</button>
</div>
</form>
</center>
</body>
</html>
'''

def vdoCtr():
    if sVdo == '' :
        print(f'<h1 style="color:skyblue;">Please enter video source name like<b style="color:gold;"> MyVideo1.mp4</b></h1>')
    elif tVdo == '' :
        print(f'<h1 style="color:skyblue;">Please enter video target name like<b style="color:gold;"> MyVideo2.mp4</b></h1>')
    elif VdoS == '' :
        print(f'<h1 style="color:skyblue;">Please enter video starting time like<b style="color:gold;"> 1038</b></h1>')
    elif VdoE == '' :
        print(f'<h1 style="color:skyblue;">Please enter video ending time like<b style="color:gold;"> 1275</b></h1>')
    else:
        print('<h2 style="color:green;">Wellcome<br>Please wait<br> Video cuter running...</h2>')
        svdo = str(sVdo).strip()
        tvdo = str(tVdo).strip()
        vdos = int(str(VdoS).strip())
        vdoe = int(str(VdoE).strip())
        
        clip = VideoFileClip(SAVE_PATH + svdo)
        clip1 = clip.subclip(vdos,vdoe)
        clip2 = clip.subclip(vdos+10,vdoe+10)
        clip3 = clip.subclip(vdos+20,vdoe+20)
        clp = clips_array([[clip1], [clip2], [clip3]])
        clp.write_videofile(SAVE_PATH + tvdo)
        print('<h2 style="color:blue;"> Video cuter fineshd</h2>')
        print(f'<video width="320" height="240" controls><source src="mov/{tvdo}" type="video/mp4"><source src="home/movie.ogg" type="video/ogg">Your browser does not support the video tag.</video>')
    
print(pg)
    
vdoCtr()
