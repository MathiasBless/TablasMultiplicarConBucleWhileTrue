
#Tablas de multiplicar con Bucle while true
while True:
    try:
        numero = int(input("Introduzca un número para conocer su tabla de multiplicar: "))
        
        for i in range(1, 13):
            resultado = i * numero
            print(numero, "x", i, "=", resultado)
        respuesta = input("¿Desea conocer la tabla de otro número? (si / no): ")
        print(":::::::::::::::::::::::::")
        if respuesta.lower() != 'si':
            break
    except ValueError:
        print("")
        print(".........::::::::::::::::Por favor ingrese un número de tipo entero, gracias::::::::::::::::.................")
        print("")