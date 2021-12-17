n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce un número: "))
n3 = int(input("Introduce un número: "))

print("El número más grande entre {}, {} y {} es {}, y el mas pequeño es {}" .format(n1,n2,n3,
                                                                                     max(n1,n2,n3),
                                                                                     min(n1,n2,n3)))
