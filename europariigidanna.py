from module1 import*

pealinn=dict()
pealinn["Belgia"] = "Brüssel"
pealinn["Saksamaa"] = "Berliin"
pealinn["Prantsusmaa"] = "Pariis"
pealinn["Itaalia"] = "Rooma"
pealinn["Luksemburg"] = "Luxembourg"
pealinn["Holland"] = "Amsterdam"
pealinn["Taani"] = "Kopenhaagen"
pealinn["Iirimaa"] = "Dublin"
pealinn["Kreeka"] = "Ateena"
pealinn["Portugal"] = "Lissabon"
pealinn["Hispaania"] = "Madrid"
pealinn["Soome"] = "Helsingi"
pealinn["Austria"] = "Viin"
pealinn["Rootsi"] = "Stockholm"
pealinn["Eesti"] = "Tallinn"
pealinn["Läti"] = "Riia"
pealinn["Malta"] = "Valletta"
pealinn["Poola"] = "Varssavi"
pealinn["Slovakkia"] = "Bratislava"
pealinn["Sloveenia"] = "Ljubljana"
pealinn["Tšehhi"] = "Praha"
pealinn["Ungari"] = "Budapest"
pealinn["Küpros"] = "Nikosia"
pealinn["Bulgaaria"] = "Sofia"
pealinn["Rumeenia"] = "Bukarest"
pealinn["Horvaatia"] = "Zagreb"
pealinn= ["Brüssel", "Berliin","Pariis","Rooma","Luxembourg","Amsterdam","Kopenhaagen","Dublin","Ateena","Lissabon","Madrid","Helsingi","Viin", "Stockholm","Tallinn", "Riia","Valletta","Varssavi","Bratislava",   ]
europaliit=["Belgia","Saksamaa","Prantsusmaa","Itaalia","Luksemburg","Holland","Taani","Iirimaa","Kreeka","Portugal","Hispaania","Soome","Austria","Rootsi","Eesti","Läti","Malta","Poola","Slovakkia","Sloveenia","Tšehhi","Küpros","Ungari","Bulgaaria","Rumeenia","Horvaatia"]

country=input("siseta riik eu liitust:   ")
for country in europaliit:
    if country in europaliit:
        print(f"linnude pealinn on {country},{pealinn}")
    else:
        print(country)

valik=input("\n1 - siseta riik \n2 - siseta listis eu liitu linnud ja pealinn. \n3 - listis viga soritama \n4 - kas oled õige?.")
if valik=="1":
    try:

while 1:
    print("\nsiseta riik - A \nsiseta listis eu liitu linnud ja pealinn - B \nlistis viga soritama - C \nkas oled õige? - D")
    valik=input("vajuta nuppu:  ")

    if valik()=="A":
        country=input("siseta riik eu liitust:   ")

    elif read_key()=="B":
      0000,0
        min_palk, kellel=minimum(palgad,inimesed)
        print("minimaalne palk ==> ", min_palk, " Kellel ==> ",kellel)

    elif read_key()=="C":
        max_palk, kellel=maksimum(palgad,inimesed)
        print("maksimaalne palk ==> ", max_palk, " Kellel ==> ",kellel)

    elif read_key()=="V":
        lisa(palgad,inimesed)
        print("siseta info  ", ans, "kellel==>")
