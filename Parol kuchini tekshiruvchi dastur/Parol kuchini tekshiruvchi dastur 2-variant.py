""" 
Parol kuchini tekshiruvchi dastur 

2-Versiya

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

xatolar=[]

#Shartlarni ketma-ketlikda tekshiramiz.

#Parol bo'sh emasligini tekshiramiz
if not parol.strip():
    xatolar.append("Parolning bo'sh bo'lmasligi kerak!")
else:
    #Agar parol bo'sh bo'lmasa, parolning birinchi belgisi harf ekanligini tekshiramiz
    if not parol[0].isalpha():
        xatolar.append("Parolning birinchi belgisi harf bo'lishi kerak!")

#Parol uzunligini tekshiramiz
if len(parol) < 8:
    xatolar.append("Parol kamida 8 ta belgidan iborat bo'lishi kerak!")
    
#Kamida bitta KATTA harf borligini tekshiramiz.
if not any(harf.isupper() for harf in parol):
    xatolar.append("Parolda kamida bitta KATTA harf bo'lishi kerak!")
  
#Kamida bitta KICHIK harf borligini tekshiramiz.
if not any(harf.islower() for harf in parol):
    xatolar.append("Parolda kamida bitta KICHIK harf bo'lishi kerak!")
 
#Kamida bitta raqam borligini tekshiramiz.
if not any(harf.isdigit() for harf in parol):
    xatolar.append("Parolda kamida bitta raqam bo'lishi kerak!")
      
#Kamida bitta belgi borligini tekshiramiz.
if not any(not harf.isalnum() for harf in parol):
    xatolar.append("Parolda kamida bitta belgi bo'lishi kerak!")
    
if xatolar:
    print("❗Zaif parol. Quyidagi tavsiyalarga amal qiling!")
    for xato in xatolar:
        print(f" — {xato}")
else:
    print("✅Tabriklayman! Siz kuchli parol kiritdingiz")
    
