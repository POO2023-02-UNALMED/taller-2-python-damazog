class Asiento:
    def __init__(self, color, precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self,color):
        if color == ("rojo" or "verde" or "amarillo" or "negro" or "blanco"):
            self.color=color

class Auto:
    def __int__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreado):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
        self.cantidadCreado=1

    def cantidadAsiento(self):
        contador=0
        for i in self.asientos:
            if i != None:
                contador+=1

    def verificarIntegridad(self):
        if (self.registro!=self.Motor.registro):
            return "Las piezas no son originales"
        for i in self.asientos:
            if i != self.registro:
                return "Las piezas no son originales"
        return "Auto original"    

class Motor:
    def __int__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    
    def cambiarRegistro(self, registro):
        self.registro=registro

    def asignarTipo(self,tipo):
        if (tipo == "electrico"):
            self.tipo=tipo
        elif (tipo == "gasolina"):
            self.tipo=tipo