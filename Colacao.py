import random

print("Bienvenido a mi programa ")

Num = random.randint(1, 10)

Num_us = int(input("Adivina el número entero que estoy pensando del 1 al 10 "))

if Num_us == Num:
    print("¡felicitaciones, sos una maquina!")

if Num_us != Num:
    print("Perdiste, !Intentalo de nuevo¡")

print("El numero ganador era {}" .format(Num))
