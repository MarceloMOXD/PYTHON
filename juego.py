import pygame
import sys
from pygame import locals
import pandas as pd
import random

pygame.init()

# COLORES
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL_CIELO = (116,207,252)

#Creacion de pantallas
ancho_ventana = 720
alto_ventana = 580

pantalla_menu = pygame.display.set_mode((ancho_ventana, alto_ventana))
pantalla_niveles = pygame.display.set_mode((ancho_ventana, alto_ventana))
pantalla_partida = pygame.display.set_mode((ancho_ventana, alto_ventana))
pantalla_opciones = pygame.display.set_mode((ancho_ventana, alto_ventana))
pantalla_transicion = pygame.display.set_mode((ancho_ventana, alto_ventana))
pantalla_aciertos = pygame.display.set_mode((ancho_ventana, alto_ventana))

pygame.display.set_caption("Multiplicando con amigos")

fondo_menu = pygame.image.load("juego/imagenes/menu/menu_principal.jpg")
fondo_menu = pygame.transform.scale(fondo_menu, (ancho_ventana, alto_ventana))
fondo_menu_n = pygame.image.load("juego/imagenes/menu_nocturno/fondo_menu_nocturno.jpg")
fondo_menu_n = pygame.transform.scale(fondo_menu_n, (ancho_ventana, alto_ventana))

fondo_niveles = pygame.image.load("juego/imagenes/niveles/fondo_niveles.jpg")
fondo_niveles = pygame.transform.scale(fondo_niveles, (ancho_ventana, alto_ventana))
fondo_niveles_n = pygame.image.load("juego/imagenes/niveles_nocturno/fondo_niveles_n.jpg")
fondo_niveles_n = pygame.transform.scale(fondo_niveles_n, (ancho_ventana, alto_ventana))

fondo_opciones = pygame.image.load("juego/imagenes/opciones/fondo_opciones.jpg")
fondo_opciones = pygame.transform.scale(fondo_opciones, (ancho_ventana, alto_ventana))
fondo_opciones_n = pygame.image.load("juego/imagenes/opciones_nocturno/fondo_opciones_n.jpg")
fondo_opciones_n = pygame.transform.scale(fondo_opciones_n, (ancho_ventana, alto_ventana))

fondo_partida = pygame.image.load("juego/imagenes/partida/fondo_partida.jpg")
fondo_partida = pygame.transform.scale(fondo_partida, (ancho_ventana, alto_ventana))
fondo_partida_n = pygame.image.load("juego/imagenes/partida_nocturno/fondo_partida_n.jpg")
fondo_partida_n = pygame.transform.scale(fondo_partida_n, (ancho_ventana, alto_ventana))

fondo_aciertos = pygame.image.load("juego/imagenes/aciertos/fondo_aciertos.jpg")
fondo_aciertos = pygame.transform.scale(fondo_aciertos, (ancho_ventana, alto_ventana))
fondo_aciertos_n = pygame.image.load("juego/imagenes/aciertos_nocturno/fondo_aciertos_n.jpg")
fondo_aciertos_n = pygame.transform.scale(fondo_aciertos_n, (ancho_ventana, alto_ventana))

#imagenes aciertos
imagen_aciertos0 = pygame.image.load("juego/imagenes/aciertos/aciertos_0.png")
imagen_aciertos1 = pygame.image.load("juego/imagenes/aciertos/aciertos_1.png")
imagen_aciertos2 = pygame.image.load("juego/imagenes/aciertos/aciertos_2.png")
imagen_aciertos3 = pygame.image.load("juego/imagenes/aciertos/aciertos_3.png")
imagen_aciertos4 = pygame.image.load("juego/imagenes/aciertos/aciertos_4.png")
imagen_aciertos5 = pygame.image.load("juego/imagenes/aciertos/aciertos_5.png")
imagen_aciertos6 = pygame.image.load("juego/imagenes/aciertos/aciertos_6.png")
imagen_aciertos7 = pygame.image.load("juego/imagenes/aciertos/aciertos_7.png")
imagen_aciertos8 = pygame.image.load("juego/imagenes/aciertos/aciertos_8.png")
imagen_aciertos9 = pygame.image.load("juego/imagenes/aciertos/aciertos_9.png")
imagen_aciertos10 = pygame.image.load("juego/imagenes/aciertos/aciertos_10.png")
boton_intentarlo = pygame.image.load("juego/imagenes/aciertos/volver_a_intentarlo.png")

