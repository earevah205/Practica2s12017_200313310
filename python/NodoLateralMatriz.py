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

    def getNodoInicioMatriz(self):
        return self.__nodoInicioMatriz

    def setNodoInicioMatriz(self, nodoInicioMatriz):
        self.__nodoInicioMatriz = nodoInicioMatriz

    def getNodoFinMatriz(self):
        return self.__nodoFinMatriz

    def setNodoFinMatriz(self, nodoFinMatriz):
        self.__nodoFinMatriz = nodoFinMatriz
