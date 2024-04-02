num : int; fac : int, i: int #Se declaran las variables a utilizar
num = int (input ("¿A que numero le quiere sacar el factorial?: ")) # Se le pide un numero al usuario
i : int = 1 #Se incializan las variables
fac : int = 1
while (i<=num): #El ciclo While se repite siempre que el iterador (i) sea menor al numero ingresado
    fac *= i # Se actuliza el valor de fac, multiplicando todos lo numero anteriores a este
    i+=1 #Se actualiza el iterador
print (f"El numero factorial de {num} es {fac}")