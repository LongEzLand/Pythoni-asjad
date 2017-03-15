from math import ceil

pikkus = input("Sisesta pikkus tükkides: ")
laius = input("Sisesta laius tükkides: ")
k6rgus = input("Sisesta kõrgus tükkides: ")
tk_pakk = input("Mitu tükki on ühes pakis: ")

def pakke():
    tk_arv = int(pikkus)*int(laius)*int(k6rgus)
    pakk_arv = tk_arv/int(tk_pakk)
 #   print ("Sul on vaja "+str(round(pakk_arv+0.49))+" pakki")
    print ("Sul on vaja "+str(ceil(pakk_arv))+" pakki")
pakke()    