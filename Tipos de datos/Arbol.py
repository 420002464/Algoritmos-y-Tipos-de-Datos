class cola:
    elems = []
    def __init__(self):
        self.elems = []

    def encola(self, x):
        self.elems.append(x)

    def desencola(self):
        if self.fcantidad() > 0: #creo que aquí está mal
            self.elems.pop(0)

    def fcantidad(self):
        return len(self.elems)

    def fprimero(self):
        if self.fcantidad() > 0:
            return self.elems[0]

    primero = property(fget = fprimero)
    cantidad = property(fget = fcantidad)
class arbol:
    _valor = None
    _hijos = None

    def __init__(self, v, hijos=[]):
        self.valor = v
        self._hijos = []
        for h in hijos:
            self._hijos.append(arbol(h))

    def añade_hijo(self, v):
        self._hijos.append(v)

    def buscar(self, v):
        return self.recorrido(buscar=v)

    def elimina_hijo(self, v):
        return self.recorrido(eliminar=v)

    def recorrido(self, imprimir=False, buscar=None, eliminar=None):
        #Para eliminar el árbol
        if eliminar is not None and eliminar is self.valor:
            self.valor = None
            self._hijos = []
            return

        c = cola()
        c.encola(self)

        while c.cantidad > 0:
            #Para imprimir el recorrido
            if imprimir:
                print(c.primero.valor)
            #Para encontrar un subárbol
            if buscar is not None and buscar is c.primero.valor:
                return c.primero
            actual = c.primero
            for i in range(len(actual._hijos)):
                #para eliminar un subárbol
                if eliminar is not None and eliminar is actual._hijos[i].valor:
                    actual._hijos.pop(i)
                    return True
                c.encola(actual._hijos[i])
            c.desencola()

    def damehijos(self):
        return self._hijos

    def damevalor(self):
        return self._valor

    def definevalor(self, v):
        self._valor = v

    def __str__(self):
        return str(self.valor)

a = arbol(1)
a.añade_hijo(arbol(2, [4,5]))
a.añade_hijo(arbol(3))
a.elimina_hijo(2)

print("Encontrado", a.buscar(3))
a.recorrido(imprimir=True)
print(a)
        
