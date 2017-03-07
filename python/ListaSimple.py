from NodoLista import NodoLista


class ListaSimple:
    def __init__(self):
        self.__nodoInicio = None
        self.__nodoFin = None

    def agregarAlInicio(self, dato):
        nuevo = NodoLista()
        nuevo.setDato(dato)
        if self.__nodoInicio is None:
            self.__nodoInicio = self.__nodoFin = nuevo
        else:
            nuevo.setSiguiente(self.__nodoInicio)
            self.__nodoInicio = nuevo

        return nuevo

    def agregarAlFinal(self, dato):
        nuevo = NodoLista()
        nuevo.setDato(dato)
        if self.__nodoFin is None:
            self.__nodoInicio = self.__nodoFin = nuevo
        else:
            self.__nodoFin.setSiguiente(nuevo)
            self.__nodoFin = nuevo
        return nuevo

    def eliminarPorIndice(self, indice):

        if self.__nodoInicio is None:
            return None

        temp = self.__nodoInicio
        anterior = None

        # recorremos la lista
        x = 0
        eliminado = False
        while temp is not None:
            # si el nodo contiene la palabra que estamos buscando
            # entonces lo eliminamos
            if x == indice:

                eliminado = True
                # es el inicio de la lista
                if anterior is None:
                    self.__nodoInicio = temp.getSiguiente()
                else:
                    anterior.setSiguiente(temp.getSiguiente())

                # para que salga del ciclo
                temp = None

            else:
                anterior = temp
                temp = temp.getSiguiente()
            x += 1
        return eliminado

    def eliminar(self, dato):

        if self.__nodoInicio is None:
            return None

        temp = self.__nodoInicio
        anterior = None

        # recorremos la lista
        eliminado = False
        while temp is not None:
            # si el nodo contiene la palabra que estamos buscando
            # entonces lo eliminamos
            if temp.getDato() == dato:
                eliminado = True
                # es el inicio de la lista
                if anterior is None:
                    self.__nodoInicio = temp.getSiguiente()
                else:
                    anterior.setSiguiente(temp.getSiguiente())

                # para que salga del ciclo
                temp = None

            else:
                anterior = temp
                temp = temp.getSiguiente()
        return eliminado

    def buscar(self, dato):

        if self.__nodoInicio is None:
            # si no hay nada en la lista retorna -1
            return -1

        temp = self.__nodoInicio

        # recorremos la lista
        i = 0
        while temp is not None:
            # si el nodo contiene la palabra que estamos buscando
            # entonces lo eliminamos
            if temp.getDato() == dato:
                return i

                # para que salga del ciclo
                temp = None

            else:
                temp = temp.getSiguiente()

            i += 1

        # si no encontro nada retorna -1
        return -1

    def getInicio(self):
        return self.__nodoInicio

    def getFinal(self):
        return self.__nodoFin

    def getGraphvizData(self):
        nodo = self.__nodoInicio
        graphvizData = ""
        x = 1
        while nodo is not None:
            if nodo.getSiguiente() is not None:
                s = "{" + nodo.getDato() + str(x)
                s += " [label=\"" + nodo.getDato() + "\"] }"
                s += " -> {" + nodo.getSiguiente().getDato() + str(x+1)
                s += " [label=\"" + nodo.getSiguiente().getDato() + "\"] }"
                graphvizData += s
            else:
                s = "{" + nodo.getDato() + str(x)
                s += " [label=\"" + nodo.getDato() + "\"] }"
                graphvizData += s
            x += 1
            nodo = nodo.getSiguiente()

        return graphvizData
