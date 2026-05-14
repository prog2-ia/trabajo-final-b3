from entidades.piezas import Pieza , Figura , Carta
from entidades.excepciones import PiezaInvalidError  

class GestorPiezas:

    """
        Clase usada por el coordinador para gestionar las piezas en la colección .


        ---ATRIBUTOS---


        ---MÉTODOS---

            crear_figura(nombre  : str , estado : str  , edicion : str  , rareza : str  , altura  : int ,anchura : int  , material : str ) -> Figura | str :
                Crea un nuevo objeto figura  y lo devuelve 
            
            crear_carta(nombre : str  , estado : str  ,edicion : str  , rareza  : str , imagen : str )-> Carta | str   : 
                Crea un nuevo objeto Carta y lo devuelve 
            

            @staticmethod
            reparar_pieza(pieza : Pieza) -> bool : 
                Repara la pieza indicada
            
            @staticmethod
            mejorar_pieza(pieza : Pieza) -> bool : 
                Mejora la pieza indicada 

            @staticmethod
            tasar_pieza(pieza : Pieza)-> int : 
                Tasa la pieza indicada

    """
    
    def __init__(self):
        pass
    

    def crear_figura(self , nombre  : str , estado : str  , edicion : str  , rareza : str  , altura  : int ,anchura : int  , material : str ) -> Figura | str : 
        try : 
            figura = Figura(nombre , estado , edicion , rareza , altura , anchura , material )
        except  Exception as exp: 
            raise PiezaInvalidError ( str(exp) )
        else : 
            return figura
    

    def crear_carta(self,nombre : str  , estado : str  ,edicion : str  , rareza  : str , imagen : str )-> Carta | str: 
        try : 
            carta = Carta(nombre , estado , edicion , rareza , imagen)
        except Exception as exp : 
            raise PiezaInvalidError ( str(exp) )
        return carta
    
    
    @staticmethod
    def reparar_pieza(pieza : Pieza) -> bool : 
        try : 
            pieza.mejorar_estado()
            return True
        except Exception as exp :       
            raise PiezaInvalidError ( str(exp) )

    @staticmethod
    def mejorar_pieza(pieza : Pieza) -> bool : 
        try : 
            return pieza.mejorar_rareza()
        except Exception as exp : 
            raise PiezaInvalidError ( str(exp) )

    @staticmethod
    def tasar_pieza(pieza : Pieza)-> int : 
        return pieza.tasar()
