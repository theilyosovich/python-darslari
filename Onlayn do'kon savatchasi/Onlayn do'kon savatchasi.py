""" 
Onlayn do'kon savatchasi 

1-Versiya

Bunda quyidagi mavzular qamrab olamiz.
🟡 While sikli
🟠 Tuples (O'zgarmas maxsulotlar)
🔵 Lists
🟢 For sikli va shartlar
🔴 Hisob-kitob va xatoliklarni oldini olish

"""
import os

def clear_console(): #Bu internedan men izlab topgan tayyor funksiya, men buni bilmas edim😊
    os.system('cls')
    
"""Ushbu qism xar safar yangi amal bajarilganda consolni tozalash uchun ishlatildi.
Console tozalanadi ammo kiritilgan ma'lumotlar o'chib ketmaydi.
Bu faqat yangi chiqadigan oynani chiroyli qilish uchun xizmat qiladi.
"""
    
mahsulotlar = [
    ("Non", 5000),
    ("Go'sht", 100000),
    ("Kartoshka", 10000),
    ("Piyoz", 8000),
    ("Olma", 7000),
    ("Yog'", 25000),
    ("Sut", 9000),
    ("Tuxum", 1200),
    ("Sariyog'", 45000),
    ("Qatiq", 6000),
    ("Baliq", 70000),
    ("Pomidor", 9000),
    ("Bodring", 5000),
    ("Shokolad", 15000),
    ("Pishloq", 35000),
    ("Olxo'ri", 8000),
    ("Uzum", 10000),
    ("Banan", 12000),
    ("Apelsin", 9000),
    ("Qovoq", 7000)
]

#Do'konchani o'zimizga kerakli maxsulotlar bilan bemalol boyitib olamiz.

savatcha=[]

menyu = """
Assalomu aleykum mijoz, qaysi amalni bajarmoqchisiz?
1. Maxsulot qo'shish
2. Savatchani ko'rish
3. Maxsulotni o'chirish
4. Umumiy narxni ko'rish
5. Chiqish

>>> """ 

#Uchta qo'shtirnoqlar bizga matnni bir nechta qatorlarga bo'lib yozish imkonini beradi.


while True:
    clear_console() #Yuqoridagi qismning davomi. Xar safar menyuga qaytganda console tozalanadi.
    
    sorov=input(menyu)
    
    if not sorov:
        print("\nXurmatli foydalanuvchi, siz xech qanday so'rov yubormadingiz.")
   
# Savatchaga mahsulot qo'shish qismi    
    elif sorov == "1":
        print("\nDo'konimizdagi mahsulotlar:\n")
        for a, (nom , narx) in enumerate(mahsulotlar, start=1):
                print(f"{a}. {nom} - {narx} so'm")
        
        
        while True:
            print("\nDo'konimizdagi mahsulotlar:\n")
            for a, (nom , narx) in enumerate(mahsulotlar, start=1):
                    print(f"{a}. {nom} - {narx} so'm")
                    
            tanlov = input("""\nQaysi mahsulotni qo'shishni istaysiz?
(Raqamni kiriting): """)
            
                
            if not tanlov.isdigit():
                print("❌ Iltimos maxsulotning to'g'ri raqamini kiriting!")
            else:
                index= int(tanlov) - 1
            
                if 0 <= index < len(mahsulotlar):
                    miqdor= input("\nQancha (KG) yoki nechta olishni istaysiz? ")
                    
                    try:
                        son=float(miqdor)
                        
                        if son < 0:
                            print("Miqdor manfiy bo'lishi mumkun emas!")
                        else:
                            savatcha.append((mahsulotlar[index][0],mahsulotlar[index][1],son))
                            print("✅ Maxsulot savatchaga qo'shildi.")
                            
                    except ValueError:
                        print("Miqdor faqat musbat son bo'lishi kerak.")
                else:
                    print("❌ Bunday maxsulot mavjud emas.")
            
            userdan_sorov=input("\nYana qo'shishni istaysizmi? (Yes/No) >>> ")
            
            if userdan_sorov != "yes".casefold():
                print("\n✅Chiqish so'rovingiz qabul qilindi.")
                break
        print(f"\n✅ Savatchaga ja'mi {len(savatcha)} ta maxsulot qo'shildi.")
    
#Savatchani ko'rsatish qismiga o'tamiz
    elif sorov == "2":
        if not savatcha:
            print("\n🛒Savatchangizda xech narsa yo'q.\n")
        else:
            print("\n🛒Savatchangizdagi maxsulotlar:")
            for a , (mahsulot,narx,son) in enumerate(savatcha, start=1):
                print(f"{a}. {int(son)} ta (kg) {mahsulot}")
        
        print(f"\nSavatchada ja'mi {len(savatcha)} ta mahsulot mavjud.\n")
   
#Savatchadan mahsulot o'chirish qismiga o'tamiz           
    elif sorov == "3":
        if not savatcha:
            print("\n🛒Savatchangizda xech narsa yo'q.\n")
        else:
            while True:
                print("\n🛒Savatchangizdagi maxsulotlar:")
                for a , (mahsulot,narx,son) in enumerate(savatcha, start=1):
                    print(f"{a}. {int(son)} ta (kg) {mahsulot}")
                
                deleted_sorovi=input("""Qaysi mahsulotni o'chirmoqchisiz?
(Raqamini kiriting: """)
                if not deleted_sorovi.isdigit():
                     print("❌ Iltimos maxsulotning to'g'ri raqamini kiriting!")
                else:
                    deleted_index = int(deleted_sorovi) - 1
                    
                    if 0 <= deleted_index < len(savatcha):
                        removed=savatcha.pop(deleted_index)
                        print(f"{removed[0]} savatchadan o'chirildi.")
                    else:
                        print("Bunday mahsulot mavjud emas.")
                userdan_sorov=input("Yana o'chirmoqchimisiz? (Yes / No) >>> ")
                if userdan_sorov.casefold() != "yes":
                    print(f"O'chirish tugadi. Savatchada {len(savatcha)} ta mahsulot qoldi.\n")
                    break
    
# Umumiy narxni ko'rish qismiga o'tamiz.
    
    elif sorov == "4":
        jami_narx=0

        if not savatcha:
            print("\n🛒Savatchangizda xech narsa yo'q.\n")
        else:
            print("\n🛒Savatchangizdagi maxsulotlar:")
            
            
            for a , (mahsulot,narx,son) in enumerate(savatcha, start=1):
                mahsulot_narxi = narx * son
                jami_narx +=mahsulot_narxi
                
                print(f"{a}. {int(son)} ta (kg) {mahsulot} – {mahsulot_narxi} so'm")
                
        print(f"\n💰Ja'mi mahsulot narxi – {jami_narx} so'm\n")

# Dasturni to'xtatish qismi                     
    elif sorov == "5":
        print("\nChiqish so'rovi qabul qilindi.")
        break