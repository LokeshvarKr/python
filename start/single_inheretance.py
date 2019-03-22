class A:
    def f1(self):
        print("f1 A")

    def f2(self):
        print("f2 A")

#B is inheriting A
class B(A):
    def f3(self):
        print("f3 B")

    def f4(self):
        print("f4 B")


b1=B()
b1.f1()
b1.f2()
b1.f3()
b1.f4()
