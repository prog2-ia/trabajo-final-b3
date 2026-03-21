from abc import ABC, abstractmethod

class Pieza(ABC) :
    """
        Clase que representa los elementos de una colección.
        Clase abstracta cuyos hijos serán Carta y Figura.

        ---ATRIBUTOS---

            __nombre : str
            __estado : str -> ['PERFECTO', 'BUENO', 'ACEPTABLE', 'MALO']
            __edicion : str
            __rareza : str -> ['LEGENDARIO', 'RARO', 'COMUN', 'COMÚN']
            __precio : float

        ---MÉTODOS---

            mejorar_rareza() -> bool :
                Mejora la rareza de la pieza a la siguiente calidad. Devuelve True si se mejoró exitosamente, False si
                ya tiene la rareza al máximo

            mejorar_estado() -> bool :
                Mejora el estado de la pieza a la siguiente calidad. Devuelve True si se mejoró, False si ya tiene
                el estado al máximo

            tasar() -> float :
                Calcula y devuelve un valor (precio) de de la pieza aplicando modificadores según su estado y rareza

            __eq__(other) -> bool :
                Compara si la pieza actual es igual a otra basándose únicamente en su nombre

            __str__() -> str :
                Devuelve una representación en cadena de texto con el nombre, estado, rareza y  precio de la pieza



    """

    def __init__(self, nombre: str, estado: str, edicion: str, rareza: str) -> None:

        if nombre is None or not nombre.strip():
            return

        if estado is None or not estado.strip() or estado.upper() not in ['PERFECTO', 'BUENO', 'ACEPTABLE', 'MALO']:
            return

        if edicion is None or not edicion.strip():
            return

        if rareza is None or not rareza.strip() or rareza.upper() not in ['LEGENDARIO', 'RARO', 'COMUN','COMÚN']:
            return

        self.__nombre = nombre
        self.__estado = estado.upper()
        self.__edicion = edicion
        self.__rareza = rareza.upper()
        self.__precio = 0

    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                PROPIEDADES DE LOS ATRIBUTOS
    -------------------------------------------------------------------------------------------------------------------------------------
    """

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def estado(self) -> str:
        return self.__estado

    @property
    def edicion(self) -> str:
        return self.__edicion

    @property
    def rareza(self) -> str:
        return self.__rareza

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, value) -> None:

        if type(value) == str or value is None or value <= 0.0:
            return

        self.__precio = value

    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                MÉTODOS
    -------------------------------------------------------------------------------------------------------------------------------------
    """

    def mejorar_rareza(self) -> bool:

        if self.__rareza == 'LEGENDARIO':
            return False

        if self.__rareza == 'RARO':
            self.__rareza = 'LEGENDARIO'


        if self.__rareza == 'COMUN' or self.__rareza =='COMÚN':
            self.__rareza = 'RARO'

        return True

    def mejorar_estado(self) -> bool:

        if self.__estado == 'PERFECTO':
            return False

        if self.__estado == 'BUENO':
            self.__estado = 'PERFECTO'

        if self.__estado == 'ACEPTABLE':
            self.__estado = 'BUENO'

        if self.__estado == 'MALO':
            self.__estado = 'ACEPTABLE'

        return True

    def tasar(self) -> float:

        precio_final = 50

        match self.estado:
            case 'PERFECTO':
                precio_final = precio_final + (precio_final * 0.5)
            case 'BUENO':
                precio_final = precio_final + (precio_final * 0.3)
            case 'ACEPTABLE':
                precio_final = precio_final + (precio_final * 0.1)
            case 'MALO':
                precio_final = precio_final - (precio_final * 0.25)

        match self.rareza:
            case 'LEGENDARIO':
                precio_final = precio_final + (precio_final * 0.5)
            case 'RARO':
                precio_final = precio_final + (precio_final * 0.3)
            case 'COMUN':
                precio_final = precio_final + (precio_final * 0.1)

        return precio_final

    def __eq__(self, other) -> bool:
        if isinstance(other, Pieza):
            return (self.__nombre == other.nombre) 

    def __str__(self) -> str:
        return f" Nombre: {self.__nombre}, Estado: {self.__estado}, Edición: {self.__edicion}, Rareza: {self.__rareza}, Precio: {self.__precio},"



