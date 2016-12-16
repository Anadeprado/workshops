#!/usr/bin/python
# -*- coding: utf-8 -*-
# Las lineas anteriores son xa q python reconozca acentos

# Para ejecutar este script:
#      >>> python3 aventura.py

print("¡Hola robonauta! Bienvenida a tu propia aventura...\n\n")

print("Érase una vez...")
print ("""
    Un pirata iba navegando por los mares del sur. Estaba un poco cansado por lo
    que desembarcó en una preciosa isla para descansar...
    """)

capitulo = 1

# Repite todas estas instrucciones como si fuese un bucle infinito:
while(True):

    if capitulo == 1:
        print ("""
        ----------------------------
        ¿Qué quieres hacer piratilla?
        ----------------------------
        \t A- Dormir la mona.
        \t B- Volver al mar.
        \t C- Explorar la isla.
        \t W- Salir de esta estúpida aventura \n
        \n
        """)
        respuesta = input(">> "); # Respuesta del usuario

        if respuesta == 'A':
            print("ZZzz.....")
            print("Sueñas en la playa hasta que... ¡Te despierta un cangrejo!")
            # No cambiamos de capítulo

        elif respuesta == 'B':
            print("Pues nada... ¡Chao pescao!")
            capitulo = 999

        elif respuesta == 'C':
            print ("""
            Te adentras en la frondosa selva que rodea la playa. \n
            Muy bien, muy valiente. Te has perdido. \n \n
            Mientras lloras a moco tendido llamando a mamá, aparece un mono
            y te dice:""")
            capitulo = 2

        else: #Cualquier otra respuesta es SALIR
            capitulo = 999

    elif capitulo == 2:
        print ("""\n
        - ¡Hola monada! ^^\n

        ----------------------------------
        ¿Qué le respondes al monito?
        ----------------------------------
        \t A- No soy una monada... ¬¬
        \t B- ¿Cómo sabes que soy MUJER??
        \t C- ¿Dónde está el tesoro perdido?
        \t W- Salir de esta estúpida aventura \n
        \n
        """)
        respuesta = input(">> "); # Respuesta del usuario

        if respuesta == 'A':
            print("El mono se queda pensativo un rato y se olvida de ti.")
            print("Te aburres y vuelves a la playa.")
            capitulo = 1

        elif respuesta == 'B':
            print("Porque me lo ha soplado Anita antes. Así que...")

        elif respuesta == 'C':
            capitulo = 3

        else: #Cualquier otra respuesta es SALIR
            capitulo = 999

    elif capitulo == 3:
        print("El monito te sopla dónde está escondido el tesoro.")
        print(" \n\n\n >>> MUY BIEEEEEN FINAL FELIZ!!!! <<< \n\n\n ")
        print("...bueno... ejem... si consigues volver al barco.")

    #Capítulo 999 significa SALIR
    elif capitulo == 999:

        print ("""
        \n\n o==|=======> T H E   E N D <=======|==0 \n\n
        """)
        break #Salir
