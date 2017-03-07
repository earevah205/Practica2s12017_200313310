from NodoCola import NodoCola


class Cola:
    def __init__(self):
        self.__nodoInicio = None
        self.__nodoFin = None
        self.__tamano = 0

    def top(self):
        if self.__nodoInicio is None:
            return None
        return self.__nodoInicio.getNumero()

    def desencolar(self):
        if self.__nodoInicio is None:
            return None

        numero = self.__nodoInicio.getNumero()

        if self.__nodoInicio.getSiguiente() is None:
            self.__nodoInicio = None
            self.__nodoFin = None
        else:
            self.__nodoInicio = self.__nodoInicio.getSiguiente()

        self.__tamano -= 1
        return numero

    def encolar(self, numero):
        nuevo = NodoCola()
        nuevo.setNumero(numero)

        if self.__nodoFin is None:
            self.__nodoInicio = nuevo
            self.__nodoFin = nuevo
        else:
            self.__nodoFin.setSiguiente(nuevo)
            self.__nodoFin = nuevo

        self.__tamano += 1

    def getTamano(self):
        return self.__tamano

    def getGraphvizData(self):
        graphvizData = ""
        nodo = self.__nodoInicio
        x = 1
        while nodo is not None:
            if nodo.getSiguiente() is not None:
                s = "{N" + str(nodo.getNumero()) + str(x)
                s += " [label=\"" + str(nodo.getNumero()) + "\"] }"
                s += " -> {N" + str(nodo.getSiguiente().getNumero()) + str(x+1)
                s += " [label=\"" + str(nodo.getSiguiente().getNumero())
                s += "\"] }"
                graphvizData += s
            else:
                s = "{N" + str(nodo.getNumero()) + str(x)
                s += " [label=\"" + str(nodo.getNumero()) + "\"] }"
                graphvizData += s
            x += 1
            nodo = nodo.getSiguiente()

        return graphvizData
