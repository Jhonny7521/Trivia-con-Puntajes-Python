import random
import time

from operaciones import compruebaRespuesta, operacionRandom

questions = [
  {'pregunta' : '\033[33m ¿Quién tiene más seguidores en Instagram?\033[39m',
  'a': 'Selena Gomez',
  'b': 'Taylor Swift',
  'c': 'Cristiano Ronaldo',
  'd': 'Lisa',
  'r': 'C',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m Tiene 369 millones de seguidores en IG! \033[39m'},
  {'pregunta' : '\033[33m ¿Cuántos huesos hay en el cuerpo humano?\033[39m',
  'a': '306',
  'b': '206',
  'c': '106',
  'd': '406',
  'r': 'B',
  'x': '205',
  'contexto': '\033[32m 206 y teníamos aún más cuando aún éramos jóvenes. \033[39m'},
  {'pregunta' : '\033[33m ¿Cómo se llama el órgano que utilizan los peces para respirar?\033[39m',
  'a': 'Pulmones',
  'b': 'Cola',
  'c': 'Escalas',
  'd': 'Agallas',
  'r': 'D',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m Las Agallas son sus pulmones \033[39m'},
  {'pregunta' : '\033[33m ¿Qué deporte se considera el pasatiempo americano?\033[39m',
  'a': 'Béisbol',
  'b': 'Baloncesto',
  'c': 'Golf',
  'd': 'Boxeo',
  'r': 'A',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m El Béisbol es su pasatiempo favorito! \033[39m'},
  {'pregunta' : '\033[33m ¿Cómo se llamaba la primera película de perros de la historia?\033[39m',
  'a': 'Cats and Dogs',
  'b': 'Lassie Come Home',
  'c': 'Hotels for Dogs',
  'd': 'Alpha',
  'r': 'B',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m Lassie se dio a conocer en 1943. \033[39m'},
  {'pregunta' : '\033[33m ¿Cómo se llama el hombre que está detrás de Mr. Bean?\033[39m',
  'a': 'Rowan Atkinson',
  'b': 'James Corden',
  'c': 'Rowan Smyth',
  'd': 'Macaulay Culkin',
  'r': 'A',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m Rowan Atkinson, aparte de Mr. Bean, también es famoso por Sr. Inglés \033[39m'},
  {'pregunta' : '\033[33m ¿Cuántas películas componen la serie de Indiana Jones?\033[39m',
  'a': '6',
  'b': '5',
  'c': '4',
  'd': '2',
  'r': 'C',
  'x': '3',
  'contexto': '\033[32m La colección de cuatro películas de Indiana Jones estaba compuesta por Indiana Jones y el Reino de la Calavera de Cristal, Indiana Jones y la Última Cruzada, Indiana Jones y los Cazadores del Arca Perdida, Indiana Jones y el Templo de la Perdición. \033[39m'},
  {'pregunta' : '\033[33m ¿Cuál fue el primer nombre acuñado para el helado?\033[39m',
  'a': 'Gelato',
  'b': 'Ensalada',
  'c': 'Agitar',
  'd': 'Sundae',
  'r': 'A',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m Los gelatos se inventaron en Italia! \033[39m'},
  {'pregunta' : '\033[33m ¿Cuántos volcanes activos hay en el mundo?\033[39m',
  'a': '1450',
  'b': '1400',
  'c': '1360',
  'd': '1350',
  'r': 'D',
  'x': '1340',
  'contexto': '\033[32m Son 1350 y estos son los únicos activos registrados \033[39m'},
  {'pregunta' : '\033[33m ¿Cuál es la isla más grande del mundo?\033[39m',
  'a': 'Australia',
  'b': 'Filipinas',
  'c': 'Groenlandia',
  'd': 'Rusia',
  'r': 'C',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m Groenlandia es la mayor extensión de tierra del mundo con 2.166.086 km2. \033[39m'},
            ]

def triviaRandom(pts, nombre):
  playAgain = True

  for i in range(1, 6):
    time.sleep(1)
    print(f'Iniciamos en {i} ...')
  
  print(f'\nMucha suerte {nombre}\n')

  while(playAgain):
    puntaje = pts
    feedback = []    
    
    for i in range (0, len(questions)):

      print(f'Pregunta {i + 1}: {questions[i]["pregunta"]}\n\n a) {questions[i]["a"]}\n b) {questions[i]["b"]}\n c) {questions[i]["c"]}\n d) {questions[i]["d"]}\n' )

      isCorrect = False
      while(not isCorrect):

        respuesta = input('Tu respuesta: ').upper()
        if respuesta == 'A' or respuesta == 'B' or respuesta == 'C' or respuesta == 'D': 

          isCorrect = True
          if respuesta == questions[i]["r"]:

            puntaje *= 2
            print(f'\033[32m ¡Correcto {nombre}!, \033[39m {questions[i]["contexto"]}')
            print(f'\033[32m Se te duplicaron los pts, puntaje acumulado: {puntaje} \033[39m \n\n-------- SIGUIENTE --------\n')
            dato = f'Pregunta {i + 1}: \033[32m correcta \033[39m'
            feedback.append(dato)
            time.sleep(2)

          else:
            # descuento = random.randint(0, 10)
            # puntaje -= descuento
            puntaje, message = operacionRandom(puntaje)

            print(f'\033[31m ¡Respuesta incorrecta {nombre}! \033[39m ')
            print(f'\033[31m Se te ha {message}, puntaje acumulado: {puntaje} \033[39m \n\n-------- SIGUIENTE --------\n')
            dato = f'Pregunta {i + 1}: \033[31m incorrecta \033[39m'
            feedback.append(dato)
            time.sleep(2)

        elif respuesta == questions[i]["x"]:

          isCorrect = True
          aumento = random.randint(0, 10)
          puntaje += aumento

          print(f'\033[36m Que tino de suerte {nombre}, no era la correcta pero es lo más cercano a la respuesta correcta.\nSe te sumaron {aumento} pts, puntaje acumulado: {puntaje} \033[39m \n\n-------- SIGUIENTE --------\n')
          dato = f'Pregunta {i + 1}: \033[35m muy cerca \033[39m'
          feedback.append(dato)
          time.sleep(2)

        else: 
          print('Ingrese una alternativa correcta\n')

    print(f'Tu puntaje total es {puntaje}\n\n ¿Deseas ver tus respuestas?')
    
    estado = True
    while(estado):

      showAnswersisReady = compruebaRespuesta()
      print('')

      if showAnswersisReady == 'SI':
        time.sleep(2)
        for i in range(0, len(feedback)):
          print(feedback[i])
        print('')
      estado = False
      time.sleep(2)

    print('¿Deseas volver a jugar?\n')
    
    isReady = compruebaRespuesta()
    
    if isReady == 'SI':
      print('Reiniciando la trivia ... \n')
      time.sleep(4)

    elif isReady == 'NO':
      playAgain = False

  return puntaje