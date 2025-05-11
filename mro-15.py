class A:
    def show(self):
        print("Method from clas A")

class B(A):
    def show(self):
        print("ethod from B")

class C(A):
    def show(self):
        print("Method from C")

class D(B, C):
    pass

d = D()
d.show()

print(D.mro())

