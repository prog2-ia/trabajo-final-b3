# Ahora desde persistencia/ficheros.py
# Las importaciones cambian porque ya no estás dentro de entidades

from entidades.usuarios import Usuario
from entidades.piezas import Pieza, Carta, Figura
from entidades.colecciones import Coleccion
import pickle
import os
import sys

def obtener_ruta_recurso(ruta_relativa):
    """
    Obtiene la ruta absoluta para recursos.
    Funciona en desarrollo y con PyInstaller.
    """
    if getattr(sys, 'frozen', False):
        # Si es un ejecutable compilado con PyInstaller
        directorio_base = os.path.dirname(sys.executable)
    else:
        # En desarrollo, usamos el directorio actual (src/)
        directorio_base = os.path.dirname(os.path.abspath(__file__))  # src/persistencia
        # Subimos un nivel para llegar a src/
        directorio_base = os.path.dirname(directorio_base)
    
    # Aseguramos que el directorio de persistencia existe
    ruta_completa = os.path.join(directorio_base, "persistencia", ruta_relativa)
    directorio = os.path.dirname(ruta_completa)
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio, exist_ok=True)
    
    return ruta_completa


class FicherosTexto:
    """
    Clase encargada de leer los ficheros de texto de la base de datos y crear o ampliar una base de datos
    """

    ruta = obtener_ruta_recurso("base_datos.txt")  # Solo el nombre del archivo

    @staticmethod
    def anyadir_usuario_fichero(usuario: Usuario) -> None:
        with open(FicherosTexto.ruta, 'a', encoding='utf-8') as writer:
            writer.write(f'\n------------------------| Usuario : {usuario.nombre} |--------------------------\n')
            contador = 0
            for coleccion in usuario.colecciones:
                writer.write(f'------------------->  Coleccion : {contador} \n')
                
                writer.write(f'------- Figuras ------- \n')
                for figura in coleccion.get_figuras():
                    writer.write(f'->Nombre:{figura.nombre}, Estado:{figura.estado}, Edicion:{figura.edicion}, Rareza:{figura.rareza}, Precio:{figura.precio}, Altura:{figura.altura}, Anchura:{figura.anchura}, Material:{figura.material}\n')
                
                writer.write(f'------- Cartas ------- \n')
                for carta in coleccion.get_cartas():
                    writer.write(f'->Nombre:{carta.nombre}, Estado:{carta.estado}, Edicion:{carta.edicion}, Rareza:{carta.rareza}, Precio:{carta.precio}, Imagen:{carta.imagen}, Frima:{carta.firma}\n')
                contador += 1

    @staticmethod
    def inicializar_fichero(usuario: Usuario) -> None:
        with open(FicherosTexto.ruta, 'w', encoding='utf-8') as writer:
            writer.write(f'........................... BASE DE DATOS DEL GESTOR DE COLECCIONES .................................\n')
        
        FicherosTexto.anyadir_usuario_fichero(usuario)


class FicherosBinarios:
    """
    Clase encargada de escribir y leer ficheros binarios
    """

    ruta = obtener_ruta_recurso("datos.pickle")  # Solo el nombre del archivo

    @staticmethod
    def escribir_fichero_binario(lista_usuarios: list) -> None:
        with open(FicherosBinarios.ruta, "wb") as writerbyte:
            pickle.dump(lista_usuarios, writerbyte)

    @staticmethod
    def cargar_base_datos() -> list:
        if not os.path.exists(FicherosBinarios.ruta):
            return None
        with open(FicherosBinarios.ruta, "rb") as readerbyte:
            usuarios = pickle.load(readerbyte)
            return usuarios if isinstance(usuarios, list) else None