titulo = "Descubre qué pokemon eres"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta  1: Con cual pokemon te identificas más?\n"
              "A- pikachu\n"
              "B- charmander\n"
              "C- Bulbasaur\n"
               "          Tu respuesta es: ")

if opcion == "A":
    puntuacion += 5
elif opcion == "B":
    puntuacion += 10
elif opcion == "C":
    puntuacion += 15
else:
    print("Las unicas respuestas son A, B y C.")
    exit()

    #Esta es la segunda pregunta

opcion = input("Pregunta  2: Con cual pokemon cogerias más?\n"
              "A- pikachu\n"
              "B- charmander\n"
              "C- Bulbasaur\n"
               "          Tu respuesta es: ")

if opcion == "A":
    puntuacion += 5
elif opcion == "B":
    puntuacion += 10
elif opcion == "C":
    puntuacion += 15
else:
    print("Las unicas respuestas son A, B y C.")
    exit()

if puntuacion >= 30:
    print("usted es una perra")
elif puntuacion >= 20:
    print("usted es una perrita")
elif puntuacion >= 10:
    print("usted es una mini zorra")
