# Importamos las librerías necesarias
import random

def main():

    # Definimos las preguntas y respuestas
    preguntas = [
        "¿Qué se necesita para desarrollar un producto o software?",
        "¿Qué define un proceso?",
        "¿El proceso de desarrollo de software?",
        "¿Cuáles son las actividades del Proceso de Desarrollo de Software?",
        "¿Cuáles son los roles en el Proceso de Desarrollo de Software?",
        "¿Qué es UML?",
        "¿Cuál es el propósito del modelado visual con UML?",
        "¿Qué representa el límite de Miller en el contexto de UML?",
        "¿Para qué se utiliza UML en el desarrollo de software?",
    ]

    opciones = [
        ["Personas", "Proyecto", "Proceso", "Producto", "Todas las anteriores"],
        ["Quién hace qué, cuándo lo hace y cómo lograr el objetivo.", "Los artefactos que se crean en la vida del proyecto.", "Las actividades que se realizan para convertir las peticiones del usuario en el producto.", "Proporcionar una guía del orden de las actividades de los equipos."],
        ["No requiere los requerimientos del usuario.", "Requiere los requerimientos del usuario para generar un producto de software.", "Es independiente de las necesidades del usuario.", "Solo se aplica a software complejo."],
        ["Comunicación, Planeación, Modelado, Construcción, Despliegue.", "Diseño, Implementación, Pruebas, Mantenimiento.", "Análisis, Requerimientos, Diseño, Codificación.", "Todas las anteriores."],
        ["Gerente de proyecto, Arquitecto de software, Desarrollador, Tester.", "Cliente, Usuario final, Analista de negocios.", "Scrum Master, Product Owner, Equipo de desarrollo.", "Todas las anteriores."],
        ["Un método de desarrollo de software.", "Un lenguaje gráfico para visualizar y documentar el desarrollo de software.", "Una técnica de programación orientada a objetos.", "Un proceso de gestión de proyectos."],
        ["Simplificar la realidad mediante abstracción y notación gráfica.", "Crear una base de datos compleja.", "Programar aplicaciones en varios lenguajes de programación.", "Desarrollar interfaces de usuario interactivas."],
        ["El número máximo de objetos que se pueden modelar.", "La capacidad máxima de procesamiento de un sistema de software.", "Una técnica para reducir la complejidad de los sistemas de software.", "El número de diagramas que se pueden utilizar en un proyecto."],
        ["Para definir los requerimientos del usuario y generar un producto de software.", "Para desplegar los límites del sistema y modelar su estructura y comportamiento.", "Para programar directamente el código fuente del software.", "Para realizar pruebas de software y garantizar su calidad."],
    ]

    respuestas_correctas = [
        "Todas las anteriores",
        "Quién hace qué, cuándo lo hace y cómo lograr el objetivo.",
        "Requiere los requerimientos del usuario para generar un producto de software.",
        "Comunicación, Planeación, Modelado, Construcción, Despliegue.",
        "Todas las anteriores.",
        "Un lenguaje gráfico para visualizar y documentar el desarrollo de software.",
        "Simplificar la realidad mediante abstracción y notación gráfica.",
        "Una técnica para reducir la complejidad de los sistemas de software.",
        "Para desplegar los límites del sistema y modelar su estructura y comportamiento.",
    ]

    # Mezclamos las preguntas y respuestas
    #random.shuffle(preguntas)
    #random.shuffle(opciones)

    # Inicializamos las variables
    puntuacion = 0
    respuestas_usuario = []

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
        print("¡Hasta la próxima!")

# Llamamos a la función main para iniciar el juego
main()