class NodoMatrizProfundidad:
    def __init__(self):
        self.__arriba = None
        self.__abajo = None
        self.__correo = None
        self.__letra = None
        self.__dominio = None

    def getArriba(self):
        return self.__arriba

    def setArriba(self, arriba):
        self.__arriba = arriba

    def getAbajo(self):
        return self.__abajo

    def setAbajo(self, abajo):
        self.__abajo = abajo

    def getCorreo(self):
        return self.__correo

    def setCorreo(self, correo):
        self.__correo = correo

    def getLetra(self):
        return self.__letra

    def setLetra(self, letra):
        self.__letra = letra

    def getDominio(self):
        return self.__dominio

    def setDominio(self, dominio):
        self.__dominio = dominio
