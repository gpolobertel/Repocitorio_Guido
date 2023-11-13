# Función para contar las Copas Mundiales ganadas por un país
def contar_copas_ganadas_por_pais(datos, pais):
    copas_ganadas = 0
    for partido in datos:
        if partido['home_team'] == pais and partido['Round'] == 'Final' and int(partido['home_score']) > int(partido['away_score']):
            copas_ganadas += 1
        elif partido['away_team'] == pais and partido['Round'] == 'Final' and int(partido['away_score']) > int(partido['home_score']):
            copas_ganadas += 1
    return copas_ganadas

# Función para contar los subcampeonatos de un país
def contar_subcampeonatos_por_pais(datos, pais):
    subcampeonatos = 0
    for partido in datos:
        if partido['home_team'] == pais and partido['Round'] == 'Final' and int(partido['home_score']) < int(partido['away_score']):
            subcampeonatos += 1
        elif partido['away_team'] == pais and partido['Round'] == 'Final' and int(partido['away_score']) < int(partido['home_score']):
            subcampeonatos += 1
    return subcampeonatos

# Función para contar participaciones de un equipo en la Copa Mundial
def contar_participaciones_equipo(datos, equipo):
    participaciones = 0
    for partido in datos:
        if partido['home_team'] == equipo or partido['away_team'] == equipo:
            participaciones += 1
    return participaciones

# Función para contar el número total de Copas Mundiales de Fútbol
def contar_copas_mundiales(datos):
    copas_mundiales = set()
    for partido in datos:
        copas_mundiales.add(partido['Year'])
    return len(copas_mundiales)

# Función para determinar la cantidad total de asistentes a todas las ediciones de la Copa Mundial
def contar_asistentes_totales(datos):
    asistentes_totales = 0
    for partido in datos:
        asistentes_totales += int(partido['Attendance'])
    return asistentes_totales

# Función para identificar cuántas finales se definieron a través de una tanda de penales
def contar_finales_penales(datos):
    finales_penales = 0
    for partido in datos:
        if partido['Round'] == 'Final' and partido['home_penalty'] != '' and partido['away_penalty'] != '':
            finales_penales += 1
    return finales_penales

# Función para calcular el total de goles anotados por todos los equipos en todas las ediciones de la Copa Mundial
def contar_goles_a_favor(datos, equipo):
    goles_a_favor = 0
    for partido in datos:
        if partido['home_team'] == equipo:
            goles_a_favor += int(partido['home_score'])
        elif partido['away_team'] == equipo:
            goles_a_favor += int(partido['away_score'])
    return goles_a_favor

# Función para calcular la cantidad total de goles en contra de un equipo en todas las ediciones de la Copa Mundial
def contar_goles_en_contra(datos, equipo):
    goles_en_contra = 0
    for partido in datos:
        if partido['home_team'] == equipo:
            goles_en_contra += int(partido['away_score'])
        elif partido['away_team'] == equipo:
            goles_en_contra += int(partido['home_score'])
    return goles_en_contra

# Función para calcular la diferencia total de goles de un equipo en todas sus participaciones en la Copa Mundial
def calcular_diferencia_goles(datos, equipo):
    diferencia_goles = 0
    for partido in datos:
        if partido['home_team'] == equipo:
            diferencia_goles += int(partido['home_score']) - int(partido['away_score'])
        elif partido['away_team'] == equipo:
            diferencia_goles += int(partido['away_score']) - int(partido['home_score'])
    return diferencia_goles

# Función para calcular el promedio de goles anotados por un equipo en todas sus participaciones
def calcular_promedio_goles(datos, equipo):
    participaciones = contar_participaciones_equipo(datos, equipo)
    if participaciones == 0:
        return 0
    goles_a_favor = 0
    for partido in datos:
        if partido['home_team'] == equipo:
            goles_a_favor += int(partido['home_score'])
        elif partido['away_team'] == equipo:
            goles_a_favor += int(partido['away_score'])
    return goles_a_favor / participaciones

# Función para determinar cuántas veces dos equipos específicos se han enfrentado en ediciones pasadas de la Copa Mundial
def veces_enfrentados(datos, equipo1, equipo2):
    enfrentamientos = 0
    for partido in datos:
        if (partido['home_team'] == equipo1 and partido['away_team'] == equipo2) or (partido['home_team'] == equipo2 and partido['away_team'] == equipo1):
            enfrentamientos += 1
    return enfrentamientos

# Función para identificar en qué edición de la Copa Mundial se han ejecutado la mayor cantidad de penales
def mundial_con_mas_penales(datos):
    penales_por_mundial = {}
    for partido in datos:
        if partido['home_penalty'] != '' and partido['away_penalty'] != '':
            mundial = partido['Year']
            if mundial not in penales_por_mundial:
                penales_por_mundial[mundial] = 1
            else:
                penales_por_mundial[mundial] += 1
    mundial_max_penales = max(penales_por_mundial, key=penales_por_mundial.get)
    return mundial_max_penales

# Función para identificar en qué edición de la Copa Mundial se ha anotado la mayor cantidad de goles en total
def mundial_con_mas_goles(datos):
    goles_por_mundial = {}
    for partido in datos:
        mundial = partido['Year']
        goles = int(partido['home_score']) + int(partido['away_score'])
        if mundial not in goles_por_mundial:
            goles_por_mundial[mundial] = goles
        else:
            goles_por_mundial[mundial] += goles
    mundial_max_goles = max(goles_por_mundial, key=goles_por_mundial.get)
    return mundial_max_goles

