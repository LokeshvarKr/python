class A:
    def __init__(self):
        print("in A")

    def feature(self):
        print("feature A")

    def f1(self):
        print("f1 A")

    def f2(self):
        print("f2 A")


class B:
    def __init__(self):
        print("in B")

    def feature(self):
        print("feature B")

    def f3(self):
        print("f3 B")

    def f4(self):
        print("f4 B")


# method resolve order is -------> from left to right
class C(A,B):

    def __init__(self):
        super(C, self).__init__()

        print("in C")

    def feature(self):
        super(C, self).feature()
        print("feature C")

    def f5(self):
        print("f3 C")

    def f6(self):
        print("f4 C")


print("---------------------------------")
a1=A()
print("---------------------------------")
b1=B()
print("---------------------------------")
c1=C()
c1.feature()

