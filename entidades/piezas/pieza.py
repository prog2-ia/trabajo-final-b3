from abc import ABC, abstractmethod

class Pieza(ABC) :
    """
    Pieza es una clase que representa una pieza de una colección

    ---ATRIBUTOS---

        __estado: str -> [PERFECTO,BUENO,ACEPTABLE,MALO]

        __rareza: str -> [LEGENDARIO,RARO,COMUN, COMÚN]
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


        if self.__rareza == 'COMUN':
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



