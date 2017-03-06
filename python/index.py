import json
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
    return json.dumps({"success": True})


@app.route('/lista/buscar/<dato>')
def listaBuscar(dato):
    x = lista.buscar(dato)
    return json.dumps({"index": x, "success": True})


@app.route('/lista/eliminar/<indice>')
def listaEliminar(indice):
    index = int(indice)
    resp = lista.eliminarPorIndice(index)
    if resp:
        return json.dumps({"success": True})
    else:
        return json.dumps({"error": "Indice " + indice + " no encontrado.", "success": False})


app.run()
