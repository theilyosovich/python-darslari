""" 
Matn tahlilchisi dasturi


Bunda quyidagi mavzularni qamrab olamiz.

🟠 Lists
🔵 for sikli
🟢 if,elif va else shartlari
🟡 Strings metodlar


"""

matn=input("Matn kiriting: ")

sozlar=matn.split() 


if not matn: #  Agar matn bo'sh bo'lsa, unga xabar beramiz.
    print("Siz matn kiritmadingiz")
else:
    print(f"\nSiz kiritgan matnda {len(matn.split())} ta so'z bor.\n")

    print(f"Siz kiritgan matnda jami {len(matn)} ta belgi bor.")
    
    tozalangan_matn=matn.lower().replace(",", "").replace(".", "").replace("!","").replace("?","").split()
    kop_soz=""
    kop_soni=0
    
    
    for soz in tozalangan_matn:
        takror=tozalangan_matn.count(soz)
        if takror > kop_soni:
            kop_soni=takror
            kop_soz=soz
    if kop_soni==1:
        print("Barcha so'zlar faqat bir martadan qatnashgan.\n")
    else:
        print(f"Eng ko'p takrorlangan so'z bu – \"{kop_soz}\"."
              f"Bu so'z matnda {kop_soni} marta qatnashgan.\n")
    
    
    gaplar=matn.replace("?", ".").replace("!",".").split(".")
    toza_gaplar=[]
    
    for gap in gaplar:
        if gap.strip() != "":
            toza_gaplar.append(gap.strip())
            
    print(f"Siz kiritgan matnda {len(toza_gaplar)} ta gap bor. Bular:")
    for gap in toza_gaplar:
        print(f"– {gap}")
        
        """Bu yerda kichik xato bor, sababi gap oxirida qanday belgi borligini kirita olmadim, 
        buni dasturning keyingi variantida qo'llayman."""