class nodo:

    _valor = ""
    _hijos = []

    def __init__(self, v):
        self._valor = v
        self._hijos = []

    def eliminar_hijo(self, v):
        for i in range(len(self._hijos)):
            if self._hijos[i]._valor == v:
                self._hijos.pop(i)
                break

    def damevalor(self):
        return self._valor

    def definevalor(self, v):
        self._valor = v 

    valor = property(fget=damevalor, fset=definevalor)

class trie:

    _raiz = None

    def __init__(self):
        self._raiz = nodo("^")

    def buscar(self, t):
        prefijo = self.prefijo_comun(t)
        nodo = prefijo[0]
        long = prefijo[1]
        for h in nodo._hijos:
            if h._valor == "$" and long is len(t):
                return True
        return False

    def prefijo_comun(self, t):
        actual = self._raiz
        i = 0
        encontrado = False
        nodos = []
        for caracter in t:
            for hijo in actual._hijos:
                if hijo._valor is caracter:
                    actual = hijo
                    i += 1
                    encontrado = True
                    nodos.append(hijo)
                    break
            if not encontrado: break
            encontrado = False

        return [actual, i, nodos]

    def insertar(self, t):
        prefijo = self.prefijo_comun(t)
        nodo_comienzo = prefijo[0]
        comienzo = prefijo[1]

        for i in range(comienzo, len(t)):
            nodo_comienzo._hijos.append(nodo(t[i]))
            l = len(nodo_comienzo._hijos)
            nodo_comienzo = nodo_comienzo._hijos[l-1]

        nodo_comienzo._hijos.append(nodo("$"))

    def eliminar(self, t):
        prefijo = self.prefijo_comun(t)
        nodo = prefijo[0]
        long = prefijo[1]
        nodos = prefijo[2]
        for h in nodo._hijos:
            if h._valor == "$" and long is len(t):
                #Borrando nodos hojas
                nodos.append(h)
                nodos.insert(0, self._raiz)
                nodos = list(reversed(nodos))
                #Eliminando de derecha a izquierda
                for i in range(len(nodos)):
                    if len(nodos[i]._hijos) == 0:#cambiamos "is" por "=="
                        nodos[i+1].eliminar_hijo(nodos[i]._valor)
                break

t = trie()
t.insertar("sting")
t.insertar("sofa")
t.insertar("sobre")
t.insertar("arnaldo")

print(t.buscar("arnaldo"))
print(t.buscar("arnaldon"))
print(t.buscar("stinger"))
print(t.buscar("sting"))
print("-"*20)
t.eliminar("arnaldo")
t.eliminar("sofa")
print(t.buscar("arnaldo"))
print(t.buscar("sofa"))
