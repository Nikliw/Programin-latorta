import random

Aleatorio = random.randint(1, 10)

while True:
    num = int(input("Ingresa un número del 1 al 10 alvr: "))

    if num == Aleatorio:
        print("Albert Ainstain adivinaste alvr")
        break
    elif num < Aleatorio:
        print("te pasaste 1000 y solo eran 10")
    else:
        print("era un numero mas del que pusiste, dedicate a otra cosa")

print("Ya ganate' quiere ma' abusadol!?") 