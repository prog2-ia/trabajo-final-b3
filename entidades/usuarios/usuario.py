from ..colecciones import  coleccion

class Usuario :
    """
        Clase que representa un usuario de la base de datos, el cual puede tener múltiples
        colecciones de piezas.

        ---ATRIBUTOS---

            __email : str
            __nombre : str
            __colecciones : list[Coleccion]

        ---MÉTODOS---

            anyadir_colecciones( coleccion : list[coleccion] )-> bool
                añade una coleccion

            eliminar_coleccion(self , coleccion : list[coleccion] ) -> bool
                elimina una coleccion

            __str__()

            __len()__
                Longitud de la lista de colecciones

    """
    def __init__(self , email : str  , nombre : str  , colecciones : list[coleccion] = None)  :

        if email is None or not email.strip() :
            print('Error email incorrecto')
            return
        self.__email = email

        if nombre is None or not nombre.strip() :
            print('Valo de nombre incorrecto')
            return
        self.__nombre = nombre

        if colecciones is None :
            self.__colecciones = []
        else :
            self.__colecciones = colecciones



    def anyadir_coleccion(self , coleccion : list[coleccion] ) -> bool:

        if coleccion is None or coleccion == [] :
            return  False
        self.__colecciones.append(coleccion)
        return True

    def eliminar_coleccion(self , coleccion : list[coleccion]) -> bool:

        if coleccion in self.__colecciones :
            self.__colecciones.remove(coleccion)
            return True
        return False

    def __str__(self) -> str :
        return f"email = {self.__email} , nombre = {self.__nombre} ,colecciones = {self.__colecciones} "

    def __len__(self) -> int :
        return len( self.__colecciones )
