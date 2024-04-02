
"""
En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones. 
Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. 
Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.
"""
año : int; pais_a : float; pais_b : float # Se declaran las variables que se van a utilizar
año = 2022 #Se inicializan las varibles que nos dan
pais_a = 25000000
pais_b = 18900000
while (pais_a > pais_b): # El ciclo se repite hasta que el numero de habitantes del pais B sea mayor al pais A
    pais_a += (pais_a*0.02)  #En cada iteracion la poblacion crece un porcentaje
    pais_b += (pais_b*0.03)
    año +=1   #Se actualiza el año en cada iteracion
print (f"El año donde la poblacion del pais B superara a la del pais A es en el año: {año + 1}") 
"""
En el año 2051 la poblacion del pais A aun sera mayor a la del pais B. por lo cual en el 2052 la poblacion sera mayor en el año siguiente, es decir en el 2052
"""