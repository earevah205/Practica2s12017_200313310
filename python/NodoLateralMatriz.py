class NodoLateralMatriz:
    def __init__(self):
        self.__arriba = None
        self.__abajo = None
        self.__nodoInicioMatriz = None
        self.__nodoFinMatriz = None
        self.__letra = None

    def getArriba(self):
        return self.__arriba

    def setArriba(self, arriba):
        self.__arriba = arriba

    def getAbajo(self):
        return self.__abajo

    def setAbajo(self, abajo):
        self.__abajo = abajo

    def getLetra(self):
        return self.__letra

    def setLetra(self, letra):
        self.__letra = letra

    def getInicioMatriz(self):
        return self.__nodoInicioMatriz

    def setInicioMatriz(self, nodoInicioMatriz):
        self.__nodoInicioMatriz = nodoInicioMatriz

    def getFinMatriz(self):
        return self.__nodoFinMatriz

    def setFinMatriz(self, nodoFinMatriz):
        self.__nodoFinMatriz = nodoFinMatriz
