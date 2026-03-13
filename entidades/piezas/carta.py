from .pieza import Pieza

class Carta(Pieza) :
    def __init__(self, nombre):
        super().__init__(nombre)
