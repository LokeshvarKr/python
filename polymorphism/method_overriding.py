class A:
    def show(self):
        print("show A")


class B(A):
    pass

class C(A):
    def show(self):
        print("show C")


a=A()
b=B()
c=C()

b.show() # b don't have show so it will call its parent show()
c.show() # c will call its own show()
