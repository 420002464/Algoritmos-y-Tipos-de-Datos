class nodo:

    _valor = None
    _visitado = False

    def __init__(self, v):
        self._valor = v
        self._visitado = -1

class grafo:

    _matriz = []
    _n = 0

    def __init__(self, n:int):
        for i in range(n):
            self._n = n
            self._matriz.append([])
            for j in range(n):
                self._matriz[i].append(nodo(-1)) 

    def insertar(self, i: int, j: int):
        if self._n < i < 0 or self._n < j < 0:
            raise Exception("Nodos incorrectos")
        self._matriz[i][j] = nodo(1)

    def dfs(self, n):
        print("Recorrido nodo ", n)
        self._matriz[n][n]._visitado = 1
        for j in self.adyacentes(n):
            if self._matriz[j][j]._visitado == -1:
                self.dfs(j)

    def adyacentes(self, i):
        result = []
        for j in range(self._n):
            if self._matriz[i][j]._valor > 0 and i != j:
                result.append(j)
        return result

    def bfs(self, n):
        c = cola()
        c.encola(n)
        #Marcar como visitado
        self._matriz[n][n]._visitado = 1

        while c.cantidad > 0:
            actual = c.primero
            print("Recorrido nodo ", actual)

            for j in self.adyacentes(actual):
                #No visitado
                if self._matriz[j][j]._visitado == -1:
                    c.encola(j)
                    self._matriz[j][j]._visitado = 1
            c.desencola()

    def dos_coloracion(self):
        blancos = [0]
        negros = []
        c = cola()
        c.encola(0)

        while c.cantidad > 0:
            actual = c.primero
            color = blancos
            if actual in blancos:
                color = negros

            for j in self.adyacentes(actual):
                if j in blancos and color is negros:
                    return None
                if j in negros and color is blancos:
                    return None
                if j not in negros and j not in blancos:
                    c.encola(j)
                    color.append(j)
            c.desencola()
        return [blancos, negros]

g = grafo(3)
g.insertar(0, 1) 
g.insertar(1, 2)
g.insertar(0, 2)

g.dfs(0)

"""
g = grafo(4)
g.insertar(0, 1)
g.insertar(1, 2)
g.insertar(0, 3)
g.insertar(1, 3)
g.bfs(0)
"""

"""
g = grafo(4)
g.insertar(0, 1)
g.insertar(1, 2)
g.insertar(0, 3)

print(g.dos_coloracion())
g.insertar(1, 3)
print(g.dos_coloracion())
"""
