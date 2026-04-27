DNI = int(input("Ingrese su DNI: ")) #pedimos el DNI
DNIrestante = DNI - int(DNI/23)*23 #sacamos el resto de dividir el DNI para encontrar la letra
modulo23 = "TRWAGMYFPDXBNJZSQVHLCKE" #de aqui sacamos la letra
print (str(DNI) + modulo23[DNIrestante]) #mostramos el dni en pantalla agregando la letra correspondiente