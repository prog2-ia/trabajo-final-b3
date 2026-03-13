from abc import ABC, abstractmethod

class Pieza(ABC) :
    def __init__(self, nombre):
        self.__nombre = nombre

