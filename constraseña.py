import secrets
import string
import sys

diccionario = {
    'letras': string.ascii_letters,
    'numeros': string.digits,
    'caracteres': string.punctuation
}

print(""" 
    ################################### 
      
       Generador de Contraseña V0.1
      
    ################################### 
""")

while True:
    print("Seleccione una de las siguientes opciones:\n")
    print(">> 1. Generar contraseña solo con letras")
    print(">> 2. Generar contraseña solo con números")
    print(">> 3. Generar contraseñas solo con letras y números")
    print(">> 4. Generar contraseñas solo con letras, números y caracteres")
    print(">> 0. Salir \n")
    
    opcion = input(">> Escriba la opción seleccionada:\n")
    
    if opcion == '1':
        tipo = diccionario['letras']
    elif opcion == '2':
        tipo = diccionario['numeros']
    elif opcion == '3':
        tipo = diccionario['letras'] + diccionario['numeros']
    elif opcion == '4':
        tipo = diccionario['letras'] + diccionario['numeros'] + diccionario['caracteres']
    elif opcion == '0':
        break
    else:
        print("Opción no válida. Intente de nuevo.")
        continue
    
    contrasena = ''.join(secrets.choice(tipo) for i in range(10))
    
    print("Tu nueva contraseña es:", contrasena)
