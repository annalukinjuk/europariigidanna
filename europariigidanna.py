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


while 1:
    print("\nsiseta riik - A \nsiseta listis eu liitu linnud ja pealinn - B \nlistis viga soritama - C \nkas oled õige? - D")
    valik=input("vajuta nuppu:  ")
    if valik()=="A":
        country=input("siseta riik eu liitust:   ")
        for country in europaliit:
            if country in europaliit:
                print(f"linnude pealinn on {country},{pealinn}")
        else:
            print(country)

