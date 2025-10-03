import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena):
    cadena = cadena.lower().strip()
    res = ""
    for i in cadena:
        if i == ("á" or "ä"):
            res += "a"
        elif i == ("é" or "ë"):
            res += "e"
        elif i == ("í" or "ï"):
            res += "i"
        elif i == ("ó" or "ö"):
            res += "o"
        elif i == ("ú" or "ü"):
            res += "u"
        else:
            res += i
    cadena = res
    return cadena

def ocultar(palabra_secreta, letras_usadas=""):
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    palabra_enmascarada = ""
    for j in palabra_secreta:
        if j in letras_usadas:
            palabra_enmascarada += j
        else:
            palabra_enmascarada += "_"
    return palabra_enmascarada


def ha_ganado(palabra_enmascarada):

    if "_" not in palabra_enmascarada:
        return True
    else:
        return False
    
def mostrar_estado(palabra_enmascarada,letras_usadas,intentos_restantes):
    print(f"Estado:","".join(palabra_enmascarada))
    if len(letras_usadas)>=1:
        print(f"Letras usadas: {letras_usadas}")
    else:
        print(f"Letras usadas: ninguna")
    print(f"Intentos: {intentos_restantes}")


def pedir_letra(letras_usadas):
    letra= str(input("Introduce una letra:"))
    while True:
        if letra not in "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM":
            str(input("Debes introducir una letra:"))
        elif len(letra) != 1:
            str(input("Debes introducir una única letra"))
        elif letra in letras_usadas :
            str(input("Esa letra ya la has usado anteriormente"))
        else:
            break
    
    return letra.lower()


def jugar(palabra_secreta):

    intentos_restantes = 6
    letras_usadas= ""
    normalizar(palabra_secreta)
    if len(palabra_secreta)<0:
        return None
    palabra_enmascarada= ocultar(palabra_secreta)
    while intentos_restantes > 0  and ha_ganado(palabra_enmascarada) == False:
        mostrar_estado(palabra_enmascarada,letras_usadas,intentos_restantes)
        letra_nueva= pedir_letra(letras_usadas)
        letras_usadas += str(letra_nueva)
        if letra_nueva not in palabra_secreta:
            intentos_restantes -= 1
            print(f"La letra recibida no pertenece a la palabra secreta, tines{intentos_restantes}intentos")

        else:
            
            print("Has acertado")
            palabra_enmascarada= ocultar(palabra_secreta,letras_usadas)
    if intentos_restantes> 0:
        print(f"Has perdido, la palabra original era:{palabra_secreta}")
    if ha_ganado(palabra_enmascarada) == True:
       print("Enhorabuena, has ganado")




jugar(elige_palabra())
