import random
import time

from operaciones import compruebaRespuesta, operacionRandom

questions = [
  {'pregunta' : '\033[33m ¿Cuántos litros de sangre tiene una persona adulta? \033[39m',
  'a': 'Tiene entre 2 y 4 litros',
  'b': 'Tiene 5 litros',
  'c': 'Tiene entre 4 y 6 litros',
  'd': 'Tiene 7.5 litros',
  'r': 'C',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m La cantidad de sangre varía de persona a persona. El volumen de sangre representa del 7 al 8\% \del peso corporal. De esta forma, en una persona adulta que pesa entre 50 y 80 kilogramos, puede haber entre 4 y 6 litros de sangre. \033[39m'},
  {'pregunta' : '\033[33m ¿Quién es el autor de la frase "Pienso, luego existo"? \033[39m',
  'a': 'Platón',
  'b': 'Francis Bacon',
  'c': 'Sócrates',
  'd': 'Descartes',
  'r': 'D',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m "Je pense, donc je suis" es la frase original, escrita en francés, del filósofo René Descartes (1596-1650). Esta frase resume el pensamiento y el método de Descartes, para quien todo se inicia con la duda. \033[39m'},
  {'pregunta' : '\033[33m ¿Cuánto tiempo tarda la luz del Sol en llegar a la Tierra? \033[39m',
  'a': '12 minutos',
  'b': '8 minutos',
  'c': '12 horas',
  'd': '1 día',
  'r': 'B',
  'x': '7 minutos',
  'contexto': '\033[32m El tiempo que tarda la luz del Sol en llegar a la Tierra se calcula dividiendo la distancia que hay entre el Sol y la Tierra, aproximadamente 150 000 000 km, entre la velocidad de la luz, que es 300 000 km/s:\n 150 000 000 km÷300 000 km/s= 500 s; 500 s ÷ 60 s/min = 8,3 minutos. \033[39m'},
  {'pregunta' : '\033[33m ¿Cuántos jugadores por equipo participan en un partido de voleibol? \033[39m',
  'a': '10 jugadores',
  'b': '8 jugadores',
  'c': '6 jugadores',
  'd': '7 jugadores',
  'r': 'C',
  'x': '5 jugadores',
  'contexto': '\033[32m Los equipos de voleibol pueden tener hasta 14 jugadores, pero en la cancha de juego participan 6 jugadores por equipo. \033[39m'},
  {'pregunta' : '\033[33m La sal común está formada por dos elementos, ¿cuáles son? \033[39m',
  'a': 'Sodio y carbono',
  'b': 'Potasio y cloro',
  'c': 'Sodio y potasio',
  'd': 'Sodio y cloro',
  'r': 'D',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m La fórmula química de la sal común o cloruro de sodio es NaCl, y está formada por los elementos sodio (Na) y cloro (Cl). \033[39m'},
  {'pregunta' : '\033[33m ¿Cuántos decimales tiene el número pi π? \033[39m',
  'a': 'Treinta',
  'b': 'Veinticinco',
  'c': 'Cien',
  'd': 'Infinitos',
  'r': 'D',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m A lo largo del tiempo, varios estudiosos se han dedicado a calcular el número π y aún no han llegado al final. Para el 2019 se habían calculado más de 31 billones de decimales. \033[39m'},
  {'pregunta' : '\033[33m ¿Cuál es el libro más vendido en el mundo después de la Biblia? \033[39m',
  'a': 'El Principito',
  'b': 'Don Quijote de la Mancha',
  'c': 'La Odisea',
  'd': 'El Señor de los Anillos',
  'r': 'B',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m El ingenioso hidalgo don Quijote de la Mancha es un clásico universal de la literatura española, escrito por Miguel de Cervantes Saavedra (1547-1616). \033[39m'},
  {'pregunta' : '\033[33m ¿Cuál es el país más grande y el más pequeño del mundo? \033[39m',
  'a': 'Rusia y Vaticano',
  'b': 'Estados Unidos y Malta',
  'c': 'India y San Marino',
  'd': 'China y Nauru',
  'r': 'A',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m Rusia es el país mas grande del mundo con un área de 17 millones de km2, mientras el Vaticano tiene apenas 0,44 km2. \033[39m'},
  {'pregunta' : '\033[33m ¿Cuáles son los tres predadores del reino animal reconocidos por: 1) habilidad de cazar en grupo, 2) camuflajearse para sorprender a su presa, 3) poseer sentidos refinados? \033[39m',
  'a': '1) León; 2) tiburón blanco; 3) orca',
  'b': '1) Cobra; 2) zorro; 3) cocodrilo',
  'c': '1) Hiena; 2) Oso polar; 3) Lobo gris',
  'd': '1) Tiburón blanco; 2) elefante; 3) escorpión',
  'r': 'C',
  'x': 'Esta pregunta no tiene respuesta secreta',
  'contexto': '\033[32m La hiena es el único animal que se enfrenta al león, atacándolo en grupo. El oso polar, u oso blanco se camuflajea en la blancura del ártico. El lobo gris tiene una audición y visión nocturna excelentes, lo que hacen de ellos grandes cazadores. \033[39m'},
  {'pregunta' : '\033[33m ¿En qué periodo de la prehistoria fue descubierto el fuego? \033[39m',
  'a': 'Edad media',
  'b': 'Edad de los metales',
  'c': 'Neolítico',
  'd': 'Paleolítico',
  'r': 'D',
  'contexto': '\033[32m Fue en el Paleolítico que los seres humanos empezaron a usar el fuego, cuando aprendieron que era posible producir fuego al frotar pedazos de madera y piedra. \033[39m'},
            ]

def triviaCulturaGeneral(pts, nombre):
  playAgain = True

  for i in range(1, 6):
    time.sleep(1)
    print(f'Iniciamos en {6 - i} ...')
  
  print(f'\nMucha suerte {nombre}\n')

  while(playAgain):
    puntaje = pts
    puntajeInicial = pts
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

        elif respuesta == questions[i]["x"].upper():

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
      puntaje = puntajeInicial
      time.sleep(4)

    elif isReady == 'NO':
      playAgain = False

  return puntaje


