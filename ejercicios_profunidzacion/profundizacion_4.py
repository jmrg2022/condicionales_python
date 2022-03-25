# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

# ingreso de palabras (3)

palabra_1 = input('Ingrese la primera palabra:')

palabra_2 = input('Ingrese la segunda palabra:')

palabra_3 = input('Ingrese la tercer palabra:')

metodo_orden = int(input('Ingrese el método de ordenación (1/2)'))

# ordenamiento alfabético

if metodo_orden == 1:
    if (palabra_1 < palabra_2) and (palabra_1 < palabra_3):
        print('Primera Palabra:',palabra_1)
        if (palabra_2 < palabra_3):
            print('Segunda Palabra:',palabra_2)
            print('Tercer Palabra:',palabra_3)
        else:
            print('Segunda Palabra:',palabra_3)
            print('Tercer Palabra:',palabra_2)
    elif (palabra_2 < palabra_1) and (palabra_2 < palabra_3):
        print('Primera Palabra:',palabra_2)
        if (palabra_1 < palabra_3):
            print('Segunda Palabra:',palabra_1)
            print('Tercer Palabra:',palabra_3)
        else:
            print('Segunda Palabra:',palabra_3)
            print('Tercer Palabra:',palabra_1)
    elif (palabra_3 < palabra_1) and (palabra_3 < palabra_2):
        print('Primera Palabra:',palabra_3)
        if (palabra_1 < palabra_2):
            print('Segunda Palabra:',palabra_1)
            print('Tercer Palabra:',palabra_2)
        else:
            print('Segunda Palabra:',palabra_2)
            print('Tercer Palabra:',palabra_1)

# ordenamiento por cantidad de letras de palabras

cant_letras_palabra_1 = len(palabra_1)
cant_letras_palabra_2 = len(palabra_2)
cant_letras_palabra_3 = len(palabra_3)

if metodo_orden == 2:
    if (cant_letras_palabra_1 < cant_letras_palabra_2) and (cant_letras_palabra_1 < cant_letras_palabra_3):
        print('Primera Palabra:',palabra_1)
        if (cant_letras_palabra_2 < cant_letras_palabra_3):
            print('Segunda Palabra:',palabra_2)
            print('Tercer Palabra:',palabra_3)
        else:
            print('Segunda Palabra:',palabra_3)
            print('Tercer Palabra:',palabra_2)
    elif (cant_letras_palabra_2 < cant_letras_palabra_1) and (cant_letras_palabra_2 < cant_letras_palabra_3):
        print('Primera Palabra:',palabra_2)
        if (cant_letras_palabra_1 < cant_letras_palabra_3):
            print('Segunda Palabra:',palabra_1)
            print('Tercer Palabra:',palabra_3)
        else:
            print('Segunda Palabra:',palabra_3)
            print('Tercer Palabra:',palabra_1)
    elif (cant_letras_palabra_3 < cant_letras_palabra_1) and (cant_letras_palabra_3 < cant_letras_palabra_2):
        print('Primera Palabra:',palabra_3)
        if (cant_letras_palabra_1 < cant_letras_palabra_2):
            print('Segunda Palabra:',palabra_1)
            print('Tercer Palabra:',palabra_2)
        else:
            print('Segunda Palabra:',palabra_2)
            print('Tercer Palabra:',palabra_1)