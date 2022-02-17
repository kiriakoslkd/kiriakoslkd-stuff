import random


sthlh=[1,2,3,4,5,6,7,8]
grammh=[1,2,3,4,5,6,7,8]

wp=0
wa=0
for i in range(100):
    p1=random.choice(sthlh)
    p2=random.choice(grammh)
    a1=random.choice(sthlh)
    a2=random.choice(grammh)
    while ((p1==a1) and (p2==a2)):
        a1=random.choice(sthlh)
        a2=random.choice(grammh)


    if (p1==a1):
        wp=wp+1
    elif (p2==a2):
        wp=wp+1
    for i in range(8):
        if ((a1==p1+i) and (a2==p2+i)):
            wa=wa+1
        elif((a1==p1-i) and (a2==a2+i)):
            wa=wa+1
        elif((a1==p1+i) and (a2==p2-i)):
            wa=wa+1
        elif ((a1==a1-i) and (a2==p2-i)):
            wa=wa+1
print("                 APOTELESMATA")
print("                      ↧")
print("")
print("               Gia to 8*8 game:")
print("   O leukos pyrgos(♜ ) kerdise ",wp," rounds!")
print(" O mauros aksiwmatikos(♗ ) kerdise ",wa," rounds!")
print("-------------------------------------------------")



sthlh=[1,2,3,4,5,6,7,]
grammh=[1,2,3,4,5,6,7,]

wp=0
wa=0
for i in range(100):
    p1=random.choice(sthlh)
    p2=random.choice(grammh)
    a1=random.choice(sthlh)
    a2=random.choice(grammh)
    if (p1==a1):
        wp=wp+1
    elif (p2==a2):
        wp=wp+1
    for i in range(8):
        if ((a1==p1+i) and (a2==p2+i)):
            wa=wa+1
        elif((a1==p1-i) and (a2==a2+i)):
            wa=wa+1
        elif((a1==p1+i) and (a2==p2-i)):
            wa=wa+1
        elif ((a1==a1-i) and (a2==p2-i)):
            wa=wa+1
print("               Gia to 7*7 game:")
print("   O leukos pyrgos(♜ ) kerdise ",wp," rounds!")
print(" O mauros aksiwmatikos(♗ ) kerdise ",wa," rounds!")
print("-------------------------------------------------")





sthlh=[1,2,3,4,5,6,7,]
grammh=[1,2,3,4,5,6,7,8]

wp=0
wa=0
for i in range(100):
    p1=random.choice(sthlh)
    p2=random.choice(grammh)
    a1=random.choice(sthlh)
    a2=random.choice(grammh)
    if (p1==a1):
        wp=wp+1
    elif (p2==a2):
        wp=wp+1
    for i in range(8):
        if ((a1==p1+i) and (a2==p2+i)):
            wa=wa+1
        elif((a1==p1-i) and (a2==a2+i)):
            wa=wa+1
        elif((a1==p1+i) and (a2==p2-i)):
            wa=wa+1
        elif ((a1==a1-i) and (a2==p2-i)):
            wa=wa+1
print("               Gia to 7*8 game:")
print("   O leukos pyrgos(♜ ) kerdise ",wp," rounds!")
print(" O mauros aksiwmatikos(♗ ) kerdise ",wa," rounds!")
print("-------------------------------------------------")

