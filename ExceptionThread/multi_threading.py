from time import sleep
from threading import  *

class Hello(Thread):
    def run(self):
        for i in range(20):
            print("hello")
            sleep(0.5)


class Hi(Thread):
    def run(self):
        for i in range(20):
            print("hi")
            sleep(0.5)


obj1=Hello()
obj2=Hi()

obj1.start()
sleep(0.2)
obj2.start()

obj1.join()
obj2.join()

print("byeeeeeeeeee.........")

