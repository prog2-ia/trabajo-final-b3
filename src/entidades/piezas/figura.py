import random
from .pieza import Pieza
from ..excepciones import FiguraInvalidError


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
            try :
                altura = float(altura)
            except  :
                raise TypeError('Tipo de dato en altura incorrecto')

        elif altura <= 0 :
            raise ValueError('Valor de dato en  altura incorrecto')
        altura = int(altura)

        if type(anchura) != int and type(altura) != float :
            try :
                anchura = float(anchura)
            except :
                raise TypeError('Tipo de anchura incorrecto')
        elif anchura <= 0  :
            raise ValueError('Valor de anchura incorrecto')

        anchura = int(anchura)

        if material is None or material.upper() not in ['PVC', 'RESINA', 'METAL']:
            raise  ValueError('Valores de material incorrectos')

        self.__altura = altura
        self.__anchura = anchura
        self.__material = material.upper()

    @property
    def altura(self) : 
        return self.__altura
    
    @property
    def anchura(self) : 
        return self.__anchura
    
    @property
    def material(self) : 
        return self.__material

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
            raise ValueError('Proporciones pasadas incorrectas')

        if altura == self.__altura and anchura == self.__anchura:
            raise ValueError('Proporciones pasadas incorrectas')

        self.__altura = altura
        self.__anchura = anchura

        return True

    """
    -------------------------------------------------------------------------------------------------------------------------------------
                                MÉTODOS ABSTRACTOS
    -------------------------------------------------------------------------------------------------------------------------------------
    """

    def mejorar_rareza(self) -> bool:
        if self.rareza == 'LEGENDARIO':
            raise  FiguraInvalidError('Error no se puede mejorar más la rareza')

        if self.__material == 'PVC':
            dificultad = 10
        elif self.__material == 'RESINA':
            dificultad = 20
        else: #METAL
            dificultad = 30

        if (self.__altura * self.__anchura) > 150:
            dificultad += 5
        else:
            dificultad += 3

        probabilidad_exito = 100 - dificultad
        tirada_dado = random.randint(1, 100)

        if tirada_dado <= probabilidad_exito:
            if self.rareza == 'COMÚN' or self.rareza == 'COMUN':
                self.rareza = 'RARO'
            elif self.rareza == 'RARO':
                self.rareza = 'LEGENDARIO'
            return True

        raise FiguraInvalidError('Error no se ha podido mejorar la rareza')

    def mejorar_estado(self) -> bool:
        if self.estado == 'PERFECTO':
            raise FiguraInvalidError('Error, el estado ya es PERFECTO')

        # Cuanto mejor el estado, mas dificil es mejorarlo
        probabilidades = {
            'MALO': 80,
            'ACEPTABLE': 50,
            'BUENO': 20
        }

        probabilidad_exito = probabilidades[self.estado]
        tirada_dado = random.randint(1, 100)

        if tirada_dado <= probabilidad_exito:
            if self.estado == 'MALO':
                self.estado = 'ACEPTABLE'
            elif self.estado == 'ACEPTABLE':
                self.estado = 'BUENO'
            elif self.estado == 'BUENO':
                self.estado = 'PERFECTO'

            return True

        #Si falla la mejora, degradamos el estado de la figura si es de RESINA
        else:
            if self.material == 'RESINA':
                if self.estado == 'BUENO':
                    self.estado = 'ACEPTABLE'
                elif self.estado == 'ACEPTABLE':
                    self.estado = 'MALO'
                raise FiguraInvalidError('Error no se ha podido mejorar el estado , al ser de resina la pieza su estado a empeordado')

            raise FiguraInvalidError('Error no se ha podido mejorar el estado')


    def __str__(self):
        padre = super().__str__()
        return padre + f"Altura: {self.__altura}, Anchura: {self.__anchura}, Material: {self.__material}"