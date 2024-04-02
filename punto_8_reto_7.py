#Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones
#Se crea una funcion para verificar si un numerp es primo o no
def evaluar_numero (num : int, i : int = 2 ): #i Se inicializa en 2, para que pueda entrar al ciclo While
    while (i <= (num**1/2)): #se implementa el ciclo While, se repite siempre y cuando i sea menor o igual a la raiz del numero
        if (num % i == 0): #Se aplica un condicional, donde retorna False si el modulo entre el numero y i es igual a cero
            return False
        i +=1 #Se actuliza la variable i aumentando 1 cada vez que pasa por el ciclo
    return True #Retorna True cuando el numero es primo

num : int = 0 #Se inicializa la variable num en 1 para estar seguros que entre en el ciclo While, y que empiece desde 1
if __name__ == "__main__": #funcion principal
    while (num <= 100): #Este ciclo while se repite siempre y cuando num sea menor o igual a 100
        if (evaluar_numero(num) == True): # Se implementa la funcion evaluar_numero para verificar cada numero del 1 al 100
            print (num)#Si la funcion es igual a True se imprime el numero primo.
            num +=1 #Se actualiza la variable num sumando 1
        else: #Si la funcion no es igual a True simplementeo se le actualiza num, sumando 1
            num +=1

