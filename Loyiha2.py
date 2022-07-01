# print(""" 
#      Assalomu alaykum xush kelibsiz
#      Saytga kirish uchun quyidagi formani to'ldiring
# """)

# print("1.- Kirish \n2.-Ro'yxardan o'tish")

# def menu():
#     while True:
#         user = input("Ma'lumot kiriting: ")
#         kirish = {}
#         if kirish == 'ism':
#             kirish.append("Habibullo")
#         elif kirish == 'familiya':
#             kirish.append("Xayrullayev")
#         elif kirish == 'gmail':
#             kirish.append("xayrullayevhabibullo745@gmail.com")
#         elif kirish == 'kod':
#             kirish.append("77777777")
#         elif kirish == 'ID raqam':
#             kirish.append("xayru20003")
    







""" Login registration """

user = [
    {"username":"test","ID raqam":"4545445","password":"4455"}
]
print("\n\nAssalomu alaykum xush kelibsiz\n Menu'dan kerakli bo'limni tanlang:")
def main():
    def login():
        username = input("Foydalanuvchi nomi: ")
        password = input("Foydanuvchi kodi: ")
        for users in user:
            if users["username"] == username and users["password"] == password:
                print("Tabriklaymiz siz akkauntga kirdingiz!")
                break
            else:
                print("Xato! Login va parolni o'ylab qayta kiriting:")
                login()         
    
    def create():
        username = input("Yangi login kiriting: ")
        password = input("Yangi kod kiriting: ")
        ID_raqam = input("ID kiriting: ")

        new_user = {"username":username,"ID_raqam":ID_raqam,"password":password}
        user.append(new_user)
        print(user)
        print("Siz ro'yxatdan o'tdingiz!")
        login()
        for new_user in users:
            for users in user:
                if users["username"] == username and users["password"] == password:
                    print("Tabriklaymiz siz akkauntga kirdingiz!")
                    break
                else:
                    print("Xato! Login va parolni o'ylab qayta kiriting:") 
        login()


    print("---menu---\nKirish\nRo'yxatdan o'tish")
    javob = int(input("Kiriting>>>"))

    if javob == 1:
        login()
    elif javob == 2:
        create()
    
  
main()