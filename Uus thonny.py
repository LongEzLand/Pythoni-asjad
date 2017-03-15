from random import *

check = randint(0,9)

def loto():
    number = input("Sisesta üks täisarv 0-9: ")
    if number.isdigit():
        print (check)
        number = int(number)
        if int(number) < check:
            print("Sisestatud number on väiksem, kui kontrollarv")
            loto()
        elif int(number) > check:
            print("Sisestatud number on suurem, kui kontrollarv")
            loto()
        else:
            print("Palju õnne! Minge auhinnale järgi.")
    else:
        print("numbrit taheti, sa igavene tainas")
loto()