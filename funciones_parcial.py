import json
import re
import os

#NOMBRE:NICOLAS BRITES

def leer_archivo(string_de_archivo_json:str):
    '''
    La funcion lee un json y lo devuelve como una lista
    Recibe: una direccion de donde se encuentra el archivo
    Devuelve: el archivo transformado a lista
    '''
    lista= []
    with open(string_de_archivo_json, "r", encoding='utf-8') as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
 
    return lista

def imprimir_menu():
    '''
    imprime el menu para este desafio
    recibe nada
    devuelve el menu impreso
    '''
    mensaje = "\
    A) Mostrar la lista de todos los jugadores del Dream Team.\n\
    B) Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas.\n\
    C) Después de mostrar las estadísticas de un jugador seleccionado por el usuario, permite al usuario\n\
    guardar las estadísticas de ese jugador en un archivo CSV.\n\
    D)Permitir al usuario buscar un jugador por su nombre y mostrar sus logros\n\
    E)Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team,\n\
    ordenado por nombre de manera ascendente.\n\
    F)Permitir al usuario ingresar el nombre de un jugador y \n\
    mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.\n\
    G)Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.\n\
    H)Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.\n\
    I)Calcular y mostrar el jugador con el mayor porcentaje de asistencias totales.\n\
    J)Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado\n\
    más puntos por partido que ese valor.\n\
    K)Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado\n\
    más rebotes por partido que ese valor.\n\
    L)Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado\n\
    más asistencias por partido que ese valor.\n\
    M)Calcular y mostrar el jugador con la mayor cantidad de robos totales.\n\
    N)Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.\n\
    O)Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido\n\
    un porcentaje de tiros libres superior a ese valor.\n\
    P)Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador\n\
    con la menor cantidad de puntos por partido.\n\
    Q)Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.\n\
    R)Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido\n\
    un porcentaje de tiros triples superior a ese valor.\n\
    S)Calcular y mostrar el jugador con la mayor cantidad de temporadas.\n\
    T)Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido\n\
    un porcentaje de tiros de campo superior a ese valor.\n\
    U)BONUS BONUS BONUS\n\
    V)EXTRA mostrar cantidad de jugadores por posicion\n\
    W)EXTRA Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente.\n\
    X)EXTRA Determinar qué jugador tiene las mejores estadísticas en cada valor.\n\
    Y)EXTRA Determinar qué jugador tiene las mejores estadísticas de todos.\n\
    Z) Salir de la aplicacion.\
    ______________________________________________________________________________________\
    "
    print(mensaje)

def menu_principal_parcial():
    '''
    La función imprime el menu y solicita al usuario que ingrese un numero, valida si es un valor valido o no
    Recibe: nada
    Devuelve: el numero ingresado pasado a int, o -1 si no puede
    '''
    imprimir_menu()
    opcion = input("Ingrese la opción deseada: ")
    if re.match(r"^[a-zA-Z]{1}$", opcion):
        return opcion.upper()
    else:
        return -1


