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
            return

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
            return False

        self.__firma = True

        return True

    def __str__(self):
        padre = super().__str__()
        return padre + f" Imagen: {self.__imagen}, Firmada: {self.__firma}"


