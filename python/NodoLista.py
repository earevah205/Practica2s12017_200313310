class NodoLista:
    def __init__(self):
        self.__siguiente = None
        self.__dato = None

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getDato(self):
        return self.__dato

    def setDato(self, dato):
        self.__dato = dato
