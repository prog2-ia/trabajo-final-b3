from ..piezas.pieza import Pieza
from ..piezas.carta import Carta
from ..piezas.figura import Figura

class Coleccion :
    """
    Clase que representa la colección de piezas de un Usuario.


    ---ATRIBUTOS---

    __id : str
    __piezas : list[Pieza]


    ---MÉTODOS---

    agregar_pieza( pieza : Pieza ) -> bool
        añade una pieza a una colección, si el parámetro dado no
        es una pieza o está repetido notifica un error

    eliminar:pieza( pieza : Pieza ) -> bool
        elimina una pieza de una coleccion, si el parámetro no es
        pieza o no se encuentra en esa coleccion notifica un error

    __str__():
        imprimre el id y número de piezas de una colección
    """
    def __init__(self, id: int, piezas: list[Pieza] = None):
        self.__id = id

        if piezas != None:
            self.__piezas = piezas
        else:
            self.__piezas = []

    def agregar_pieza(self, pieza: Pieza) -> bool:

        if not isinstance(pieza, Pieza):
            #print("Error: El objeto que quieres agregar no es una pieza válida")
            return False

        if pieza in self.__piezas:
           # print("Error: La pieza ya se encuentra en la colección")
            return False

        self.__piezas.append(pieza)
        return True

    def eliminar_pieza(self, pieza: Pieza) -> bool:
        if not isinstance(pieza, Pieza):
            return False # Error: El objeto que quieres eliminar no es una pieza válida

        if pieza in self.__piezas:
            self.__piezas.remove(pieza)
            return True # Éxito: La pieza ha sido eliminada correctamente
        else:
            return False # La pieza es válida pero no se encuentra en esta colección

    def get_figuras(self) -> list[Figura]:
        figuras = []
        for pieza in self.__piezas:
           if isinstance(pieza,Figura):
               figuras.append(pieza)
        return figuras.copy()

    def get_cartas(self) -> list[Carta]:
        cartas = []
        for pieza in self.__piezas:
            if isinstance(pieza,Carta):
                cartas.append(pieza)
        return cartas.copy()




    def __str__(self) -> str:
        return f" Colección ID: {self.__id}  \n Número de piezas: {len(self.__piezas)}"







