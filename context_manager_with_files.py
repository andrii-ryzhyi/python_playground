class File:

    def __init__(self, name, mode):
        self._name = name
        self._mode = mode

    def __enter__(self):
        self._filehandler = open(self._name, self._mode)
        return self._filehandler

    def __exit__(self, *args):
        self._filehandler.close()
        if args[0] is not None:
            raise Exception("There is some exception")

    def write(self, value):
        self._filehandler.write(value)

with File("test.txt", "w") as f:
    f.write("3")