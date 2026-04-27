import random 
maquina = random.randrange (1, 11)
usuario = 0
for i in range (3):
    usuario = int(input("Adivina el numero entre 1 y 10: "))
    if usuario < maquina:
        print("Demasiado bajo")
    elif usuario > maquina:
        print("Demasiado alto")
    else:
        print("¡Correcto!")

        if usuario == maquina:
            break
