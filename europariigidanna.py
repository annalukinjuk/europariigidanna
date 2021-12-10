from module1 import*

pealinn={}
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
for country in europaliit:
 if country in pealinn:
    print("linnude pealinn on" + country + ': ' + Capitals[country])
 else:
    print( + country)

while 1:
    print("\n1 - siseta riik \n2 - siseta listis eu liitu linnud ja pealinn. \n3 - Исравить ошибку в списке. \n4 - Проверь себя.")
