import random
import time
from operaciones import compruebaRespuesta
from startTrivia import startTrivia


gameOver = False

while (not gameOver):
  intento = 0
  print ("\nBienvenido a la trivia \"Midiendo Conocimientos\"\n")
  print ("Donde pondremos a prueba tus conocimientos en diferentes temas\n¿Empezamos?\n")

  startToPlay = compruebaRespuesta()

  if startToPlay == 'SI':
    
    userName = input("Ingresa tu nombre: ")
    time.sleep(2)
    print(f"\nUn gusto conocerte {userName}, te explico un poco la dinamica de la trivia. Empezaras con una cantidad de puntaje y si aciertas en las respuestas se sumarán 10 pts y si fallas se te descontarán una cantidad aleatoria de pts. Asi también, existen algunas respuestas secretas que son las mas cercanas a la correcta y si logras adivinarlas se te sumarán una cantidad aleatoria de pts. Espero que puedas obtener el mayor número de puntaje. ¡Suerte {userName}!\n")

    playAgain = True
    while(playAgain):

      intento += 1
      print(f'Intento número {intento}\n')
      time.sleep(5)

      puntajeTotal = startTrivia(userName)

      #Implementamos un bono extra con ruleta random
      time.sleep(2)
      print('Girando ruleta para un bono extra de puntos\n')
      bonoExtra = random.randint(0, 10)
      puntajeTotal += bonoExtra

      for i in range(1, 6):
        time.sleep(1)
        print('Girando ...')
      
      print(f'Listo {userName}, se te a dado un bono de {bonoExtra} pts.\nPor lo que tu puntaje total es de: {puntajeTotal}\n')

      print(f'{userName}, ¿Deseas realizar un intento más?\n')

      oneMore = compruebaRespuesta()
      if oneMore == 'SI':
        puntajeTotal = 0

      elif oneMore == 'NO':
        print(f"\nEspero {userName} que lo hayas pasado bien, hasta pronto!")
        playAgain = False
    
  elif startToPlay == 'NO':
    print('Ok')
    gameOver = True
