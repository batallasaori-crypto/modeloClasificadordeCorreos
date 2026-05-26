#1. NUESTROS DATOS (mensajes de prueba)

correo_nuevos = [

"Hola, ¿vamos por unos tacos saliedo de la escuela "

"¡URGENTE! Gana dinero rapido desde casa dando un olio ya"

"Recuerda que mañana es el examen de inteligencia artificial"

"Felidades, ganaste un premio gratis, da clic ya"

#2. NUESTRO MODELO (Entrenamiento/Reclas)
#El modelo "aprende" qe estas palabras suelen ser

palabras_spam = ["Gratis", "ganaste", "clic", "dinero",

def modelo_ia_filtro(correo):

    #convertimos a minusculas para que no efecten las

    correo_minuscula = correo.lower()

    #El modelo busca si alguna palabra sospechosa esta 
    for palabra in list(palabras_spam):
    if palabra in correo_minuscula:
        return "SPAM" # prediccioon 1

return "CORREO DESEADO" #Prediccion 2

#3 EVALUACCION Y PREDICCIÓN

print("----EJERCUTANDO NUESTRA IA---")

for 1, correo in enumerte (correos_nuevos, 1):
    predicion = modelo_ia_filtro(correo_nuevos, 1):
    print(f"Correo (1): '{correo)' -> PREDICCION DE LA IA
