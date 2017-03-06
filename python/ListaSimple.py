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

    def eliminar(self, dato):

        if self.__nodoInicio is None:
            return None

        temp = self.__nodoInicio
        anterior = None

        # recorremos la lista
        while temp is not None:
            # si el nodo contiene la palabra que estamos buscando
            # entonces lo eliminamos
            if temp.getDato() == dato:

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


'''
    public String crearImagenGraphviz(){


        GraphViz gv = new GraphViz();
        gv.addln(gv.start_graph());


        NodoDiccionario nodo = nodoInicio;
        int x = 1;
        while(nodo!=null){
            if (nodo.getSiguiente()!=null){
                String s = "{" + nodo.getPalabra().get().toLowerCase() + x + " [label=\"" + nodo.getPalabra().get() + "\"] }";
                s += " -> {" + nodo.getSiguiente().getPalabra().get().toLowerCase() + (x+1) + " [label=\"" + nodo.getSiguiente().getPalabra().get() + "\"] }";
                gv.addln(s);
            }else{
                String s = "{" + nodo.getPalabra().get().toLowerCase() + x + " [label=\"" + nodo.getPalabra().get() + "\"] }";
                gv.addln(s);
            }
            x++;
            nodo = nodo.getSiguiente();
        }

        gv.addln(gv.end_graph());

        System.out.println(gv.getDotSource());
        gv.decreaseDpi();   // 106 dpi
        String type = "gif";
        String repesentationType= "dot";
        String imagePath = gv.getTempDir() + "/diccionario"+frmScrabbleGame.now()+gv.getImageDpi()+"."+ type;
	File out = new File( imagePath );
	gv.writeGraphToFile( gv.getGraph(gv.getDotSource(), type, repesentationType), out );

        return imagePath;

    }
'''
