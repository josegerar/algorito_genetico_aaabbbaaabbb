import random


def format_model(model):
    for i in range(len(model)):
        model[i] = ord(model[i])
    return model


def get_individuo(min, max, lenght):
    return [random.randint(min, max) for i in range(lenght)]


def generate_poblacion(min, max, largo_genetico, largo_poblacion):
    return [get_individuo(min, max, largo_genetico) for i in range(largo_poblacion)]


def evaluar_individuo(individuo, modelo):
    res = 0
    for i in range(len(individuo)):
        if individuo[i] == modelo[i]:
            res += 1
    return res


def seleccion_por_torneo(poblacion, cantidad_seleccion):
    poblacion_seleccionada = []
    _poblacion = poblacion.copy()
    for i in range(cantidad_seleccion):
        aleatorio = random.randint(0, len(poblacion) - 1 - i)
        poblacion_seleccionada.append(_poblacion[aleatorio])
        _poblacion.pop(aleatorio)

    return poblacion_seleccionada


def seleccion(poblacion, modelo, cantidad_seleccion):
    _poblacion = [{'cant': 0, 'index': index, 'item': item} for index, item in enumerate(poblacion.copy())]

    for i in range(cantidad_seleccion * cantidad_seleccion):
        _poblacion_seleccionada = seleccion_por_torneo(_poblacion, cantidad_seleccion)

        puntos_poblacion = [(evaluar_individuo(individuo=i['item'], modelo=modelo), i) for i in _poblacion_seleccionada]

        _mejores_puntuados = sorted(puntos_poblacion, key=lambda individuo: individuo[0], reverse=True)

        _mejor = _mejores_puntuados[0]

        _poblacion[_mejor[1]['index']]['cant'] += 1

    _poblacion = sorted(_poblacion, key=lambda individuo: individuo['cant'], reverse=True)

    _poblacion = _poblacion[0:cantidad_seleccion]

    _poblacion = [i['item'] for i in _poblacion]

    return _poblacion


def cruce_por_un_punto(mejores_padres, largo_genetico, cantidad_poblacion):
    nueva_generacion = []
    for i in range(int(cantidad_poblacion / 2)):
        punto_cruce = random.randint(1, largo_genetico - 1)

        padres_seleccionados = random.sample(mejores_padres, 2)

        hijo_1 = [0 for i in range(largo_genetico)]
        hijo_2 = hijo_1.copy()

        hijo_1[punto_cruce:] = padres_seleccionados[0][punto_cruce:]
        hijo_1[:punto_cruce] = padres_seleccionados[1][:punto_cruce]

        hijo_2[punto_cruce:] = padres_seleccionados[1][punto_cruce:]
        hijo_2[:punto_cruce] = padres_seleccionados[0][:punto_cruce]

        nueva_generacion.append(hijo_1)
        nueva_generacion.append(hijo_2)

    return nueva_generacion


def cruce_por_dos_puntos(mejores_padres, largo_genetico, cantidad_poblacion):
    nueva_generacion = []
    for i in range(int(cantidad_poblacion / 2)):
        punto_cruce_1 = random.randint(1, int((largo_genetico / 2) - 1))

        punto_cruce_2 = random.randint(int(largo_genetico / 2), largo_genetico - 1)

        padres_seleccionados = random.sample(mejores_padres, 2)

        hijo_1 = [0 for i in range(largo_genetico)]
        hijo_2 = hijo_1.copy()

        hijo_1[:punto_cruce_1] = padres_seleccionados[0][:punto_cruce_1]
        hijo_1[punto_cruce_2:] = padres_seleccionados[1][punto_cruce_2:]
        hijo_1[punto_cruce_1:punto_cruce_2] = padres_seleccionados[0][punto_cruce_1:punto_cruce_2]
        #
        hijo_1[:punto_cruce_1] = padres_seleccionados[1][:punto_cruce_1]
        hijo_1[punto_cruce_2:] = padres_seleccionados[0][punto_cruce_2:]
        hijo_1[punto_cruce_1:punto_cruce_2] = padres_seleccionados[1][punto_cruce_1:punto_cruce_2]

        nueva_generacion.append(hijo_1)
        nueva_generacion.append(hijo_2)

    return nueva_generacion


def cruce_probabilistico(mejores_padres, largo_genetico, cantidad_poblacion, probabilidad):
    nueva_generacion = []
    for i in range(int(cantidad_poblacion / 2)):
        padres_seleccionados = random.sample(mejores_padres, 2)

        hijo_1 = [0 for i in range(largo_genetico)]
        hijo_2 = hijo_1.copy()

        for j in range(largo_genetico):
            if random.random() <= probabilidad:
                hijo_1[j] = padres_seleccionados[0][j]
                hijo_2[j] = padres_seleccionados[1][j]
            else:
                hijo_1[j] = padres_seleccionados[1][j]
                hijo_2[j] = padres_seleccionados[0][j]

        nueva_generacion.append(hijo_1)
        nueva_generacion.append(hijo_2)

    return nueva_generacion


def mutacion_binaria(nueva_generacion, largo_genetico, probabilidad):
    for i in range(len(nueva_generacion)):
        if random.random() <= probabilidad:
            posicion_aleatoria_1 = random.randint(0, largo_genetico - 1)
            posicion_aleatoria_2 = random.randint(0, largo_genetico - 1)

            valor_a_cambiar = nueva_generacion[i][posicion_aleatoria_1]

            nuevo_valor = nueva_generacion[i][posicion_aleatoria_2]

            while valor_a_cambiar == nuevo_valor:
                posicion_aleatoria_2 = random.randint(0, largo_genetico - 1)
                nuevo_valor = nueva_generacion[i][posicion_aleatoria_2]

            nueva_generacion[i][posicion_aleatoria_1] = nuevo_valor

    return nueva_generacion


def mutacion_por_permutacion(nueva_generacion, largo_genetico, probabilidad):
    for i in range(len(nueva_generacion)):
        if random.random() <= probabilidad:
            posicion_aleatoria_1 = random.randint(0, largo_genetico - 1)
            posicion_aleatoria_2 = random.randint(0, largo_genetico - 1)

            while posicion_aleatoria_1 == posicion_aleatoria_2:
                posicion_aleatoria_2 = random.randint(0, largo_genetico - 1)

            nueva_generacion[i][posicion_aleatoria_1] = nueva_generacion[i][posicion_aleatoria_2]

    return nueva_generacion


def mejor_individuo(poblacion, modelo):
    puntos_poblacion = [(evaluar_individuo(individuo=i, modelo=modelo), i) for i in poblacion]

    _mejores_puntuados = sorted(puntos_poblacion, key=lambda individuo: individuo[0], reverse=True)

    _mejor = _mejores_puntuados[0]

    return _mejor[1]
