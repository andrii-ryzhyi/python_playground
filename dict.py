import copy

class MyDict:

    __slots__ = "_holder", "_size"

    def __init__(self):
        self._holder = []
        self._size = 0

    def __setitem__(self, key, value):
        if hasattr(key, '__hash__') and not self._has_key(key):
            self._holder.append(tuple([key, value]))
            self._size += 1
        else:
            raise TypeError("Key must be immutable or unique")

    def __getitem__(self, key):
        for element in self._holder:
            if element[0] == key:
                return element[1]
        return None

    def _has_key(self, key):
        for obj in self._holder:
            if obj[0] == key:
                return True
        return False

    def items(self):
        return self._holder

    def keys(self):
        _keys = []
        for obj in self._holder:
            _keys.append(obj[0])
        return _keys

    def values(self):
        _vals = []
        for obj in self._holder:
            _vals.append(obj[1])
        return _vals

    def __add__(self, obj):
        result = MyDict()
        for key, value in self.items():
            result[key] = value
        for key, value in obj.items():
            try:
                result[key] = value
            except Exception as e:
                print(e)
                raise ValueError("Keys must be unique. Operation is not possible")
        return result

    def __repr__(self):
        result = ''
        for obj in self._holder:
            result += f'{obj[0]} : {obj[1]} \n'
        return result

a = MyDict()
a['key'] = "value"
a['key1'] = "value1"
a['key2'] = "value2"
a['key3'] = "value3"
a['key4'] = "value4"
print(a)

b = MyDict()
b['key0'] = "value0"
# b['key1'] = "value1"
b['key7'] = "value7"
b['key8'] = "value8"
b['key9'] = "value9"

c = a + b
print(c)

items = a.items()
keys = a.keys()
vals = a.values()
print(items)
print(keys)
print(vals)
