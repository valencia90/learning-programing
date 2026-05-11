def dados():
    from random import randint
    dado1= randint(1,6)
    dado2= randint(1,6)
    return dado1,dado2,



print("introdusca el numero de jugadores")
num_player = int(input ())
if (num_player == 1):
    print("como minimo tienen que aver 2 juagadore")
else:
    if (num_player == 2 or num_player == 3 or num_player ==4):
        print ("escoge el nivel con su respectivo numero")
        print("1) nivel basico")
        print("2) nivel intermedio")
        print("3) nivel avanzado")
        print("4) nivel experto")
        level = int(input())
        if level == 1:
            meta=20
        if level == 2:
            meta=30
        if level == 3:
            meta=50
        else:
            level == 4
            meta=100 

posiciones=[0,0,0,0]
dobles=[0,0,0,0]
ganador = False 
 
while ganador == False:
    for i in range(num_player):
        print("\nTurno jugador", i + 1)
        dado1, dado2 = dados()
        print(f"el valor del dado1{dado1}") 
        print(f"el valor del dado2{dado2}")
        suma = dado1 + dado2
        posiciones[i] = posiciones[i] + suma
        print("la posicion es", posiciones[i])


if dado1 == dado2:
    dobles[i] = dobles[i] + 1
else:
    dobles[i] = 0


if dobles[i] == 3:
    print("Jugador", i + 1, "gana por 3 dobles")
    ganador = True


if posiciones[i] >= meta:
    print("Jugador", i + 1, "gano la carrera")
    ganador = True