from  entidades.piezas.pieza import Pieza 
from entidades.piezas.carta import Carta
from entidades.piezas.figura import Figura

class GestorPiezas:

    """
        Clase usada por el coordinador para gestionar las piezas en la colección .


        ---ATRIBUTOS---


        ---MÉTODOS---

            crear_figura(nombre  : str , estado : str  , edicion : str  , rareza : str  , altura  : int ,anchura : int  , material : str ) -> Figura | str :
                Crea un nuevo objeto figura  y lo devuelve 
            
            crear_carta(nombre : str  , estado : str  ,edicion : str  , rareza  : str , imagen : str )-> Carta | str   : 
                Crea un nuevo objeto Carta y lo devuelve 
            
            comprobador (nombre : str ,estado  str ,edicion : str ,rareza : str ) -> str | None: 
                Comprueba e indica si los datos para crear un nuevo objeto con correctos

            @staticmethod
            reparar_pieza(pieza : Pieza) -> bool : 
                Repara la pieza indicada
            
            @staticmethod
            mejorar_pieza(pieza : Pieza) -> bool : 
                Mejora la pieza indicada 

            @staticmethod
            tasar_pieza(pieza : Pieza)-> int : 
                Tasa la pieza indicada

            @staticmethod
            comprobar_numeros(numeros) -> bool :
                Devuelve si un str puede ser convertido a int o float sin errores 

    """
    
    def __init__(self):
        pass
    

    def crear_figura(self , nombre  : str , estado : str  , edicion : str  , rareza : str  , altura  : int ,anchura : int  , material : str ) -> Figura | str : 
        
        comprobador = self.comprobador(nombre,estado,edicion,rareza)
        if type(comprobador) is str : 
            return comprobador
        
        if not self.comprobar_numeros(altura)  :
            return '\n ----Altura inválida----'
        altura = int(altura)
        if altura <= 0:
            return '\n ----Altura inválida----'

        if not self.comprobar_numeros(anchura)  :
            return '\n ----Anchura inválida----'
        anchura = int(anchura)
        if anchura <= 0:
            return '\n ----Anchura inválida----'

        if material is None or material.upper() not in ['PVC', 'RESINA', 'METAL']:
            return '\n ----Material inválido----'

        figura = Figura(nombre , estado , edicion , rareza , altura , anchura , material )
        return figura
    

    def crear_carta(self,nombre : str  , estado : str  ,edicion : str  , rareza  : str , imagen : str )-> Carta | str: 

        comprobador = self.comprobador(nombre,estado,edicion,rareza)
        
        if type(comprobador) is str : 
            return comprobador
        
        if imagen is None or not imagen.strip():
            return('Imagen inválida')
            
        
        carta = Carta(nombre , estado , edicion , rareza , imagen)
        return carta
    
    def comprobador (self, nombre : str ,estado : str ,edicion : str ,rareza : str ) -> str | None: 

        if nombre is None or not nombre.strip():
            return("\n ----Nombre inválido----")
            
        if estado is None or not estado.strip() or estado.upper() not in ['PERFECTO', 'BUENO', 'ACEPTABLE', 'MALO']:
            return("\n ----Estado inválido----")
            

        if edicion is None or not edicion.strip():
            return('\n ----Edición inválido----')
            

        if rareza is None or not rareza.strip() or rareza.upper() not in ['LEGENDARIO', 'RARO', 'COMÚN' , 'COMUN']:
            return('\n ----Rareza inválida----')
        
        return None 
    
    @staticmethod
    def reparar_pieza(pieza : Pieza) -> bool : 
        return pieza.mejorar_estado()
    
    @staticmethod
    def mejorar_pieza(pieza : Pieza) -> bool : 
        return pieza.mejorar_rareza()

    @staticmethod
    def tasar_pieza(pieza : Pieza)-> int : 
        return pieza.tasar()
    
    @staticmethod
    def comprobar_numeros(numeros) -> bool  : 
        for numero in numeros :
            if numero not in ['0','1','2','3','4','5','6','7','8','9'] :
                return False
        return True 
    
    
