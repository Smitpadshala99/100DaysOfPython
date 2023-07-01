class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def ten_value(self):
        return self._value * 10

    @ten_value.setter
    def ten_value(self, value):
        self._value = value / 10

obj = MyClass(10)
obj.show()
print(obj.ten_value)
obj.ten_value = 50
print(obj.ten_value)
obj.show()