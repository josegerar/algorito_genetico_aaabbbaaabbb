import random

from funciones import *


def main():
    patron = ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B']
    cantidad_poblacion = 10
    largo_genetico = len(patron)
    punto_cruce = 0.8
    punto_mutacion = 0.05
    cantidad_seleccion = int(cantidad_poblacion / 3)
    cantidad_generaciones = 100
    modelo = format_model(model=patron)
    minimo = min(modelo)
    maximo = max(modelo)

    poblacion = generate_poblacion(min=minimo, max=maximo, largo_genetico=largo_genetico,
                                   largo_poblacion=cantidad_poblacion)

    print("Poblacion inicial: {}".format(poblacion))

    for i in range(cantidad_generaciones):
        mejores_seleccionados = seleccion(poblacion=poblacion, modelo=modelo, cantidad_seleccion=cantidad_seleccion)

        nueva_generacion = cruce_probabilistico(mejores_padres=mejores_seleccionados, largo_genetico=largo_genetico,
                                                cantidad_poblacion=cantidad_poblacion, probabilidad=punto_cruce)

        nueva_generacion_mutada = mutacion_binaria(nueva_generacion=nueva_generacion, largo_genetico=largo_genetico,
                                                   probabilidad=punto_mutacion)

        poblacion = nueva_generacion_mutada

    print("Poblacion evolucionada: {}".format(poblacion))

    _mejor_individuo = mejor_individuo(poblacion, modelo)
    print("Mejor idividuo: {}".format(_mejor_individuo))

    _mejor_individuo = [chr(_mejor_individuo[i]) for i in range(len(_mejor_individuo))]
    print("Mejor idividuo: {}".format(_mejor_individuo))


if __name__ == '__main__':
    main()
