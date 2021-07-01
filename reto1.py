import sys
def calcular_distancia_y_tiempo_a_estrella():
    
    alpha_centauri = 4.36
    anio_luz = 9460730472580.8
    distancia_centauri_km = alpha_centauri * anio_luz
    sonda_solar_parker = 430000
    milla_a_km = 1.60934
    sonda_solar_km_hora = sonda_solar_parker * milla_a_km
    # velocidad_luz = 299792.458
    # segundos_a_hora = 60*60
    # velocidad_luz_km_por_hora = velocidad_luz * segundos_a_hora
    anios_distancia = int((((distancia_centauri_km / sonda_solar_km_hora) / 24) / 365))
    print(anios_distancia)
    
    print(f'La distancia a alpha centauri es {alpha_centauri} años luz, lo que equivale a {distancia_centauri_km} kilometros')
    print(f'La sonda solar parker viaja a {sonda_solar_parker} m/h, y equivale a {sonda_solar_km_hora} km/h')
    print(f'La sonda solar parker llegaria a alpha centauri en {anios_distancia} años aproximadamente')
    
    caso = input('Deseas conocer los datos de una estrella diferente??\nmarca\n1. Si\n2. No\n-> ')
    if caso == '1':
        try:
            a = float(input("Ingrese la distancia a la estrella en años luz\n-> "))
            b = float(input("Ingrese la velocidad de la sonda espacial en m/h\n-> "))
           
        except ValueError:
            print("Error, digite un número")
        
        
        distance_star_km = a * anio_luz
        sonda_espacial_km = b * milla_a_km
        tiempo_a_estrella = int((((distance_star_km / sonda_espacial_km) / 24) / 365))
        print(f'La distancia a la estrella es {a} años luz, lo que equivale a {distance_star_km} kilometros')
        print(f'La sonda viaja a {b} m/h y equivale a {sonda_espacial_km} km/h')
        print(f'La sonda espacial llegaria a la estrealla en {tiempo_a_estrella} años aproximadamente')
        
    else:
        print('Hasta pronto')
        sys.exit()
        
res= calcular_distancia_y_tiempo_a_estrella()
