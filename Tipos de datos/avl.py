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


class avl(arbol_binario_busqueda):
    _factor_equilibrio = 0
    _altura = 0

    def __init__(self, v, izq=None, der=None):
        super().__init__(v, izq=izq, der=der)
        self.factor_equilibrio = 0
        self._altura = 0

    def insertar(self, v):
        if v > self.valor:
            if self.hijoder is not None:
                self.hijoder.insertar(v)
            else:
                self.hijoder = avl(v)
        if v <= self.valor:
            if self.hijoizq is not None:
                self.hijoizq.insertar(v)
            else:
                self.hijoizq = avl(v)
        self.resuelve_desbalance()

    #Realiza las rotaciones necesarias
    #y actualiza el factor de equil.

    def resuelve_desbalance(self):
        self.actualiza_factor_equilib()

        #Rotación a la derecha
        if self.es_rotacion_der():
            self.rotacion_derecha()
        #Rotación a la izquierda
        elif self.es_rotacion_izq():
            self.rotacion_izquierda()
        elif self.es_rotacion_doble_der():
            self.rotacion_doble_der()
        elif self.es_rotacion_doble_izq():
            self.rotacion_doble_izq()

    def actualiza_factor_equilib(self):
        hder = self.hijoder
        hizq = self.hijoizq

        if not hder and not hizq:
            return
        if not hder:
            self._altura = hizq._altura + 1
            self.factor_equilibrio = -(self._altura)
        elif not hizq:
            self._altura = hder._altura + 1
            self.factor_equilibrio = self._altura
        else:
            self._altura = max(hder._altura, hizq._altura) + 1
            self.factor_equilibrio = hder._altura - hizq._altura

    #Decide si efectuar una rotación derecha
    def es_rotacion_der(self):
        return self.factor_equilibrio == -2 and self.hijoizq.factor_equilibrio == -1

    #Decide si efectuar una rotación izquierda
    def es_rotacion_izq(self):
        return self.factor_equilibrio == 2 and self.hijoder.factor_equilibrio == 1

    #Decide si efectuar una doble rotacion derecha
    def es_rotacion_doble_der(self):
        return self.factor_equilibrio == -2 and self.hijoizq.factor_equilibrio == 1

    #Decide si efectuar una doble rotacion izquierda
    def es_rotacion_doble_izq(self):
        return self.factor_equilibrio == 2 and self.hijoder.factor_equilibrio == -1

    def rotacion_derecha(self):
        #prerrequisito
        if self.hijoizq is not None:
            temp = self.valor
            self.valor = self.hijoizq.valor
            hizq = self.hijoizq
            hder = self.hijoder
            self.hijoder = avl(temp, izq=None, der=hder)
            if hizq.hijoder is not None:
                self.hijoder.hijoizq = hizq.hijoder
            if hizq.hijoizq is not None:
                self.hijoizq = hizq.hijoizq
            self.hijoder.actualiza_factor_equilib()
            self.actualiza_factor_equilib()

    def rotacion_izquierda(self):
        #Análogo a rotacion_derecha
        #prerrequisito
        if self.hijoder is not None:
            temp = self.valor
            self.valor = self.hijoder.valor #al parecer aquí está el error
            hizq = self.hijoizq
            hder = self.hijoder
            self.hijoizq = avl(temp, izq=hizq, der=None)
            if hder.hijoizq is not None:
                self.hijoizq.hijoder = hder.hijoizq
            if hder.hijoder is not None:
                self.hijoder = hder.hijoder
            self.hijoizq.actualiza_factor_equilib()
            self.actualiza_factor_equilib()

    def rotacion_doble_der(self):
        self.hijoizq.rotacion_izq() #a lo mejor hay un problema con el nombre
        self.rotacion_derecha()

    def rotacion_doble_izq(self):
        self.hijoder.rotacion_der()
        self.rotacion_izquierda()

    #De igual forma a como sería en un abb pero considerando las rotaciones necesarias cuando se sube por el arbol
    def eliminar(self, v):
        #El valor se encuentra en el hijo derecho
        if self.valor < v:
            if self.hijoder.valor is v:
                if self.hijoder.eshoja():
                    self.hijoder = None
                    self.actualiza_factor_equilib()
                    return True
                if self.hijoder.hijoder is None:
                    #Si no tiene hijo derecho y no es una hoja entonces debe tener hijo izquierdo
                    self.hijoder = self.hijoder.hijoizq
                elif self.hijoder.hijoizq is None:
                    #Si no tiene hijo izquierdo y no es una hoja entonces debe tener hijo derecho
                    self.hijoder = self.hijoder.hijoder
                else:
                    #Tiene dos hijos
                    if self.hijoder is not None:
                        nvalor = self.hijoder._menor_valor(elimina=True)
                    else:
                        nvalor = self.hijoizq._mayor_valor(elimina=True)
                    self.hijoder.valor = nvalor
                self.actualiza_factor_equilib()
            else:
                if self.hijoder.eliminar(v):
                    self.actualiza_factor_equilib()
        #El valor se encuentra en el hijoizq
        elif self.valor >= v:
            #El valor se encuentra en el nodo actual
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
                return True
            #Si el hijo izquierdo tiene valor v
            elif self.hijoizq.valor is v:
                #Si es una hoja
                if self.hijoizq.eshoja():
                    self.hijoizq = None
                    return
                if self.hijoizq.hijoder is None:
                    #Si no tiene hijo derecho y no es una hoja entonces debe tener hijo izquierdo
                    self.hijoizq = self.hijoizq.hijoizq
                elif self.hijoizq.hijoizq is None:
                    #Si no tiene hijoizquierdo y no es una hoja entonces debe tener hijo derecho
                    self.hijoizq = self.hijoizq.hijoder
                else:
                    #Tiene dos hijos
                    if self.hijoder is not None:
                        nvalor = self.hijoder._menor_valor(elimina=True)
                    else:
                        nvalor = self.hijoizq._mayor_valor(elimina=True)
                    self.hijoizq.valor = nvalor
            else:
                if self.hijoizq.eliminar(v):
                    self.actualiza_factor_equilib()
            #Para resolver cualquier problema de desbalance que pueda haber surgido
            self.resuelve_desbalance()

    def _damefactor(self):
        return self._factor_equilibrio

    def _definefactor(self, v):
        self._factor_equilibrio = v

    factor_equilibrio = property(fget = _damefactor, fset = _definefactor)

a = avl(4)
a.insertar(6)
a.insertar(1)
a.insertar(5)
a.insertar(7)
a.insertar(8)
#Eliminando nodo 8
a.eliminar(8)
#Recorrido preorden
# 6 4 1 5 7
