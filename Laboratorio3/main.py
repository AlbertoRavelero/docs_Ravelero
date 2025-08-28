import requests
import random

def trivia_fetch(num):
    """
    Función que toma un número y devuelve la trivia desde la API local
    """
    url = f"http://localhost:5000/trivia/{num}"
    
    try:
        response = requests.get(url, timeout=3)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("text", f"Curiosidad sobre el número {num}")
        else:
            return f"Curiosidad sobre el número {num}"
    
    except requests.exceptions.RequestException:
        # Si la API local no está disponible
        return f"Curiosidad sobre el número {num}"
    
    except Exception as e:
        return f"Curiosidad sobre el número {num}"

# ===== FUNCIONES DEL CUESTIONARIO =====
def generar_pregunta_trivia():
    """
    Genera una pregunta de trivia usando los datos de trivia_fetch()
    """
    numero_correcto = random.randint(1, 99)
    
    # Usar trivia_fetch para obtener la curiosidad
    curiosidad = trivia_fetch(numero_correcto)
    
    # Generar 3 números incorrectos únicos
    opciones_incorrectas = []
    while len(opciones_incorrectas) < 3:
        num_incorrecto = random.randint(1, 99)
        if num_incorrecto != numero_correcto and num_incorrecto not in opciones_incorrectas:
            opciones_incorrectas.append(num_incorrecto)
    
    # Combinar y mezclar opciones
    todas_opciones = [numero_correcto] + opciones_incorrectas
    random.shuffle(todas_opciones)
    
    letras = ["A", "B", "C", "D"]
    opciones_mezcladas = list(zip(letras, todas_opciones))
    
    # Encontrar respuesta correcta
    for letra, num in opciones_mezcladas:
        if num == numero_correcto:
            letra_correcta = letra
            break
    
    return {
        "pregunta": curiosidad,
        "opciones": opciones_mezcladas,
        "respuesta_correcta": letra_correcta,
        "numero_correcto": numero_correcto
    }

def mostrar_pregunta(pregunta, numero_pregunta):
    """
    Muestra la pregunta con líneas horizontales
    """
    print("=" * 60)
    print(f"PREGUNTA {numero_pregunta}")
    print("=" * 60)
    print(f"¿Qué número corresponde a esta curiosidad?")
    print(f"{pregunta['pregunta']}")
    print("-" * 60)
    
    # Mostrar opciones
    for letra, numero in pregunta["opciones"]:
        print(f"{letra}) {numero}")
    
    print("-" * 60)

def ejecutar_cuestionario():
    """
    Ejecuta el cuestionario de trivia con 4 preguntas
    """
    print("=" * 60)
    print("CUESTIONARIO DE TRIVIA NUMÉRICA")
    print("Adivina el número basado en la curiosidad")
    print("=" * 60)
    print("La API local debe estar ejecutándose en http://localhost:5000")
    print("=" * 60)
    
    puntaje = 0
    total_preguntas = 4
    
    for i in range(total_preguntas):
        pregunta = generar_pregunta_trivia()
        mostrar_pregunta(pregunta, i + 1)
        
        # Obtener respuesta del usuario
        while True:
            try:
                respuesta = input("Tu respuesta (A/B/C/D): ").upper().strip()
                if respuesta in ["A", "B", "C", "D"]:
                    break
                print("Por favor, ingresa A, B, C o D")
            except KeyboardInterrupt:
                print("\n¡Juego interrumpido!")
                return
        
        # Verificar respuesta
        if respuesta == pregunta["respuesta_correcta"]:
            print("✅ ¡Correcto!")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta era {pregunta['respuesta_correcta']}) {pregunta['numero_correcto']}")
        
        print()  # Línea en blanco entre preguntas
    
    # Mostrar resultados finales
    print("=" * 60)
    print("RESULTADOS FINALES")
    print("=" * 60)
    print(f"Puntuación: {puntaje}/{total_preguntas}")
    print("-" * 60)
    
    if puntaje == total_preguntas:
        print("¡Perfecto! Eres un genio de los números")
    elif puntaje >= total_preguntas / 2:
        print("¡Muy bien! Buen conocimiento")
    else:
        print("Sigue aprendiendo, los números son fascinantes")
    
    print("=" * 60)

def jugar_otra_vez():
    """
    Pregunta al usuario si quiere jugar otra vez
    """
    while True:
        respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower().strip()
        if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        else:
            print("Por favor, responde 's' o 'n'")

# ===== PROGRAMA PRINCIPAL =====
def main():
    """
    Función principal que inicia el programa
    """
    print("Iniciando cuestionario de trivia numérica...")
    print()
    
    while True:
        ejecutar_cuestionario()
        
        if not jugar_otra_vez():
            print("¡Gracias por jugar! Hasta la próxima.")
            break
        print()
        
if __name__ == "__main__":
    main()