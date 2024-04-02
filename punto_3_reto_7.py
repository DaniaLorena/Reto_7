#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
num : int
num = int (input("Ingrese un numero natural: ")) #Se solicita un numero al usuario
i : int = 0 # Se inicializa una variable que sera el iterador 
while (num > i): #Se implementa el ciclo While, el cual se repetira siempre y cuando el numero ingresado sea mayor al iterador (i)
    if (num % 2 != 0 ): #Si aplica un condicion para evaluar si el numero es impar
        num = num - 1 #Si es impar se el resta uno para que quede un numero par
    if (num % 2 == 0): # Se verifica que cada numero sea par
        print (num) #Se imprime el numero par
    num -= 2 #El iterador debe ir cambiando restando 2, para se impriman los numero hasta 2 y no hasta 0