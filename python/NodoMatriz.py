from NodoMatrizProfundidad import NodoMatrizProfundidad


class NodoMatriz:
    def __init__(self):
        self.__arriba = None
        self.__abajo = None
        self.__izquierda = None
        self.__derecha = None
        self.__cabecera = None
        self.__lateral = None
        self.__profundidadInicio = None
        self.__profundidadFin = None
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

    def getCabecera(self):
        return self.__cabecera

    def setCabecera(self, cabecera):
        self.__cabecera = cabecera

    def getLateral(self):
        return self.__lateral

    def setLateral(self, lateral):
        self.__lateral = lateral

    def getProfundidadInicio(self):
        return self.__profundidadInicio

    def setProfundidadInicio(self, profundidadInicio):
        self.__profundidadInicio = profundidadInicio

    def getProfundidadFin(self):
        return self.__profundidadFin

    def setProfundidadFin(self, profundidadFin):
        self.__profundidadFin = profundidadFin

    def insertar(self, letra, dominio, correo):
        nuevo = NodoMatrizProfundidad()
        nuevo.setLetra(letra)
        nuevo.setDominio(dominio)
        nuevo.setCorreo(correo)

        if self.__profundidadInicio is None:
            self.__profundidadInicio = self.__profundidadFin = nuevo
        else:
            # insertar al final
            self.__profundidadFin.setAbajo(nuevo)
            nuevo.setArriba(self.__profundidadFin)
            self.__profundidadFin = nuevo

        return nuevo

    def buscar(self, correo):
        nodo = self.__profundidadInicio
        while nodo is not None:
            if nodo.getCorreo() == correo:
                return nodo
            nodo = nodo.getAbajo()
        return None
