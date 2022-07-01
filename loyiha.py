import random

import os

def menu():
    birinchi = True
    while True:
        if birinchi:
            print("""\n\n Assalomu alaykum bu == MATEMATIKA == o'yini dasturi.
            Bu orqali siz o'z bilimingizni sinab ko'rishingiz mumkin.
            dasturni ishga tushirish uchun quyidagi menu'dan kerakli darajani tanlab o'yinni boshlang.
            """)
            saralash = input("""\n\t\t - + / * kerakli bo'limni tanlang * / + - 
                            1.Oson.
                            2.O'rta.
                            3.Qiyin.
                            4.Ortga.
                        1 va 4 oralig'idagi son kiriting.
                Kiriting>>>
            """)
            birinchi = False
        else:
            saralash = input("Xato, 1 va 4 oralig'idagi son kiriting: ")
        if saralash.isdigit() and int(saralash) in range(1,5):
            return int(saralash)


        if saralash == "1":
            print("Siz menu'dan Oson bo'limini tanladingiz")
        
        elif saralash == "2":
            print("Siz menu'dan O'rta bo'limini tanladingiz")

        elif saralash == "3":
            print("Siz menu'dan Qiyin bo'limini tanladingiz")   

        elif saralash == "4":
            print("Siz menu'dan Ortga bo'limini tanladingiz") 

def play(daraja):
      takror = 5
      user_bal = 0
      for j in range(takror):
        amallar = random.choice(["+","-","*","/"])
        masala = None 
        javob = None
        for son in range(daraja + 1):
            a = random.randint(1,10)
            if son == 0:
                masala = str(a)
                javob = a
            else:
                masala += f" {amallar} {a} "
                if amallar == "+":
                    javob += a
                elif amallar == "-":
                    javob -= a
                elif amallar == "*":
                    javob *= a
                if amallar == "/":
                    javob = round(javob / a, 2)
        natija = input(f"Misolni javobini yozing: {masala} = ")
        if float(natija) == javob:
            print("Javob to'g'ri!")
            user_bal += 1
        else:
            print(f"Xato, to'g'ri javob: {javob}\n")
        print(f"Siz {takror} savoldan {user_bal} ta to'g'ri javob berdingiz")

while True:
    
    os.system("cls")
    tanlov = menu()
    if tanlov == 1:
        print("\n Hurmatli o'yinchi siz menu'dan <Oson> bo'limini tanladingiz:")
        play(daraja = 1)
    
    elif tanlov == 2:
        print("\n Hurmatli o'yinchi siz menu'dan <Qiyin> bo'limini tanladingiz:")
        play(daraja = 2) 

    elif tanlov == 3:
        print("\n Hurmatli o'yinchi siz menu'dan <O'rta> bo'limini tanladingiz:")
        play(daraja = 3)

    elif tanlov == 4:
        print("Dasturdan chiqdingiz!")

    savol = input("Yana o'yin o'ynaysizmi? ha | yo'q : ")
    if savol == "ha":
        continue
    else:
        print("O'yin tugadi!")
        break    