def parcial_app(lista_jugadores:list):
    '''
    La función inicia la app
    Recibe: La lista de personajes
    Devuelve: la ejecucion del programa en si, eligiendo que hacer en el menu
    '''

    exportar_CSV = ""
    while True:
        opcion = menu_principal_parcial()

        if opcion == "A":
            listar_jugadores(lista_jugadores)
        elif opcion == "B":
            exportar_CSV = seleccionar_jugador(lista_jugadores)
        elif opcion == "C":
            guardar_estadisticas_csv(exportar_CSV)
        elif opcion == "D":
            buscar_logros_por_nombre(lista_jugadores, False)
        elif opcion == "E": 
            calcular_y_mostrar_promedios(lista_jugadores)
        elif opcion == "F": 
            buscar_logros_por_nombre(lista_jugadores, salon_de_la_fama = True)
        elif opcion == "G": 
            calcular_y_mostrar_jugador_mayor(lista_jugadores, "", "rebotes_totales")
        elif opcion == "H": 
            calcular_y_mostrar_jugador_mayor(lista_jugadores, "", "porcentaje_tiros_de_campo" )
        elif opcion == "I": 
            calcular_y_mostrar_jugador_mayor(lista_jugadores, "", "asistencias_totales")
        elif opcion == "J": 
            mostrar_jugadores_mayor_promedio_al_ingresado(lista_jugadores, "promedio_puntos_por_partido")
        elif opcion == "K": 
            mostrar_jugadores_mayor_promedio_al_ingresado(lista_jugadores, "promedio_rebotes_por_partido")
        elif opcion == "L": 
            mostrar_jugadores_mayor_promedio_al_ingresado(lista_jugadores, "promedio_asistencias_por_partido")
        elif opcion == "M": 
            calcular_y_mostrar_jugador_mayor(lista_jugadores, "", "robos_totales")
        elif opcion == "N": 
            calcular_y_mostrar_jugador_mayor(lista_jugadores, "" , "bloqueos_totales")   
        elif opcion == "O": 
            mostrar_jugadores_mayor_promedio_al_ingresado(lista_jugadores, "porcentaje_tiros_libres")    
        elif opcion == "P": 
            calcular_y_mostrar_promedios(lista_jugadores, True)  
        elif opcion == "Q": 
            calcular_y_mostrar_jugador_mayor(lista_jugadores, "logros", "") 
        elif opcion == "R": 
            mostrar_jugadores_mayor_promedio_al_ingresado(lista_jugadores, "porcentaje_tiros_triples")   
        elif opcion == "S": 
            calcular_y_mostrar_jugador_mayor(lista_jugadores,"" , "temporadas")    
        elif opcion == "T": 
            mostrar_jugadores_mayor_promedio_al_ingresado(lista_jugadores, "porcentaje_tiros_de_campo")     
        elif opcion == "U":
            bonus_bonus_bonus(lista_jugadores)         
        elif opcion == "V":
            extra_cantidad_por_posicion(lista_jugadores)     
        elif opcion == "W":
            extra_lista_cantidad_All_star(lista_jugadores)
        elif opcion == "X":
            extra_mejores_estadisticas(lista_jugadores)
        elif opcion == "Y":
            extra_mejores_estadisticas_de_todos(lista_jugadores)
        elif opcion == "Z":
            break
        else:
            print("Opción inválida. Intente de nuevo.")
        clear_console()

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

def listar_jugadores(lista_jugadores:list) -> str:   #1
    '''
    Muestra por consola la lista de jugadores en el formato pedido
    Recibe una lista de jugadores
    devuelve un string con los datos para imprimir el csv
    '''
    lista_para_trabajar = []
    lista_para_trabajar = lista_jugadores[:]

    indice = 1
    for jugadores in lista_para_trabajar:

        print("{0}) {1} - {2}".format(indice, jugadores["nombre"], jugadores["posicion"]))
        indice += 1

