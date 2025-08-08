# Variables
ancho = 60

# Funciones de diseño
def marco_superior():
    print("╔" + "═" * (ancho - 2) + "╗")

def marco_inferior():
    print("╚" + "═" * (ancho - 2) + "╝")

def linea_texto(texto):
    espacio = ancho - 4 - len(texto)  # Define el espacio al tamaño del recuadro, restando los bordes y el largo del texto
    izq = espacio // 2  # Espacio de margen hacia la izquierda
    der = espacio - izq # Espacio de margen hacia la derecha
    print(f"║ {' ' * izq}{texto}{' ' * der} ║") 

def linea_vacia():
    print("║" + " " * (ancho - 2) + "║")

# Funciones Matemáticas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Error: No se puede dividir por cero")
    return a / b

def modulo(a, b):
    if b == 0:
        raise ValueError("Error: No se puede dividir por cero")
    return a % b

def opLibres():
    while True:
        marco_superior()
        linea_texto("OPERACIONES LIBRES")
        linea_vacia()
        linea_texto("Ingrese espresión matemática con 3 o mas números")
        linea_texto("Ejemplo: 2 + 4 / 3 * 5")
        linea_vacia()
        linea_texto("Operadores disponibles: + - * / %")
        linea_texto("1. Calcular espresión")
        linea_texto("2. Volver al menú principal")
        linea_vacia()
        marco_inferior()

        opcion = input("║ Seleccione una opción: ")

        if opcion == "2":
            return
        
        elif opcion =="1":
            try:
                expresion = input("║ Ingrese la expresión matemática: ")
                elementos = expresion.split()
                # .split() Método que divide una cadena en partes

                # Validacion básica
                if len(elementos) < 5 or len(elementos) % 2 == 0:
                    print("║ Error: Formato incorrecto. Ejemplo válido: 5 + 3 * 2")
                    continue

                # Procesar números y operadores
                numeros = []
                operadores = []

                for i, elem in enumerate(elementos):
                    if i % 2 == 0: # Posiciones pares son números
                        try:
                            numeros.append(float(elem)) # Agrega el número al arreglo
                        except ValueError:
                            print(f"║ Error: '{elem}' no es un número válido")
                            break
                    else: # Posiciones impares son operadores
                        if elem in '+-*/%': # Valida el tipo de operador
                            operadores.append(elem) # Agrega el operador al arreglo
                        else:
                            print(f"║ Error: Operador '{elem}' no válido")
                            break
                else: # Solo se ejecuta si el for no se rompió
                    if len(numeros) < 3:
                        print("║ Error: Formato incorrecto. Use 3+ números y operadores. Ejemplo: 5 + 3 * 2")
                        continue # para volver al inicio del bucle while

                    # Realizar cálculos (izquierda a derecha)
                    resultado = numeros [0] # inicializar
                    historial = []

                    for i in range(len(operadores)): # Bucle for, se ejecuta tantas veces como operadores allá
                        num = numeros[i+1]
                        op = operadores[i]

                        try:
                            if op == '+':
                                resultado = suma(resultado, num)
                            elif op == '-':
                                resultado = resta(resultado, num)
                            elif op == '*':
                                resultado = multiplicacion(resultado, num)
                            elif op == '/':
                                resultado = division(resultado, num)
                            elif op == '%':
                                resultado = modulo(resultado, num)

                            historial.append(f"{resultado-num if op in '+-' else resultado/num if op in '*/%' else ''} {op} {num} = {resultado}")
                        
                        except ValueError as e:
                            print(f"║ {str(e)}")
                            break
                    else:
                        # Mostrar resultados
                        marco_superior()
                        for paso in historial:
                            linea_texto(paso)
                        linea_vacia()
                        linea_texto(f"Resultado final: {resultado}")
                        marco_inferior()

            except Exception as e:
                print(f"║ Error inesperado: {str(e)}")

        else:
            print("║ Opción no válida. Intente nuevamente")

# Funciones Conversiones
def deci_a_hexa(num):
    return hex(int(num))[2:].upper() 
# hex() Funcion que convierte a hexadecimal (devuelve formato "oxff")
# [2:] Elimina los 2 primeros caracteres ("ox")
# .upper() Convierte letras a mayúsculas

def deci_a_bina(num):
    return bin(int(num))[2:]
# bin() Funcion que convierte a binario (devuelve formato "0b101")

def hexa_a_deci(hexad):
    return int(hexad, 16)
# Convierte el String hexadecima a entero base 16

def bina_a_deci(binar):
    return int(binar, 2)
# Convierte el String binario a entero base 2

