a = int(input("Dime un numero: ")) #Pide el primer numero al usuario
b = int(input("Dime otro numero: ")) #Pide el segundo numero al usuario
operacion = input("Dime la operacion que quieres hacer (+, -, *, /, %): ") #Pide la operacion al usuario
if operacion == "+": #Si la operacion es suma
    print("El resultado es: ", a + b) #Muestra el resultado de la suma
if operacion == "-": #Si la operacion es restar
    print("El resultado es: ", a - b) #Muestra el resultado de la resta
if operacion == "*": #Si la operacion es multiplicar
    print("El resultado es: ", a * b) #Muestra el resultado de la multiplicacion
if operacion == "/": #Si la operacion es dividir
    if b != 0: #Si el segundo numero no es 0
        print("El resultado es: ", a / b) #Muestra el resultado de la division
    else: #Si el segundo numero es 0
        print("No se puede dividir entre 0") #Muestra un mensaje de error
if operacion == "%": #Si la operacion es el resto
    if b != 0: #Si el segundo numero no es 0
        print("El resultado es: ", a % b) #Muestra el resultado del resto
    else: #Si el segundo numero es 0
        print("No se puede dividir entre 0") #Muestra un mensaje de error