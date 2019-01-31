# -*- coding: utf-8 -*-
ponoviVajo = 'da'

print "Pozdravljeni. Sem pretvornik enot, kilometrov v milje. " \
      "\nVpiši željene kilometre in pretvoril jih bom v kilometre."

while ponoviVajo == "da":
    try:
        kilometri = float(raw_input("\nVpiši kilometre: "))
        milje = round(kilometri * 0.621371192, 1)
        print "Vpisal si" ,kilometri, " kilometrov, kar je približno ", milje," milj"
    except ValueError:
        print "Napačen vnos! Poskusi ponovno, tokrat s številko..."
    ponoviVajo = str(raw_input("Ali želiš še kaj pretvoriti? (da/ne)"))
