a = 7
b = 4
print ("A vous de jouer.")
x = int(input())
y = int(input())
if x == a and y == b :
    print("Coulé")
else:
    if x == a or y == b :
        print ("en vue")
    else :
        print("Dans l'eau")
