import random

from funciones import *


def main():
    """patron resultante"""
    patron = ['A', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'B']
    """poblacion de estudio"""
    cantidad_poblacion = 10
    """cantidad de genes de cada individuo"""
    largo_genetico = len(patron)
    """punto para hacer el cruce de genes"""
    punto_cruce = 0.8
    """punto en que es posible mutar los genes"""
    punto_mutacion = 0.05
    """cantidad de individuos que van a seleccionarse en la fase de seleccion por torneo"""
    cantidad_seleccion = round(cantidad_poblacion / 3)
    """cantidad de generaraciones que van a ser estudiadas"""
    cantidad_generaciones = 200
    """convertir modelo a numeros equivalentes"""
    modelo = format_model(model=patron)
    """valor minimo a estudiar"""
    minimo = min(modelo)
    """valor maximo a estudiar"""
    maximo = max(modelo)

    """poblacion inicial de estudio"""
    poblacion = generate_poblacion(min=minimo, max=maximo, largo_genetico=largo_genetico,
                                   largo_poblacion=cantidad_poblacion)

    print("Poblacion inicial: {}".format(poblacion))

    for i in range(cantidad_generaciones):
        """fase de seleccion"""
        mejores_padres_seleccionados = seleccion(poblacion=poblacion, modelo=modelo,
                                                 cantidad_seleccion=cantidad_seleccion)

        """establecemos el tipo de cruce que realizaremos"""
        # nueva_generacion = cruce_probabilistico(mejores_padres=mejores_padres_seleccionados,
        #                                         largo_genetico=largo_genetico,
        #                                         cantidad_poblacion=cantidad_poblacion, probabilidad=punto_cruce)
        nueva_generacion = cruce_por_dos_puntos(mejores_padres=mejores_padres_seleccionados,
                                                largo_genetico=largo_genetico,
                                                cantidad_poblacion=cantidad_poblacion)

        """proceso de mutacion"""
        nueva_generacion_mutada = mutacion_por_permutacion(nueva_generacion=nueva_generacion,
                                                           largo_genetico=largo_genetico,
                                                           probabilidad=punto_mutacion)

        poblacion = nueva_generacion_mutada

    print("Poblacion evolucionada: {}".format(poblacion))

    _mejor_individuo = mejor_individuo(poblacion, modelo)
    print("Mejor idividuo: {}".format(_mejor_individuo))

    """lo volvemos a convertir a letras"""
    _mejor_individuo = [chr(_mejor_individuo[i]) for i in range(len(_mejor_individuo))]
    print("Mejor idividuo: {}".format(_mejor_individuo))


if __name__ == '__main__':
    main()
