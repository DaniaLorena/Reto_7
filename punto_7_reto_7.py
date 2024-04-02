num : int
num = int (input ("Ingrese  a que numero quiere sacar los divisores: ")) #Se pide un numero al ususario
i : int = 1 # Se inializa el iterador del ciclo
print (f"los divisores de {num} son: ")
while (num > i): # El ciclo While se repite siempre cuando i sea menor al numero
    if (num % i == 0): # Se implementa un condicional, en el cual se evalua el numero por todos lo numero anteriores
        print (i) # Si esto se cumple, indica que si es divisor y este se imprime
    i +=1 # Se actualiza la variable
    