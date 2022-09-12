from operaciones import compruebaRespuesta
from triviaCulturaGeneral import triviaCulturaGeneral
from triviaProgramacion import triviaProgramacion
from triviaRandom import triviaRandom
import random

area = ['Cultura general', 'Programación con python', 'Random']

def startTrivia(userName):

  puntosCG = 0
  puntosP = 0
  puntosR = 0

  print("Instrucciones: \n - Elige un área de preguntas para medir tus conocimientos\n - Por cada área se te asignará dará un puntaje aleatorio\n - Lee atentamente las preguntas y posibles respuestas.\n - Responde las  preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta.\n")

  endGame = False
  while( not endGame):

    print('¿Estas listo?\n')
    isReady = compruebaRespuesta()  
    
    if isReady == 'SI':  

      estado = True
      while(estado):

        questionArea = input(f'Escoge un área de preguntas:\n\n a) {area[0]} \n b) {area[1]}\n c) {area[2]}\n\nTu respuesta: ').upper()
        print('')

        if questionArea == 'A':
          puntosCG = random.randint(0, 10)
          print(f'Tu puntaje inicial es de {puntosCG}\n')
          puntosCG = triviaCulturaGeneral(puntosCG, userName)
          
          print('¿Desea escoger otra área de preguntas?\n')
          playAgain = compruebaRespuesta()

          if playAgain == 'NO':

            print('Finalizando el juego y cargando datos ...\n')
            estado = False
            endGame = True
          
        elif questionArea == 'B':
          
          puntosP = random.randint(0, 10)
          print(f'Tu puntaje inicial es de {puntosP}')
          puntosP = triviaProgramacion(puntosP, userName)

          print('¿Desea escoger otra área de preguntas?\n')
          playAgain = compruebaRespuesta()

          if playAgain == 'NO':

            print('Finalizando el juego y cargando datos ...\n')
            estado = False
            endGame = True
            
        elif questionArea == 'C':
          
          puntosR = random.randint(0, 10)
          print(f'Tu puntaje inicial es de {puntosR}')
          puntosR = triviaRandom(puntosR, userName)

          print('¿Desea escoger otra área de preguntas?\n')
          playAgain = compruebaRespuesta()

          if playAgain == 'NO':
            print('Finalizando el juego y cargando datos ...\n')
            estado = False
            endGame = True
            
        else:
          print('Ingrese una opción válida\n')

    else: 
      print('No hay problema\n')

  datos = puntosCG + puntosP + puntosR

  return datos

