from abc import ABC, abstractmethod

class Pieza(ABC) :
    """
    Pieza es una clase que representa una pieza de una colección

    ---ATRIBUTOS---

        __estado: str -> [PERFECTO,BUENO,ACEPTABLE,MALO]

        __rareza: str -> [LEGENDARIO,RARO,COMÚN]
    """
    def __init__(self, nombre: str, estado: str, edicion: str, rareza: str) -> None:
        if nombre is None or not nombre.strip():
            print("Nombre inválido")
            return

        if estado is None or not estado.strip() or estado.upper() not in ['PERFECTO', 'BUENO', 'ACEPTABLE', 'MALO']:
            print("Estado inválido")
            return

        if edicion is None or not edicion.strip():
            print('Edición inválido')
            return

        if rareza is None or not rareza.strip() or rareza.upper() not in ['LEGENDARIO', 'RARO', 'COMÚN']:
            print('Rareza inválida')
            return

        self.__nombre = nombre
        self.__estado = estado.upper()
        self.__edicion = edicion
        self.__rareza = rareza.upper()
        self.__precio = 0

    #PROPIEDADES

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

    def mejorar_rareza(self) -> bool:

        if self.__rareza == 'LEGENDARIO':
            return False

        if self.__rareza == 'RARO':
            self.__rareza = 'LEGENDARIO'


        if self.__rareza == 'COMÚN':
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

    @abstractmethod
    def tasar(self) -> float:
        pass


    def __eq__(self, other) -> bool:
        if isinstance(other, Pieza):
            return (self.__nombre == other.nombre and self.__estado == other.estado and
                    self.__rareza == other.rareza and self.__edicion == other.edicion)

    def __str__(self) -> str:
        return f" Nombre: {self.__nombre}, Estado: {self.__estado}, Edición: {self.__edicion}, Rareza: {self.__rareza}, Precio: {self.__precio},"



