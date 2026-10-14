class arbolbinario:
    _hijoizq = None
    _hijoder = None
    _valor = None

    def __init__(self, v, izq=None, der=None):
        self._valor = v
        self._hijoder = der
        self._hijoizq = izq

    def añadehijo(self, hijo, derecho=False):
        if derecho:
            self._hijoder = hijo
        else:
            self._hijoizq = hijo

    def buscar(self, v):
        return self.recorrido(buscar=v)

    def eliminar(self, v):
        if v is self.valor:
            self = None
        return self.recorrido(eliminar=v)

    def recorrido(self, buscar=None, eliminar=None):
        if buscar is None and eliminar is None:
            print(self.valor)
        if buscar is not None and buscar is self.valor:
            return self
        else:
            #Para eliminar nodos
            if eliminar is not None:
                if eliminar is self.hijoizq.valor:
                    self.hijoizq = None
                if eliminar is self.hijoder.valor:
                    self.hijoder = None
                return
            #para buscar nodos
            if self.hijoizq is not None:
                izq = self.hijoizq.recorrido(buscar=buscar)
                if izq is not None:
                    return izq
            if self.hijoder is not None:
                der = self.hijoder.recorrido(buscar=buscar)
                return der

    def _damevalor(self):
        return self._valor

    def _damehijoizq(self):
        return self._hijoizq

    def _damehijoder(self):
        return self._hijoder

    def _definehijoizq(self, v):
        self._hijoizq = v

    def _definehijoder(self, v):
        self._hijoder = v

    valor = property(fget = _damevalor)
    hijoizq = property(fget = _damehijoizq, fset = _definehijoizq)
    hijoder = property(fget=_damehijoder, fset=_definehijoder)

abb = arbolbinario(1,
                   arbolbinario(2, arbolbinario(4)),
                   arbolbinario(3))

abb.añadehijo(arbolbinario("x"), derecho=True)

abb.recorrido()
