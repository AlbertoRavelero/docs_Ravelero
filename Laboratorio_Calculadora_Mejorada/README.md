# Instructions
Now is your opportunity to build a better calculator. Your calculator can work however you wish it to but it should be usable as a calculator.

Firstly, we're going to separate out of our *interactive* logic into the `main()` function, like so:

```
def main():
  print("Hello learners!")

if __name__=="__main__":
  main()
```

This is Python *boilerplate* code, which will only run when the program is invoked by a person. All your code should now be inside a function - either this `main()` function (where you can put things like input statements) or another function.

Automatic grading will be scored out of 8, and will test the functionality of the following functions:

* `addmultiplenumbers([num, num, ..])` - this function must exist in your program, it should take a list of numbers as input, and it should output the sum of those numbers.
* `multiplymultiplenumbers([num, num, ..])` - this function must exist in your program, it should take a list of numbers as input, and it should output the result of multiplying each number in turn with the following number.
* `isiteven(num)` - this function must exist in your program, it should take a single number as input, and it should output a boolean value - `True` if the number is an even, whole number, `False` otherwise.
* `isitaninteger(num)` - this function must exist in your program, it should take a single number as input, and it should output a boolean value - `True` if the number is an integer, `False` otherwise.

**Remember** This project will be automatically graded, and computers are very literal!

**Note:** Use the tests! There's nothing wrong with running the tests until they pass. It's not cheating!

**Note:** If you get stuck getting one function to work, try working on a different one. You might find you can solve later functions more quickly than earlier ones.
____________________________________________________________________________________________________________

Proyecto: “Una mejor calculadora” (versión fácil)

¿Qué tienen que hacer?
Crear una calculadora en Python que funcione desde la consola. La calculadora debe tener estas 4 funciones (con estos nombres exactos):

1) addmultiplenumbers(lista)
   Suma todos los números de una lista y regresa el resultado.

2) multiplymultiplenumbers(lista)
   Multiplica todos los números de una lista y regresa el resultado.

3) isiteven(numero)
   Regresa True si el número es par (y entero), o False si no.

4) isitaninteger(numero)
   Regresa True si el número es entero (por ejemplo 7 o 7.0), o False si no.

Reglas del trabajo:
- Usar una función principal para arrancar el programa.
- Dividir el código en funciones (no todo junto).
- Aceptar números positivos y negativos.
- Pensar en casos especiales (lista vacía, números decimales).
- Mensajes claros para el usuario.

Calidad mínima:
- Código ordenado y con nombres claros.
- Comentarios cortos donde haga falta.
- Archivo README con una breve explicación.

Cómo trabajar con el repositorio (GitHub):
1) Hacer Fork del repositorio original.
2) Clonar su Fork a su computadora.
3) Crear una rama de trabajo.
4) Subir cambios y hacer Pull Request.

Herramientas necesarias:
- Python 3 instalado.
- Librerías: pytest, pytest-cov, black, flake8, isort, mypy (estas se instalan con pip).
- Extensiones VS Code: Python, Pylance, Black Formatter, isort, GitHub Pull Requests and Issues.

Evaluación (8 puntos):
- (2 pts) Suma y multiplicación correctas (incluye casos especiales).
- (2 pts) isiteven e isitaninteger correctas.
- (2 pts) Proyecto ordenado y pruebas pasando.
- (1 pt) Mensajes claros para el usuario.
- (1 pt) README breve con explicación.

Sugerencia: Si se traban con una función, avancen con otra y luego regresen.