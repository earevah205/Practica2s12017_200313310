class NodoCabeceraMatriz:
    def __init__(self):
        self.__izquierda = None
        self.__derecha = None
        self.__nodoInicioMatriz = None
        self.__nodoFinMatriz = None
        self.__dominio = None

    def getIzquierda(self):
        return self.__izquierda

    def setIzquierda(self, izquierda):
        self.__izquierda = izquierda

    def getDerecha(self):
        return self.__derecha

    def setDerecha(self, derecha):
        self.__derecha = derecha

    def getDominio(self):
        return self.__dominio

    def setDominio(self, dominio):
        self.__dominio = dominio

    def getInicioMatriz(self):
        return self.__nodoInicioMatriz

    def setInicioMatriz(self, nodoInicioMatriz):
        self.__nodoInicioMatriz = nodoInicioMatriz

    def getFinMatriz(self):
        return self.__nodoFinMatriz

    def setFinMatriz(self, nodoFinMatriz):
        self.__nodoFinMatriz = nodoFinMatriz
