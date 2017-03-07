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
                self.insertarAlInicio(nuevo)
            elif dominio > self.__nodoFin.getDominio():
                self.insertarAlFinal(nuevo)
            else:
                self.insertarAlMedio(nuevo)
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
            if nodo.getDominio() == dominio:
                return nodo
            nodo = nodo.getDerecha()
        return None

    def eliminar(self, dominio):

        if self.__nodoInicio is None:
            return None

        temp = self.__nodoInicio
        anterior = None

        # recorremos la lista
        eliminado = False
        while temp is not None:
            # si el nodo contiene la palabra que estamos buscando
            # entonces lo eliminamos
            if temp.getDominio() == dominio:
                eliminado = True
                # es el inicio de la lista
                if anterior is None:
                    if temp.getDerecha() is None:
                        self.__nodoFin = None
                        self.__nodoInicio = None
                    else:
                        temp.getDerecha().setIzquierda(None)
                        self.__nodoInicio = temp.getDerecha()
                else:
                    if temp.getDerecha() is None:
                        self.__nodoFin = anterior
                        anterior.setDerecha(None)
                    else:
                        temp.getDerecha().setIzquierda(anterior)
                        anterior.setDerecha(temp.getDerecha())

                # para que salga del ciclo
                temp = None

            else:
                anterior = temp
                temp = temp.getDerecha()
        return eliminado

    def getNodoInicio(self):
        return self.__nodoInicio

    def setNodoInicio(self, nodoInicio):
        self.__nodoInicio = nodoInicio

    def getNodoFin(self):
        return self.__nodoFin

    def setNodoFin(self, nodoFin):
        self.__nodoFin = nodoFin
