#Ejercicio clase 2
print (f'Estas en un bosque sin recursos y encuentras un CUCHILLO , un PEDERNAL y una BENGALA ¿Cual escoges?')
respuesta = input(f'Escribe tu eleccion: ')
respuesta_minuscula = respuesta.lower()
if respuesta_minuscula == 'cuchillo':
    print (f'Tomaste el cuchillo y encontraste una cuerda parar armar tu refugio')
    respuesta2 = input(f'¿Quieres BUSCAR materiales o DESCANSAR?: ')
    respuesta2 = respuesta2.lower()
    if respuesta2 == 'buscar':
        print(f'Buscando materiales encontraste una cabaña abandonada donde puedes pasar la noche')
    else: print (f'Te quedaste descansando y te alcanzo la inundacion de un rio')   


elif respuesta_minuscula == 'pedernal': 
    print (f'Tomaste el pedernal y armaste una fogata para espantar depredadores')
    respuesta3 = input(f'¿Quieres CAZAR tu comida o FABRICAR agua potable?: ')
    respuestamin = respuesta3.lower()
    if respuestamin == 'cazar': 
       print (f'Encontraste un rio repleto de peces gigantes pero no eres buen pescador')
    else: print (f'Afortunadamente comenzo a llover y pudiste almacenar agua para los proximos dias')   

elif respuesta_minuscula == 'bengala':
    print (f'Tomaste la bengala, puedes usarla para tener mayor visibilidad durante la noche')
    respuesta4 = input(f'¿Quieres USAR la bengala esta noche o ESPERAR el momento adecuado?: ')
    respuestam = respuesta4.lower()
    if respuestam == 'usar': 
        print (f'Usaste la bengala y pudiste observar todo a tu alrededor estando alerta')
    else: print (f'Decidiste esperar y tu olor atrajo a un puma durante la noche asi que fuiste devorado')   
else: print (f'No escogiste una opcion valida >:(')    