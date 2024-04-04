# Importamos las librerías necesarias
import random

def main():

    # Definimos las preguntas y respuestas
    preguntas = [
        "¿Qué es el análisis orientado a objetos?",
        "¿Qué es el diseño orientado a objetos?",
        "¿Cuál es la finalidad del modelo del dominio?",
        "¿Qué tipo de diagrama se utiliza para visualizar los conceptos del dominio del mundo real?",
        "¿Cuál es la finalidad del diseño orientado a objetos?",
        "¿Qué tipo de diagrama ilustra las colaboraciones entre los objetos software?",
        "¿Qué tipo de diagrama muestra una vista estática de las definiciones de las clases?",
        "¿Cómo se relaciona el diagrama de interacción con el diagrama de clases de diseño?",
        "¿Qué es el análisis en el contexto de desarrollo de software?",
        "¿Qué es el diseño en el contexto de desarrollo de software?",
        "¿Qué implica la construcción de sistemas software?",
        "¿Qué se representa en un caso de uso?",
        "¿Qué es un diagrama de interacción?",
        "¿Qué es un objeto software en el diseño orientado a objetos?",
        "¿Qué es un diagrama de clases de diseño?",
        "¿Qué es un modelo del dominio en el análisis orientado a objetos?",
    ]

    opciones = [
        [
            "Encontrar y describir los objetos/conceptos en el dominio del problema.",
            "Desarrollar diagramas de flujo de datos.",
            "Definir la base de datos del sistema.",
            "Implementar la lógica de negocio.",
        ],
        [
            "Definir los objetos software y cómo colaboran para satisfacer los requisitos.",
            "Diseñar la interfaz gráfica del usuario.",
            "Seleccionar el lenguaje de programación.",
            "Definir la arquitectura del sistema.",
        ],
        [
            "Crear una descripción del dominio desde la perspectiva de la clasificación de objetos.",
            "Definir la arquitectura del sistema.",
            "Diseñar la interfaz de usuario.",
            "Implementar la lógica de negocio.",
        ],
        [
            "Diagrama de flujo de datos.",
            "Diagrama de casos de uso.",
            "Diagrama de clases de dominio.",
            "Diagrama de secuencia.",
        ],
        [
            "Definir los objetos software y sus colaboraciones.",
            "Diseñar la interfaz gráfica del usuario.",
            "Seleccionar el lenguaje de programación.",
            "Definir la arquitectura del sistema.",
        ],
        [
            "Diagrama de clases.",
            "Diagrama de secuencia.",
            "Diagrama de interacción.",
            "Diagrama de estado.",
        ],
        [
            "Diagrama de flujo de datos.",
            "Diagrama de casos de uso.",
            "Diagrama de actividad.",
            "Diagrama de clases de diseño.",
        ],
        [
            "El diagrama de interacción define los métodos necesarios para las clases del diagrama de clases de diseño.",
            "El diagrama de clases de diseño define la estructura de las clases del diagrama de interacción.",
            "Ambos diagramas son independientes entre sí.",
            "No hay relación entre ambos diagramas.",
        ],
        [
            "Una investigación del problema.",
            "Identificar los requerimientos que resuelven el problema.",
            "Ambas a y b son correctas.",
            "Ninguna de las anteriores.",
        ],
        [
            "Solución conceptual que satisface los requisitos.",
            "No implementación.",
            "Ambas a y b son correctas.",
            "Ninguna de las anteriores.",
        ],
        [
            "Va a poder ser planificable y repetible.",
            "Obtienes un sistema de mejor calidad al final.",
            "Ambas a y b son correctas.",
            "Ninguna de las anteriores.",
        ],
        [
            "Una descripción de los procesos del dominio relacionados.",
            "Historias escritas, no son artefactos orientados a objetos.",
            "Ambas a y b son correctas.",
            "Ninguna de las anteriores.",
        ],
        [
            "Es una visualización de los conceptos en el dominio del mundo real.",
            "Muestra el flujo de mensajes entre los objetos software y la invocación de métodos.",
            "Es una descripción del dominio desde la perspectiva de la clasificación de objetos.",
            "Ninguna de las anteriores.",
        ],
        [
            "Es una descripción del dominio desde la perspectiva de la clasificación de objetos.",
            "Es la definición de los objetos que colaboran para satisfacer los requisitos.",
            "Es un diagrama que muestra el flujo de mensajes entre los objetos software.",
            "Ninguna de las anteriores.",
        ],
        [
            "Muestra el flujo de mensajes entre los objetos software y la invocación de métodos.",
            "Es una vista estática de las definiciones de las clases.",
            "Es una visualización de los conceptos en el dominio del mundo real.",
            "Ninguna de las anteriores.",
        ],
        [
            "Es una descripción del dominio desde la perspectiva de la clasificación de objetos.",
            "Es un diagrama que muestra el flujo de mensajes entre los objetos software.",
            "Es una vista estática de las definiciones de las clases.",
            "Ninguna de las anteriores.",
        ],
    ]


    respuestas_correctas = [
        "Encontrar y describir los objetos/conceptos en el dominio del problema.",
        "Definir los objetos software y cómo colaboran para satisfacer los requisitos.",
        "Crear una descripción del dominio desde la perspectiva de la clasificación de objetos.",
        "Diagrama de clases de dominio.",
        "Definir los objetos software y sus colaboraciones.",
        "Diagrama de interacción.",
        "Diagrama de clases de diseño.",
        "El diagrama de clases de diseño define la estructura de las clases del diagrama de interacción.",
        "Ambas a y b son correctas.",
        "Ambas a y b son correctas.",
        "Ambas a y b son correctas.",
        "Ambas a y b son correctas.",
        "Muestra el flujo de mensajes entre los objetos software y la invocación de métodos.",
        "Es la definición de los objetos que colaboran para satisfacer los requisitos.",
        "Muestra el flujo de mensajes entre los objetos software y la invocación de métodos.",
        "Es una descripción del dominio desde la perspectiva de la clasificación de objetos.",
    ]


    # Mezclamos las preguntas y respuestas
    #random.shuffle(preguntas)
    #random.shuffle(opciones)

    # Inicializamos las variables
    puntuacion = 0
    respuestas_usuario = []

    print()
    print("\033[94m **Bienvenido a la trivia de Desarrollo de Software Orientado a Objetos #2**\n   by Richi :p \033[0m")
    print()

    # Bucle para recorrer las preguntas
    for i in range(len(preguntas)):
        print(f"Pregunta {i + 1}: {preguntas[i]}")
        for j in range(len(opciones[i])):
            print(f"{j + 1}: {opciones[i][j]}")

        # Pedimos la respuesta del usuario
        respuesta_usuario = input("Introduce tu respuesta (número): ")

        # Validamos la respuesta del usuario
        while not respuesta_usuario.isdigit() or int(respuesta_usuario) < 1 or int(respuesta_usuario) > len(opciones[i]):
            respuesta_usuario = input("Respuesta inválida. Introduce tu respuesta (número): ")

        # Guardamos la respuesta del usuario
        respuestas_usuario.append(opciones[i][int(respuesta_usuario) - 1])

        # Comprobamos si la respuesta es correcta
        if respuestas_usuario[i] == respuestas_correctas[i]:
            puntuacion += 1
            print()
            print("¡¡Tu respuesta es correcta!!")
        else:
            print()
            print(f"¡¡Tu respuesta es incorrecta!!\nLa respuesta correcta es: {respuestas_correctas[i]}")

        print()        

    # Mostramos los resultados
    print("**Resultados:**")
    print(f"Has acertado {puntuacion} preguntas.")
    print()

    # Mostramos un mensaje final
    if puntuacion == len(preguntas):
        print("¡Felicidades! Has acertado todas las preguntas.")
    elif puntuacion > len(preguntas) / 2:
        print("¡Buen trabajo! Has acertado la mayoría de las preguntas.")
    else:
        print("Puedes seguir estudiando para mejorar tus resultados.")

    # Preguntamos si el usuario quiere jugar de nuevo
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no): ")

    # Si el usuario quiere jugar de nuevo, reiniciamos el programa
    if jugar_de_nuevo.lower() == "si":
        print()
        main()

    # Si el usuario no quiere jugar de nuevo, terminamos el programa
    else:
        print()
        print(" \033[92m ¡Buena suerte en tu exámen! \033[0m")

# Llamamos a la función main para iniciar el juego
main()