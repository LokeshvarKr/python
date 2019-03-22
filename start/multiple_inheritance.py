class A:
    def f1(self):
        print("f1 A")

    def f2(self):
        print("f2 A")


class B:
    def f3(self):
        print("f3 B")

    def f4(self):
        print("f4 B")

#multiple inheritance (C inherits both B and A)
class C(A,B):
    def f5(self):
        print("f3 C")

    def f6(self):
        print("f4 C")

c1=C()
c1.f1()
c1.f2()
c1.f3()
c1.f4()
c1.f5()
c1.f6()

