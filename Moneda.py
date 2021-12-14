import random
def lanzarmoneda():
    Lanzamiento = input("Numero de veces a tirar la moneda ")
    Registro = []
    cara = 0
    tails = 0
    for x in range (int(Lanzamiento)):
         giro = random.randint(0, 1)
         if (giro == 0):
              print("cara")
              Registro.append("cara")
         else:
              print("cruz")
              Registro.append("cruz")
    print(str(Registro))
    print(str(Registro.count("cara")) + str(Registro.count("cruz")))

lanzarmoneda()