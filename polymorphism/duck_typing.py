class codeblock:

    def execute(self):
        print("compiling")
        print ("running")


class pychamp:

    def execute(self):
        print ("spell check")
        print ("convention check")
        print("compiling")
        print ("running")


class laptop:
    def code(self,ide):
        ide.execute()


# why this is duck typing because in laptop class there is a
# method code which takes an argument it doesn't care which type of this argument
# only need is that this argument should have execute() method

ide=pychamp()

lap=laptop()
lap.code(ide)

