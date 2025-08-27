import requests

def trivia_fetch(num):
    """
    Función que toma un número y devuelve un diccionario con trivia sobre ese número.
    """
    url = f"http://numbersapi.com/{num}/trivia?json"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # La API devuelve un JSON con: 'text' (dato curioso), 'number' (número), 'type' (trivia)
        return {
            "number": data["number"],
            "trivia": data["text"],
            "type": data["type"]
        }
    except Exception as e:
        return {"error": f"Error al obtener datos: {str(e)}"}

def main():
    # Ejemplo de uso
    num = 42
    result = trivia_fetch(num)
    print(result)

if __name__ == "__main__":
    main()