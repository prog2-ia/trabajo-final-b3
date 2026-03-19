from .pieza import Pieza


class Carta(Pieza):
    """


    """

    def __init__(self, nombre: str, estado: str, edicion: str, rareza: str, imagen: str):
        super().__init__(nombre, estado, edicion, rareza)


        if imagen is None or not imagen.strip():
            print('Imagen inválida')
            return

        self.__imagen = imagen
        self.__firma = False


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
            case 'COMÚN':
                precio_final = precio_final + (precio_final * 0.1)

        if self.__firma == True:
            precio_final = precio_final * 2


        self.precio = precio_final

        return precio_final

    def firmar_carta(self) -> bool:
        if self.__firma == True:
            return False

        self.__firma = True

        return True

    def __str__(self):
        padre = super().__str__()
        return padre + f" Imagen: {self.__imagen}, Firmada: {self.__firma}"


