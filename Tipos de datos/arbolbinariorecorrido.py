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

    def eshoja(self):
        return self.hijoder is None and self.hijoizq is None
    
class arbol_binario_busqueda(arbolbinario):
    def __init__(self, v, izq=None, der=None):
        super().__init__(v, izq=izq, der=der)

    def insertar(self, v):
        if v > self.valor:
            if self.hijoder is not None:
                return self.hijoder.insertar(v)
            else:
                self.hijoder = arbol_binario_busqueda(v)
        if v <= self.valor:
            if self.hijoizq is not None:
                self.hijoizq.insertar(v)
            else:
                self.hijoizq = arbol_binario_busqueda(v)

    def buscar(self, v):
        if self.valor is v:
            return self
        if self.valor < v:
            if self.hijoder is not None:
                return self.hijoder.buscar(v)
        else:
            if self.hijoizq is not None:
                return self.hijoizq.buscar(v)

    def eliminar(self, v):
        #El valor se encuentra en el hijo derecho
        if self.valor < v:
            if self.hijoder.valor is v:
                if self.hijoder.eshoja():
                    self.hijoder = None
                    return 
                if self.hijoder.hijoder is None:
                    #si no tiene hijo derecho y no es una hoja entonces debe tener hijo izquierdo
                    self.hijoder = self.hijoder.hijoizq
                elif self.hijoder.hijoizq is None:
                    #si no tiene hijo izquierdo y no es una hoja entonces debe tener hijo derecho
                    self.hijoder = self.hijoder.hijoder
                else : 
                    #tiene dos hijos
                    if self.hijoder is not None:
                        nvalor = self.hijoder._menor_valor(elimina=True)
                    else:
                        nvalor = self.hijoizq._mayor_valor(elimina=True)
                    self.hijoder.valor = nvalor
            else:
                self.hijoder.eliminar(v)
        #el valor se encuentra en el hijo izquierdo
        elif self.valor >= v:
            #el valor se encuentra en el nodo actual
            if self.valor is v:
                if self.eshoja():
                    self.valor = None
                elif self.hijoder is None:
                    self.valor = self.hijoizq.valor
                    temp = self.hijoizq
                    self.hijoizq = temp.hijoizq
                    self.hijoder = temp.hijoder
                elif self.hijoizq is None:
                    self.valor = self.hijoder.valor
                    temp = self.hijoder
                    self.hijoizq = temp.hijoizq
                    self.hijoder = temp.hijoder
                else:
                    if self.hijoder is not None:
                        nvalor = self.hijoder._menor_valor(elimina=True)
                    else:
                        nvalor = self.hijoizq._mayor_valor(elimina=True)
                    self.valor = nvalor
            #si el hijo izquierdo tiene valor v
            elif self.hijoizq.valor is v:
                #si es una hoja
                if self.hijoizq.eshoja():
                    self.hijoizq = None
                    return
                if self.hijoizq.hijoder is None:
                    #si no tiene hijo derecho y no es una hoja entonces debe tener hijo izquierdo
                    self.hijoizq = self.hijoizq.hijoizq
                elif self.hijoizq.hijoizq is None:
                    #si no tiene hijo izquierdo y no es una hoja entonces debe tener hijo derecho
                    self.hijoizq = self.hijoizq.hijoder
                else:
                    #tiene dos hijos
                    if self.hijoder is not None:
                        nvalor = self.hijoder._menor_valor(elimina=True)
                    else:
                        nvalor = self.hijoizq._mayor_valor(elimina=True)
                    self.hijoizq.valor = nvalor
            else:
                self.hijoizq.eliminar(v)

    def _menor_valor(self, elimina = False):
        actual = self
        if self.hijoizq.hijoizq is not None:
            actual = self.hijoizq
            while not actual.eshoja():
                actual = actual.hijoizq

        valor = actual.hijoizq.valor
        if elimina:
            actual.hijoizq = None
        return valor

    def _mayor_valor(self, elimina = False):
        actual = self
        if self.hijoder.hijoder is not None:
            actual = self.hijoder
            while not actual.eshoja():
                actual = actual.hijoder

        valor = actual.hijoder.valor
        if elimina:
            actual.hijoder = None
        return valor

    def inorden(self):
        if self.eshoja():
            print(self.valor)
        else:
            if self.hijoizq is not None:
                self.hijoizq.inorden()
            print(self.valor)
            if self.hijoder is not None:
                self.hijoder.inorden()

    def preorden(self):
        if self.eshoja():
            print(self.valor)
        else:
            print(self.valor)
            if self.hijoizq is not None:
                self.hijoizq.preorden()
            if self.hijoder is not None:
                 self.hijoder.preorden()

    def postorden(self):
        if self.eshoja():
            print(self.valor)
        else:
            if self.hijoizq is not None:
                self.hijoizq.postorden()
            if self.hijoder is not None:
                self.hijoder.postorden()
            print(self.valor)

abb = arbol_binario_busqueda(6)
abb.insertar(4)
abb.insertar(2)
abb.insertar(1)
abb.insertar(3)
abb.insertar(8)
abb.insertar(7)
abb.insertar(9)
print("recorrido inorden")
abb.inorden()

print("recorrido preorden")
abb.preorden()

print("recorrido postorden")
abb.postorden()
