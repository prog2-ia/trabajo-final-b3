from ..piezas.pieza import Pieza
from ..piezas.carta import Carta
from ..piezas.figura import Figura

class Coleccion :
    """
        Clase que representa una colección de un usuario, este último puede tener varias colecciones distintas

        ---ATRIBUTOS---

            __id : str
            __piezas : list[Pieza]

        ---MÉTODOS---

            agregar_pieza( pieza : Pieza ) -> bool
                añade una pieza a una colección

            eliminar_pieza( pieza : Pieza ) -> bool
                elimina una pieza de una coleccion

            __eq__(  ):
                Compara 2 colecciones 

            __str__():
                imprimre el id y número de piezas de una colección

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







