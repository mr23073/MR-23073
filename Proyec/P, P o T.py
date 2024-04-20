import random

def mostrar_opciones():
  """
  Función para mostrar las opciones disponibles al jugador.
  """
  print("Elige tu opción:")
  for i, opcion in enumerate(opciones):
    print(f"{i+1}. {opcion}")

def obtener_seleccion_jugador():
  """
  Función para obtener la selección del jugador con validación.
  """
  while True:
    try:
      seleccion = int(input("Tu elección (número): "))
      if 1 <= seleccion <= len(opciones):
        return seleccion - 1
      else:
        print("Opción inválida. Inténtalo de nuevo.")
    except ValueError:
      print("Debes ingresar un número.")

def obtener_seleccion_computadora():
  """
  Función para obtener la selección aleatoria de la computadora.
  """
  return random.randrange(len(opciones))

def mostrar_resultado(seleccion_jugador, seleccion_computadora):
  """
  Función para mostrar el resultado del juego.
  """
  print(f"Tú elegiste: {opciones[seleccion_jugador]}")
  print(f"La computadora eligió: {opciones[seleccion_computadora]}")

def determinar_ganador(seleccion_jugador, seleccion_computadora):
  """
  Función para determinar el ganador del juego.
  """
  if seleccion_jugador == seleccion_computadora:
    return "Empate"
  elif (seleccion_jugador == 0 and seleccion_computadora == 2) or \
       (seleccion_jugador == 1 and seleccion_computadora == 0) or \
       (seleccion_jugador == 2 and seleccion_computadora == 1):
    return "Ganaste"
  else:
    return "Perdiste"

# Definición de las opciones
opciones = ["Piedra", "Papel", "Tijera"]

while True:
  # Mostrar las opciones al jugador
  mostrar_opciones()

  # Obtener la selección del jugador
  seleccion_jugador = obtener_seleccion_jugador()

  # Obtener la selección aleatoria de la computadora
  seleccion_computadora = obtener_seleccion_computadora()

  # Mostrar el resultado del juego
  mostrar_resultado(seleccion_jugador, seleccion_computadora)

  # Determinar el ganador y mostrarlo
  resultado = determinar_ganador(seleccion_jugador, seleccion_computadora)
  print(f"¡{resultado}!")

  # Preguntar si el jugador quiere jugar otra vez
  otra_partida = input("¿Quieres jugar otra vez? (Sí/No): ").lower()
  