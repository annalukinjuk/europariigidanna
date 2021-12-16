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

def europaliit(d:dict, v:int):
    keys_list=(list(d.keys()))
    values_list=(list(d.values()))
    if v=="1":
        mas=[]
        capital=(input("Введи столицу: ")).capitalize()
        capital.title()
        for i in values_list:
            if i==capital:
                for i in range(len(values_list)):
                    if values_list[i]==capital:
                        mas.append(int(i))
                        print("Страна -", keys_list[i],"<-->", "Cтолица -", values_list[i])
    else:
        country=(input("Введите страну: ")).capitalize()
        a=d.get(country)
        print("Страна -", country ,"<-->", "Cтолица -", a)
    return


def new_key_value(d:dict):
    new={}
    country=(input("Введите страну: ")).capitalize()
    capital=(input("Введите страну: ")).capitalize()
    new={country:capital}

    return d,new
