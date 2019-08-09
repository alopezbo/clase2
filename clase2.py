# EJEMPLO 1
#producto = input ("producto") 
#precio = float (input ("precio")) 
#IVA = precio*0.13 
#Total = precio+IVA 
#print ("El IVA es", IVA) 
#print("El total es", Total)

#Ejemplo 2
while True:
    try:
        salario=input("Digite el salario del trabajador")
        break
    except:
        print("ingrese un numero")
        patrono=salario*0.3
        trabajador=salario*0.1
        total=patrono+trabajador+salario
        print("El total de cargas sociales es",total)