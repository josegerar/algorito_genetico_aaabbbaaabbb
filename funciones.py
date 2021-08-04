import random


def format_model(model):
    """convertir la letra a su base assci"""
    for i in range(len(model)):
        model[i] = ord(model[i])
    return model


def get_individuo(min, max, largo_genetico):
    """genera cada individuo de la poblacion"""
    return [random.randint(min, max) for i in range(largo_genetico)]


def generate_poblacion(min, max, largo_genetico, largo_poblacion):
    """generamos un array con todos los individuos de la poblacion"""
    return [get_individuo(min, max, largo_genetico) for i in range(largo_poblacion)]


def evaluar_individuo(individuo, modelo):
    """comparamos cuanto se parace el individuo actual al del modelo"""
    res = 0
    for i in range(len(individuo)):
        """si se parecen le damos un punto"""
        if individuo[i] == modelo[i]:
            res += 1
    """puntos que obtubo el individuo"""
    return res


def seleccion_por_torneo(poblacion, cantidad_seleccion):
    """seleccionar aleatoriamente los individuos que van a ir al torneo"""
    poblacion_seleccionada = []
    """copamos la poblacion para no ser alterada"""
    _poblacion = poblacion.copy()
    for i in range(cantidad_seleccion):
        """escogemos el individuo a participar dentro del torneo actual"""
        aleatorio = random.randint(0, len(poblacion) - 1 - i)
        """separamos el indoviduo para que no vuelva a ser seleccionado"""
        poblacion_seleccionada.append(_poblacion[aleatorio])
        """eliminamos el individuo de la poblacion actual"""
        _poblacion.pop(aleatorio)

    """retornamos la poblacion seleccionadas"""
    return poblacion_seleccionada


def seleccion(poblacion, modelo, cantidad_seleccion):
    """entra al procesos de seleccion para obtener los mejores padres"""
    _poblacion = [{'cant': 0, 'index': index, 'item': item} for index, item in enumerate(poblacion.copy())]

    for i in range(cantidad_seleccion * cantidad_seleccion):
        """entra a la seleccion"""
        _poblacion_seleccionada = seleccion_por_torneo(poblacion=_poblacion, cantidad_seleccion=cantidad_seleccion)

        """creamos un arreglo con el individuo actual y los puntos que obtubo"""
        puntos_poblacion = [(evaluar_individuo(individuo=i['item'], modelo=modelo), i) for i in _poblacion_seleccionada]

        """para obtener los mejores puntuados ordenamos el arreglo con el valor de los puntos obtenidos"""
        _mejores_puntuados = sorted(puntos_poblacion, key=lambda individuo: individuo[0], reverse=True)

        """obtenemos al ganador del toneo"""
        _mejor = _mejores_puntuados[0]

        """asignamos un punto al ganador del torneo"""
        _poblacion[_mejor[1]['index']]['cant'] += 1

    """ordenar la poblacion por los que ganaron el torneo"""
    _poblacion = sorted(_poblacion, key=lambda individuo: individuo['cant'], reverse=True)

    """obtnemos la poblacion ganadora desde la posicion 0 hasta la posicion=cantidad_seleccion"""
    _poblacion = _poblacion[0:cantidad_seleccion]

    """reconstruimos la estructura de la poblacion inicial con los individuos ganadores"""
    _poblacion = [i['item'] for i in _poblacion]

    """retornamos"""
    return _poblacion


