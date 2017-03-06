from NodoCabeceraMatriz import NodoCabeceraMatriz


class ListaCabeceraMatriz:
    def __init__(self):
        self.__nodoInicio = None
        self.__nodoFin = None

    def insertar(self, dominio):
        nuevo = NodoCabeceraMatriz()
        nuevo.setDominio(dominio)

        if self.__nodoInicio is None:
            self.__nodoInicio = self.__nodoFin = nuevo
        else:
            if dominio < self.__nodoInicio.getDominio():
                self.__insertarAlInicio(nuevo)
            elif dominio > self.__nodoFin.getdominio():
                self.__insertarAlFinal(nuevo)
            else:
                self.__insertarAlMedio(nuevo)
        return nuevo

    def insertarAlInicio(self, nuevo):
        nuevo.setDerecha(self.__nodoInicio)
        self.__nodoInicio.setIzquierda(nuevo)
        self.__nodoInicio = nuevo

    def insertarAlFinal(self, nuevo):
        self.__nodoFin.setDerecha(nuevo)
        nuevo.setIzquierda(self.__nodoFin)
        self.__nodoFin = nuevo

    def insertarAlMedio(self, nuevo):
        temp = self.__nodoInicio
        while temp.getDominio() < nuevo.getDominio():
            temp = temp.getDerecha()

        temp2 = temp.getIzquierda()
        temp2.setDerecha(nuevo)
        nuevo.setDerecha(temp)
        nuevo.setIzquierda(temp2)
        temp.setIzquierda(nuevo)

    def buscar(self, dominio):

        nodo = self.__nodoInicio
        while nodo is not None:
            if nodo.getdominio() == dominio:
                return nodo
            nodo = nodo.getDerecha()
        return None

    def getNodoInicio(self):
        return self.__nodoInicio

    def setNodoInicio(self, nodoInicio):
        self.__nodoInicio = nodoInicio

    def getNodoFin(self):
        return self.__nodoFin

    def setNodoFin(self, nodoFin):
        self.__nodoFin = nodoFin