imagen_aciertos0_n = pygame.image.load("juego/imagenes/aciertos_nocturno/aciertos_0n.png")
imagen_aciertos1_n = pygame.image.load("juego/imagenes/aciertos_nocturno/aciertos_1n.png")
imagen_aciertos2_n = pygame.image.load("juego/imagenes/aciertos_nocturno/aciertos_2n.png")
imagen_aciertos3_n = pygame.image.load("juego/imagenes/aciertos_nocturno/aciertos_3n.png")
imagen_aciertos4_n = pygame.image.load("juego/imagenes/aciertos_nocturno/aciertos_4n.png")
imagen_aciertos5_n = pygame.image.load("juego/imagenes/aciertos_nocturno/aciertos_5n.png")
imagen_aciertos6_n = pygame.image.load("juego/imagenes/aciertos_nocturno/aciertos_6n.png")
imagen_aciertos7_n = pygame.image.load("juego/imagenes/aciertos_nocturno/aciertos_7n.png")
imagen_aciertos8_n = pygame.image.load("juego/imagenes/aciertos_nocturno/aciertos_8n.png")
imagen_aciertos9_n = pygame.image.load("juego/imagenes/aciertos_nocturno/aciertos_9n.png")
imagen_aciertos10_n = pygame.image.load("juego/imagenes/aciertos_nocturno/aciertos_10n.png")
boton_intentarlo_n = pygame.image.load("juego/imagenes/aciertos_nocturno/volver_a_intentarlo_n.png")

fuente_pregunta = pygame.font.Font("juego/fuente_letra/crayone.otf", 90)
font = pygame.font.Font(None, 28)

#funciones para reloj
reloj = pygame.time.Clock()
contador = 6000  # Inicializa el contador en 6000 segundos
imagen_reloj = pygame.image.load("juego/imagenes/partida/reloj.png")
imagen_reloj = pygame.transform.scale(imagen_reloj,(100,100))
reloj_rec = pygame.Rect(620,10,100,100)
def cronometro():
    texto_tiempo = f"{contador // 100:02d}"  # Muestra solo el contador con dos dígitos
    fuente_reloj = pygame.font.Font("juego/fuente_letra/digital.TTF", 40)
    superficie_texto_tiempo = fuente_reloj.render(texto_tiempo, True, (0, 0, 0))
    texto_rec = pygame.Rect(648,45,40,40)
    pantalla_partida.blit(imagen_reloj,reloj_rec)
    pygame.draw.rect(pantalla_partida, AZUL_CIELO, (648, 50, 50, 35))
    pantalla_partida.blit(superficie_texto_tiempo, texto_rec)
    reloj.tick(1.5 * 60)

def cargar_csv(csv_file):
    df = pd.read_csv(csv_file)
    return df

dataframe = cargar_csv("juego/datos_juego/preguntas_facil.csv")

def generar_pregunta(df, preguntas_anteriores):
    filas_disponibles = df.index.difference(preguntas_anteriores).tolist()
    if not filas_disponibles:
        return None, None, None, None
    fila_aleatoria = random.choice(filas_disponibles)
    preguntas_anteriores.append(fila_aleatoria)
    columna1, columna2, columna3, columna4, columna5 = df.loc[fila_aleatoria]
    # Cambiar de posición aleatoriamente
    if random.randint(0, 1) == 0:
        pregunta = f"{columna1} x {columna2} = ?"
        respuesta_correcta = str(columna3)
        respuesta_incorrecta1 = str(columna4)
        respuesta_incorrecta2 = str(columna5)
    else:
        pregunta = f"{columna2} x {columna1} = ?"
        respuesta_correcta = str(columna3)
        respuesta_incorrecta1 = str(columna5)
        respuesta_incorrecta2 = str(columna4)
    return pregunta, respuesta_correcta, respuesta_incorrecta1, respuesta_incorrecta2

def mostrar_pregunta(pregunta, aciertos):
    texto_pregunta = fuente_pregunta.render(pregunta, True, BLANCO)
    text_rect = pygame.Rect(120, 90, 300, 180)
    pantalla_partida.blit(texto_pregunta, text_rect)
    texto_aciertos = font.render(f"Aciertos: {aciertos}", True, (255, 255, 255))
    pantalla_partida.blit(texto_aciertos, (10, 10))

def cargar_fondo(ruta_imagen):
    fondo = pygame.image.load(ruta_imagen).convert()
    fondo = pygame.transform.scale(fondo, (720, 580))
    return fondo

def cambiar_pregunta(df, preguntas_anteriores):
    pregunta, respuesta_correcta, respuesta_incorrecta1, respuesta_incorrecta2 = generar_pregunta(df, preguntas_anteriores)
    mostrar_pregunta(pregunta, aciertos)
    return pregunta, respuesta_correcta, respuesta_incorrecta1, respuesta_incorrecta2

def mostrar_opcion(button_rect, button_image, button_text):
    pantalla_partida.blit(button_image, button_rect)
    button_texto_pregunta = font.render(button_text, True, (0, 0, 0))
    button_text_rect = button_texto_pregunta.get_rect(center=button_rect.center)
    pantalla_partida.blit(button_texto_pregunta, button_text_rect)

def verificar_respuesta(respuesta_seleccionada, respuesta_correcta):
    if respuesta_seleccionada == respuesta_correcta:
        return True
    return False

