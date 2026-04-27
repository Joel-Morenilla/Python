DNI = int(input("Introdueix el teu DNI: ")) #demana el DNI a l'usuari
print("El teu DNI es: ", DNI) #mostra el DNI a l'usuari
preu = float(input("Introdueix el preu del producte: "))#demana el preu del producte a l'usuari
descompte = float(input("quin es el descompte en decimal: "))#demana el descompte a l'usuari
IVA = float(input("cual es el IVA en decimal: "))#demana l'IVA a l'usuari
preuambdescompte = preu - (preu * descompte / 100) #calcula el preu amb descompte
preu_final = preuambdescompte + (preuambdescompte * IVA / 100) #calcula el preu final de la compra
print("El preu final del producte es: ", preu_final) #mostra el preu final del producte a l'usuari
