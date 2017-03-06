
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
# from flask import request
from ListaSimple import ListaSimple

app = Flask(__name__)
lista = ListaSimple()


@app.route('/')
def hello_world():
    return 'Practica2'


@app.route('/lista/agregar/<dato>')
def listaAgregar(dato):
    lista.agregarAlInicio(dato)
    return 'Dato = ' + dato + ' agregado correctamente.'


@app.route('/lista/buscar/<dato>')
def listaBuscar(dato):
    x = lista.buscar(dato)
    if x >= 0:
        return 'El dato ' + dato + ' se encontro en el indice = ' + str(x)
    else:
        return 'No se encontro el dato ' + dato


@app.route('/lista/eliminar/<indice>')
def listaEliminar(indice):
    lista.eliminarPorIndice(indice)
    return 'Se elimino correctamente el indice = ' + indice


app.run()
