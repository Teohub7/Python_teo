titulo = "Test sobre que color eres"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0
opcion= input("Pregunta 1: ¿Eres tímido? \n"
                "A- Casi siempre me da pena\n"
                "B- Solo algunas veces cuando estoy nervioso\n"
                "C- Claro que no, yo soy confiado")
if opcion =="A":
    puntuacion = puntuacion+0
elif opcion =="B":
    puntuacion = puntuacion+5
elif opcion =="C":
    puntuacion = puntuacion+10
else:
    print("Las únicas opciones son A,B,C")
    exit()




opcion= input("Pregunta 2: ¿Te gusta llamar la atención?\n"
                "A- No, entre menos me vean es mejor\n"
                "B- Solo con mis amigos\n"
                "C- Claro que si, entre más me vea es mejor")
if opcion =="A":
    puntuacion = puntuacion+0
elif opcion =="B":
    puntuacion = puntuacion+5
elif opcion =="C":
    puntuacion = puntuacion+10
else:
    print("Las únicas opciones son A,B,C")
    exit()





opcion= input("Pregunta 3: ¿Como es tu personalidad?\n"
                "A- Soy callado, hablo solo lo necesario\n"
                "B- Me gusta hablar solo con mis amigos\n"
                "C- Me gusta hablar con todos y hacer nuevos amigos")

if opcion =="A":
    puntuacion = puntuacion+0
elif opcion =="B":
    puntuacion = puntuacion+5
elif opcion =="C":
    puntuacion = puntuacion+10
else:
    print("Las únicas opciones son A,B,C")
    exit()

opcion= input("Pregunta 4: ¿Qué estación del año te gusta más?\n"
                "A- invierno\n"
                "B- Otoño\n"
                "C- Verano")

if opcion =="A":
    puntuacion = puntuacion+0
elif opcion =="B":
    puntuacion = puntuacion+5
elif opcion =="C":
    puntuacion = puntuacion+10
else:
    print("Las únicas opciones son A,B,C")
    exit()

opcion= input("Pregunta 5: ¿Como te gustan tus amigos?\n"
                "A- Que sean algo callados\n"
                "B- Que sean chistosos\n"
                "C- Me gustan los amigos populares y que hablen mucho")

if opcion =="A":
    puntuacion = puntuacion+0
elif opcion =="B":
    puntuacion = puntuacion+5
elif opcion =="C":
    puntuacion = puntuacion+10
else:
    print("Las únicas opciones son A,B,C")
    exit()


opcion= input("Pregunta 6: ¿Si te dieran la oportunidad de viajar a donde irias?\n"
                "A- Alemania\n"
                "B- Rusia\n"
                "C- egipto")

if opcion =="A":
    puntuacion = puntuacion+0
elif opcion =="B":
    puntuacion = puntuacion+5
elif opcion =="C":
    puntuacion = puntuacion+10
else:
    print("Las únicas opciones son A,B,C")
    exit()


opcion= input("Pregunta 7: ¿Qué paisaje te gusta más?\n"
                "A- Una montaña con nieve\n"
                "B- Una cascada o montaña\n"
                "C- Una playa")

if opcion =="A":
    puntuacion = puntuacion+0
elif opcion =="B":
    puntuacion = puntuacion+5
elif opcion =="C":
    puntuacion = puntuacion+10
else:
    print("Las únicas opciones son A,B,C")
    exit()

opcion= input("Pregunta 8: ¿Cual es tu bebida favorita?\n"
                "A- Agua de horchata\n"
                "B- Un jugo de manzana\n"
                "C- Una limonada")

if opcion =="A":
    puntuacion = puntuacion+0
elif opcion =="B":
    puntuacion = puntuacion+5
elif opcion =="C":
    puntuacion = puntuacion+10
else:
    print("Las únicas opciones son A,B,C")
    exit()


opcion= input("Pregunta 9: ¿Qué colores prefieres?\n"
                "A- Colores pastel o claros\n"
                "B- Colores rey o más fuertes\n"
                "C- Colores que se noten mucho o que sean fosforescentes")

if opcion =="A":
    puntuacion = puntuacion+0
elif opcion =="B":
    puntuacion = puntuacion+5
elif opcion =="C":
    puntuacion = puntuacion+10
else:
    print("Las únicas opciones son A,B,C")
    exit()


opcion= input("Pregunta 10: ¿Qué clima te gusta más?\n"
                "A- Frío\n"
                "B- Cálido\n"
                "C- Que haga mucho calor")

if opcion =="A":
    puntuacion = puntuacion+0
elif opcion =="B":
    puntuacion = puntuacion+5
elif opcion =="C":
    puntuacion = puntuacion+10
else:
    print("Las únicas opciones son A,B,C")
    exit()





if puntuacion >= 100:
    print("Respuesta:Tu pareces mucho de ser color amarillo")
elif puntuacion >= 50:
    print("Tu color parece ser el color rojo")
else:
    print("Tu pareces mucho de ser color blanco")


print(puntuacion)