def seleccionar_jugador(lista_jugadores:list): #2
    '''
    Muestra las estadisticas completas de un jugador, el cual lo ingresa el usuario
    Recibe una lista de jugadores
    devuelve nada, solo imprime
    '''
    while True:
        opcion = input("Ingrese el indice del jugador (antes listado, de 1 a 12):")
        if opcion.isdigit() and (int(opcion) >=1 and int(opcion) <13):

            for indice in range(len(lista_jugadores)):
                if indice+1 == int(opcion):
                    
                    mensaje = "\
    {0} \n\
    Temporadas : {1}\n\
    Puntos totales: {2}\n\
    Promedio puntos por partido: {3}\n\
    Rebotes totales: {4}\n\
    Promedio rebotes por partido: {5}\n\
    Asistencias totales: {6}\n\
    Promedio asistencias por partido: {7}\n\
    Robos totales: {8}\n\
    Bloqueos totales: {9}\n\
    Porcentaje_tiros_de_campo: {10}\n\
    Porcentaje_tiros_libres: {11}\n\
    Porcentaje_tiros_triples: {12}"
                    mensaje = mensaje.format(lista_jugadores[indice]["nombre"], lista_jugadores[indice]["estadisticas"]["temporadas"],
                                            lista_jugadores[indice]["estadisticas"]["puntos_totales"],
                                            lista_jugadores[indice]["estadisticas"]["promedio_puntos_por_partido"],
                                            lista_jugadores[indice]["estadisticas"]["rebotes_totales"],
                                            lista_jugadores[indice]["estadisticas"]["promedio_rebotes_por_partido"],
                                            lista_jugadores[indice]["estadisticas"]["asistencias_totales"],
                                            lista_jugadores[indice]["estadisticas"]["promedio_asistencias_por_partido"],
                                            lista_jugadores[indice]["estadisticas"]["robos_totales"],
                                            lista_jugadores[indice]["estadisticas"]["bloqueos_totales"],
                                            lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_de_campo"],
                                            lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_libres"],
                                            lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_triples"], end= "\n") 
                    print(mensaje)
                    
                    imprimir_csv = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13}"
                    imprimir_csv = imprimir_csv.format(lista_jugadores[indice]["nombre"],lista_jugadores[indice]["posicion"],
                                            lista_jugadores[indice]["estadisticas"]["temporadas"],
                                            lista_jugadores[indice]["estadisticas"]["puntos_totales"],
                                            lista_jugadores[indice]["estadisticas"]["promedio_puntos_por_partido"],
                                            lista_jugadores[indice]["estadisticas"]["rebotes_totales"],
                                            lista_jugadores[indice]["estadisticas"]["promedio_rebotes_por_partido"],
                                            lista_jugadores[indice]["estadisticas"]["asistencias_totales"],
                                            lista_jugadores[indice]["estadisticas"]["promedio_asistencias_por_partido"],
                                            lista_jugadores[indice]["estadisticas"]["robos_totales"],
                                            lista_jugadores[indice]["estadisticas"]["bloqueos_totales"],
                                            lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_de_campo"],
                                            lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_libres"],
                                            lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_triples"])

            break
        else:
            print("Formato invalido o no existe el indice. Intente de nuevo.")

    return imprimir_csv
    
def guardar_estadisticas_csv(exportar_CSV:str): #3
    '''
    Guarda la info pedida en formato csv
    Recibe un string con los datos para exportar
    devuelve Nada
    '''
    if exportar_CSV != "":
        exportar_CSV_separado = exportar_CSV.split(",")
        nombre_de_archivo = "{0}.csv".format(exportar_CSV_separado[0])

        with open(nombre_de_archivo, "w") as archivo:
                archivo.write(exportar_CSV)

        print("Se imprimio correctamente el archivo")
    else:
        print("Todavia seleccionaste un jugador en el punto anterior")    


def buscar_logros_por_nombre(lista_jugadores:list, salon_de_la_fama:bool = False):# 4 y 6
    '''
    Le pide al usuario ingresar un nombre y mostar los logros del jugador que pide
    Recibe una lista de jugadores y un bool para buscar solo el logro del salon de la fama o no
    devuelve Nada, solo imprime
    '''
    lista_para_trabajar = []
    lista_para_trabajar = lista_jugadores[:]
    flag_break = 0

    while True:
        opcion = input("Ingrese el nombre del jugador: ") 
        opcion = opcion.lower()
        opcion = opcion.capitalize()
        for jugadores in lista_para_trabajar:
            if salon_de_la_fama == False and re.match(r"(Michael|Jordan|Magic|Johnson|Larry|\
                    Bird|Scottie|Pippen|David|Robinson|Patrick|Ewing|Karl|Malone|John|\
                    Stockton|Clyde|Drexler|Chris|Mullin|Christian|Laettner)",opcion):
                if opcion in jugadores["nombre"]:
                    imprimir_logros_jugadores(jugadores)
                    flag_break = 1

            elif salon_de_la_fama == True and re.match(r"(Michael|Jordan|Magic|Johnson|Larry|\
                    Bird|Scottie|Pippen|David|Robinson|Patrick|Ewing|Karl|Malone|John|\
                    Stockton|Clyde|Drexler|Chris|Mullin|Christian|Laettner)",opcion):
                if opcion in jugadores["nombre"]:
                    imprimir_logros_jugadores(jugadores, True)
                    flag_break = 1
            else:
                print("Escribio cualquier cosa, escriba el nombre de un jugador.")
                break

        if flag_break == 1:
            break 


def imprimir_logros_jugadores(jugadores:dict, salon_de_la_fama:bool = False): # 4 y 6
    '''
    imprime los logros del jugador pedido (ahorra 3 lineas de codigo por jugador al ejercicio anterior)
    Recibe una lista de jugadores
    devuelve Nada, solo imprime
    '''
    if salon_de_la_fama == False:
        retorno = "\n".join(jugadores["logros"])
    else:
        retorno = jugadores["logros"][-1]
    print(jugadores["nombre"])
    print(retorno)  


def ivan_sort_diccionarios_promedios(lista:list , clave:str, clave_estadisticas:str, up:bool = True): #SORT PARA EL 5 , 6 , 7 , 8 , 9
    '''
    El algoritmo de ordenamiento, recibe una lista y varios parametros y los ordena en orden dependiendo los parametros ingresado,
    Si es up seria de mayor a menor o viceversa 
    recibe una lista de cosas, una clave para saber que clave del dicc comparar, una clave del dicc estadistica,
    up es un bool 
    devuelve Nada, ( la funcion solo ordena )
    '''
    rango_a = len(lista)
    flag_swap = True


    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1

        for indice_A in range(rango_a):
            if clave_estadisticas!= "" and up == True and  float(lista[indice_A][clave][clave_estadisticas]
               ) > float(lista[indice_A+1][clave][clave_estadisticas]) \
                or up == False and  float(lista[indice_A][clave][clave_estadisticas]
                 ) < float(lista[indice_A+1][clave][clave_estadisticas]):
                lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                flag_swap = True

            if clave_estadisticas== "" and up == True and  lista[indice_A][clave]\
                > lista[indice_A+1][clave] \
                or clave_estadisticas== "" and up == False and  lista[indice_A][clave]\
                < lista[indice_A+1][clave]:
                lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                flag_swap = True

def calcular_y_mostrar_promedios(lista_jugadores:list, excluir_jugador:bool = False): # 5 , 16
    '''
    calcula el promedio total de puntos por partido de todo el dream team y ordena a los jugadores por promedio individual 
    si no hay que excluir al jugador con menor puntaje, si hay que excluirlo solo imprime el prom total sin el jugador exluido
    recibe una lista 
    devuelve Nada, Solo imprime el promedio total y la lista de jugadores en orden O
    imprime el prom total sin el jugador exluido
    '''
    lista_para_trabajar = []
    lista_para_trabajar = lista_jugadores[:]
    acumulador = 0

    if excluir_jugador == True:
        ivan_sort_diccionarios_promedios(lista_para_trabajar,"estadisticas", "promedio_puntos_por_partido", True)
        lista_para_trabajar.pop(0)

    for jugador in lista_para_trabajar:
        valor = jugador["estadisticas"]["promedio_puntos_por_partido"]
        acumulador += valor

    promedio = acumulador / len(lista_para_trabajar)

    if excluir_jugador == True:
        print("El promedio total de puntos por partido de todo el Dream Team excluyendo\n\
              al jugador con la menor cantidad de puntos es : {0}".format(round(promedio,2)))

    if excluir_jugador == False:

        print("El promedio total de puntos por partido de todo el Dream Team es : {0}".format(round(promedio,2)))
        print("Y el promedio de cada jugador ordenado por nombre de manera ascendente es:")

        ivan_sort_diccionarios_promedios(lista_para_trabajar,"nombre", "", True)

        for jugador in lista_para_trabajar:
            print("{0}  | Promedio de puntos por partido: {1}".format(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"]))
        

def calcular_y_mostrar_jugador_mayor(lista_jugadores:list, clave:str, clave_estadistica:str): # 7 , 8 , 9 , 13 , 14, 17 , 19
    '''
    Calcula y muestra al jugador con mayor cantidad de la estadistica ingresada
    recibe una lista y un string con la clave de la estadistica a evaluar
    devuelve Nada, Solo imprime el jugador y la estadistica solicitada
    '''
    lista_para_trabajar = []
    lista_para_trabajar = lista_jugadores[:] 


    if clave == "": 
        indice = calcular_mayor(lista_jugadores,"", clave_estadistica)
        if type(indice) == list:
            for indices in indice:
                respuesta_formateada = formato_respuestas(clave_estadistica)
                print("{0} | {1} : {2}".format(lista_para_trabajar[indices]["nombre"], respuesta_formateada,
                                                        lista_para_trabajar[indices]["estadisticas"][clave_estadistica]))       
        else:
            respuesta_formateada = formato_respuestas(clave_estadistica)
            print("{0} | {1} : {2}".format(lista_para_trabajar[indice]["nombre"], respuesta_formateada,
                                                        lista_para_trabajar[indice]["estadisticas"][clave_estadistica]))   
    else :
        indice = calcular_mayor(lista_jugadores,clave, clave_estadistica)
        print("{0} | Cantidad de logros : {1}".format(lista_para_trabajar[indice]["nombre"],
                                                    len(lista_para_trabajar[indice][clave])))
 

def calcular_mayor(lista_jugadores,clave, clave_estadistica):
    '''
    Calcula al jugador de la lista que tiene el valor mayor en la clave determinada
    Recibe una lista de jugadores, una clave y una clave estadistica
    Devuelve el indice del jugador con el valor mas alto
    '''
    lista_para_trabajar = []
    lista_para_trabajar = lista_jugadores[:] 

    lista_jugadores_maximos_mismo_valor = []

    for indice in range(len(lista_para_trabajar)):
        if clave == "":
            dato_string = lista_para_trabajar[indice]["estadisticas"][clave_estadistica]
            dato_float = float(dato_string)
            if (indice == 0 or float(lista_para_trabajar[maximo_alto_indice]["estadisticas"][clave_estadistica]) < dato_float):
                maximo_alto_indice = indice
        else :
            dato_float = len(lista_para_trabajar[indice][clave])
            if (indice == 0 or len(lista_para_trabajar[maximo_alto_indice][clave]) < dato_float):
                maximo_alto_indice = indice

    if clave == "":
        lista_jugadores_maximos_mismo_valor.append(maximo_alto_indice)
        for indice in range(len(lista_para_trabajar)):
            dato_string = lista_para_trabajar[indice]["estadisticas"][clave_estadistica]
            dato_float = float(dato_string)
            if indice != maximo_alto_indice and lista_para_trabajar[maximo_alto_indice]["estadisticas"][clave_estadistica] == dato_float:
                lista_jugadores_maximos_mismo_valor.append(indice)
    
    if len(lista_jugadores_maximos_mismo_valor) > 1:
        return lista_jugadores_maximos_mismo_valor
    else:
        return maximo_alto_indice

def formato_respuestas(clave_estadistica):
    '''
    Prepara el formato de una clave para imprimirse bonito
    recibe la clave a modificar
    devuelve la clave modificada
    '''
    respuesta_formateada = clave_estadistica.capitalize()
    respuesta_formateada = respuesta_formateada.replace("_", " ")

    return respuesta_formateada


def mostrar_jugadores_mayor_promedio_al_ingresado(lista_jugadores:list, clave:str): # 10, 11, 12 , 15 , 18, 20
    '''
    Imprime a los jugadores que han promediado mas puntos o pórcentaje que el valor ingresado por el usuario
    y si es porcentaje de tiros de campo devuelve a todos los jugadores ordenados por pocision
    recibe una lista y un string con la clave de la estadistica a evaluar
    devuelve Nada, Solo imprime el jugador y la estadistica solicitada
    '''
    lista_para_trabajar = []
    lista_para_trabajar = lista_jugadores[:] 

    while True:
        opcion = input("Ingrese un promedio/porcentaje a evaluar :") 
        if re.match(r"^[0-9\.\,]{1,5}$",opcion) and (float(opcion)<100 and float(opcion)>0) :
            opcion_float = float(opcion)
            if clave != "porcentaje_tiros_de_campo":
                for jugador in lista_para_trabajar:
                    filtar_jugador_mayor(jugador, opcion_float, clave)
                break
            if clave == "porcentaje_tiros_de_campo":   
                filtar_jugador_mayor_ordenado_por_posicion(lista_jugadores, opcion)
                break
        else:
            print("No ingreso un promedio.") 
                     

def filtar_jugador_mayor(jugador:dict, opcion:float, clave_estadistica:str):
    '''
    Filtra si los jugadores superan el valor de la opcion en la clave solicitada
    recibe un dicc de un jugador, un float y un string con la clave estadistica
    devuelve nada, solo imprime
    '''
    respuesta_formateada = formato_respuestas(clave_estadistica)

    if jugador["estadisticas"][clave_estadistica] > opcion:
        print("{0} | {1} : {2}".format(jugador["nombre"], respuesta_formateada,
                                                    jugador["estadisticas"][clave_estadistica]))   

def filtar_jugador_mayor_ordenado_por_posicion(lista_jugadores:list, opcion:float):
    '''
    filtra a los jugadores que sean mayor que la opcion y los imprime ordenados por posicion
    recibe la lista de jugadores y un float opcion
    devuelve nada, solo imprime
    '''
    lista_base = []
    lista_escolta = []
    lista_alero = []
    lista_ala_pivot = []
    lista_pivot = []
    lista_posicion_de_cancha = []

    for jugador in lista_jugadores:
       if jugador["estadisticas"]["porcentaje_tiros_de_campo"] > float(opcion):
                        if jugador["posicion"] == "Base":
                            lista_base.append(jugador)
                        if jugador["posicion"] == "Escolta":
                            lista_escolta.append(jugador)
                        if jugador["posicion"] == "Alero":
                            lista_alero.append(jugador)
                        if jugador["posicion"] == "Ala-Pivot":
                            lista_ala_pivot.append(jugador)
                        if jugador["posicion"] == "Pivot":
                            lista_pivot.append(jugador) 
    
    lista_posicion_de_cancha.extend(lista_base)
    lista_posicion_de_cancha.extend(lista_escolta)
    lista_posicion_de_cancha.extend(lista_alero)
    lista_posicion_de_cancha.extend(lista_ala_pivot)
    lista_posicion_de_cancha.extend(lista_pivot)
    for jugador in lista_posicion_de_cancha:
        print("{0} | {1} | Porcentaje tiros de campo: {2}".format(jugador["nombre"],
                jugador["posicion"], jugador["estadisticas"]["porcentaje_tiros_de_campo"]))

def bonus_bonus_bonus(lista_jugadores):
    '''
    BONUS BONUS, CREA UN CSV CON EL NOMBRE DE JUGADOR Y AL LADO LA POCISION DEPENDIENDO INDICE DE PUNTOS,
    REBOTES, ASISTENCIA Y ROBO,muy god
    recibe lista de jugadores
    devuelve nada, solo exporta csv
    '''
    lista_para_sacar_indices_puntos = lista_jugadores[:] 
    lista_para_sacar_indices_rebotes = lista_jugadores[:] 
    lista_para_sacar_indices_asistencias = lista_jugadores[:] 
    lista_para_sacar_indices_robos = lista_jugadores[:] 

    ivan_sort_diccionarios_promedios(lista_para_sacar_indices_puntos , "estadisticas", "puntos_totales", False)
    ivan_sort_diccionarios_promedios(lista_para_sacar_indices_rebotes , "estadisticas", "rebotes_totales", False)
    ivan_sort_diccionarios_promedios(lista_para_sacar_indices_asistencias , "estadisticas", "asistencias_totales", False)
    ivan_sort_diccionarios_promedios(lista_para_sacar_indices_robos , "estadisticas", "robos_totales", False)

    csv_exportar = ""

    for indice_puntos in range(len(lista_para_sacar_indices_puntos)):
        for indice_rebotes in range(len(lista_para_sacar_indices_rebotes)):
            for indice_asistencias in range(len(lista_para_sacar_indices_asistencias)):
                for indice_robos in range(len(lista_para_sacar_indices_robos)):
                    for jugadores in lista_jugadores:
                        if jugadores["nombre"] == lista_para_sacar_indices_puntos[indice_puntos]["nombre"]:
                            if jugadores["nombre"] == lista_para_sacar_indices_rebotes[indice_rebotes]["nombre"]:
                                if jugadores["nombre"] == lista_para_sacar_indices_asistencias[indice_asistencias]["nombre"]:
                                    if jugadores["nombre"] == lista_para_sacar_indices_robos[indice_robos]["nombre"]:
                                        csv_exportar += "{0},{1},{2},{3},{4}\n".format(jugadores["nombre"], \
                                                        indice_puntos+1,indice_rebotes+1,indice_asistencias+1,indice_robos+1)

    with open("BONUS GOD DERECHITO PAL EXCEL.csv", "w") as archivo:
        archivo.write(csv_exportar)


def extra_cantidad_por_posicion(lista_jugadores):
    '''
    Filtra a los jugadores por su posicion en la cancha y devuelve la cantuidad de cada uno
    recibe, la lista de jugadores
    retorna nada, solo imprime las cantidades
    '''
    lista_para_trabajar = lista_jugadores[:] 

    contador_base = 0
    contador_escolta= 0
    contador_alero=0
    contador_alapivot = 0
    contador_pivot = 0

    for jugador in lista_para_trabajar:
        if jugador["posicion"] == "Base":
            contador_base +=1
        if jugador["posicion"] == "Escolta":
            contador_escolta +=1
        if jugador["posicion"] == "Alero":
            contador_alero +=1
        if jugador["posicion"] == "Ala-Pivot":
            contador_alapivot +=1
        if jugador["posicion"] == "Pivot":
            contador_pivot +=1

 
    print("Base : {0}".format(contador_base))
    print("Escolta : {0}".format(contador_escolta))
    print("Alero : {0}".format(contador_alero))
    print("Ala-Pivot : {0}".format(contador_alapivot))
    print("Pivot : {0}".format(contador_pivot))
    

def extra_lista_cantidad_All_star(lista_jugadores):
    '''
    Revisa los logros de todos los jugadores y los ordena segun la cantidad de veces que fueron All-star
    Recibe, la lista de jugadores
    Retorna, nada, solo imprime en orden de forma descendente
    '''
    lista_para_trabajar = lista_jugadores[:] 

    for jugador in lista_para_trabajar:
        if jugador["nombre"] ==  "Christian Laettner":
            jugador["All-Star"]= 0
            break
        else:
            for logros in jugador["logros"]:
                if re.match(r"^[0-9]{1,2}( veces All-Star)$", logros):
                    veces_allstar_split = logros.split(" ")
                    veces_allstar = veces_allstar_split[0]
                    jugador["All-Star"]= veces_allstar
 
                    break

    ivan_sort_diccionarios_extra_extras(lista_para_trabajar, "All-Star","", False)

    for jugador in lista_para_trabajar:
        print("{0} ({1} veces All-Star)".format(jugador["nombre"], jugador["All-Star"]))



def ivan_sort_diccionarios_extra_extras(lista:list , clave:str, clave_estadisticas:str, up:bool = True): #SORT PARA EL 5 , 6 , 7 , 8 , 9
    '''
    El algoritmo de ordenamiento, recibe una lista y varios parametros y los ordena en orden dependiendo los parametros ingresado,
    Si es up seria de mayor a menor o viceversa 
    recibe una lista de cosas, una clave para saber que clave del dicc comparar, una clave del dicc estadistica,
    up es un bool 
    devuelve Nada, ( la funcion solo ordena )
    '''
    rango_a = len(lista)
    flag_swap = True


    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1

        for indice_A in range(rango_a):
            if clave_estadisticas== "" and up == True and int(lista[indice_A][clave])\
                > int(lista[indice_A+1][clave]) \
                or clave_estadisticas== "" and up == False and  int(lista[indice_A][clave])\
                < int(lista[indice_A+1][clave]):
                lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                flag_swap = True


def extra_mejores_estadisticas(lista_jugadores):
    '''
    imprime a cada jugador que sea el mejor en cada una de las estadisticas
    recibe, la lista de jugadores
    retorna, nada solo imprime
    '''
    lista_para_trabajar = lista_jugadores[:] 

    for jugadores in lista_para_trabajar:
        for estadisticas in jugadores["estadisticas"]:
            calcular_y_mostrar_jugador_mayor(lista_jugadores, "", estadisticas)


def extra_mejores_estadisticas_de_todos(lista_jugadores):
    '''
    Busca al jugador con las mejores estadisticas de todos.
    recibe la lista de jugadores
    retorna nada, solo imprime al mejor    
    '''
    lista_para_trabajar = lista_jugadores[:] 


    for indice in range(len(lista_para_trabajar)):
        contador_mayor = 0
        for estadisticas in lista_para_trabajar[indice]["estadisticas"]:
            contador_mayor += int(lista_para_trabajar[indice]["estadisticas"][estadisticas])

        lista_para_trabajar[indice]["Es mayor"] = contador_mayor

    ivan_sort_diccionarios_extra_extras(lista_para_trabajar, "Es mayor", "", False)

    print("El jugador que tiene mayor cantidad de mejores estadisticas es {0}, con {1} de puntos totales\
           en todas las estadisticas.".format(lista_para_trabajar[0]["nombre"], lista_para_trabajar[0]["Es mayor"]))

