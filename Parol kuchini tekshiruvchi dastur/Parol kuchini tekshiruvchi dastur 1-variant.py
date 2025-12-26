""" 
Parol kuchini tekshiruvchi dastur 

1-Versiya

Bunda quyidagi mavzular qamrab olamiz.

🟠 Strings
🔵 Tarmoqlanish shartlari
🟢 String methods
🟡 Xatolar bilan ishlash

"""

print("\nAssalomu aleykum xurmatli foydalanuvchi."
      "Ushbu dastur sizga siz yaratayotgan parol qanchalik murakkab ekanini tekshirib beradi.")

#Foydalanuvchidan parol kiritishni so'raymiz
parol=input("\nParol kiriting: ")

#Bu yerda FLAG ya'ni mantiqiy ishora ishlatamiz.
xato=False

#Shartlarni ketma-ketlikda tekshiramiz.

#Parol bo'sh emasligini va birinchi belgi harf ekanligini tekshiramiz
if parol and not parol[0].isalpha():
    print("\n❗Parolning birinchi belgisi harf bo'lishi kerak!")
    xato = True
    
#Parol uzunligini tekshiramiz
if len(parol) < 8:
    print("\n❗Parol kamida 8 ta belgidan iborat bo'lishi kerak!")
    xato = True

#Kamida bitta KATTA harf borligini tekshiramiz.
if not any(harf.isupper() for harf in parol):
    print("\n❗Parolda kamida bitta KATTA harf bo'lishi kerak!")
    xato = True
    
#Kamida bitta KICHIK harf borligini tekshiramiz.
if not any(harf.islower() for harf in parol):
    print("\n❗Parolda kamida bitta KICHIK harf bo'lishi kerak!")
    xato = True
    
#Kamida bitta raqam borligini tekshiramiz.
if not any(harf.isdigit() for harf in parol):
    print("\n❗Parolda kamida bitta raqam bo'lishi kerak!")
    xato = True
    
#Kamida bitta belgi borligini tekshiramiz.
if not any(not harf.isalnum() for harf in parol):
    print("\n❗Parolda kamida bitta belgi bo'lishi kerak!")
    xato = True
    
#Barcha shartlardan muvaffaqqiyatli o'tgandan so'ng, parolni chiqarish.  
if not xato:  
    print(f"✅Tabriklayman! \n>>> {parol} Siz kuchli parol kiritdingiz")

