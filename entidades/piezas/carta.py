from .pieza import Pieza

class Carta(Pieza) :
    """
    Carta es una subclase de pieza que representa una carta de colacción

    ---ATRIBUTOS---

        __material: str -> [PVC,RESINA,METAL]

    """
    def __init__(self, nombre: str, estado: str, edicion: str, rareza: str, altura: float, anchura: float, material: str):
        super().__init__(nombre,estado,edicion,rareza)

        if type(altura) == str or altura <= 0:
            print('Altura inválida')
            return

        if type(anchura) == str or anchura <= 0:
            print('Anchura inválida')
            return

        if material is None or material.upper() not in ['PVC','RESINA','METAL']:
            print('Material inválido')
            return

        self.__altura = altura
        self.__anchura = anchura
        self.__material = material

    def tasar(self) -> float:
        precio_final = (self.__altura * self.__anchura)*0.5
        match super().estado:
            case 'PERFECTO':
                precio_final = precio_final + (precio_final*0.5)
            case 'BUENO':
                precio_final = precio_final + (precio_final*0.3)
            case 'ACEPTABLE':
                precio_final = precio_final + (precio_final*0.1)
            case 'MALO':
                precio_final = precio_final - (precio_final*0.25)





    #    __estado: str -> [PERFECTO, BUENO, ACEPTABLE, MALO]

     #   __rareza: str -> [LEGENDARIO, RARO, COMÚN]