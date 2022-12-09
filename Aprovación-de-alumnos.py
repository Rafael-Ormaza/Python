"""En este segundo ejercicio, tendréis que crear un programa que tenga una
clase llamada Alumno que tenga como atributos su nombre y su nota.
Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un
mensaje con el resultado de la nota y si ha aprobado o no."""


class Alumno():
    nombre = None
    nota = None
    def nombreIngresado(self):
        self.notaIngresada = None

    def notaIngresada(self):
        self.nota = None





resultado = Alumno()
nombreDeLaSentencia = resultado.nombre = ' Nombre: Rafael, '
sentencia = resultado.nota = 8
print(resultado.nombre, resultado.nota)


if sentencia > 6:
    print('El estuiante de ' + nombreDeLaSentencia + 'aprovo el curso')
else:
    print('El estudiante de ' + nombreDeLaSentencia + 'no aprovo el curso')
