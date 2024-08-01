print("__name__:",__name__)
def func(v):
    i = v + 3
    return i

class MyClass:
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

    def show_attributes(self):
        print("a = {}, b = {}, sum: {}".format(self.a, self.b, self.sum()))

    def sum(self):
        return self.a + self.b

if __name__ == "__main__":
    my_class = MyClass(3, 5)
    my_class.show_attributes()

import my_module2
m2 = my_module2.MyClass(3, 5)
m2.show_attributes()
