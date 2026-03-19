from .pieza import Pieza


class Figura(Pieza):
    """
    Figura es una subclase de pieza que representa una figura

    ---ATRIBUTOS---

        __material: str -> [PVC,RESINA,METAL]

    """

    def __init__(self, nombre: str, estado: str, edicion: str, rareza: str, altura: float, anchura: float, material: str):
        super().__init__(nombre, estado, edicion, rareza)

        if type(altura) == str or altura <= 0:
            print('Altura inválida')
            return

        if type(anchura) == str or anchura <= 0:
            print('Anchura inválida')
            return

        if material is None or material.upper() not in ['PVC', 'RESINA', 'METAL']:
            print('Material inválido')
            return

        self.__altura = altura
        self.__anchura = anchura
        self.__material = material.upper()

    def tasar(self) -> float:
        precio_final = (self.__altura * self.__anchura) * 0.5
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
            case 'COMÚN':
                precio_final = precio_final + (precio_final * 0.1)

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
            return False

        if altura < self.__altura or anchura < self.__anchura:
            return False

        if altura == self.__altura and anchura == self.__anchura:
            return False

        self.__altura = altura
        self.__anchura = anchura

        return True

    def __str__(self):
        padre = super().__str__()
        return padre + f"Altura: {self.__altura}, Anchura: {self.__anchura}, Material: {self.__material}"