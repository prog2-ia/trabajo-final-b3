import random
from .pieza import Pieza
from ..excepciones import PiezaInvalidError


class Figura(Pieza):
    """
        Figura es una subclase de Pieza que representa una figura coleccionable.

        ---ATRIBUTOS---

            __altura : float
            __anchura : float
            __material : str -> ['PVC', 'RESINA', 'METAL']

        ---MÉTODOS---

            tasar() -> float :
                Calcula el precio final de la figura basándose en la tasación base de la pieza (padre), aplicando
                modificadores adicionales por su tamaño (altura y anchura) y su material. Actualiza y devuelve el
                precio final

            aumentar_tamanyo(altura : float, anchura : float) -> bool :
                Actualiza el tamaño de la figura. Devuelve True si se cambiaron correctamente, y False si los
                valores no son numéricos, o si son menores o iguales al tamaño actual

            __str__() -> str :
                Devuelve una representación en cadena de texto con la información base de la pieza con
                la altura, anchura y material específicos de la figura
    """

    def __init__(self, nombre: str, estado: str, edicion: str, rareza: str, altura: float, anchura: float, material: str):
        super().__init__(nombre, estado, edicion, rareza)


        if type(altura) != int and type(altura) != float :
            raise TypeError('Tipo de dato en altura incorrecto')
        elif altura <= 0 :
            raise ValueError('Valor de dato en  altura incorrecto')
        altura = int(altura)

        if type(anchura) != int or type(altura) != float :
            raise TypeError('Tipo de anchura incorrecto')
        elif anchura <= 0  :
            raise ValueError('Valor de anchura incorrecto')

        anchura = int(anchura)

        if material is None or material.upper() not in ['PVC', 'RESINA', 'METAL']:
            raise  ValueError('Valores de material incorrectos')

        self.__altura = altura
        self.__anchura = anchura
        self.__material = material.upper()

    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                MÉTODO
    -------------------------------------------------------------------------------------------------------------------------------------
    """

    def tasar(self) -> float:

        precio_final = super().tasar()
        precio_final = precio_final + precio_final*(self.__altura * self.__anchura) * 0.5

        match self.__material:

            case 'PVC':
                precio_final = precio_final + (precio_final * 0.5)
            case 'RESINA':
                precio_final = precio_final + (precio_final * 0.2)
            case 'METAL':
                precio_final = precio_final + (precio_final * 0.1)

        self.precio = precio_final

        return precio_final

    def aumentar_tamanyo(self, altura, anchura) -> bool:

        if (type(altura) != int and type(altura) != float) or (type(anchura) != int and type(anchura) != float):
            raise  TypeError('Solo se permiten valores numéricos ')

        if altura < self.__altura or anchura < self.__anchura:
            return False

        if altura == self.__altura and anchura == self.__anchura:
            return False

        self.__altura = altura
        self.__anchura = anchura

        return True

    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                MÉTODOS ABSTRACTOS
    -------------------------------------------------------------------------------------------------------------------------------------
    """
    def mejorar_rareza(self) -> bool: # Hay una probabilidad de que se mejore
        #__material : str -> ['PVC', 'RESINA', 'METAL']
        if self.__material == 'PVC' :
            dificultad = 1
        elif self.__material =='RESINA' :
            dificultad = 2
        else :
            dificultad = 3
        dificultad *= 10

        if  (self.__altura * self.__anchura) > 150  : # Cuanto más grande más dificil de mejorar
            dificultad  += 5
        else :
            dificultad += 3


        if n > probabilidad:
            if self.__rareza == 'LEGENDARIO':
                return False

            if self.__rareza == 'RARO':
                self.__rareza = 'LEGENDARIO'

            if self.__rareza == 'COMUN' or self.__rareza == 'COMÚN':
                self.__rareza = 'RARO'

            return True






    def __str__(self):
        padre = super().__str__()
        return padre + f"Altura: {self.__altura}, Anchura: {self.__anchura}, Material: {self.__material}"