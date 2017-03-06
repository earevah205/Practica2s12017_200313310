class NodoCola:
    def __init__(self):
        self.__numero = 0
        self.__siguiente = None

    def getNumero(self):
        return self.__numero

    def setNumero(self, numero):
        self.__numero = numero

    def getSiguiente(self):
        return self.__siguiente

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