def mensaje_advertencia():
    mensaje_aviso = "Estas seguro de salir? se perdera tu progreso"
    superficie_mensaje = font.render(mensaje_aviso, True, NEGRO)
    rectangulo_mensaje = pygame.Rect(210, 120, 300, 300 )
    pygame.draw.rect(pantalla_partida, BLANCO, (50, 100, 600, 420))
    pygame.draw.rect(pantalla_partida, NEGRO, (50, 100, 600, 420), 5)
    salir_ad_rec = pygame.Rect(200,460,ancho_boton_partida,alto_boton_partida)
    continuar_ad_rec = pygame.Rect(400,460,ancho_boton_partida,alto_boton_partida)
    pantalla_partida.blit(superficie_mensaje,rectangulo_mensaje)
    pantalla_partida.blit(boton_salir,salir_ad_rec)
    pantalla_partida.blit(boton_continuar, continuar_ad_rec)
    if salir_ad_rec.collidepoint(event.pos):
        sonido_boton.play()
        return True
    if continuar_ad_rec.collidepoint(event.pos):
        sonido_boton.play()
    
        


preguntas_anteriores = []
aciertos = 0

pregunta, respuesta_correcta, respuesta_incorrecta1, respuesta_incorrecta2 = cambiar_pregunta(dataframe, preguntas_anteriores)
mostrar_pregunta(pregunta, aciertos)

# Tamaño de la barra de sonido
barra_ancho = ancho_ventana / 4
barra_alto = 4
barra_x = ancho_ventana - barra_ancho - 20
barra_y = alto_ventana - 50 - barra_alto

# Estado de la barra de sonido
punto_radio = 10
punto_x = 600
volumen = 5
pygame.mixer.music.set_volume(volumen)

# Estado de la barra de sonido
punto_radio_op = 10
punto_x_op = 400
volumen_boton = 5
pygame.mixer.music.set_volume(volumen_boton)

# Tamaño de la barra de sonido
barra_ancho_op = ancho_ventana / 4
barra_alto_op = 4
barra_x_op = ancho_ventana - barra_ancho_op - 230
barra_y_op = alto_ventana - 338 - barra_alto_op

# Estado de la barra de sonido
punto_radio_music = 10
punto_x_op_music = 400
volumen_musica = 5
pygame.mixer.music.set_volume(volumen_musica)

# Tamaño de la barra de sonido
barra_ancho_music = ancho_ventana / 4
barra_alto_music = 4
barra_x_music = ancho_ventana - barra_ancho_music - 230
barra_y_music = alto_ventana - 230 - barra_alto_music

# Función para dibujar la barra de sonido
def dibujar_barra_musica():
    pygame.draw.rect(pantalla_menu, NEGRO, (barra_x_music, barra_y_music, barra_ancho_music, barra_alto_music))  # Dibujar fondo de la barra
    pygame.draw.circle(pantalla_menu, BLANCO, (punto_x_op_music, barra_y_music + barra_alto_music / 2), punto_radio_music)  # Dibujar punto
    
# Función para dibujar la barra de sonido
def dibujar_barra_efectos_op():
    pygame.draw.rect(pantalla_menu, NEGRO, (barra_x_op, barra_y_op, barra_ancho_op, barra_alto_op))  # Dibujar fondo de la barra
    pygame.draw.circle(pantalla_menu, BLANCO, (punto_x_op, barra_y_op + barra_alto_op / 2), punto_radio_op)  # Dibujar punto
   
# Función para dibujar la barra de sonido
def dibujar_barra_sonido():
    pygame.draw.rect(pantalla_menu, NEGRO, (barra_x, barra_y, barra_ancho, barra_alto))  # Dibujar fondo de la barra
    pygame.draw.circle(pantalla_menu, BLANCO, (punto_x, barra_y + barra_alto / 2), punto_radio)  # Dibujar punto
    

    
# Carga de sonido y música
pygame.mixer.init()
sonido_boton = pygame.mixer.Sound("juego/sonidos/sonido_boton.mp3")
sonido_boton.set_volume(0.5)
musica = pygame.mixer.music.load("juego/sonidos/musica.mp3")
pygame.mixer.music.play(-1)



preguntas_anteriores = []
aciertos = 0
acierto = False
fallaste = False



# Definir dimensiones y posición de los botones
ancho_boton = 200
alto_boton = 50
ancho_boton_partida = 180
alto_boton_partida = 60
espacio_botones = 50
espacio_botones_partida = 10
pos_botones_x = (ancho_ventana - ancho_boton) / 2
pos_botones_y = (alto_ventana - (4 * alto_boton + 2 * espacio_botones)) / 2

