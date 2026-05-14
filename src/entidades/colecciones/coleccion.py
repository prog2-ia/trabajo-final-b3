from ..piezas import Pieza , Carta , Figura
from ..excepciones import  PiezaInvalidError

class Coleccion :
    """
        Clase que representa una colección de un usuario, este último puede tener varias colecciones distintas

        ---ATRIBUTOS---

            __identificador : str
            __piezas : list[Pieza]

        ---MÉTODOS---

            agregar_pieza(pieza : Pieza) -> bool :
                Añade una pieza a la colección. Devuelve True si se añade correctamente.

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
        if value is None :
            raise  TypeError('Tipo erroneo')
        self.__piezas = value.copy()

    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                MÉTODOS
    -------------------------------------------------------------------------------------------------------------------------------------
    """
    
    def agregar_pieza(self, pieza: Pieza) -> bool:

        if not isinstance(pieza, Pieza):
            raise TypeError('Tipo de dato pieza equivocado')

        if pieza in self.__piezas:
            raise PiezaInvalidError('Pieza ya existe en la colección') # Excepción piezas ya está

        self.__piezas.append(pieza)

        return True

    def eliminar_pieza(self, pieza: Pieza) -> bool:

        if not isinstance(pieza, Pieza):
            raise TypeError('Tipo de dato pieza equivocado')

        if pieza in self.__piezas:
            self.__piezas.remove(pieza)
            return True
        else:
            raise PiezaInvalidError('Pieza no existe en la colección')

    def get_figuras(self) -> list[Figura]:

        return [pieza for pieza in self.__piezas if isinstance(pieza,Figura)]

    def get_cartas(self) -> list[Carta]:

        return [carta for carta in self.__piezas if isinstance(carta,Carta)]

    def __eq__(self, other) -> bool:
        if isinstance(other, Coleccion) :
            return self.__identificador == other.__identificador
        else :
            raise TypeError('Tipo de dato other erroneo')
        
    def __len__(self) -> int : 
        return len(self.__piezas)

    def __str__(self) -> str:
        return f" Colección ID: {self.__identificador}  , Número de piezas: {len(self.__piezas)}"







