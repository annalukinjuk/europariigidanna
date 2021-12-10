from gtts import gTTS
import os
sõnastik={}
riigid=[]
linnad=[]
file=open("riigid_pealinnad.txt", 'r')
for line in file:
    k, v=line.strip().split('-') #riik:pealinn
    sonastik[k.strip()]=v.strip
    riigid.append(k)
    linnad.append(sonastik[k.strip()])
file.close()
print(sonastik)
print("riigid:  ")
print(riigid)
print("pealinnad:  ")
print(linnad)
s=gTTS(text=linnad[0],lang='et',slow=True).save("heli.mp3")
os.system("heli.mp3")
a=input()
