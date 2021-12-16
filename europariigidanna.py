from random import*
from module2 import*
Capitals=dict()
Capitals["Estonia"]="Tallinn"
Capitals["Albania"]="Tirana"
Capitals["Belgium"]="Brussels"
Capitals["Czechia"]="Prague"
Capitals["Poland"]="Warsaw"
Capitals["Portugal"]="Lisbon"
Capitals["Finland"]="Helsinki"
Capitals["France"]="Paris"
Capitals["Germany"]="Berlin"
Capitals["Sweden"]="Stockholm"
Capitals["Spain"]="Madrid"
Capitals["Serbia"]="Belgrade"
Capitals["Norway"]="Oslo"
Capitals["Moldova"]="Chisinau"
Capitals["Greece"]="Athens"
Capitals["Bulgaria"]="Sofia"
Capitals["Austria"]="Vienna"
Capitals["Switzerland"]="Bern"
Countries=["Estonia","Albania","Belgium","Czechia","Poland","Portugal","Finland","France","Germany","Sweden","Spain","Serbia","Norway","Moldova","Greece","Bulgaria","Austria","Switzerland"]
valik=input("\n siseta riik ja vaata linnud - 1,\n Test - 2")
if valik=="1":

    for country in Countries:
        country=input("Введите страну: ")
        if country in Capitals:
            print("Столица страны "+country+": " +Capitals[country])
        else:
            print("В базе данных нет страны с названием " +country)
            v=input("Хотите внести " +country+ " в базу данных?Да или Нет? ")
            if v=="Да":
                ca=input("Введите столицу страны " +country+": ")
                Capitals.update({country: ca})
                p=input("Возможно в базе данных ошибка, хотите исправить её? Да или Нет? ")
                if p=="Нет":
                    print("Хорошо")
                if p=="Да":
                    o=input("Введите правильно страну: ")
                    l=input("Введите правильно столицу: ")
                    Capitals.pop(country)
                    Capitals.update({o: l})
            if v=="Нет":
                print("Хорошо")
        d=input("Хотите ли вы начать проговаривание слов для самостоятельного изучения? Да или Нет? ")
        if d=="Да":
            sonastik()
        if d=="Нет":
            print("Хорошо")
if valik=="2":
        Countries.sort()
        Countries.reverse()
        m=0
        for i in range(10):
            country=str(choice(Countries))
            print(country)
            st=input("Введите столицу: ")
            if st==Capitals[country]:
                print("Правильно!")
                punkt+=1
            else:
                print("Неправильно!")
        if punkt==0:
            print("0%")
        elif punkt==1:
            print("10%")
        elif punkt==2:
            print("20%")
        elif punkt==3:
            print("30%")
        elif punkt==4:
            print("40%")
        elif punkt==5:
            print("50%")
        elif punkt==6:
            print("60%")
        elif punkt==7:
            print("70%")
        elif punkt==8:
            print("80%")
        elif punkt==9:
            print("90%")
        elif punkt==10:
            print("100%")

