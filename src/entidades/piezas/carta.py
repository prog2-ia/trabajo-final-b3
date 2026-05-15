import random
from .pieza import Pieza
from ..excepciones import CartaInvalidError

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


    
    @property
    def imagen(self) : 
        return self.__imagen
    
    @property
    def firma(self) : 
        return self.__firma

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
            raise CartaInvalidError('Carta ya contiene firma') # Excepción la carta ya está firmada
        self.__firma = True
        return True

    def mejorar_rareza(self) -> bool:
        if self.rareza == 'LEGENDARIO':
            raise CartaInvalidError('la rareza no se puede mejorar más ')

        probabilidad_exito = 70

        # Si esta firmada, el proceso es mas estricto y difícil
        if self.firma:
            probabilidad_exito -= 30

        tirada_dado = random.randint(1, 100)

        if tirada_dado <= probabilidad_exito:
            if self.rareza == 'COMUN' or self.rareza == 'COMÚN':
                self.rareza = 'RARO'
            elif self.rareza == 'RARO':
                self.rareza = 'LEGENDARIO'
            return True
        
        # Cuando sucede un error al mejorar la carta , la firma se borra si existe
        raise CartaInvalidError('No se ha podido mejorar la carta y se ha borrado la firma ') if self.__firma else  CartaInvalidError('No se ha podido mejorar la carta')

    def mejorar_estado(self) -> bool:
        if self.estado == 'PERFECTO':
            raise CartaInvalidError('el estado no se puede mejorar más')

        probabilidades = {
            'MALO': 80,
            'ACEPTABLE': 50,
            'BUENO': 20
        }

        probabilidad_exito = probabilidades[self.estado]

        # Limpiar una carta firmada es más difícil
        if self.__firma:
            probabilidad_exito -= 15

        tirada_dado = random.randint(1, 100)

        if tirada_dado <= probabilidad_exito:
            if self.estado == 'MALO':
                self.estado = 'ACEPTABLE'
            elif self.estado == 'ACEPTABLE':
                self.estado = 'BUENO'
            elif self.estado == 'BUENO':
                self.estado = 'PERFECTO'
            return True

        # Si falla la mejora y estaba firmada se borra la firma
        else:
            if self.__firma == True:
                self.__firma = False
                raise CartaInvalidError ('No se ha podido mejorar el estado y se ha borrado la firma ')
            raise CartaInvalidError ('No se ha podido mejorar el estado  ')

    def __str__(self):
        padre = super().__str__()
        return padre + f" Imagen: {self.__imagen}, Firmada: {self.__firma}"


