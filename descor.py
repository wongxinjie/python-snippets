class DataAttr(object):

    def __init__(self, val):
        self.val = val

    def __get__(self, instance, owner):
        print("DataAttr.__get__() called, self.val=", self.val)
        return self.val

    def __set__(self, instance, value):
        self.val = value


class NonDataAttr(object):

    def __init__(self, val):
        self.val = val

    def __get__(self, instance, owner):
        print("NonDataAttr.__get__() called, self.val=", self.val)
        return self.val


class A(object):

    def __init__(self):
        self.x = DataAttr(10)
        self.x = NonDataAttr(12)
        self.x = 8
        self.name = "A"
        print(self.__dict__)


a = A()
print(a.x)

print(a.__dict__['x'].__get__(a, type(a)))