# Menú
def menu_inicial():
    marco_superior()
    linea_texto("CALCULADORA")
    linea_vacia()
    linea_texto("1. Operaciones básicas")
    linea_texto("2. Operaciones libres")
    linea_texto("3. Conversión entre sistemas")
    linea_texto("4. Salir")
    linea_vacia()
    marco_inferior()

# Operaciones básicas
def opBasicas():
    while True:
        marco_superior()
        linea_texto("OPERACIONES BÁSICAS")
        linea_vacia()
        linea_texto("1. Suma")
        linea_texto("2. Resta")
        linea_texto("3. Multiplicación")
        linea_texto("4. División")
        linea_texto("5. Modulo")
        linea_texto("6. Volver al menú principal")
        linea_vacia()
        marco_inferior()

        opcion = input("║ Seleccione una opción: ")
        try:
            opcion_num = int(opcion) # intenta convertir a entero
            if 1 <= opcion_num <= 5 :
            
                numero1 = float(input("║ Ingrese el primer número: "))
                numero2 = float(input("║ Ingrese el segundo número: "))

                if opcion_num == 1:
                  resultado = suma(numero1, numero2)
                elif opcion_num == 2:
                  resultado = resta(numero1, numero2)
                elif opcion_num == 3:
                  resultado = multiplicacion(numero1, numero2)
                elif opcion_num == 4:
                  if numero2 == 0:
                      print("║ Error: No se puede dividir por cero")
                      continue
                  resultado = division(numero1, numero2)
                elif opcion_num == 5:
                  if numero2 == 0:
                      print("║ Error: No se puede calcular módulo por cero")
                      continue
                  resultado = modulo(numero1, numero2)
                else:
                    print("║ Opción no válida. Intente nuevamente.")
                    break

                marco_superior()
                linea_texto(f"Resultado: {resultado}")
                marco_inferior()

            elif opcion_num == 6 :
               return
            else: 
               print("║ Opción no válida. Intente nuevamente.")
        
        except ValueError as e:
            print(f"║ Ingrese un número valido")

# Conversiones Decimal, Binario, Hexadecimal
def opConversiones():
    marco_superior()
    linea_texto("CONVERSIÓN ENTRE SISTEMAS")
    linea_vacia()
    linea_texto("1. Decimal → Hexadecimal y Binario")
    linea_texto("2. Hexadecimal → Decimal y Binario")
    linea_texto("3. Binario → Decimal y Hexadecimal")
    linea_texto("4. Volver al menú principal")
    linea_vacia()
    marco_inferior()

    opcion = input("║ Seleccione una opción: ")
    if opcion == "4":
        return
    
    try:
    
        if opcion == "1":
            num = input("║ Ingrese número Decimal: ")
            hexa = deci_a_hexa(num)
            bina = deci_a_bina(num)
            marco_superior()
            linea_texto(f"Decimal: {num}")
            linea_texto(f"Hexadecimal: {hexa}")
            linea_texto(f"Binario: {bina}")
            ()

        elif opcion == "2":
            hexad = input("║ Ingrese número Hexadecimal: ")
            deci = hexa_a_deci(hexad)
            bina = deci_a_bina(deci)
            marco_superior()
            linea_texto(f"Hexadecimal: {hexad}")
            linea_texto(f"Decimal: {deci}")
            linea_texto(f"Binario: {bina}")
            ()
        
        elif opcion == "3":
            binar = input("║ Ingrese número binario: ")
            deci = bina_a_deci(binar)
            hexa = deci_a_hexa(deci)
            marco_superior()
            linea_texto(f"Binario: {binar}")
            linea_texto(f"Decimal: {deci}")
            linea_texto(f"Hexadecimal: {hexa}")
            ()
        
        else:
            print("║ Opción no válida")
    
    except ValueError as e:
        print(f"║ Error: Número no válido")

# Main
def main():
    while True:
        menu_inicial()
        opcion = input("║ Seleccione una opción: ")

        if opcion == "1":
            opBasicas()
        elif opcion == "2":
            opLibres()
        elif opcion == "3":
            opConversiones()
        elif opcion =="4":
            linea_vacia()
            print("║ Saliendo del programa...")
            break
        else:
            print("║ Opción no válida. Intente nuevamente.")

# primera suma
def suma_inicial():
    marco_superior()
    linea_texto("Bienvenido")
    linea_vacia()
    linea_texto("Suma inicial")
    marco_inferior()
    try:
        numero1 = float(input("║ Ingrese el primer número: "))
        numero2 = float(input("║ Ingrese el segundo número: "))

        resultado = suma(numero1, numero2)
        marco_superior()
        linea_texto(f"Resultado: {resultado}")
        marco_inferior()
    
    except ValueError as e:
        print("║ Error: Ingrese un número válido")

suma_inicial()
main()