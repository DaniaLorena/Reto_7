#Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
j : int = 0 # Se inicializa la varible j que se va a encargar de cambiar en el ciclo While
print ("La lista de los numeros impares del 1 hasta el 1000 es:") # Se imprime un mensaje
while(j < 1000): # j entra en el ciclo While y este se repite siempre que j sea menor a 1000
  j += 1 # La variable j se actualiza
  if (j % 2 == 0): #Se utiliza un condicional en el cual se evalua si modulo de j entre 2 es igual a cero, si esto es verdad es un numero para
    continue #Si esto es verdad, sale de la iteracion actual y continua con el ciclo
  print (j)#Se imprime j, que vendria siendo un numero impar

i : int = 0 
print ("La lista de los numeros pares del 1 hasta el 1000 es:")
while(i < 1000): 
  i += 1 
  if (i % 2 != 0): #Se evalua si el modula entre i y 2 es diferente a 0, si es verdad significa que es un numero impar
    continue # Ya que es un numero impar sale de la iteracion y continua con el ciclo
  print (i)






