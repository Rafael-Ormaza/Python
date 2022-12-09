class vehiculo():
    color = None
    ruedas = None
    puertas = None

    def color(self):
        self.color = None
    def ruedas(self):
        self.ruedas = None
    def puertas(self):
        self.puertas = None

class coche(vehiculo):
    velocidad = None
    cilindraje = None
    def velocidad(self):
        self.velocidad = None
    def cilindraje(self):
        self.cilindraje = None

p = coche()
p.color = 'Rojo, '
p.ruedas = '4 Ruedas, '
p.puertas = '4 Puertas, '
p.velocidad = 'Velocidad: 300 Km/h, '
p.cilindraje = '2000 cl'
print(p.color, p.ruedas, p.puertas, p.velocidad, p.cilindraje)
