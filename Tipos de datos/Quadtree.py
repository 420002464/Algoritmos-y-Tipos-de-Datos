class punto:

    color = None
    coord = None

    def __init__(self, x, y, c):
        self.coord = [x, y]
        self.color = c

    def damexcoord(self):
        return self.coord[0]

    def dameycoord(self):
        return self.coord[1]

    x = property(fget=damexcoord)
    y = property(fget=dameycoord)

class quadtree:
    #Regiones
    sup_izq = None
    sup_der = None
    inf_izq = None
    inf_der = None

    pto_medio = None
    color = None
    #Coordenadas
    xmax = None
    xmin = None
    ymax = None
    ymin = None

    def __init__(self, xmax, xmin, ymax, ymin):
        if xmax - xmin != ymax - ymin:
            raise Exception("Las longitudes deben ser iguales")

        self.pto_medio = ((xmax+xmin)/2, (ymax+ymin)/2)
        self.xmax = xmax
        self.xmin = xmin
        self.ymax = ymax
        self.ymin = ymin
        self.color = "blanco"

    def insertar(self, p):
        if self.pertenece(p):
            if self.xmax - self.xmin <= 1 and self.ymax - self.ymin <= 1:
                self.color = p.color
                return
            if self.vacio():
                self.divide()
            self.sup_izq.insertar(p)
            self.sup_der.insertar(p)
            self.inf_izq.insertar(p)
            self.inf_der.insertar(p)

    def divide(self):
        #Estan volteados los subcuadrados
        self.sup_izq = quadtree(self.pto_medio[0], self.xmin, self.pto_medio[1], self.ymin)
        self.sup_der = quadtree(self.xmax,self.pto_medio[0], self.pto_medio[1], self.ymin)
        self.inf_izq = quadtree(self.pto_medio[0], self.xmin, self.ymax, self.pto_medio[1])
        self.inf_der = quadtree(self.xmax, self.pto_medio[0], self.ymax, self.pto_medio[1])
        #¿no sería lo mismo usar el pto_medio[0] que [1] porque al final del día siempre deben dar el mismo resultado por ser cuadrado 

    #Devuelve True si el punto p pertenece al QuadTree
    def pertenece(self, p):
        if self.xmin <= p.x < self.xmax and self.ymin <= p.y < self.ymax:
            return True
        return False

    def vacio(self):
        if self.sup_izq == None:
            return True

q = quadtree(4, 2, 4, 2)
q.insertar(punto(2, 2, "negro"))
q.insertar(punto(3, 3, "negro"))
