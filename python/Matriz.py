from NodoMatriz import NodoMatriz
from ListaCabeceraMatriz import ListaCabeceraMatriz
from ListaLateralMatriz import ListaLateralMatriz


class Matriz:
    def __init__(self):
        self.__listaCabecera = ListaCabeceraMatriz()
        self.__listaLateral = ListaLateralMatriz()

    def getListaCabecera(self):
        return self.__listaCabecera

    def insertar(self, dominio, letra, correo):
        nuevo = NodoMatriz()
        nuevo.setCorreo(correo)

        cabecera = self.__listaCabecera.buscar(dominio)
        if cabecera is None:
            cabecera = self.__listaCabecera.insertar(dominio)
        nuevo.setCabecera(cabecera)

        lateral = self.__listaLateral.buscar(letra)
        if lateral is None:
            lateral = self.__listaLateral.insertar(letra)
        nuevo.setLateral(lateral)

        # si la cabecera aun no tiene el inicio del Matriz
        # es porque esta vacio
        if cabecera.getNodoInicioMatriz() is None:
            cabecera.setNodoInicioMatriz(nuevo)
            cabecera.setNodoFinMatriz(nuevo)
        else:
            if letra < cabecera.getNodoInicioMatriz().getLateral().getLetra():
                self.insertarAlInicioY(cabecera.getNodoInicioMatriz(), nuevo)
                cabecera.setNodoInicioMatriz(nuevo)
            elif letra > cabecera.getNodoFinMatriz().getLateral().getLetra():
                self.insertarAlFinalY(cabecera.getNodoFinMatriz(), nuevo)
                cabecera.setNodoFinMatriz(nuevo)
            else:
                self.insertarAlMedioY(cabecera.getNodoInicioMatriz(), nuevo)

        # si la cabecera aun no tiene el inicio del Matriz
        # es porque esta vacio
        if lateral.getNodoInicioMatriz() is None:
            lateral.setNodoInicioMatriz(nuevo)
            lateral.setNodoFinMatriz(nuevo)
        else:
            iDominio = lateral.getNodoInicioMatriz().getCabecera().getDominio()
            fDominio = lateral.getNodoFinMatriz().getCabecera().getDominio()
            if (dominio < iDominio):
                self.insertarAlInicioX(lateral.getNodoInicioMatriz(), nuevo)
                lateral.setNodoInicioMatriz(nuevo)
            elif (dominio > fDominio):
                self.insertarAlFinalX(lateral.getNodoFinMatriz(), nuevo)
                lateral.setNodoFinMatriz(nuevo)
            else:
                self.insertarAlMedioX(lateral.getNodoInicioMatriz(), nuevo)
        return nuevo

    def insertarAlInicioY(self, nodoInicio, nuevo):
        nuevo.setAbajo(nodoInicio)
        nodoInicio.setArriba(nuevo)
        nodoInicio = nuevo

    def insertarAlFinalY(self, nodoFin, nuevo):
        nodoFin.setAbajo(nuevo)
        nuevo.setArriba(nodoFin)
        nodoFin = nuevo

    def insertarAlMedioY(self, nodoInicio, nuevo):
        temp = nodoInicio
        while temp.getLateral().getLetra() < nuevo.getLateral().getLetra():
            temp = temp.getAbajo()

        temp2 = temp.getArriba()
        temp2.setAbajo(nuevo)
        nuevo.setAbajo(temp)
        nuevo.setArriba(temp2)
        temp.setArriba(nuevo)

    def insertarAlInicioX(self, nodoInicio, nuevo):
        nuevo.setDerecha(nodoInicio)
        nodoInicio.setIzquierda(nuevo)
        nodoInicio = nuevo

    def insertarAlFinalX(self, nodoFin, nuevo):
        nodoFin.setDerecha(nuevo)
        nuevo.setIzquierda(nodoFin)
        nodoFin = nuevo

    def insertarAlMedioX(self, nodoInicio, nuevo):
        temp = nodoInicio
        while (
            temp.getCabecera().getDominio() < nuevo.getCabecera().getDominio()
        ):
            temp = temp.getDerecha()

        temp2 = temp.getIzquierda()
        temp2.setDerecha(nuevo)
        nuevo.setDerecha(temp)
        nuevo.setIzquierda(temp2)
        temp.setIzquierda(nuevo)

    def bucarCabecera(self, dominio):
        lista = []
        if (self.__listaCabecera.buscar(dominio) is not None):
            nodo = self.__listaCabecera.buscar(dominio).getNodoInicioMatriz()

            while (nodo is not None):
                lista.append(nodo.getCorreo())
                nodo = nodo.getAbajo()

        return lista

    def obtenerNodo(self, dominio, letra):
        nodoResultante = None
        if (self.__listaCabecera.buscar(dominio) is not None):
            nodo = self.__listaCabecera.buscar(dominio).getNodoInicioMatriz()

            while (nodo is not None):
                if (nodo.getLateral().getLetra() == letra):
                    nodoResultante = nodo
                    nodo = None
                else:
                    nodo = nodo.getAbajo()

        if (nodoResultante is not None):
            return nodoResultante

        return None
