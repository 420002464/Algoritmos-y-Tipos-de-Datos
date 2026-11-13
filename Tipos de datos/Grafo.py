class grafo:

    _matriz = []
    _n = 0

    def __init__(self, n:int):
        for i in range(n):
            self._n = n
            self._matriz.append([])
            for j in range(n):
                self._matriz[i].append(-1)

    def insertar(self, i:int, j:int, p):
        if self._n < i < 0 or self._n < j < 0:
            raise Exception("Nodos incorrectos")
        self._matriz[i][j] = p

    def borrar(self, i, j):
        if self._n < i < 0 or self._n < j < 0:
            raise Exception("Nodos incorrectos")
        self._matriz[i][j] = -1 #-1 indicaba que dos nodos no tenían arista

    def imprime_aristas(self):
        for i in range(self._n):
            for j in range(self._n):
                if self._matriz[i][j] >= 0:
                    #print("(" + str(i) + "," + str(j) + ")")
                    print(f"({str(i)},{str(j)})")

g = grafo(4)
g.insertar(1, 1, 2)
g.insertar(2, 1, 1)
g.imprime_aristas()
