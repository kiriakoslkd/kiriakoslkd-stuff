
print("            Epeksergasia tou arxeioy 'two_cities_ascii.txt'...")

x = open('two_cities_ascii.txt')
x1 = str(x.read())
pinakas = bytearray(x1, "utf8")


b = []
ar2=[]
ar1=[]
for i in pinakas:
    dyadika = bin(i)
    b.append(dyadika[2:])


for i in b:
    arr=list(i)
    if len(arr)<7:
        arr.insert(0,'0')
    m1=0
    m2=0
    s1=0
    s2=0

    for bit in arr:
        if bit=='0':
            s1+=1
            s2=0
            if m1<s1:
                m1=s1
            
        else:
            s2+=1
            s1=0
            if m2<s2:
                m2=s2
            
    ar2.append(m2)
    ar1.append(m1)

b1=max(ar1)
b2=max(ar2)

print("")
print("                          APOTELESMATA")
print("                               ↧")
print("")
print("H megalyterh akoluthia apo synexomena mhdenika einai ",b1," mhdenika!")
print(" H megalyterh akolouthia apo synexomenous assous einai ",b2," assoi!")
