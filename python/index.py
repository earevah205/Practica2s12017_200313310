from ListaSimple import ListaSimple

lista = ListaSimple()

lista.agregarAlInicio("hello")
lista.agregarAlInicio("my")
lista.agregarAlFinal("friend")

x = lista.buscar("friend")
print x

y = lista.buscar("friend2")
print y

lista.eliminar("friend")
x = lista.buscar("friend")
print x

print "Finnn"
