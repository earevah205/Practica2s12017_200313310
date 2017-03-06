from NodoLateralMatriz import NodoLateralMatriz


class ListaLateralMatriz:
    def __init__(self):
        self.__nodoInicio = None
        self.__nodoFin = None

    def insertarAlInicio(self, nuevo):
        nuevo.setAbajo(self.__nodoInicio)
        self.__nodoInicio.setArriba(nuevo)
        self.__nodoInicio = nuevo

    def insertarAlFinal(self, nuevo):
        self.__nodoFin.setAbajo(nuevo)
        nuevo.setArriba(self.__nodoFin)
        self.__nodoFin = nuevo

    def insertarAlMedio(self, nuevo):
        temp = self.__nodoInicio

        while temp.getLetra() < nuevo.getLetra():
            temp = temp.getAbajo()

        temp2 = temp.getArriba()
        temp2.setAbajo(nuevo)
        nuevo.setAbajo(temp)
        nuevo.setArriba(temp2)
        temp.setArriba(nuevo)

    def insertar(self, letra):
        nuevo = NodoLateralMatriz()
        nuevo.setLetra(letra)

        if self.__nodoInicio is None:
            self.__nodoInicio = self.__nodoFin = nuevo
        else:
            if letra < self.__nodoInicio.getLetra():
                self.insertarAlInicio(nuevo)
            elif letra > self.__nodoFin.getLetra():
                self.insertarAlFinal(nuevo)
            else:
                self.insertarAlMedio(nuevo)
        return nuevo

    def buscar(self, letra):
        nodo = self.__nodoInicio
        while nodo is not None:
            if nodo.getLetra() == letra:
                return nodo
            nodo = nodo.getAbajo()
        return None

    def getNodoInicio(self):
        return self.__nodoInicio

    def setNodoInicio(self, nodoInicio):
        self.__nodoInicio = nodoInicio

    def getNodoFin(self):
        return self.__nodoFin

    def setNodoFin(self, nodoFin):
        self.__nodoFin = nodoFin