def cruce_por_un_punto(mejores_padres, largo_genetico, cantidad_poblacion):
    """realiza un cruce de genes de los padres obtenidos de forma aleatoria para crear nuevos hijos
            que correspondan a la siguiente generacion
        """
    nueva_generacion = []
    for i in range(int(cantidad_poblacion / 2)):
        """obtiene un punto en el cual se va a realizar el cruce de genes"""
        punto_cruce = random.randint(1, largo_genetico - 1)

        """escogemos dos padres de forma aleatoria"""
        padres_seleccionados = random.sample(mejores_padres, 2)

        """creamos los hijos vacio (sin genes de los padres)"""
        hijo_1 = [0 for i in range(largo_genetico)]
        hijo_2 = hijo_1.copy()

        """el hijo uno recibe del primer padre sus genes desde el punto de cruce hacia atras"""
        hijo_1[punto_cruce:] = padres_seleccionados[0][punto_cruce:]
        """el hijo uno recibe del segundo padre sus genes desde el punto de cruce hacia adelante"""
        hijo_1[:punto_cruce] = padres_seleccionados[1][:punto_cruce]

        """el hijo dos recibe del segundo padre sus genes desde el punto de cruce hacia atras"""
        hijo_2[punto_cruce:] = padres_seleccionados[1][punto_cruce:]
        """el hijo dos recibe del primer padre sus genes desde el punto de cruce hacia adelante"""
        hijo_2[:punto_cruce] = padres_seleccionados[0][:punto_cruce]

        """asigna a la nueva poblacion los nuevos hijos"""
        nueva_generacion.append(hijo_1)
        nueva_generacion.append(hijo_2)

    """retorna la nueva poblacion"""
    return nueva_generacion


def cruce_por_dos_puntos(mejores_padres, largo_genetico, cantidad_poblacion):
    """realiza un cruce de genes de los padres obtenidos de forma aleatoria para crear nuevos hijos
                que correspondan a la siguiente generacion
            """
    nueva_generacion = []
    for i in range(int(cantidad_poblacion / 2)):
        """obtiene el primer punto en el cual se va a realizar el cruce de genes"""
        punto_cruce_1 = random.randint(1, int((largo_genetico / 2) - 1))

        """obtiene el segundo punto en el cual se va a realizar el cruce de genes"""
        punto_cruce_2 = random.randint(int(largo_genetico / 2), largo_genetico - 1)

        """escogemos dos padres de forma aleatoria"""
        padres_seleccionados = random.sample(mejores_padres, 2)

        """creamos los hijos vacios (sin genes de los padres)"""
        hijo_1 = [0 for i in range(largo_genetico)]
        hijo_2 = hijo_1.copy()

        """el hijo uno recibe del primer padre sus genes desde el punto de cruce 1 hacia atras"""
        hijo_1[:punto_cruce_1] = padres_seleccionados[0][:punto_cruce_1]
        """el hijo uno recibe del segundo padre sus genes desde el punto de cruce 2 hacia adelante"""
        hijo_1[punto_cruce_2:] = padres_seleccionados[1][punto_cruce_2:]
        """el hijo uno recibe del primer padre sus genes existentes entre el punto de cruce 1 y el punto de cruce 2"""
        hijo_1[punto_cruce_1:punto_cruce_2] = padres_seleccionados[0][punto_cruce_1:punto_cruce_2]

        """el hijo dos recibe del segundo padre sus genes desde el punto de cruce 1 hacia atras"""
        hijo_2[:punto_cruce_1] = padres_seleccionados[1][:punto_cruce_1]
        """el hijo dos recibe del primer padre sus genes desde el punto de cruce 2 hacia adelante"""
        hijo_2[punto_cruce_2:] = padres_seleccionados[0][punto_cruce_2:]
        """el hijo dos recibe del segundo padre sus genes existentes entre el punto de cruce 1 y el punto de cruce 2"""
        hijo_2[punto_cruce_1:punto_cruce_2] = padres_seleccionados[1][punto_cruce_1:punto_cruce_2]

        """asigna a la nueva poblacion los nuevos hijos"""
        nueva_generacion.append(hijo_1)
        nueva_generacion.append(hijo_2)

    """retorna la nueva poblacion"""
    return nueva_generacion


