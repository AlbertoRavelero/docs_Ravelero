ancho = 60

# Funciones de diseño
def m_Superior():
  print("╔" + "═" * (ancho - 2) + "╗")

def m_Inferior():
  print("╚" + "═" * (ancho - 2) + "╝")

def linea_texto(texto):
    espacio = ancho - 4 - len(texto)  # Define el espacio al tamaño del recuadro, restando los bordes y el largo del texto
    izq = espacio // 2  # Espacio de margen hacia la izquierda
    der = espacio - izq # Espacio de margen hacia la derecha
    print(f"║ {' ' * izq}{texto}{' ' * der} ║") 

def linea_vacia():
    print("║" + " " * (ancho - 2) + "║")

#Funciones Requeridas
def addmultiplenumbers(numeros):
   """
    Suma todos los números en una lista
    Entrada: Lista de números [num1, num2, ...]
    Salida: Suma total (float/int)
    """
   resultado = sum(numeros)
   return round(numeros,2)

def multiplymultiplenumbers(numeros):
   """
   Multiplica todos los número en una lista
   Entrada: numeros de números [num1, num2, ...]
   Salida: Producto total (float/int)
   """
   total = 1
   for num in numeros:
      total *= num
   return round(total,2)

def isiteven(numero):
   """
   Verifica si un número es par y entero
   Entrada: un número
   Salida: True/False
   """
   return isitaninteger(numero) and numero % 2 == 0

def isitaninteger(numero):
   """
   Verifica si un número es entero
   Entrada: un número
   Salida: True/False
   """
   return isinstance(numero, int) or (isinstance(numero, float) and numero.is_integer())

def menu_incial():
  m_Superior()
  linea_texto("Calculadora Mejorada")
  linea_vacia()
  linea_texto("1. Sumar múltiples números")
  linea_texto("2. Multiplicar múltiples número")
  linea_texto("3. Verificar si el número es par y entero")
  linea_texto("4. Verificar si es número es entero")
  linea_texto("5. Salir")
  linea_vacia()
  m_Inferior()
   

def main():
  while True:
     menu_incial()
     opcion = input ("║ Selecciones una opción: ")

     if opcion == "1":
        m_Superior()
        linea_texto("Ingrese número separados por espacios")
        m_Inferior()
        entrada = input("║ Ejemplo : 5 10 46 34: ")
        m_Superior()
        try:
          if not entrada.strip():
              linea_texto("No se ingresaron números")
          else:
           numeros = [float(num) for num in entrada.split()]
           resultado = addmultiplenumbers(numeros)
           linea_texto(f"Resultado: {resultado}")
        except ValueError:
           print("║ Error: Ingrese solo números válidos")
        m_Inferior()

     elif opcion == "2":
        m_Superior()
        linea_texto("Ingrese número separados por espacios")
        m_Inferior()
        entrada = input("║ Ejemplo : 5 10 46 34: ")
        m_Superior()
        try:
          if not entrada.strip():
              print("║ No se ingresaron números")
          else:
           numeros = [float(num) for num in entrada.split()]
           resultado = multiplymultiplenumbers(numeros)
           linea_texto(f"Resultado: {resultado}")
        except ValueError:
           print("║ Error: Ingrese solo números válidos")
        m_Inferior()

     elif opcion == "3":
        num = input("Ingrese un número: ")
        m_Superior()
        try:
           num = float(num)
           if isiteven(num):
              linea_texto(f"{num} es un número par y entero")
           else:
              linea_texto(f"{num} No es par y entero")

        except ValueError:
           linea_texto("Error: Ingrese un número válido")
        m_Inferior()

     elif opcion == "4":
        num = input("Ingrese un número: ")
        m_Superior()
        try:
           num = float(num)
           if isitaninteger(num):
              linea_texto(f"{num} es un número entero")
           else:
              linea_texto(f"{num} No es un número entero")
        except ValueError:
           linea_texto("Error: Ingrese un número válido")
        m_Inferior()

     elif opcion == "5":
        print("║ Saliendo del programa...")
        break

     else:
        print("║ Opción no válida. Intente nuevamente.")


if __name__=="__main__":
  main()