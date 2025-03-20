class Parent:
    def __init__(self):
        self.name = 'parent'

    def print_name(self):
        print(self.name)

    class Child:
        def __init__(self):
            self.name = 'child'

        def print_name(self):
            print(self.name)


if __name__ == '__main__':
    p = Parent()
    c = Parent.Child()

    p.print_name()
    c.print_name()

    print(type(p),p)
    print(type(c),c)