# Cargar imágenes de los botones
#botones menu
boton_jugar = pygame.image.load("juego/imagenes/menu/boton_jugar.png")
boton_opciones = pygame.image.load("juego/imagenes/menu/boton_opciones.png")
boton_salir = pygame.image.load("juego/imagenes/menu/boton_salir.png")
boton_jugar = pygame.transform.scale(boton_jugar, (ancho_boton, alto_boton))
boton_opciones = pygame.transform.scale(boton_opciones, (ancho_boton, alto_boton))
boton_salir = pygame.transform.scale(boton_salir, (ancho_boton, alto_boton))
boton_jugar_n = pygame.image.load("juego/imagenes/menu_nocturno/boton_jugar_n.png")
boton_opciones_n = pygame.image.load("juego/imagenes/menu_nocturno/boton_opciones_n.png")
boton_salir_n = pygame.image.load("juego/imagenes/menu_nocturno/boton_salir_n.png")
boton_jugar_n = pygame.transform.scale(boton_jugar_n, (ancho_boton, alto_boton))
boton_opciones_n = pygame.transform.scale(boton_opciones_n, (ancho_boton, alto_boton))
boton_salir_n = pygame.transform.scale(boton_salir_n, (ancho_boton, alto_boton))

#botones niveles
boton_facil = pygame.image.load("juego/imagenes/niveles/boton_facil.png")
boton_facil_n = pygame.image.load("juego/imagenes/niveles_nocturno/boton_facil_n.png")
boton_medio = pygame.image.load("juego/imagenes/niveles/boton_medio.png")
boton_medio_n = pygame.image.load("juego/imagenes/niveles_nocturno/boton_medio_n.png")
boton_dificil = pygame.image.load("juego/imagenes/niveles/boton_dificil.png")
boton_dificil_n = pygame.image.load("juego/imagenes/niveles_nocturno/boton_dificil_n.png")
boton_volver = pygame.image.load("juego/imagenes/niveles/boton_volver.png")
boton_volver_n = pygame.image.load("juego/imagenes/niveles_nocturno/boton_volver_n.png")
boton_facil = pygame.transform.scale(boton_facil, (ancho_boton, alto_boton))
boton_facil_n = pygame.transform.scale(boton_facil_n, (ancho_boton, alto_boton))
boton_medio = pygame.transform.scale(boton_medio, (ancho_boton, alto_boton))
boton_medio_n = pygame.transform.scale(boton_medio_n, (ancho_boton, alto_boton))
boton_dificil = pygame.transform.scale(boton_dificil, (ancho_boton, alto_boton))
boton_dificil_n = pygame.transform.scale(boton_dificil_n, (ancho_boton, alto_boton))
boton_volver = pygame.transform.scale(boton_volver, (ancho_boton, alto_boton))
boton_volver_n = pygame.transform.scale(boton_volver_n, (ancho_boton, alto_boton))

#botones partida
boton_pista = pygame.image.load("juego/imagenes/partida/boton_pista.png")
boton_respuesta1 = pygame.image.load("juego/imagenes/partida/boton_respuesta1.png")
boton_respuesta2 = pygame.image.load("juego/imagenes/partida/boton_respuesta2.png")
boton_respuesta3 = pygame.image.load("juego/imagenes/partida/boton_respuesta3.png")

boton_salir_partida = pygame.image.load("juego/imagenes/partida/boton_salir_partida.png")

boton_pista = pygame.transform.scale(boton_pista, (120, 40))
boton_respuesta1 = pygame.transform.scale(boton_respuesta1, (ancho_boton_partida, alto_boton_partida))
boton_respuesta2 = pygame.transform.scale(boton_respuesta2, (ancho_boton_partida, alto_boton_partida))
boton_respuesta3 = pygame.transform.scale(boton_respuesta3, (ancho_boton_partida, alto_boton_partida))
boton_salir_partida = pygame.transform.scale(boton_salir_partida, (ancho_boton_partida, alto_boton))

#botones aciertos
boton_intentarlo = pygame.transform.scale(boton_intentarlo,(ancho_boton_partida,alto_boton_partida))

#botones opciones
boton_modo_oscuro = pygame.image.load("juego/imagenes/opciones/modo_oscuro.png")
efectos = pygame.image.load("juego/imagenes/opciones/efectos.png")
flecha_seleccion = pygame.image.load("juego/imagenes/opciones_nocturno/flecha_seleccion.png")


# Crear los rectángulos de los botones
boton_jugar_rec = pygame.Rect(pos_botones_x, pos_botones_y, ancho_boton,alto_boton)
boton_opciones_rec = pygame.Rect(pos_botones_x, boton_jugar_rec.bottom + espacio_botones, ancho_boton, alto_boton)
boton_salir_rec = pygame.Rect(pos_botones_x, boton_opciones_rec.bottom + espacio_botones, ancho_boton, alto_boton)

