from NodoMatriz import NodoMatriz
from ListaCabeceraMatriz import ListaCabeceraMatriz
from ListaLateralMatriz import ListaLateralMatriz


class Matriz:
    def __init__(self):
        self.__listaCabecera = ListaCabeceraMatriz()
        self.__listaLateral = ListaLateralMatriz()

    def getListaCabecera(self):
        return self.__listaCabecera

    def eliminar(self, dominio, letra, correo):
        mensaje = ""
        cabecera = self.__listaCabecera.buscar(dominio)
        if cabecera is None:
            mensaje = "No existe el Dominio " + dominio
            print(mensaje)
            return mensaje

        lateral = self.__listaLateral.buscar(letra)
        if lateral is None:
            mensaje = "No existe ningun correo con inicial " + letra
            print(mensaje)
            return mensaje

        nodo = self.obtenerNodo(dominio, letra)
        nodoProfundidad = nodo.buscar(correo)
        if nodoProfundidad is None:
            mensaje = "No existe el correo " + correo + "@" + dominio
            print(mensaje)
            return mensaje

        # ya que lo encontramos procedemos a eliminarlo de la matriz
        if nodoProfundidad != nodo.getProfundidadInicio():
            # simplemente remover el nodoProfundidad
            if nodoProfundidad.getAbajo() is not None:
                nodoProfundidad.getArriba().setAbajo(
                    nodoProfundidad.getAbajo()
                )
                nodoProfundidad.getAbajo().setArriba(
                    nodoProfundidad.getArriba()
                )
            else:
                nodoProfundidad.getArriba().setAbajo(None)
                nodo.setProfundidadFin(nodoProfundidad.getArriba())
        else:

            if nodoProfundidad.getAbajo() is not None:
                nodo.setProfundidadInicio(nodoProfundidad.getAbajo())
            else:
                # tenemos que remover el nodo y luego revisar si tenemos que
                # eliminar la cabecera y el lateral

                # operaciones con la cabecera
                if (nodo.getCabecera().getInicioMatriz() != nodo):
                    if nodo.getAbajo() is not None:
                        nodo.getArriba().setAbajo(nodo.getAbajo())
                        nodo.getAbajo().setArriba(nodo.getArriba())
                    else:
                        nodo.getArriba().setAbajo(None)
                        nodo.getCabecera().setFinMatriz(nodo.getArriba())
                else:
                    if nodo.getAbajo() is not None:
                        nodo.getCabecera().setInicioMatriz(nodo.getAbajo())
                        nodo.getAbajo().setArriba(None)
                    else:
                        # remover cabecera
                        self.__listaCabecera.eliminar(dominio)

                # operaciones con el lateral
                if (nodo.getLateral().getInicioMatriz() != nodo):
                    if nodo.getDerecha() is not None:
                        nodo.getIzquierda().setDerecha(nodo.getDerecha())
                        nodo.getDerecha().setIzquierda(nodo.getIzquierda())
                    else:
                        nodo.getIzquierda().setDerecha(None)
                        nodo.getLateral().setFinMatriz(nodo.getIzquierda())
                else:
                    if nodo.getDerecha() is not None:
                        nodo.getLateral().setInicioMatriz(nodo.getDerecha())
                        nodo.getDerecha().setIzquierda(None)
                    else:
                        # remover lateral
                        self.__listaLateral.eliminar(letra)
        return ""

    def insertar(self, dominio, letra, correo):
        cabecera = self.__listaCabecera.buscar(dominio)
        if cabecera is None:
            print("---creando cabecera " + dominio)
            cabecera = self.__listaCabecera.insertar(dominio)
        print("usando cabecera " + dominio)

        lateral = self.__listaLateral.buscar(letra)
        if lateral is None:
            print("---creando lateral " + letra)
            lateral = self.__listaLateral.insertar(letra)
        print("usando lateral " + letra)

        # buscamos si ya existe el primer nodo con la letra
        nodo = self.obtenerNodo(dominio, letra)

        if nodo is not None:
            nodo.insertar(letra, dominio, correo)
            return nodo
        else:
            nuevo = NodoMatriz()
            nuevo.setLetra(letra)
            nuevo.setDominio(dominio)
            nuevo.setCabecera(cabecera)
            nuevo.setLateral(lateral)
            nuevo.insertar(letra, dominio, correo)

            # si la cabecera aun no tiene el inicio del Matriz
            # es porque esta vacio
            if cabecera.getInicioMatriz() is None:
                print("---lista cabecera vacia, creando nodo inicio y fin")
                cabecera.setInicioMatriz(nuevo)
                cabecera.setFinMatriz(nuevo)
            else:
                if letra < cabecera.getInicioMatriz().getLateral().getLetra():
                    print("insertarAlInicioY")
                    self.insertarAlInicioY(cabecera.getInicioMatriz(), nuevo)
                    cabecera.setInicioMatriz(nuevo)
                elif letra > cabecera.getFinMatriz().getLateral().getLetra():
                    print("insertarAlFinalY")
                    self.insertarAlFinalY(cabecera.getFinMatriz(), nuevo)
                    cabecera.setFinMatriz(nuevo)
                else:
                    print("insertarAlMedioY")
                    self.insertarAlMedioY(cabecera.getInicioMatriz(), nuevo)

            # si la cabecera aun no tiene el inicio del Matriz
            # es porque esta vacio
            if lateral.getInicioMatriz() is None:
                print("---lista lateral vacia, creando nodo inicio y fin")
                lateral.setInicioMatriz(nuevo)
                lateral.setFinMatriz(nuevo)
            else:
                iDominio = lateral.getInicioMatriz().getCabecera().getDominio()
                fDominio = lateral.getFinMatriz().getCabecera().getDominio()
                if (dominio < iDominio):
                    print("insertarAlInicioX")
                    self.insertarAlInicioX(lateral.getInicioMatriz(), nuevo)
                    lateral.setInicioMatriz(nuevo)
                elif (dominio > fDominio):
                    print("insertarAlFinalX")
                    self.insertarAlFinalX(lateral.getFinMatriz(), nuevo)
                    lateral.setFinMatriz(nuevo)
                else:
                    print("insertarAlMedioX")
                    self.insertarAlMedioX(lateral.getInicioMatriz(), nuevo)

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
            nodo = self.__listaCabecera.buscar(dominio).getInicioMatriz()

            while (nodo is not None):
                lista.append(nodo.getCorreo())
                nodo = nodo.getAbajo()

        return lista

    def obtenerNodo(self, dominio, letra):
        nodoResultante = None
        if (self.__listaCabecera.buscar(dominio) is not None):
            nodo = self.__listaCabecera.buscar(dominio).getInicioMatriz()

            while (nodo is not None):
                if (nodo.getLateral().getLetra() == letra):
                    nodoResultante = nodo
                    nodo = None
                else:
                    nodo = nodo.getAbajo()

        if (nodoResultante is not None):
            return nodoResultante

        return None

    def buscarPorDominio(self, dominio):
        lista = []
        if (self.__listaCabecera.buscar(dominio) is not None):
            nodo = self.__listaCabecera.buscar(dominio).getInicioMatriz()

            while (nodo is not None):
                nodoProfundidad = nodo.getProfundidadInicio()
                while (nodoProfundidad is not None):
                    lista.append(nodoProfundidad.getCorreo())
                    nodoProfundidad = nodoProfundidad.getAbajo()
                nodo = nodo.getAbajo()

        return lista

    def buscarPorLetra(self, letra):
        lista = []
        if (self.__listaLateral.buscar(letra) is not None):
            nodo = self.__listaLateral.buscar(letra).getInicioMatriz()

            while (nodo is not None):
                nodoProfundidad = nodo.getProfundidadInicio()
                while (nodoProfundidad is not None):
                    lista.append(nodoProfundidad.getCorreo())
                    nodoProfundidad = nodoProfundidad.getAbajo()
                nodo = nodo.getDerecha()

        return lista
