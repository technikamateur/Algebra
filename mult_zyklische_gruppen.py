#!/usr/bin/python3
# -*- coding: utf-8 -*-
def checker(zuPrüfen, dieZahl):
	x = -1
	count = 1
	while (x != zuPrüfen):
		count = count + 1
		if (count == dieZahl):
			break
		if (x == -1):
			x = zuPrüfen
		x = x * zuPrüfen
		if (x > dieZahl):
			x = x % dieZahl
	if (x == zuPrüfen or x == 0):
		return(False)
	else:
		return(True)
		


zahlen = []
erg = []
zahl = int(input("Max. Zahl eingeben: "))
alleZahlen = input("Auch Zhalen von 0 bis deine Zahl (j für ja)? ")
if (alleZahlen == "j"):
	for i in range(1, zahl):
		zahlen.append(i)
else:
	zahlen.append((zahl - 1))

for element in zahlen:
	if checker(element, zahl):
		erg.append(element)

print(erg)