boton_facil_rec = pygame.Rect(pos_botones_x, pos_botones_y, ancho_boton,alto_boton)
boton_medio_rec = pygame.Rect(pos_botones_x, boton_facil_rec.bottom + espacio_botones, ancho_boton, alto_boton)
boton_dificil_rec = pygame.Rect(pos_botones_x, boton_medio_rec.bottom + espacio_botones, ancho_boton, alto_boton)
boton_volver_rec = pygame.Rect(20, 510, ancho_boton, alto_boton)

boton_pista_rec = pygame.Rect(580, 40, 120, 40)
boton_respuesta1_rec = pygame.Rect(40, 420, ancho_boton_partida, alto_boton)
boton_respuesta2_rec = pygame.Rect(240, 420, ancho_boton_partida, alto_boton)
boton_respuesta3_rec = pygame.Rect(440, 420, ancho_boton_partida, alto_boton)
boton_salir_partida_rec = pygame.Rect(20, 510, ancho_boton_partida, alto_boton)

boton_intentarlo_rec = pygame.Rect(520,500,ancho_boton_partida,alto_boton_partida)

efectos_rec = pygame.Rect(170,220,200,70)
boton_modo_oscuro_rec = pygame.Rect(200,400, 300,alto_boton)
flecha_seleccion_rec = pygame.Rect(460,390, 100,100)

# Estado de los botones
boton_jugar_expandir = False
boton_opciones_expandir = False
boton_salir_expandir = False

# Tamaño actual de los botones
boton_jugar_tam = ancho_boton, alto_boton
boton_opciones_tam = ancho_boton, alto_boton
boton_salir_tam = ancho_boton, alto_boton

boton_facil_tam = ancho_boton, alto_boton
boton_dificil_tam = ancho_boton, alto_boton
boton_volver_tam = ancho_boton, alto_boton

boton_modo_oscuro_tam = ancho_boton,alto_boton


#Mensaje y recuadro en caso de acertar o fallar
mensaje_acierto = "GENIAL, ACERTASTE!"
mensaje_fallaste = "Respuesta incorrecta:("
mensaje_tiempo = "Se te agoto el tiempo:("
rectangulo_mensaje = pygame.Rect(240, 120, 300, 300 )
imagen_acierto = pygame.image.load("juego/imagenes/partida/flecha_correcto.png")
imagen_acierto = pygame.transform.scale(imagen_acierto, (300, 300))
imagen_fallaste = pygame.image.load("juego/imagenes/partida/tacha_incorrecto.png")
imagen_fallaste = pygame.transform.scale(imagen_fallaste, (300, 300))
aciertofallo_rec = pygame.Rect(200,150,300,300)
boton_continuar = pygame.image.load("juego/imagenes/partida/boton_continuar.png")
boton_continuar_rec = pygame.Rect(260,460, ancho_boton_partida, alto_boton)



texto_botones = [str(respuesta_correcta), str(respuesta_incorrecta1), str(respuesta_incorrecta2)]
button_images = [
    pygame.image.load("juego/imagenes/partida/boton_respuesta1.png"),
    pygame.image.load("juego/imagenes/partida/boton_respuesta2.png"),
    pygame.image.load("juego/imagenes/partida/boton_respuesta3.png")
]

button_images_n = [
    pygame.image.load("juego/imagenes/partida_nocturno/boton_respuesta1_n.png"),
    pygame.image.load("juego/imagenes/partida_nocturno/boton_respuesta2_n.png"),
    pygame.image.load("juego/imagenes/partida_nocturno/boton_respuesta3_n.png")
]

random.shuffle(button_images)
button_rects = [
    button_images[0].get_rect(center=(160, 420)),
    button_images[1].get_rect(center=(360, 420)),
    button_images[2].get_rect(center=(560, 420))
]

#Salir de partida
mensaje_aviso = "Estas seguro de salir? se perdera tu progreso"
imagen_aviso = pygame.image.load("juego/imagenes/partida/pregunta.png")
imagen_aviso = pygame.transform.scale(imagen_aviso, (300, 300))
salir_ad_rec = pygame.Rect(120,460,ancho_boton_partida,alto_boton_partida)
continuar_ad_rec = pygame.Rect(400,460,ancho_boton_partida,alto_boton_partida)

# Variable para controlar la pantalla actual
pantalla_actual = "menu"
modo_oscuro = False
limite_tiempo = False
tiempo_agotado = False
modo_dificil = False
salir = False
facil = False
partida_iniciada = False

