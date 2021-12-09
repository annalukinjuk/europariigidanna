from module1 import*
countries_dict={"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам", 
           "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
           "Северная Македония": "Скопье", "Сербия": "Белград"}
print(countries_dict )
while True:
    print("Привет! Пройдёмся по странам и их столицам!")
    print("1 - Узнать столицу страны или наоборот,\n2 - Добавить новую страну и столицу,\n3 - Исправить ошибку,\n4 - Проверь свои знания")
    menu=input()
    if menu=="1":
        v=input("Будем искать страну по стoлице(1) или стoлицу по стране(2)? ")
        countries(countries_dict,v)
    elif menu=="2":
        new_key_value(countries_dict)

        Capitals={}
Capitals=dict()
def contry():
    Capitals["Нидерланды"]="Амстердам"
    Capitals["Андорра"]="Андорра-ла-Велья"
    Capitals["Греция"]="Афины"
    Capitals["Сербия"]="Белград"
    Capitals["Германия"]="Берлин"
    Capitals["Швейцария"]="Берн"
    Capitals["Словакия"]="Братислава"
    Capitals["Бельгия"]="Брюссель"
    Capitals["Венгрия"]="Будапешт"
    Capitals["Румыния"]="Бухарест"
    Capitals["Лихтенштейн"]="Вадуц"
    Capitals["Мальта"]="Валлетта"
    Capitals["Польша"]="Варшава"
    Capitals["Ватикан"]="Ватикан"
    Capitals["Австрия"]="Вена"
    Capitals["Литва"]="Вильнюс"
    Capitals["Ирландия"]="Дублин"
    Capitals["Хорватия"]="Загреб"
    Capitals["Украина"]="Киев"
    Capitals["Молдавия"]="Кишинёв"
    Capitals["Дания"]="Копенгаген"
    Capitals["Португалия"]="Лиссабон"
    Capitals["Великобритания"]="Лондон"
    Capitals["Словения"]="Любляна"
    Capitals["Люксембург"]="Люксембург"
    Capitals["Испания"]="Мадрид"
    Capitals["Белоруссия"]="Минск"
    Capitals["Монако"]="Монако"
    Capitals["Россия"]="Москва"
    Capitals["Норвегия"]="Осло"
    Capitals["Франция"]="Париж"
    Capitals["Черногория"]="Подгорица"
    Capitals["Чехия"]="Прага"
    Capitals["Исландия"]="Рейкьявик"
    Capitals["Латвия"]="Рига"
    Capitals["Италия"]="Рим"
    Capitals["Сан-Марино"]="Сан-Марино"
    Capitals["Босния и Герцеговина"]="Сараево"
    Capitals["Северная Македония"]="Скопье"
    Capitals["Болгария"]="София"
    Capitals["Швеция"]="Стокгольм"
    Capitals["Эстония"]="Таллин"
    Capitals["Албания"]="Тирана"
    Capitals["Финляндия"]="Хельсинки"
Capitals["Euroopa riigid"]="Нидерланды, Андорра, Греция, Сербия, Германия, Швейцария, Словакия, Бельгия, Венгрия, Румыния, Лихтенштейн, Мальта, Польша, Ватикан, Австрия, Литва, Ирландия, Хорватия, Украинa, Молдавия, Дания, Португалия, Великобритания, Словения, Люксембург, Испания, Белоруссия, Монако, Россия, Норвегия, Франция, Черногория, Чехия, Исландия, Латвия, Италия, Сан-Марино, Босния и Герцеговина, Северная Македония, Болгария, Швеция, Эстония, Албания, Финляндия"
Countries=["Нидерланды", "Андорра", "Греция", "Сербия", "Германия", "Швейцария", "Словакия", "Бельгия", "Венгрия", "Румыния", "Лихтенштейн", "Мальта", "Польша", "Ватикан", "Австрия", "Литва", "Ирландия", "Хорватия", "Украинa", "Молдавия", "Дания", "Португалия", "Великобритания", "Словения", "Люксембург", "Испания", "Белоруссия", "Монако", "Россия", "Норвегия", "Франция", "Черногория", "Чехия", "Исландия", "Латвия", "Италия", "Сан-Марино", "Босния и Герцеговина", "Северная Македония", "Болгария", "Швеция", "Эстония", "Албания", "Финляндия"]
Country=["Амстердам, Андорра-ла-Велья, Афины, Белград, Берлин, Берн, Братислава, Брюссель, Будапешт, Бухарест, Вадуц, Валлетта, Варшава, Ватикан, Вена, Вильнюс, Дублин, Загреб, Киев, Кишинёв, Копенгаген, Лиссабон, Лондон, Любляна, Люксембург, Мадрид, Минск, Монако, Москва, Осло, Париж, Подгорица, Прага, Рейкьявик, Рига, Рим, Сан-Марино, Сараево, Скопье, София, Стокгольм, Таллин, Тирана, Хельсинки"]
contry()
for country in Countries:
 if country in Capitals:
    print("Столица страны " + country + ": " + Capitals[country])

 else:
    print("В базе нет страны c названием " + country)

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
for country in Countries:
 if country in Capitals:
    print("linnude pealinn on" + country + ': ' + Capitals[country])
 else:
    print( + country)

while 1:
    print("\n1 - siseta riik \n2 - Добавить в список город или страну. \n3 - Исравить ошибку в списке. \n4 - Проверь себя.")