import random

from .pieza import Pieza


class Carta(Pieza):
    """
        Carta es una subclase de Pieza que representa una carta coleccionable.

        ---ATRIBUTOS---

            __imagen : str
            __firma : bool

        ---MÉTODOS---

            tasar() -> float :
                Calcula el precio final de la carta basándose en la tasación base de la pieza (padre) y duplica su valor si la carta está firmada. Actualiza y devuelve el precio final

            firmar_carta() -> bool :
                Marca la carta como firmada. Devuelve True si se firmó con éxito, y False si la carta ya estaba firmada previamente

            __str__() -> str :
                Devuelve una representación de la información base de la pieza con la URL de la imagen y el estado de la firma

    """

    def __init__(self, nombre: str, estado: str, edicion: str, rareza: str, imagen: str):
        super().__init__(nombre, estado, edicion, rareza)

        if imagen is None or not imagen.strip():
            raise ValueError('Valor de imagen incorrecto')

        self.__imagen = imagen
        self.__firma = False


    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                MÉTODOS
    -------------------------------------------------------------------------------------------------------------------------------------
    """
    def tasar(self) -> float:


        precio_final = super().tasar()

        if self.__firma == True:
            precio_final = precio_final * 2


        self.precio = precio_final

        return precio_final

    def firmar_carta(self) -> bool:
        if self.__firma == True:
            return False # Excepción la carta ya está firmada

        self.__firma = True

        return True

    def mejorar_rareza(self) -> bool:
        if self.__rareza == 'LEGENDARIO':
            return False

        probabilidad_exito = 70

        # Si esta firmada, el proceso es mas estricto y difícil
        if self.__firma:
            probabilidad_exito -= 30

        tirada_dado = random.randint(1, 100)

        if tirada_dado <= probabilidad_exito:
            if self.__rareza == 'COMUN' or self.__rareza == 'COMÚN':
                self.__rareza = 'RARO'
            elif self.__rareza == 'RARO':
                self.__rareza = 'LEGENDARIO'
            return True

        return False

    def mejorar_estado(self) -> bool:
        if self.__estado == 'PERFECTO':
            return False

        probabilidades = {
            'MALO': 80,
            'ACEPTABLE': 50,
            'BUENO': 20
        }

        probabilidad_exito = probabilidades[self.__estado]

        # Limpiar una carta firmada es más difícil
        if self.__firma:
            probabilidad_exito -= 15

        tirada_dado = random.randint(1, 100)

        if tirada_dado <= probabilidad_exito:
            if self.__estado == 'MALO':
                self.__estado = 'ACEPTABLE'
            elif self.__estado == 'ACEPTABLE':
                self.__estado = 'BUENO'
            elif self.__estado == 'BUENO':
                self.__estado = 'PERFECTO'
            return True

        # Si falla la mejora y estaba firmada se borra la firma
        else:
            if self.__firma == True:
                self.__firma = False

            return False

    def __str__(self):
        padre = super().__str__()
        return padre + f" Imagen: {self.__imagen}, Firmada: {self.__firma}"


