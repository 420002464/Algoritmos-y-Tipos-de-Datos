class pila:
    #elems = []

    def __init__(self):
        self.elems = []

    def fcantidad(self):
        return len(self.elems)

    def apila(self, x):
        self.elems.append(x)

    def desapila(self):
        return self.elems.pop()

    def ftope(self):
        return self.elems[-1]

    tope = property(fget=ftope)
    cantidad = property(fget=fcantidad)
p = pila()
p.apila(1)
p.apila(2)
p.apila(5)
p.desapila()

print(p.ftope())
print(p.fcantidad())

class pila:
    #elems = []

    def __init__(self):
        self.elems = []

    def fcantidad(self):
        return len(self.elems)

    def apila(self, x):
        self.elems.append(x)

    def desapila(self):
        return self.elems.pop()

    def ftope(self):
        return self.elems[-1]

    tope = property(fget=ftope)
    cantidad = property(fget=fcantidad)
p = pila()
p.apila(1)
p.apila(2)
p.apila(5)
p.desapila()

print(p.ftope())
print(p.fcantidad())