def cruce_probabilistico(mejores_padres, largo_genetico, cantidad_poblacion, probabilidad):
    """realiza un cruce de genes de los padres obtenidos de forma aleatoria para crear nuevos hijos
        que correspondan a la siguiente generacion
    """
    nueva_generacion = []
    for i in range(int(cantidad_poblacion / 2)):
        """escogemos dos padres de forma aleatoria"""
        padres_seleccionados = random.sample(mejores_padres, 2)

        """creamos los hijos vacio (sin genes de los padres)"""
        hijo_1 = [0 for i in range(largo_genetico)]
        hijo_2 = hijo_1.copy()

        """asigamos a los nuevos hijos los genes de los padres"""
        for j in range(largo_genetico):
            """de acuerdo a la probabilidad de cruce obtendran bien el gen del padre uno o bien del padre 2"""
            if random.random() <= probabilidad:
                hijo_1[j] = padres_seleccionados[0][j]
                hijo_2[j] = padres_seleccionados[1][j]
            else:
                hijo_1[j] = padres_seleccionados[1][j]
                hijo_2[j] = padres_seleccionados[0][j]

        """asigna a la nueva poblacion los nuevos hijos"""
        nueva_generacion.append(hijo_1)
        nueva_generacion.append(hijo_2)

    """retorna la nueva poblacion"""
    return nueva_generacion


def mutacion_binaria(nueva_generacion, largo_genetico, probabilidad):
    """realiza una mutacion de un gen de cada individuo de acuerdo a la probabilidad de mutacion"""
    for i in range(len(nueva_generacion)):
        if random.random() <= probabilidad:
            """obtenemos la posicion a mutar"""
            posicion_aleatoria_1 = random.randint(0, largo_genetico - 1)

            """obteneos la posicion de el nuevo valor"""
            posicion_aleatoria_2 = random.randint(0, largo_genetico - 1)

            """obtenemos el valor que queremos mutar"""
            valor_a_cambiar = nueva_generacion[i][posicion_aleatoria_1]

            """obtenemos el nuevo valor """
            nuevo_valor = nueva_generacion[i][posicion_aleatoria_2]

            """generamos un ciclo que recorra solo si los dos valores son iguales"""
            while valor_a_cambiar == nuevo_valor:
                """seguimos buscando nuevas posiciones"""
                posicion_aleatoria_2 = random.randint(0, largo_genetico - 1)
                """asignamos el valor nuevo valor"""
                nuevo_valor = nueva_generacion[i][posicion_aleatoria_2]

            """asigna el nuevo valor distinto al gen"""
            nueva_generacion[i][posicion_aleatoria_1] = nuevo_valor

    """retornamos la poblacion mutada"""
    return nueva_generacion


def mutacion_por_permutacion(nueva_generacion, largo_genetico, probabilidad):
    """realiza una mutacion de un gen de cada individuo de acuerdo a la probabilidad de mutacion"""
    for i in range(len(nueva_generacion)):
        if random.random() <= probabilidad:
            """obtner la primera posicion aleatoria a cambiar"""
            posicion_aleatoria_1 = random.randint(0, largo_genetico - 1)
            """obtner la segunda posicion aleatoria a cambiar"""
            posicion_aleatoria_2 = random.randint(0, largo_genetico - 1)

            """generamos un ciclo hasta que las posciones escogidas sean diferentes"""
            while posicion_aleatoria_1 == posicion_aleatoria_2:
                posicion_aleatoria_2 = random.randint(0, largo_genetico - 1)

            """asigna el valor del gen de la posicion dos lo cambia por el valor del gen de la posicion 1"""
            nueva_generacion[i][posicion_aleatoria_1] = nueva_generacion[i][posicion_aleatoria_2]

    """retornamos la poblacion mutada"""
    return nueva_generacion


def mejor_individuo(poblacion, modelo):
    """escoge al mejor individuo de la poblacion"""
    puntos_poblacion = [(evaluar_individuo(individuo=i, modelo=modelo), i) for i in poblacion]

    """ordena los individuos para que los mejores esten al principio"""
    _mejores_puntuados = sorted(puntos_poblacion, key=lambda individuo: individuo[0], reverse=True)

    """el individuo en la primera posicion sera el mejor de esa poblacion"""
    _mejor = _mejores_puntuados[0]

    """retornamos al mejor individuo"""
    return _mejor[1]
