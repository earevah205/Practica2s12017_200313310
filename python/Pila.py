from NodoPila import NodoPila


class Pila:
    def __init__(self):
        self.__nodoInicio = None
        self.__nodoFin = None

    def push(self, numero):
        nuevo = NodoPila()
        nuevo.setNumero(numero)
        if self.__nodoInicio is None:
            self.__nodoInicio = self.__nodoFin = nuevo
        else:
            nuevo.setSiguiente(self.__nodoInicio)
            self.__nodoInicio = nuevo

        return nuevo

    def pop(self):
        if self.__nodoInicio is None:
            return 0

        temp = self.__nodoInicio
        anterior = None

        # recorremos la lista
        x = 0
        numero = 0
        while temp is not None:
            # si el nodo contiene la palabra que estamos buscando
            # entonces lo eliminamos
            if x == 0:

                numero = temp.getNumero()
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
        return numero

    def getGraphvizData(self):
        nodo = self.__nodoInicio
        graphvizData = ""
        x = 1
        while nodo is not None:
            if nodo.getSiguiente() is not None:
                s = "{N" + str(nodo.getNumero()) + str(x)
                s += " [label=\"" + str(nodo.getNumero()) + "\"] }"
                s += " -> {N" + str(nodo.getSiguiente().getNumero()) + str(x+1)
                s += " [label=\"" + str(nodo.getSiguiente().getNumero()) + "\"] }"
                graphvizData += s
            else:
                s = "{N" + str(nodo.getNumero()) + str(x)
                s += " [label=\"" + str(nodo.getNumero()) + "\"] }"
                graphvizData += s
            x += 1
            nodo = nodo.getSiguiente()

        return graphvizData
