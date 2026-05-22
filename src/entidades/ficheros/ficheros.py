from ..usuarios import Usuario
from ..piezas import  Pieza ,Carta , Figura
from ..colecciones import  Coleccion
import pickle
import os
class FicherosTexto : 
    
    """
        Clase encargada de leer los ficheros de texto de la base de datos y crear o ampliar una base de datos 
    """


    @staticmethod
    def anyadir_usuario_fichero(   usuario : Usuario ) -> None : 
        
        with open( 'persistencia/base_datos.txt', 'a' ,  encoding= 'utf-8' ) as writer : 

            writer.write(f'\n------------------------| Usuario : {usuario.nombre} |--------------------------\n')
            contador = 0 
            for coleccion in usuario.colecciones :
                writer.write(f'------------------->  Coleccion : {contador} \n')

                writer.write(f'------- Figuras ------- \n')
                for figura in coleccion.get_figuras() : 
                    writer.write(f'->Nombre:{figura.nombre}, Estado:{figura.estado}, Edicion:{figura.edicion}, Rareza:{figura.rareza}, Precio:{figura.precio}, Altura:{figura.altura}, Anchura:{figura.anchura}, Material:{figura.material}\n')
                
                writer.write(f'------- Cartas ------- \n')
                for carta in coleccion.get_cartas() :
                    writer.write(f'->Nombre:{carta.nombre}, Estado:{carta.estado}, Edicion:{carta.edicion}, Rareza:{carta.rareza}, Precio:{carta.precio}, Imagen:{carta.imagen}, Frima:{carta.firma}\n')
                contador+=1 

    @staticmethod
    def inicializar_fichero( usuario : Usuario ) -> None :
        with open(  'persistencia/base_datos.txt'    , 'w' ,  encoding= 'utf-8') as writer : 
            writer.write(f'........................... BASE DE DATOS DEL GESTOR DE COLECCIONES .................................\n')
        
        FicherosTexto.anyadir_usuario_fichero(usuario)

class FicherosBinarios :
    """
    Clase encargada de escribir y leer ficheros binarios
    """

    @staticmethod
    def escribir_fichero_binario(lista_usuarios : list) -> None:
        with open("persistencia/datos.pickle" ,"wb") as writerbyte :
            pickle.dump(lista_usuarios,writerbyte)

    @staticmethod
    def cargar_base_datos() -> list:
        if not os.path.exists("persistencia/datos.pickle" ) :
            return None
        with open("persistencia/datos.pickle", "rb") as readerbyte:
            usuarios = pickle.load(readerbyte)
            # Verificamos que lo cargado sea una lista, si no, devolvemos lista vacía
            return usuarios if isinstance(usuarios, list) else None

