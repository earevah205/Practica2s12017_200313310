import json
from flask import Flask
# from flask import request
from ListaSimple import ListaSimple
from Cola import Cola
from Pila import Pila

app = Flask(__name__)
mLista = ListaSimple()
mCola = Cola()
mPila = Pila()


@app.route('/')
def hello_world():
    return 'Practica2'


@app.route('/lista/agregar/<dato>')
def listaAgregar(dato):
    mLista.agregarAlFinal(dato)
    return json.dumps({"success": True})


@app.route('/lista/buscar/<dato>')
def listaBuscar(dato):
    x = mLista.buscar(dato)
    return json.dumps({"index": x, "success": True})


@app.route('/lista/eliminar/<indice>')
def listaEliminar(indice):
    index = int(indice)
    resp = mLista.eliminarPorIndice(index)
    if resp:
        return json.dumps({"success": True})
    else:
        o = {"error": "Indice " + indice + " no encontrado.", "success": False}
        return json.dumps(o)


@app.route('/cola/queue/<dato>')
def colaQueue(dato):
    numero = int(dato)
    if numero == 0:
        o = {"error": "No se permite ingresar el numero 0.", "success": False}
        return json.dumps(o)
    else:
        mCola.encolar(numero)
        return json.dumps({"success": True})


@app.route('/cola/dequeue')
def colaDequeue():
    x = mCola.desencolar()
    return json.dumps({"numero": x, "success": True})


@app.route('/pila/push/<dato>')
def pilaPush(dato):
    numero = int(dato)
    if numero == 0:
        o = {"error": "No se permite ingresar el numero 0.", "success": False}
        return json.dumps(o)
    else:
        mPila.push(numero)
        return json.dumps({"success": True})


@app.route('/pila/pop')
def pilaPop():
    x = mPila.pop()
    return json.dumps({"numero": x, "success": True})


app.run()
