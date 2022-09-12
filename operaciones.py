import random


def compruebaRespuesta():
  estado = True
  respuesta = ''
  while(estado):
    inputValue = input('Si tu respuesta es afirmativa ingresa Si o S, de lo contrario ingresa No o N\nTu respuesta: ').upper()
    print('')
    if inputValue == "SI" or inputValue == 'S':
        estado = False
        respuesta = "SI"      
    elif inputValue == "NO" or inputValue == 'N':
        estado = False
        respuesta = "NO"
    else:
      print('Ingrese una opción válida\n')

  return respuesta

def operacionRandom (puntaje):
  #operaciones --> 1: suma, 2: resta, 3: division
  numeroRandom = random.randint(0,10)
  operacionRandom = random.randint(1,3)
  mensaje = ''
  if operacionRandom == 1 :
    puntaje += numeroRandom
    mensaje = f'sumado {numeroRandom} pts'

  elif operacionRandom == 2:
    puntaje -= numeroRandom
    mensaje = f'restado {numeroRandom} pts'
    
  elif operacionRandom == 3:
    puntaje/=2
    mensaje = f'dividido el puntaje a la mitad'
  
  return (puntaje, mensaje)