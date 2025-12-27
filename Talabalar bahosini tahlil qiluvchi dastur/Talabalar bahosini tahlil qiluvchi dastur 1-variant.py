""" 
Talabalar bahosini tahlil qiluvchi dastur 


Bunda quyidagi mavzular qamrab olamiz.

🟠 Lists
🔵 for sikli
🟢 if,elif va else shartlari
🟡 Sonlar bilan ishlash
🔴 Statistik hisoblar

"""

ballar=[45,59,64,53,50,89,57,86,66,59,70,96,100,82,95,40,56,75,90] # Bu ixtiyoriy, istalgancha kiritish mumkun.

qoniqarli_baho=[]
baho_2=[]
baho_3=[]
baho_4=[]
baho_5=[]

#Shartlar asosida ballarni baxoli guruhlarga ajratib olamiz.
for ball in ballar:
    if ball <= 55:
        baho_2.append(ball)
    elif ball >= 56 and ball <= 70:
        baho_3.append(ball)
    elif ball >= 71 and ball <= 85:
        baho_4.append(ball)
    else:
        baho_5.append(ball)
        
average_ball=(sum(ballar))/len(ballar)  # average ball - bu o'rtacha ball.

for n in ballar:
    if n >= average_ball:
        qoniqarli_baho.append(n) #  O'rtacha balldan yuqori balllar ro'yxati
        
qoniqarli_baho.sort()   #   Teskari tartiblash uchun .sort(reverse=True) ishlatamiz.

print(f"\n\"Baholar\" ro'yxatida ja'mi {len(ballar)} ta baho mavjud. Shulardan:\n ")

print(f"\"5\" baho olganlar soni – {len(baho_5)} ta\n")
print(f"\"4\" baho olganlar soni – {len(baho_4)} ta\n")
print(f"\"3\" baho olganlar soni – {len(baho_3)} ta\n")
print(f"\"2\" baho olganlar soni – {len(baho_2)} ta\n")


print(f"Baholar ro'yxatidagi eng katta baho – {max(ballar)}\n")
print(f"Baholar ro'yxatidagi eng kichik baho – {min(ballar)}\n")

print("O'rtachadan yuqori ballar ro'yxati quyidagicha:")

for n in qoniqarli_baho:
    print(f"- {n}")
    
jamoa_bali=(5*len(baho_5) + 4*len(baho_4) + 3*len(baho_3) + 2*len(baho_2))/len(ballar)
print(f"\nJamoaning o'rtacha bahosi – {jamoa_bali:.2f}") 
print(f"\nJamoaning o'rtacha bali – {average_ball:.2f}")
#Bu yerda :.2f natijani ikki xonali o'nlik bilan yaxlitlab chiqaradi. Agar :.3f bo'lsa 3 xonali va xokozo...