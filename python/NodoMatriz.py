class NodoMatriz:
    def __init__(self):
        self.__arriba = None
        self.__abajo = None
        self.__izquierda = None
        self.__derecha = None
        self.__cabecera = None
        self.__lateral = None
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

    def getIzquierda(self):
        return self.__izquierda

    def setIzquierda(self, izquierda):
        self.__izquierda = izquierda

    def getDerecha(self):
        return self.__derecha

    def setDerecha(self, derecha):
        self.__derecha = derecha

    def getLetra(self):
        return self.__letra

    def setLetra(self, letra):
        self.__letra = letra

    def getDominio(self):
        return self.__dominio

    def setDominio(self, dominio):
        self.__dominio = dominio

    def getCorreo(self):
        return self.__correo

    def setCorreo(self, correo):
        self.__correo = correo

    def getCabecera(self):
        return self.__cabecera

    def setCabecera(self, cabecera):
        self.__cabecera = cabecera

    def getLateral(self):
        return self.__lateral

    def setLateral(self, lateral):
        self.__lateral = lateral
