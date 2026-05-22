from ..usuarios import Usuario
import os
class FicherosTexto : 
    
    """
        Clase encargada de leer los ficheros de texto de la base de datos y crear o ampliar una base de datos 
    """


    @staticmethod
    def anyadir_usuario_fichero(   usuario : Usuario ) -> None : 
        
        with open( 'persistencia/base_datos.txt', 'a') as writer : 

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
        with open(  'persistencia/base_datos.txt'    , 'w') as writer : 
            writer.write(f'........................... BASE DE DATOS DEL GESTOR DE COLECCIONES .................................\n')
        
        FicherosTexto.anyadir_usuario_fichero(usuario)
        FicherosTexto.escribir_fichero_binario() # Sobreescribimos también el fichero binario , para así poder cargar los datos a futuro
    
    @staticmethod
    def escribir_fichero_binario() -> None : 
        pass 

    @staticmethod 
    def cargar_base_datos() -> None : 
        pass 