print("Šis ir mans kursa darbs!")

import random
print()
x = 0 

rows, cols = (3, 3) 
arr=[] 
for i in range(cols): 
    col = [] 
    for j in range(rows): 
        col.append("( )")
    arr.append(col) 

print("Spēlētājam jāievada rindas un kolonnas numurs, kurā vēlas ievietot simbolu.")
print("Pirmais spēlētājs, kurš iegūs attiecīgo simbolu skaitu 3, (rindā, kolonnā vai diagonāli) uzvarēs.")
print("Spēles laukums:")

for i in range(rows):
    for j in range(cols):
        print(arr[i][j], end=" ")
    print()
print()


nosacijums = True
nosacijums_2 = False


while nosacijums != False:
    r = int(input("(1.spēlētājs)Ievadiet rindas numuru, kuru vēlaties atzīmēt ar (x): "))
    k = int(input("(1.spēlētājs)Ievadiet kolonnas numuru, kuru vēlaties atzīmēt ar (x) : "))

    if arr[r-1][k-1] == ("(x)") or arr[r-1][k-1] == ("(O)"):
        print("Jūsu izvēlētais laukums ir aizņemts!")
        print("Mēģiniet vēlreiz!")
        while nosacijums_2 == False:
            r = int(input("(1.spēlētājs)Ievadiet rindas numuru, kuru vēlaties atzīmēt ar (x): "))
            k = int(input("(1.spēlētājs)Ievadiet kolonnas numuru, kuru vēlaties atzīmēt ar (x) : "))
            if arr[r-1][k-1] == ("( )"):
                arr[r-1][k-1] = ("(x)")
                nosacijums_2 = True
            else:
                print("Jūsu izvēlētais laukums ir aizņemts!")
                print("Mēģiniet vēlreiz!")
        nosacijums_2 = False
    else:
        arr[r-1][k-1] = ("(x)")
    print()

    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end=" ")
        print()

    if arr[0][0] == ("(x)") and arr[0][1] == ("(x)") and arr[0][2] == ("(x)"): 
        print("Jūs uzvarējāt!")
        break
    elif arr[1][0] == ("(x)") and arr[1][1] == ("(x)") and arr[1][2] == ("(x)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[2][0] == ("(x)") and arr[2][1] == ("(x)") and arr[2][2] == ("(x)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[0][0] == ("(x)") and arr[1][0] == ("(x)") and arr[2][0] == ("(x)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[0][1] == ("(x)") and arr[1][1] == ("(x)") and arr[2][1] == ("(x)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[0][2] == ("(x)") and arr[1][2] == ("(x)") and arr[2][2] == ("(x)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[0][0] == ("(x)") and arr[1][1] == ("(x)") and arr[2][2] == ("(x)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[0][2] == ("(x)") and arr[1][1] == ("(x)") and arr[2][0] == ("(x)"):
        print("Jūs uzvarējāt!")
        break
    if x == 4:
        print("Neizšķirts!")
        break
    x = x+1

    print()

    rr = int(input("(2.spēlētājs)Ievadiet rindas numuru, kuru vēlaties atzīmēt ar (O): "))
    kk = int(input("(2.spēlētājs)Ievadiet kolonnas numuru, kuru vēlaties atzīmēt ar (O) : "))
    
    if arr[rr-1][kk-1] == ("(x)") or arr[rr-1][kk-1] == ("(O)"):
        print("Jūsu izvēlētais laukums ir aizņemts!")
        print("Mēģiniet vēlreiz!")
        while nosacijums_2 == False:
            rr = int(input("(2.spēlētājs)Ievadiet rindas numuru, kuru vēlaties atzīmēt ar (O): "))
            kk = int(input("(2.spēlētājs)Ievadiet kolonnas numuru, kuru vēlaties atzīmēt ar (O) : "))
            if arr[rr-1][kk-1] == ("( )"):
                arr[rr-1][kk-1] = ("(O)")
                nosacijums_2 = True
            else:
                print("Jūsu izvēlētais laukums ir aizņemts!")
                print("Mēģiniet vēlreiz!")
        nosacijums_2 = False
    else:
        arr[rr-1][kk-1] = ("(O)")
    print()

    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end=" ")
        print()

    if arr[0][0] == ("(O)") and arr[0][1] == ("(O)") and arr[0][2] == ("(O)"): 
        print("Jūs uzvarējāt!")
        break
    elif arr[1][0] == ("(O)") and arr[1][1] == ("(O)") and arr[1][2] == ("(O)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[2][0] == ("(O)") and arr[2][1] == ("(O)") and arr[2][2] == ("(O)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[0][0] == ("(O)") and arr[1][0] == ("(O)") and arr[2][0] == ("(O)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[0][1] == ("(O)") and arr[1][1] == ("(O)") and arr[2][1] == ("(O)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[0][2] == ("(O)") and arr[1][2] == ("(O)") and arr[2][2] == ("(O)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[0][0] == ("(O)") and arr[1][1] == ("(O)") and arr[2][2] == ("(O)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[0][2] == ("(O)") and arr[1][1] == ("(O)") and arr[2][0] == ("(O)"):
        print("Jūs uzvarējāt!")
        break
print("Paldies par spēli!")
        
        
print()
x = 0 

rows, cols = (3, 3) 
arr=[] 
for i in range(cols): 
    col = [] 
    for j in range(rows): 
        col.append("( )")
    arr.append(col) 

print("Spēlētājam jāievada rindas un kolonnas numurs, kurā vēlas ievietot simbolu.")
print("Pirmais spēlētājs, kurš iegūs attiecīgo simbolu skaitu 3, (rindā, kolonnā vai diagonāli) uzvarēs.")
print("Spēles laukums:")

for i in range(rows):
    for j in range(cols):
        print(arr[i][j], end=" ")
    print()
print()


nosacijums = True
nosacijums_2 = False


while nosacijums != False:
    r = int(input("(1.spēlētājs)Ievadiet rindas numuru, kuru vēlaties atzīmēt ar (x): "))
    k = int(input("(1.spēlētājs)Ievadiet kolonnas numuru, kuru vēlaties atzīmēt ar (x) : "))

    if arr[r-1][k-1] == ("(x)") or arr[r-1][k-1] == ("(O)"):
        print("Jūsu spēles laukums jau bija izvēlēts!")
        print("Mēģiniet vēlreiz!")
        while nosacijums_2 == False:
            r = int(input("(2.spēlētājs)Ievadiet rindas numuru, kuru vēlaties atzīmēt ar (x): "))
            k = int(input("(2.spēlētājs)Ievadiet kolonnas numuru, kuru vēlaties atzīmēt ar (x) : "))
            if arr[r-1][k-1] == ("( )"):
                arr[r-1][k-1] = ("(x)")
                nosacijums_2 = True
            else:
                print("Jūsu spēles laukums jau bija izvēlēts!")
                print("Mēģiniet vēlreiz!")
        nosacijums_2 = False
    else:
        arr[r-1][k-1] = ("(x)")
    print()

    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end=" ")
        print()

    if arr[0][0] == ("(x)") and arr[0][1] == ("(x)") and arr[0][2] == ("(x)"): 
        print("Jūs uzvarējāt!")
        break
    elif arr[1][0] == ("(x)") and arr[1][1] == ("(x)") and arr[1][2] == ("(x)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[2][0] == ("(x)") and arr[2][1] == ("(x)") and arr[2][2] == ("(x)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[0][0] == ("(x)") and arr[1][0] == ("(x)") and arr[2][0] == ("(x)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[0][1] == ("(x)") and arr[1][1] == ("(x)") and arr[2][1] == ("(x)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[0][2] == ("(x)") and arr[1][2] == ("(x)") and arr[2][2] == ("(x)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[0][0] == ("(x)") and arr[1][1] == ("(x)") and arr[2][2] == ("(x)"):
        print("Jūs uzvarējāt!")
        break
    elif arr[0][2] == ("(x)") and arr[1][1] == ("(x)") and arr[2][0] == ("(x)"):
        print("Jūs uzvarējāt!")
        break
    if x == 4:
        print("Neizšķirts!")
        break
    x = x+1

    print()

    rr = random.randint(1,3)
    kk = random.randint(1,3)
    
    if arr[rr-1][kk-1] == ("(x)") or arr[rr-1][kk-1] == ("(O)"):
        while nosacijums_2 == False:
            rr = random.randint(1,3)
            kk = random.randint(1,3)
            if arr[rr-1][kk-1] == ("( )"):
                arr[rr-1][kk-1] = ("(O)")
                nosacijums_2 = True
        nosacijums_2 = False
    else:
        arr[rr-1][kk-1] = ("(O)")
    print()

    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end=" ")
        print()

    if arr[0][0] == ("(O)") and arr[0][1] == ("(O)") and arr[0][2] == ("(O)"): 
        print("Dators uzvarēja")
        break
    elif arr[1][0] == ("(O)") and arr[1][1] == ("(O)") and arr[1][2] == ("(O)"):
        print("Dators uzvarēja")
        break
    elif arr[2][0] == ("(O)") and arr[2][1] == ("(O)") and arr[2][2] == ("(O)"):
        print("Dators uzvarēja")
        break
    elif arr[0][0] == ("(O)") and arr[1][0] == ("(O)") and arr[2][0] == ("(O)"):
        print("Dators uzvarēja")
        break
    elif arr[0][1] == ("(O)") and arr[1][1] == ("(O)") and arr[2][1] == ("(O)"):
        print("Dators uzvarēja")
        break
    elif arr[0][2] == ("(O)") and arr[1][2] == ("(O)") and arr[2][2] == ("(O)"):
        print("Dators uzvarēja")
        break
    elif arr[0][0] == ("(O)") and arr[1][1] == ("(O)") and arr[2][2] == ("(O)"):
        print("Dators uzvarēja")
        break
    elif arr[0][2] == ("(O)") and arr[1][1] == ("(O)") and arr[2][0] == ("(O)"):
        print("Dators uzvarēja")
        break
print("Paldies par spēli!")