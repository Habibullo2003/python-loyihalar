import random as r


# bu yerda yangi kod yozildi!


print("""
\n\n\tAssalomu alaykum komyuter bilan <quduq>, <qaychi>, <qog'oz> o'yiniga xush kelibsiz.
\tO'yinni  boshlash uchun shartlardan birini tanlang.
""")
lugat = r.choice(['quduq','qaychi','qog\'oz'])
a = 0
b = 0
c = 0
for i in range(5):
    u = input("Variantingizni tanlang: <quduq>, <qaychi>, <qog'oz>: ")
    if u == "quduq" and lugat=="qaychi" or u == "qaychi" and lugat == "quduq":
        print("Kompyuter yutdi")
    elif u == "qog'oz" and lugat == "quduq" or u == "quduq" and lugat == "qog'oz":
        print("Kompyuter yutdi")
    elif u == "qog'oz" and lugat == "qaychi" or u == "qaychi" and lugat == "qog'oz":
        print("Kompyuter yutdi")
        a += 1
        break

    if u == "quduq" and lugat=="qaychi" or u == "qaychi" and lugat == "quduq":
        print("Siz yutdingiz")
    elif u == "qog'oz" and lugat == "quduq" or u == "quduq" and lugat == "qog'oz":
        print("Siz yutdingiz")
    elif u == "qog'oz" and lugat == "qaychi" or u == "qaychi" and lugat == "qog'oz":
        print("Siz yutdingiz")  
        b += 1
        break

    if u == "quduq" and lugat=="quduq" or u == "qaychi" and lugat == "qaychi":
        print("Durang")
    elif u == "qog'oz" and lugat == "qog'oz" or u == "quduq" and lugat == "quduq":
        print("Durang")
    elif u == "qaychi" and lugat == "qaychi" or u == "qog'oz" and lugat == "qog'oz":
        print("Durang")
        c += 1
        break    

print(f"Komyuter {a}:{b} Foydalanuvchi")
print(f"Duranglar soni {c}")
    


    