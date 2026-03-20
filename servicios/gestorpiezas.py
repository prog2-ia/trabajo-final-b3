from  entidades.piezas.pieza import Pieza 
from entidades.piezas.carta import Carta
from entidades.piezas.figura import Figura

class GestorPiezas:
    
    def __init__(self):
        pass
    

    def crear_figura(self , nombre , estado , edicion , rareza , altura ,anchura , material): 
        
        comprobador = self.comprobador(nombre,estado,edicion,rareza)
        if type(comprobador) is str : 
            return comprobador
        
        altura = int(altura)
        if type(altura) == str or altura <= 0:
            return 'Altura inválida'

        anchura = int(anchura)
        if type(anchura) == str or anchura <= 0:
            return 'Anchura inválida'

        if material is None or material.upper() not in ['PVC', 'RESINA', 'METAL']:
            return 'Material inválido'

        figura = Figura(nombre , estado , edicion , rareza , altura , anchura , material )
        return figura
    

    def crear_carta(self,nombre , estado ,edicion , rareza , imagen): 

        comprobador = self.comprobador(nombre,estado,edicion,rareza)
        
        if type(comprobador) is str : 
            return comprobador
        
        if imagen is None or not imagen.strip():
            return('Imagen inválida')
            
        
        carta = Carta(nombre , estado , edicion , rareza , imagen)
        return carta
    
    def comprobador (self, nombre,estado,edicion,rareza) -> str | None: 

        if nombre is None or not nombre.strip():
            return("Nombre inválido")
            
        if estado is None or not estado.strip() or estado.upper() not in ['PERFECTO', 'BUENO', 'ACEPTABLE', 'MALO']:
            return("Estado inválido")
            

        if edicion is None or not edicion.strip():
            return('Edición inválido')
            

        if rareza is None or not rareza.strip() or rareza.upper() not in ['LEGENDARIO', 'RARO', 'COMÚN' , 'COMUN']:
            return('Rareza inválida')
        
        return None 
    
    @staticmethod
    def reparar_pieza(pieza : Pieza) -> bool : 
        return pieza.mejorar_estado()
    
    @staticmethod
    def mejorar_pieza(pieza : Pieza) -> bool : 
        return pieza.mejorar_rareza()