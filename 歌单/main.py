import os

MusicList = os.listdir("./")
MusicList.remove("main.py")
MusicList.remove("生成歌单文件.bat")
MusicList.remove("歌单列表.txt")
MusicList.remove("这里放 卡古娅AI 跑出来的歌文件一定要是 歌名.wav 1")

Music = str(MusicList).replace("[","").replace("]","").replace("'","").replace(", ","\n").replace(".wav","")
print(Music)

with open('歌单列表.txt', 'w') as f:
    f.write(Music)