# Función para identificar los partidos con la mayor diferencia de goles en la historia de la Copa Mundial
def mayores_goleadas(datos):
    mayores_goleadas = []
    for partido in datos:
        diferencia_goles = abs(int(partido['home_score']) - int(partido['away_score']))
        if len(mayores_goleadas) < 5 or diferencia_goles > mayores_goleadas[-1][3]:
            mayor_goleada = (partido['Year'], partido['home_team'], partido['away_team'], diferencia_goles)
            mayores_goleadas.append(mayor_goleada)
            mayores_goleadas = sorted(mayores_goleadas, key=lambda x: x[3], reverse=True)[:5]
    return mayores_goleadas

# Función para cargar los datos desde un archivo CSV
def cargar_datos_csv(nombre_archivo):
    datos = []
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        # Omitir el encabezado
        next(archivo)
        for linea in archivo:
            # Remover salto de línea y dividir la línea en campos
            linea = linea.rstrip()
            campos = linea.split(',')
            # Crear un diccionario con los datos y agregarlo a la lista
            partido = {
                'home_team': campos[0],
                'away_team': campos[1],
                'home_score': campos[2],
                'home_penalty': campos[3],
                'away_score': campos[4],
                'away_penalty': campos[5],
                'home_manager': campos[6],
                'home_captain': campos[7],
                'away_manager': campos[8],
                'away_captain': campos[9],
                'Attendance': campos[10],
                'Venue': campos[11],
                'Round': campos[12],
                'Date': campos[13],
                'Referee': campos[14],
                'Host': campos[15],
                'Year': campos[16]
            }
            datos.append(partido)
    return datos

# Cargar los datos desde el archivo CSV
nombre_archivo = "wcm.csv"
datos = cargar_datos_csv(nombre_archivo)

# Menú principal
while True:
    print("\nMenú:")
    print("1. Conocer el número de Copas Mundiales ganadas por un país")
    print("2. Conocer el número de subcampeonatos de un país")
    print("3. Conocer el número de participaciones de un equipo al mundial")
    print("4. Conocer el número de Copas Mundiales jugadas hasta la fecha")
    print("5. Conocer el número de asistentes a las Copas Mundiales")
    print("6. Conocer el número de finales disputadas por penales")
    print("7. Conocer el número de goles a favor de los equipos en los mundiales")
    print("8. Conocer el número de goles en contra de los equipos en los mundiales")
    print("9. Conocer la diferencia de goles en todas sus presentaciones")
    print("10. Conocer el promedio de goles de un equipo en mundiales")
    print("0. Salir")
    
    opcion = input("Ingrese el número de la opción que desea: ")
    
    if opcion == "1":
        pais = input("Ingrese el nombre del país: ")
        copas_ganadas = contar_copas_ganadas_por_pais(datos, pais)
        print(f"{pais} ha ganado {copas_ganadas} Copas Mundiales.")
    
    elif opcion == "2":
        pais = input("Ingrese el nombre del país: ")
        subcampeonatos = contar_subcampeonatos_por_pais(datos, pais)
        print(f"{pais} ha sido subcampeón {subcampeonatos} veces en la Copa Mundial.")
    
    elif opcion == "3":
        equipo = input("Ingrese el nombre del equipo: ")
        participaciones = contar_participaciones_equipo(datos, equipo)
        print(f"{equipo} ha participado en {participaciones} Copas Mundiales.")
    
    elif opcion == "4":
        num_copas_mundiales = contar_copas_mundiales(datos)
        print(f"Se han jugado un total de {num_copas_mundiales} Copas Mundiales.")
    
    elif opcion == "5":
        asistentes_totales = contar_asistentes_totales(datos)
        print(f"La cantidad total de asistentes a todas las ediciones de la Copa Mundial es: {asistentes_totales}")
    
    elif opcion == "6":
        finales_penales = contar_finales_penales(datos)
        print(f"Se han definido {finales_penales} finales de la Copa Mundial a través de una tanda de penales.")
    
    elif opcion == "7":
        equipo = input("Ingrese el nombre del equipo: ")
        goles_a_favor = contar_goles_a_favor(datos, equipo)
        print(f"{equipo} ha marcado un total de {goles_a_favor} goles en todas las ediciones de la Copa Mundial.")
    
    elif opcion == "8":
        equipo = input("Ingrese el nombre del equipo: ")
        goles_en_contra = contar_goles_en_contra(datos, equipo)
        print(f"{equipo} ha recibido un total de {goles_en_contra} goles en contra en todas las ediciones de la Copa Mundial.")
    
    elif opcion == "9":
        equipo = input("Ingrese el nombre del equipo: ")
        diferencia_goles = calcular_diferencia_goles(datos, equipo)
        print(f"La diferencia total de goles de {equipo} en todas sus participaciones es: {diferencia_goles}")
    
    elif opcion == "10":
        equipo = input("Ingrese el nombre del equipo: ")
        promedio_goles = calcular_promedio_goles(datos, equipo)
        print(f"El promedio de goles anotados por {equipo} en todas sus participaciones es: {promedio_goles}")
    
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")
