import random

choices = ["kő", "papír", "olló"]
machine_choice = random.choice(choices)
gyozelem = 0
vereseg = 0
dontetlen = 0
jatek = True
print("Üdvözöllek! Ez itt a Kő, Papír, Olló játék!")
while jatek == True:
    jatekos = input("Kérlek válassz, Kő, papír, olló? ")
    print(f"A választásod: {jatekos}")
    print(f"A gép választása: {machine_choice}")
    if machine_choice == jatekos:
        print("Döntetlen")
        dontetlen += 1
    elif machine_choice == "kő" and jatekos == "papír":
        print("Győzelem!")
        gyozelem += 1
    elif machine_choice == "kő" and jatekos == "olló":
        print("Vereség")
        vereseg += 1
    elif machine_choice == "papír" and jatekos == "olló":
        print("Győzelem!")
        gyozelem += 1
    elif machine_choice == "papír" and jatekos == "kő":
        print("Vereség!")
        vereseg += 1
    elif machine_choice == "olló" and jatekos == "kő":
        print("Győzelem!")
        gyozelem += 1
    elif machine_choice == "olló" and jatekos == "papír":
        print("Vereség!")
        vereseg += 1
    print(f"Győzelem: {gyozelem}\nVereség: {vereseg}\nDöntetlen: {dontetlen}")
        
    again = input("Akarsz még játszani? (i/n) ")
    if again == "n":
        jatek = False
        print("Játék vége!")
        break
    elif again == "i":
        continue
    else:
        print("Csak i/n válasz elfogadott!")