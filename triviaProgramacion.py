import random
import time
from operaciones import compruebaRespuesta, operacionRandom

questions = [
  {'pregunta' : '\033[33m Si utilizo el operador * tal se muestra en el código siguiente. ¿Cuál es el resultado obtenido?\n\n  \'dos\' * 3 \033[39m',
  'a': 'Seis',
  'b': '6',
  'c': 'dosdosdos',
  'd': 'dos3',
  'r': 'C',
  'x': 'dosdos',
  'contexto': '\033[32m Imprime \'dosdosdos\' \033[39m '},
  {'pregunta' : '\033[33m ¿Cuál es la salida que produce este bloque de código en python?\n\nx = 0\nwhile x < 3:\n   x = x + 1\nelse:\n   print(x) \033[39m',
  'a': '0',
  'b': '3',
  'c': '5',
  'd': '1',
  'r': 'B',
  'x': '2',
  'contexto': '\033[32m El resultado es 3 \033[39m'},
  {'pregunta' : '\033[33m ¿Cuál es la salida que produce este bloque de código en python?.\n\nfor num in range(5)\n   print(num) \033[39m',
  'a': '0,1,2,3,4,5',
  'b': '1,2,3,4',
  'c': '1,2,3,4,5',
  'd': '0,1,2,3,4',
  'r': 'D',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m Imprime 0,1,2,3,4 \033[39m'},
  {'pregunta' : '\033[33m ¿Qué números imprime el siguiente código en python?\n\nx = range(7, 15, 2)\nfor n in x:\n   print(x) \033[39m',
  'a': '7,9,11,13 y 15',
  'b': '9,11 y 13',
  'c': '7,9,11 y 13',
  'd': '9,11,13 y 15',
  'r': 'C',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m Imprime 7,9,11 y 13 \033[39m'},
  {'pregunta' : '\033[33m ¿Cuál es la salida que produce este bloque de código en python?\n\nx = 0\nwhile x < 3:\n   x = x + 1\nelse:\n   for n in range(x, x+3):\n      print(n) \033[39m',
  'a': '0,1 y 2',
  'b': '3,4 y 5',
  'c': '1,2 y 3',
  'd': '2,3 y 4',
  'r': 'B',
  'x': '3,4 y 6',
  'contexto': '\033[32m Imprime 3,4 y 5 \033[39m'},
  {'pregunta' : '\033[33m Complete la palabra reservada de python en el siguiente programa:\n\nx = 6\nif x < 0:\n   print("negativo")\n???? x == 0:\n   print("cero")\nelse:\n   print("positivo") \033[39m',
  'a': 'elif',
  'b': 'else',
  'c': 'elseif',
  'd': 'else if',
  'r': 'A',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m El comando es "elif" \033[39m'},
  {'pregunta' : '\033[33m ¿Qué elementos tendrá la lista después de la ejecución del siguiente código?\n\nlista =  [9, 35.2, "python"]\nlista.append("flask") \033[39m',
  'a': '["flask", 35.2, "python"]',
  'b': '[9, 35.2, "python","flask"]',
  'c': '["flask", 9, 35.2, "python"]',
  'd': '[9, 35.2,"flask"]',
  'r': 'B',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m Imprime [9, 35.2, "python","flask"] \033[39m'},
  {'pregunta' : '\033[33m ¿Cómo obtengo el elemento cuyo valor es "Django" de la lista list?\n\nlist = ["Ruby on Rails", "Laravel", "Django", "Zend Framework"] \033[39m',
  'a': 'list.pop(2, 1)',
  'b': 'list[2]',
  'c': 'list.pop(2)',
  'd': 'list[2:1]',
  'r': 'B',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m Para poder acceder al valor "Django" utilizamos list[2] \033[39m'},
  {'pregunta' : '\033[33m ¿Cuál de estos tipos de datos es mutable? \033[39m',
  'a': 'bool (Booleano)',
  'b': 'decimal',
  'c': 'float (Número de coma flotante)',
  'd': 'List',
  'r': 'D',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m Las listas son mutables \033[39m'},
  {'pregunta' : '\033[33m ¿Cuál de estos tipos de datos es inmutable? \033[39m',
  'a': 'diccionarios',
  'b': 'bytearrays',
  'c': 'sets',
  'd': 'Ninguno de los anteriores',
  'r': 'D',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m La respuesta es ninguna de las anteriores \033[39m'},
            ]

def triviaProgramacion(pts, nombre):
  playAgain = True

  for i in range(1, 6):
    time.sleep(1)
    print(f'Iniciamos en {6 - i} ...')
  
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

