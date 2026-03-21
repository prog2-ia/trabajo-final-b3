from ..colecciones.coleccion import Coleccion

class Usuario :
    """
        Clase que representa un usuario de la base de datos, el cual puede tener múltiples
        colecciones de piezas.

        ---ATRIBUTOS---

            __email : str
            __nombre : str
            __colecciones : list[Coleccion]

        ---MÉTODOS---

            anyadir_coleccion(coleccion : list[Coleccion]) -> bool :
                Añade una colección a la lista de colecciones del usuario

            eliminar_coleccion(coleccion : list[Coleccion]) -> bool :
                Elimina la colección indicada de la lista de colecciones

            __eq__(other) -> bool :
                Compara si el usuario actual es igual a otro basándose en su email y nombre

            __str__() -> str :
                Devuelve una representación en cadena de texto con el email, nombre y número de colecciones

            __len()__ -> int :
                Devuelve la longitud de la lista de colecciones (la cantidad de colecciones que posee)

    """

    def __init__(self , email : str  , nombre : str  , colecciones : list[Coleccion] = None)  :

        if email is None or not email.strip() :
            return
        self.__email = email

        if nombre is None or not nombre.strip() :
            return
        self.__nombre = nombre

        if colecciones is None :
            self.__colecciones = []
        else :
            self.__colecciones = colecciones

    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                PROPIEDADES DE LOS ATRIBUTOS
    -------------------------------------------------------------------------------------------------------------------------------------
    """

    @property
    def email(self) -> str :
        return  self.__email

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def colecciones(self) -> list[Coleccion] :
        return self.__colecciones

    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                MÉTODOS
    -------------------------------------------------------------------------------------------------------------------------------------
    """

    def anyadir_coleccion(self , coleccion : list[Coleccion] ) -> bool:

        if coleccion is None or coleccion == [] :
            return  False
        self.__colecciones.append(coleccion)
        return True

    def eliminar_coleccion(self , coleccion : list[Coleccion]) -> bool:

        if coleccion in self.__colecciones :
            self.__colecciones.remove(coleccion)
            return True
        return False

    def __eq__(self, other) -> bool:
        if not isinstance(other, Usuario):
            return False
        return self.email == other.email and self.nombre == other.nombre

    def __str__(self) -> str :
        return f"Email = {self.__email} , Nombre = {self.__nombre} ,Numero de colecciones = {len(self)} "

    def __len__(self) -> int :
        return len( self.__colecciones )
    