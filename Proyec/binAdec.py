def convertir_binario_a_decimal(numero_binario):
  """
  Función para convertir un número binario a decimal.

  Argumentos:
    numero_binario (str): El número binario a convertir.

  Retorno:
    int: El número decimal equivalente o None si hay un error.
  """
  if not numero_binario:
    return None
  if not all(digito in "01" for digito in numero_binario):
    return None
  decimal = 0
  for i, digito in enumerate(reversed(numero_binario)):
    decimal += int(digito) * 2**i
  return decimal

numero_binario = input("Ingrese un número binario: ")

numero_decimal = convertir_binario_a_decimal(numero_binario)

if numero_decimal is not None:
  print(f"{numero_binario} en binario equivale a {numero_decimal} en decimal.")
else:
  print("¡Error! El valor ingresado no es un número binario válido tiene que ser 0 y 1 .")
