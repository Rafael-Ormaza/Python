"""
la agencia de transito dictamino una ley que prohive a los carros fabricados antes del año 2019 circular por las calles
del territorio ###########, crear un programa que imprima por consola el nombre del vehiculos con su respectivo modelo y
año y si este puede crircular o no.
"""

class Carro:

    def inicializar(self, modelo, año):
        self.modelo = modelo
        self.año = año

    def imprimir(self):
        print('Modelo:',self.modelo,'- Año del vehiculo:',self.año)

        if self.año > 2018:
            print('Este vehiculo puede cricular')
        else:
            print('Este vehiculo no puede circular')





Vehiculo1 = Carro()
Vehiculo2 = Carro()
Vehiculo3 = Carro()
Vehiculo4 = Carro()
Vehiculo5 = Carro()

Vehiculo1.inicializar('Chevrolet Aveo', 2018)
Vehiculo2.inicializar('Chevrolet Sail', 2019)
Vehiculo3.inicializar('Chevrolet D-max', 2019)
Vehiculo4.inicializar('chevrolet Colorado', 2015)
Vehiculo5.inicializar('Chevrolet Onix', 2020)

Vehiculo1.imprimir()
Vehiculo2.imprimir()
Vehiculo3.imprimir()
Vehiculo4.imprimir()
Vehiculo5.imprimir()
