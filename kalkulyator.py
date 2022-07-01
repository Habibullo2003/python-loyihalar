print(" Phytonda kalkulyator dasturi ")
# a = int(input("a onni kiriting: "))
# b = int(input("b sonni kiriting: "))
# son = int(input('son kiriting:'))
while True:
    a = int(input("a onni kiriting: "))
    b = int(input("b sonni kiriting: "))
    son = int(input('son kiriting:'))
    c = 0
    ishora = ' '
    if son == 1:
        c = a + b
        print("Qo'shish")
        ishora = '+'
    elif son ==2:
        c = a - b
        ishora = '-'
    elif son == 3:
        c = a * b
        ishora = '*'
    elif son == 4:
        c = a // b
        ishora = '/'
    else:
        print("Dastur ishlamaydi. Boshqa sonni kiriting: ")  
        continue
    print(f"Natija: {a} {ishora} {b} = {c}")