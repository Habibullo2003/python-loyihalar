#Phytonda mehmonxona dasturi

def mehmonxona():
    while True:
        print("""  
        ------ MENU ------
            1.Xona bron qilish.
            2.Mehmonxona haqida ma'lumot olish.
            3.Admin kabinetiga kirish.
            4.Dasturni to'xtatish...
        """)
        a = int(input("1 dan 4 gacha raqam kiriting: "))
        if a == 1:
            print("""
                Bizda 2 xil xonalar bor
            1. Lux xonalar
            2. Standart xonalar
            """)
            xona = int(input("Sizga kerakli bo'lgan xonani tanlash uchun raqamni kriiting: "))
            if xona == 1:
                print("Siz lux xonani tanladingiz")
                l_xona = int(input(""" 
                	1. Lux xonalar haqida ma'lumot olish: 
	                2. Lux xonalar narxlari bilan tanishish: 
                """))
                if l_xona == 1:
                    print("Bizda ajoyib yorug' va shinam lux xonalarimiz bor. Xonalarimizda siz istagan barcha sharoitlar yetatrli.")
                    
                elif l_xona == 2:
                    b = int(input("Sizga nechta xona kerak: "))
                    if b == 1:
                        print("Siz 1 ta lux xona tanladingiz. Bizda bitta lux xona narxi 100$.")
                        
                    elif b == 2:
                        print("Siz 2 ta lux xona tanladingiz. Bizda 2 ta lux xona narxi 200$.")
                        
                    elif b != 1 or b != 2:
                        print("Xato! 1 yoki 2 raqamini kiriting.")
                        break
                    
                    tanlash = input("Xosh xonalarimiz sizga yoqdimi! Agar sotib olmoqchi bo'lsangiz 'ha' ni Agarbekor qilmoqchi bo'lsangiz 'yoq' ni bosing: ")
                    if tanlash == 'ha':
                        print("Anketani to'ldiring")
                        ismi = input("Ismingizni kiriting: ")
                        familiya = input("Familiyangizni kiriting: ")
                        t_raqam = int(input("Telefon raqamingizni kiriting: "))
                        manzil = input("Manzilingizni kiriting: ")
                        email = input("emailingizni kiriting: ")
                        
                        tulov = input("To'lov turini tanlang: naqd\karta: ")
                        if tulov == 'naqd':
                            print("Siz naqd pul orqali to'lov qilishni tanladingiz.Marhamat to'lovni amalga oshirishingiz mumkin.")
                            m_tulovi = int(input("mijoz to'lagan pul: "))
                            if m_tulovi < l_xona*100:
                                print(f"sizga xona bron qilish uchun {l_xona*100 - m_tulovi} $ pul yetmayapti")
                            
                            elif m_tulovi > l_xona*100:
                                print(f"Tabriklaymiz siz xona bron qildingiz. Sizga {m_tulovi - l_xona*100} $ pul qaytarib beriladi")
                            
                            continue

                        if tulov == 'karta':
                            raqam = int(input("Kartangizni oxirgi 4 ta raqamini kiriting: "))
                            if raqam > 999 and raqam < 10000:
                                xona_tulov = int(input("Xona uchun qancha to'lashingizni kiriting: "))
                                if xona_tulov < l_xona*100:
                                    print(f"sizga xona bron qilish uchun {l_xona*100 - xona_tulov} $ pul yetmayapti")
                                
                                elif xona_tulov > l_xona*100:
                                    print(f"""Tabriklaymiz sizning pulingiz xona bron qilishga yetar ekan.Siz xona bron qildingiz.
                                    {xona_tulov - l_xona} $ pulingiz qaytarib beriladi.
                                    """)

                            elif raqam < 999 and raqam > 10000:
                                print("Xato! Yana qayta urinib ko'ring.")  

                    elif tanlash == 'yoq':
                        print("Xizmatlar bekor qilindi")    
                                
                        continue

            elif xona == 2:
                print("Siz standart xonani tanladingiz.")   
                st_xona = int(input(""" 
                	1. Standart xonalar haqida ma'lumot olish: 
	                2. Standart xonalar narxlari bilan tanishish: 
                """))
                if st_xona == 1:
                    print("Bizda ajoyib yorug' va shinam standart xonalarimiz bor. Xonalarimizda siz istagan deyarli barcha sharoitlar yetatrli.")
                    
                elif st_xona == 2:
                    c = int(input("Sizga nechta xona kerak: "))
                    if c == 1:
                        print("Siz 1 ta lux xona tanladingiz. Bizda bitta lux xona narxi 80$.")
                        
                    elif c == 2:
                        print("Siz 2 ta lux xona tanladingiz. Bizda 2 ta lux xona narxi 160$.")
                       
                    elif c != 1 or c != 2:
                        print("Xato! 1 yoki 2 raqamini kiriting.")
                        break

                    tanlash = input("Xosh xonalarimiz sizga yoqdimi! Agar sotib olmoqchi bo'lsangiz 'ha' ni Agarbekor qilmoqchi bo'lsangiz 'yoq' ni bosing: ")
                    if tanlash == 'ha':
                        print("Anketani to'ldiring")
                        ismi = input("Ismingizni kiriting: ")
                        familiya = input("Familiyangizni kiriting: ")
                        t_raqam = int(input("Telefon raqamingizni kiriting: "))
                        manzil = input("Manzilingizni kiriting: ")
                        email = input("emailingizni kiriting: ")
                        
                        tulov = input("To'lov turini tanlang: naqd\karta: ")
                        if tulov == 'naqd':
                            print("Siz naqd pul orqali to'lov qilishni tanladingiz.Marhamat to'lovni amalga oshirishingiz mumkin.")
                            m_tulovi = int(input("mijoz to'lagan pul: "))
        
                            if m_tulovi < st_xona*80:
                                print(f"sizga xona bron qilish uchun {st_xona*80 - m_tulovi} $ pul yetmayapti")
                            
                            elif m_tulovi > st_xona*80:
                                print(f"Tabriklaymiz siz xona bron qildingiz. Sizga {m_tulovi - st_xona*80} $ pul qaytarib beriladi")
                            
                            continue

                        if tulov == 'karta':
                            raqam = int(input("Kartangizni oxirgi 4 ta raqamini kiriting: "))
                            if raqam > 999 and raqam < 10000:
                                xona_tulov = int(input("Xona uchun qancha to'lashingizni kiriting: "))
                    
                                if xona_tulov < st_xona*80:
                                    print(f"sizga xona bron qilish uchun {st_xona*80 - xona_tulov} $ pul yetmayapti")
                                
                                elif xona_tulov >= st_xona*80:
                                    print(f"""Tabriklaymiz sizning pulingiz xona bron qilishga yetar ekan.Siz xona bron qildingiz.
                                    {xona_tulov - st_xona} $ pulingiz qaytarib beriladi.
                                    """)

                            elif raqam < 999 and raqam > 10000:
                                print("Xato! Yana qayta urinib ko'ring.")  

                    elif tanlash == 'yoq':
                        print("Xizmatlar bekor qilindi")   

                    continue

        elif a == 2:
            print("""
            Siz mehmonxona haqida ma'lumot olish menyusini tanladingiz.
            Bizning mehmonxona siz kutgan barcha qulayliklarga ega.
            Mehmonxonamiz nufuzli mehmonxonalardan bo'lib 2017 - yillarda qurib bitkazilgan.
            Mehmonxona 2018 - yil 1- yanvarda foydalanishga topshirilgan.
            Mehmonxanamiz 15 qavat 500 xonadan iborat. liftlarimiz standart zamonaviy talablarga javob beradi.
            Siz bizning mehmonxonada maza qilib dam olishingiz mumkin.
            """)
            
            continue

        if a == 3:
            print("Siz admin kabinetiga kirishni tanladingiz.")
            admin_logini = 603247
            login = int(input("Loginni kiriting: "))
            if login != admin_logini:
                print("Xato! Siz admin emassiz.")
            
            elif login == admin_logini:
                print("""
                Salom Admin xush kelibsiz.
                Bugun 5 ta lux va 8 ta standart xona bron qilindi.
                Jami bo'lib 1140 $ kassaga pul tushdi.
                 """)

        continue
    
mehmonxona()                       