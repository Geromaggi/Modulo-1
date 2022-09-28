import random


class JuegoCartas:
    def __init__(self):
        self.__numero_elegido = int(input("Ingrese un numero: "))
    def juego(self):
        numeros_aleatorios = []
        #creacion de lista de numeros enteros aleatorios.
        numeros_aleatorios = random.sample(range(21),20)
        print(numeros_aleatorios)

        #creacion de list de numeros que SACAMOS.
        numeros_sacados = []
        #agregamos en una lista la cantidad de numeros elegidos
        for i in range (0,self.__numero_elegido):
            numero_escogido = numeros_aleatorios[i]
            numeros_sacados.append(numero_escogido)
        #sumaos cuanto da la lista de los elementos sacados
        suma_sacados = sum(numeros_sacados)
        print(numeros_sacados)
        print(suma_sacados)
        #verificamos si el usuario gano o no.
        if suma_sacados > 50:
            print("la suma de las cartas que elegio es de:",suma_sacados,'. Has perdido, suerte la proxima!')
        else: 
            cantidad_restante = 50 - suma_sacados
            #print(cantidad_restante)
            rango_final = self.__numero_elegido + cantidad_restante
            #print(rango_final)
            lista_final = []
            for j in range (self.__numero_elegido, rango_final):
                numero_escogido1 = numeros_aleatorios[j]
                lista_final.append(numero_escogido1)
                numeros_sacados.append(numero_escogido1)
            #print(lista_final)
            suma_final = sum(lista_final)

            print('Usted ha ganado con un total de:',suma_final)
        
nuevo_juego = JuegoCartas()
nuevo_juego.juego()

