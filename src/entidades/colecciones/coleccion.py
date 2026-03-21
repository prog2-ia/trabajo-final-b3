from ..piezas.pieza import Pieza
from ..piezas.carta import Carta
from ..piezas.figura import Figura

class Coleccion :
    """
        Clase que representa una colección de un usuario, este último puede tener varias colecciones distintas

        ---ATRIBUTOS---

            __identificador : str
            __piezas : list[Pieza]

        ---MÉTODOS---

            agregar_pieza(pieza : Pieza) -> bool :
                Añade una pieza a la colección. Devuelve True si se añade correctamente, y False si el objeto no es
                una Pieza o si ya se encuentra en la colección

            eliminar_pieza(pieza : Pieza) -> bool :
                Elimina la pieza indicada de la colección. Devuelve True si se elimina con éxito, y False si no
                existe en la colección o no es una Pieza válida

            get_figuras() -> list[Figura] :
                Filtra y devuelve una lista con todas las piezas de tipo Figura almacenadas en la colección

            get_cartas() -> list[Carta] :
                Filtra y devuelve una lista con todas las piezas de tipo Carta almacenadas en la colección

            __eq__(other) -> bool :
                Compara si la colección actual es igual a otra basándose únicamente en su identificador

            __str__() -> str :
                Devuelve una cadena de texto con el identificador de la colección y la cantidad de piezas que contiene

    """

    __identificador: int = 0

    def __init__(self, piezas: list[Pieza] = None):

        if piezas != None:
            self.__piezas = piezas
        else:
            self.__piezas = []

        type(self).__identificador += 1

        self.__identificador = type(self).__identificador

    
    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                PROPIEDADES DE LOS ATRIBUTOS
    -------------------------------------------------------------------------------------------------------------------------------------
    """

    @property
    def identificador(self) -> int:
        return self.__identificador

    @property
    def piezas(self) -> list[Pieza]:
        return  self.__piezas.copy()

    @piezas.setter
    def piezas(self, value):
        if value is None:
            return
        self.__piezas = value.copy()

    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                MÉTODOS
    -------------------------------------------------------------------------------------------------------------------------------------
    """
    
    def agregar_pieza(self, pieza: Pieza) -> bool:

        if not isinstance(pieza, Pieza):
            return False

        if pieza in self.__piezas:
            return False

        self.__piezas.append(pieza)

        return True

    def eliminar_pieza(self, pieza: Pieza) -> bool:

        if not isinstance(pieza, Pieza):
            return False

        if pieza in self.__piezas:
            self.__piezas.remove(pieza)
            return True
        else:
            return False

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

    def __eq__(self, other) -> bool:
        if isinstance(other, Coleccion):
            return self.__identificador == other.__identificador

    def __str__(self) -> str:
        return f" Colección ID: {self.__identificador}  , Número de piezas: {len(self.__piezas)}"







