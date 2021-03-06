import json
from flask import Flask
# from flask import request
from ListaSimple import ListaSimple
from Cola import Cola
from Pila import Pila
from Matriz import Matriz

app = Flask(__name__)
mLista = ListaSimple()
mCola = Cola()
mPila = Pila()
mMatriz = Matriz()


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


@app.route('/lista/graphviz')
def listaGraphviz():
    graphviz = mLista.getGraphvizData()
    return json.dumps({"graphviz": graphviz, "success": True})


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


@app.route('/cola/graphviz')
def colaGraphviz():
    graphviz = mCola.getGraphvizData()
    return json.dumps({"graphviz": graphviz, "success": True})


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


@app.route('/pila/graphviz')
def pilaGraphviz():
    graphviz = mPila.getGraphvizData()
    return json.dumps({"graphviz": graphviz, "success": True})


@app.route('/matriz/agregar/<dato>')
def matrizAgregar(dato):
    dato = dato.strip()
    letra = list(dato)[0]
    dominio = dato.split("@")[1]
    username = dato.split("@")[0]
    mMatriz.insertar(dominio, letra, username)
    return json.dumps({"success": True})


@app.route('/matriz/eliminar/<dato>')
def matrizEliminar(dato):
    dato = dato.strip()
    letra = list(dato)[0]
    dominio = dato.split("@")[1]
    username = dato.split("@")[0]
    message = mMatriz.eliminar(dominio, letra, username)

    if message == "":
        return json.dumps({"success": True})
    else:
        return json.dumps({"success": False, "error": message})


@app.route('/matriz/buscarLetra/<letra>')
def matrizBuscarLetra(letra):
    letra = letra.strip()
    lista = mMatriz.buscarPorLetra(letra)
    return json.dumps({"success": True, "lista": lista})


@app.route('/matriz/buscarDominio/<dominio>')
def matrizBuscarDominio(dominio):
    dominio = dominio.strip()
    lista = mMatriz.buscarPorDominio(dominio)
    return json.dumps({"success": True, "lista": lista})


@app.route('/matriz/graphviz')
def matrizGraphviz():
    graphviz = mMatriz.getGraphvizData()
    return json.dumps({"graphviz": graphviz, "success": True})


app.run()