# Bucle principal del juego
while True:
    if partida_iniciada == True:
        if facil == False:
            if tiempo_agotado == False and salir == False:
                contador -= 1  # Resta 1 al contador en cada bucle
    if contador <= 0:
        contador = 0
        tiempo_agotado = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()  # Detiene la reproducción de la música
            sys.exit()
        # Verificar si se hizo clic en los botones
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pantalla_actual == "menu":
                if boton_jugar_rec.collidepoint(event.pos):
                    sonido_boton.play()
                    pantalla_actual = "niveles"
                elif boton_opciones_rec.collidepoint(event.pos):
                    sonido_boton.play()
                    pantalla_actual = "opciones"
                elif boton_salir_rec.collidepoint(event.pos):
                    sonido_boton.play()
                    sys.exit()
            elif pantalla_actual == "niveles":
                contador += 1
                preguntas_anteriores = []
                limite_tiempo = False
                aciertos = 0
                facil = False
                salir = False
                modo_dificil = False
                if boton_facil_rec.collidepoint(event.pos):
                    partida_iniciada = False
                    limite_tiempo = False
                    tiempo_agotado = False
                    facil = True
                    contador = 6000
                    dataframe = cargar_csv("juego/datos_juego/preguntas_facil.csv")
                    pregunta, respuesta_correcta, respuesta_incorrecta1, respuesta_incorrecta2 = cambiar_pregunta(dataframe, preguntas_anteriores)
                    sonido_boton.play()
                    pantalla_actual = "partida"
                if boton_medio_rec.collidepoint(event.pos):
                    partida_iniciada = True
                    limite_tiempo = True
                    contador = 6000
                    dataframe = cargar_csv("juego/datos_juego/preguntas_medio.csv")
                    pregunta, respuesta_correcta, respuesta_incorrecta1, respuesta_incorrecta2 = cambiar_pregunta(dataframe, preguntas_anteriores)
                    sonido_boton.play()
                    pantalla_actual = "partida"
                if boton_dificil_rec.collidepoint(event.pos):
                    partida_iniciada = True
                    modo_dificil = True
                    limite_tiempo = True
                    contador = 3000
                    dataframe = cargar_csv("juego/datos_juego/preguntas_dificil.csv")
                    pregunta, respuesta_correcta, respuesta_incorrecta1, respuesta_incorrecta2 = cambiar_pregunta(dataframe, preguntas_anteriores)
                    sonido_boton.play()
                    pantalla_actual = "partida"
                if boton_volver_rec.collidepoint(event.pos):
                    sonido_boton.play()
                    pantalla_actual = "menu"
            elif pantalla_actual == "opciones":
                if boton_modo_oscuro_rec.collidepoint(event.pos):
                    sonido_boton.play()
                    if modo_oscuro == False:
                        modo_oscuro = True
                    else:
                        modo_oscuro = False
                if boton_volver_rec.collidepoint(event.pos):
                    sonido_boton.play()
                    pantalla_actual = "menu"
            elif pantalla_actual == "partida":
                partida_iniciada = True
                if salir == True:
                    if salir_ad_rec.collidepoint(event.pos):
                        sonido_boton.play()
                        pantalla_actual = "niveles"
                    if continuar_ad_rec.collidepoint(event.pos):
                        salir = False
                        sonido_boton.play()
                if boton_pista_rec.collidepoint(event.pos):
                    sonido_boton.play()
                if boton_volver_rec.collidepoint(event.pos):
                    sonido_boton.play()
                    salir = True
                for i, button_rect in enumerate(button_rects):
                    if button_rect.collidepoint(event.pos):
                        respuesta_seleccionada = texto_botones[i]
                        if verificar_respuesta(respuesta_seleccionada, respuesta_correcta):
                            aciertos += 1
                            acierto = True #Respuesta correcta
                        else:
                            fallaste = True #Respuesta incorrecta
                    if boton_continuar_rec.collidepoint(event.pos):
                        acierto = False
                        fallaste = False
                        tiempo_agotado = False
                        if salir == False:
                            if modo_dificil == True:
                                contador = 3000
                            else:
                                contador = 6000
                        pregunta, respuesta_correcta, respuesta_incorrecta1, respuesta_incorrecta2 = cambiar_pregunta(dataframe, preguntas_anteriores)
                        if pregunta is None:
                            done = True  # No hay más preguntas disponibles
                            pantalla_actual = "aciertos"
                            break
                        texto_botones = [str(respuesta_correcta), str(respuesta_incorrecta1), str(respuesta_incorrecta2)]
                        if modo_oscuro == True:
                            random.shuffle(button_images_n)
                        else:
                            random.shuffle(button_images)
                        random.shuffle(button_rects)
                        break
            elif pantalla_actual == "aciertos":
                preguntas_anteriores = []
                pregunta, respuesta_correcta, respuesta_incorrecta1, respuesta_incorrecta2 = cambiar_pregunta(dataframe, preguntas_anteriores)
                if boton_volver_rec.collidepoint(event.pos):
                    tiempo_agotado = False
                    aciertos = 0
                    sonido_boton.play()
                    pantalla_actual = "niveles"
                if boton_intentarlo_rec.collidepoint(event.pos):
                    sonido_boton.play()
                    preguntas_anteriores = []
                    aciertos = 0
                    tiempo_agotado = False
                    if facil == False:
                        limite_tiempo = True
                        if modo_dificil == True:
                            contador = 3000
                        else:
                            contadro = 6000
                    pantalla_actual = "partida"
        # Actualizar el volumen en función de la posición del punto en la barra de sonido
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            if barra_x <= event.pos[0] <= barra_x + barra_ancho:
                punto_x = event.pos[0]
                volumen = (punto_x - barra_x) / barra_ancho
                volumen_boton *= volumen
                pygame.mixer.music.set_volume(volumen)
                sonido_boton.set_volume(volumen_boton)
            if barra_x_op <= event.pos[0] <= barra_x_op + barra_ancho_op:
                punto_x_op = event.pos[0]
                volumen_boton = (punto_x_op - barra_x_op) / barra_ancho_op
                sonido_boton.set_volume(volumen_boton)

    
    if pantalla_actual == "menu":
        if modo_oscuro == False:
            pantalla_menu.blit(fondo_menu, (0, 0))  # Dibujar fondo de pantalla_menu
            pantalla_menu.blit(boton_jugar, boton_jugar_rec)
            pantalla_menu.blit(boton_opciones, boton_opciones_rec)
            pantalla_menu.blit(boton_salir, boton_salir_rec)
        else:
            pantalla_menu.blit(fondo_menu_n, (0, 0))  # Dibujar fondo de pantalla_menu
            pantalla_menu.blit(boton_jugar_n, boton_jugar_rec)
            pantalla_menu.blit(boton_opciones_n, boton_opciones_rec)
            pantalla_menu.blit(boton_salir_n, boton_salir_rec)
        dibujar_barra_sonido()  # Dibujar la barra de sonido
        pygame.display.update()

    elif pantalla_actual == "niveles":
        if modo_oscuro == False:
            pantalla_niveles.blit(fondo_niveles, (0, 0))  # Dibujar fondo de pantalla_niveles
            pantalla_niveles.blit(boton_facil, boton_facil_rec)
            pantalla_niveles.blit(boton_medio, boton_medio_rec)
            pantalla_niveles.blit(boton_dificil, boton_dificil_rec)
            pantalla_niveles.blit(boton_volver, boton_volver_rec)
        else:
            pantalla_niveles.blit(fondo_niveles_n, (0, 0))  # Dibujar fondo de pantalla_niveles
            pantalla_niveles.blit(boton_facil_n, boton_facil_rec)
            pantalla_niveles.blit(boton_medio_n, boton_medio_rec)
            pantalla_niveles.blit(boton_dificil_n, boton_dificil_rec)
            pantalla_niveles.blit(boton_volver_n, boton_volver_rec)
        dibujar_barra_sonido()
        pygame.display.update()
    elif pantalla_actual == "opciones":
        if modo_oscuro == False:
            pantalla_opciones.blit(fondo_opciones, (0, 0))  # Dibujar fondo de pantalla_opciones
            pantalla_opciones.blit(boton_volver, boton_volver_rec)
            pantalla_opciones.blit(boton_modo_oscuro,boton_modo_oscuro_rec)
        else:
            pantalla_opciones.blit(fondo_opciones_n, (0, 0))
            pantalla_opciones.blit(boton_volver_n, boton_volver_rec)
            pantalla_opciones.blit(boton_modo_oscuro,boton_modo_oscuro_rec)
            pantalla_opciones.blit(flecha_seleccion,flecha_seleccion_rec)
        dibujar_barra_efectos_op()
        
        pantalla_opciones.blit(efectos,efectos_rec)
        dibujar_barra_sonido()
        pygame.display.update()
    elif pantalla_actual == "partida":
        texto_botones = [str(respuesta_correcta), str(respuesta_incorrecta1), str(respuesta_incorrecta2)]
        if modo_oscuro == True:
            pantalla_partida.blit(fondo_partida_n,(0,0))
            for i, button_rect in enumerate(button_rects):
                mostrar_opcion(button_rect, button_images_n[i], texto_botones[i])
        else:
            pantalla_partida.blit(fondo_partida,(0, 0))
            for i, button_rect in enumerate(button_rects):
                mostrar_opcion(button_rect, button_images[i], texto_botones[i])
        mostrar_pregunta(pregunta, aciertos)
        
        if acierto == True:
            superficie_mensaje = font.render(mensaje_acierto, True, NEGRO)
            rectangulo_mensaje = pygame.Rect(240, 120, 300, 300 )
            pygame.draw.rect(pantalla_partida, BLANCO, (50, 100, 600, 420))
            pygame.draw.rect(pantalla_partida, NEGRO, (50, 100, 600, 420), 5)
            pantalla_partida.blit(superficie_mensaje,rectangulo_mensaje)
            pantalla_partida.blit(imagen_acierto,aciertofallo_rec)
            pantalla_partida.blit(boton_continuar, boton_continuar_rec)
        elif fallaste == True:
            acierto -= 1
            superficie_mensaje = font.render(mensaje_fallaste, True, NEGRO)
            rectangulo_mensaje = pygame.Rect(240, 120, 300, 300 )
            pygame.draw.rect(pantalla_partida, BLANCO, (50, 100, 600, 420))
            pygame.draw.rect(pantalla_partida, NEGRO, (50, 100, 600, 420), 5)
            pantalla_partida.blit(superficie_mensaje,rectangulo_mensaje)
            pantalla_partida.blit(imagen_fallaste,aciertofallo_rec)
            pantalla_partida.blit(boton_continuar, boton_continuar_rec)
        elif tiempo_agotado == True:
            superficie_mensaje = font.render(mensaje_tiempo, True, NEGRO)
            rectangulo_mensaje = pygame.Rect(210, 120, 300, 300 )
            pygame.draw.rect(pantalla_partida, BLANCO, (50, 100, 600, 420))
            pygame.draw.rect(pantalla_partida, NEGRO, (50, 100, 600, 420), 5)
            pantalla_partida.blit(superficie_mensaje,rectangulo_mensaje)
            pantalla_partida.blit(imagen_fallaste,aciertofallo_rec)
            pantalla_partida.blit(boton_continuar, boton_continuar_rec)
        if limite_tiempo == True:
            cronometro()
        pantalla_partida.blit(boton_salir_partida, boton_salir_partida_rec)
        if salir == True:
            superficie_mensaje = font.render(mensaje_aviso, True, NEGRO)
            rectangulo_mensaje = pygame.Rect(150, 120, 300, 300 )
            pygame.draw.rect(pantalla_partida, BLANCO, (50, 100, 600, 420))
            pygame.draw.rect(pantalla_partida, NEGRO, (50, 100, 600, 420), 5)
            pantalla_partida.blit(superficie_mensaje,rectangulo_mensaje)
            pantalla_partida.blit(boton_salir,salir_ad_rec)
            pantalla_partida.blit(imagen_aviso,aciertofallo_rec)
            pantalla_partida.blit(boton_continuar, continuar_ad_rec)
        dibujar_barra_sonido()
        pygame.display.update()
    elif pantalla_actual == "aciertos":
        if modo_oscuro == True:
            pantalla_aciertos.blit(fondo_aciertos_n,(0,0))
            if aciertos == 0:
                pantalla_aciertos.blit(imagen_aciertos0_n,(0,0))
            elif aciertos == 1:
                pantalla_aciertos.blit(imagen_aciertos1_n,(0,0))
            elif aciertos == 2:
                pantalla_aciertos.blit(imagen_aciertos2_n,(0,0))
            elif aciertos == 3:
                pantalla_aciertos.blit(imagen_aciertos3_n,(0,0))
            elif aciertos == 4:
                pantalla_aciertos.blit(imagen_aciertos4_n,(0,0))
            elif aciertos == 5:
                pantalla_aciertos.blit(imagen_aciertos5_n,(0,0))
            elif aciertos == 6:
                pantalla_aciertos.blit(imagen_aciertos6_n,(0,0))
            elif aciertos == 7:
                pantalla_aciertos.blit(imagen_aciertos7_n,(0,0))
            elif aciertos == 8:
                pantalla_aciertos.blit(imagen_aciertos8_n,(0,0))
            elif aciertos == 9:
                pantalla_aciertos.blit(imagen_aciertos9_n,(0,0))
            elif aciertos == 10:
                pantalla_aciertos.blit(imagen_aciertos10_n,(0,0))
            pantalla_aciertos.blit(boton_intentarlo_n,boton_intentarlo_rec)
        else:
            pantalla_aciertos.blit(fondo_aciertos,(0,0))
            if aciertos == 0:
                pantalla_aciertos.blit(imagen_aciertos0,(0,0))
            elif aciertos == 1:
                pantalla_aciertos.blit(imagen_aciertos1,(0,0))
            elif aciertos == 2:
                pantalla_aciertos.blit(imagen_aciertos2,(0,0))
            elif aciertos == 3:
                pantalla_aciertos.blit(imagen_aciertos3,(0,0))
            elif aciertos == 4:
                pantalla_aciertos.blit(imagen_aciertos4,(0,0))
            elif aciertos == 5:
                pantalla_aciertos.blit(imagen_aciertos5,(0,0))
            elif aciertos == 6:
                pantalla_aciertos.blit(imagen_aciertos6,(0,0))
            elif aciertos == 7:
                pantalla_aciertos.blit(imagen_aciertos7,(0,0))
            elif aciertos == 8:
                pantalla_aciertos.blit(imagen_aciertos8,(0,0))
            elif aciertos == 9:
                pantalla_aciertos.blit(imagen_aciertos9,(0,0))
            elif aciertos == 10:
                pantalla_aciertos.blit(imagen_aciertos10,(0,0))
            pantalla_aciertos.blit(boton_intentarlo,boton_intentarlo_rec)
        pantalla_aciertos.blit(boton_salir_partida, boton_salir_partida_rec)
        pygame.display.update()

pygame.quit()
