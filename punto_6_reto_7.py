import random  #Se importa la libreria random para que el python genere un elemento al asar en un rango establecido

num_aleatorio : int; num_2 : int; oportunidad : int = 0 # Se declaran e incializan las variables
num_aleatorio = random.randrange (1,100) # devuelve un elemento aleatorio extraído de la secuencia de números enteros generada por range
num_1 = int ( input ("Ingrese el numero: ")) # Permite ingresar un numero para intentar adivinar el numero
while ( num_aleatorio != num_1): #El ciclo se repite siempre que el numero aleatorio sea diferente al numero ingresado
    if (num_aleatorio > num_1): # Se implementa un incondicional para evaluar si el numero ingresado es mayor o menor al numero aleatorio
        print ( "El numero a adivinar es  mayor")
        num_1 = int ( input ("Ingrese nuevamente un otro numero: "))
    else:
        print ( "El numero a adivinar es  menor")
        num_1 = int ( input ("Ingrese nuevamente otro el numero: ")) #Se muestran los mensajes correspondientes
    oportunidad += 1 #Se actualiza el numero de intentos que se ha hecho
print (f"Excelente, Has adivinado el numero que era {num_aleatorio} en {oportunidad} oportunidades")

