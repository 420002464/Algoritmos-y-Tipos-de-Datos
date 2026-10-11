class nodo:
    _valor = None
    _proximo = None

    def __init__(self, v, p=None):
        self._valor = v
        self._proximo = p

    def _damevalor(self):
        return self._valor

    def _definevalor(self, v):
        self._valor = v 

    def _dameproximo(self):
        return self._proximo

    def _defineproximo(self, v):
        self._proximo = v

    valor = property(fget = _damevalor,
                     fset = _definevalor)
    proximo = property(fget = _dameproximo,
                       fset = _defineproximo)

class lista_enlazada:

    _primero = None
    _ultimo = None
    _cantidad = 0

    def __init__(self, v):
        self._primero = nodo(v)
        self._ultimo = self._primero
        self._cantidad += 1 

    def _damecantidad(self):
        return self._cantidad

    def añadir(self, x):
        nuevo = nodo(x)
        self._ultimo.proximo = nuevo
        self._ultimo = nuevo
        self._cantidad += 1

    def insertar(self, x, pos):
        if pos < 0 or pos > self.cantidad:
            raise Exception('pos '
                            'fuera de rango')
        actual = self._primero
        nuevo = nodo(x)
        if pos == 0: #is
            nuevo.proximo = self._primero
            self._primero = nuevo
        else:
            i = 0
            while i < pos - 1:
                actual = actual.proximo
                i += 1
                temp = actual.proximo
                actual.proximo = nuevo
                nuevo.proximo = temp
                if pos == self.cantidad: # is
                    self._ultimo = nuevo
        self._cantidad += 1

    def posicion(self, x):
        temp = self._primero
        i = 0
        while 1:
            if temp.valor == x: #is
                return i
            if temp.proximo == None: #is
                return -1
            i += 1
            temp = temp.proximo

    def eliminar(self, x):
        posicion = self.posicion(x)
        if posicion == -1: return None #is
        if posicion == 0:
            self._primero = self._primero.proximo
        else:
            actual = self._primero
            i = 0
            while i < posicion - 1:
                actual = actual._proximo
                i += 1
            actual.proximo = actual.proximo.proximo
            if posicion is self.cantidad - 1:
                self._ultimo = actual
        self._cantidad -= 1

    def elementos(self):
        actual = self._primero
        while actual is not None:
            yield actual._valor
            actual = actual.proximo

    cantidad = property(fget = _damecantidad)

l = lista_enlazada(1)
l.añadir(2)
l.añadir(3)
l.insertar(2.3, 2)
l.eliminar(3)

for e in l.elementos():
    print("elementos", e)

print("cantidad", l.cantidad)

        
