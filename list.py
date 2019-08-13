from typing import Iterable

class CustomList:

    __slots__ = "_holder", "_size"

    def __init__(self, values=None):
        self._size = 0
        self._holder = []
        
        if values:
            if isinstance(values, Iterable):
                for value in values:
                    self._holder.append(value)
                    self._size += 1
            else:
                self._holder.append(values)
                self._size += 1

    def __getitem__(self, idx):
        if idx > self._size-1:
            raise TypeError("Out of range bound")
        return self._holder[idx]

    def __setitem__(self, idx, value):
        if idx > self._size-1 or idx < 0:
            raise TypeError("Out of range bound")
        self._holder[idx] = value

    def __iter__(self):
        return iter(self._holder)

    def pop(self):
        if self._size > 0:
            self._size -= 1
            return self._holder.pop()
        else:
            raise ValueError("List is empty")

    def append(self, value):
        self._holder.append(value)
        self._size += 1

    def insert(self, idx, value):
        if idx <= self._size-1:
            self._holder.insert(idx, value)
            self._size += 1
        else:
            raise ValueError("Out of range bound")

    def remove(self, value):
        if value in self._holder:
            self._holder.remove(value)
            self._size -= 1
        else:
            raise Exception(f"{value} not in list")

    def clear(self):
        self._holder = []
        self._size = 0

    def __repr__(self):
        vals = ''
        for el in self._holder:
            vals += str(el) + ' '
        return vals

    def __len__(self):
        return self._size
    

a = CustomList([10, 20, 30, 40, 50, "end"])
a[0] = 20
a.append(30)
print(a)
a[1] = 0
print(a)
a.pop()
print(a)
a.insert(1, 60)
print(a)
a.remove(60)
print(a)
print(len(a))
a.clear()
print(a)






    