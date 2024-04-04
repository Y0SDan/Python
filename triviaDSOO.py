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
        "¿Qué diferencia a OpenUP del Proceso Unificado (RUP)?",
        "¿Cuáles son las fases del Proceso Unificado (RUP)?",
        "¿En qué se basa el método iterativo de Craig Larman?",
        "¿Qué es una de las mejores prácticas en el desarrollo de software según el Proceso Unificado?",
        "¿Qué son los \"roles\" en el Proceso Unificado?",
        "¿Qué son las \"actividades\" en el Proceso Unificado?",
        "¿Qué son los \"artefactos\" en el Proceso Unificado?",
        "¿Qué son los \"flujos de trabajo\" en el Proceso Unificado?",
        "¿Cuál es la principal diferencia entre un ciclo de vida iterativo e incremental y un ciclo de vida lineal?",
        "¿Qué es un caso de uso?",
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
        ["OpenUP no utiliza flujos de trabajo ni fases.","OpenUP no es iterativo ni incremental.","OpenUP no se enfoca en casos de uso.","OpenUP es más flexible y adaptable a diferentes tipos de proyectos."],
        ["Inicio, Planificación, Ejecución y Cierre.","Inicio, Elaboración, Construcción y Transición.","Diseño, Implementación, Pruebas y Despliegue.","Requerimientos, Análisis, Diseño y Desarrollo."],
        ["En el modelo Waterfall.", "En el Proceso Unificado (RUP).", "En el modelo XP (Extreme Programming).", "En el modelo Scrum."],
        ["Desarrollo lineal y secuencial.", "No involucrar al usuario en la gestión de requisitos.", "Implementar una arquitectura rígida y sin flexibilidad.", "Verificación constante de la calidad del software."],
        ["Los diferentes tipos de software que se pueden desarrollar.", "Las herramientas utilizadas en el desarrollo de software.", "Los diferentes tipos de participantes en un proyecto de software y sus responsabilidades.", "Las diferentes etapas del ciclo de vida del software."],
        ["Los diferentes tipos de documentos que se generan en un proyecto de software.", "Las diferentes herramientas utilizadas en el desarrollo de software.", "Las tareas que se realizan dentro de un proyecto de software.", "Los diferentes tipos de pruebas que se realizan al software."],
        ["Las diferentes metodologías de desarrollo de software.", "Los diferentes tipos de riesgos que se pueden presentar en un proyecto de software.", "Los productos tangibles que se generan en un proyecto de software.", "Las diferentes métricas utilizadas para medir el avance de un proyecto de software."],
        ["La secuencia en la que se realizan las actividades en un proyecto de software.", "Las diferentes áreas de responsabilidad en un proyecto de software.", "Las diferentes herramientas utilizadas en el desarrollo de software.", "Los diferentes tipos de pruebas que se realizan al software."],
        ["En el ciclo de vida iterativo e incremental, el software se desarrolla en una sola fase.", "En el ciclo de vida lineal, el software se desarrolla en una sola iteración.", "En el ciclo de vida iterativo e incremental, el software se desarrolla en pequeñas partes y se mejora con cada iteración.", "En el ciclo de vida lineal, el software se desarrolla de forma completa antes de pasar a la siguiente fase."],
        ["Una herramienta para la gestión de requisitos.", "Un tipo de diagrama utilizado en el modelado de software.", "Una descripción de cómo un usuario interactúa con el software para lograr un objetivo específico.", "Un tipo de prueba que se realiza al software."],
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
        "OpenUP es más flexible y adaptable a diferentes tipos de proyectos.",
        "Inicio, Elaboración, Construcción y Transición.",
        "En el Proceso Unificado (RUP).",
        "Verificación constante de la calidad del software.",
        "Los diferentes tipos de participantes en un proyecto de software y sus responsabilidades.",
        "Las tareas que se realizan dentro de un proyecto de software.",
        "Los productos tangibles que se generan en un proyecto de software.",
        "Las diferentes áreas de responsabilidad en un proyecto de software.",
        "En el ciclo de vida iterativo e incremental, el software se desarrolla en pequeñas partes y se mejora con cada iteración.",
        "Una descripción de cómo un usuario interactúa con el software para lograr un objetivo específico.",
    ]

    # Mezclamos las preguntas y respuestas
    #random.shuffle(preguntas)
    #random.shuffle(opciones)

    # Inicializamos las variables
    puntuacion = 0
    respuestas_usuario = []

    print()
    print("\033[94m **Bienvenido a la trivia de Desarrollo de Software Orientado a Objetos**\n   by Richi :p \033[0m")
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