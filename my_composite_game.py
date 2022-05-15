from abc import ABC, abstractmethod


class Figure(ABC):
    def add(self, child):
        pass
    def remove(self, child):
        pass
    def is_composite(self):
        return False
    @abstractmethod
    def draw(self):
        pass

class Sphere(Figure):
    def draw(self):
        return 'Sphere'

class Parallelepiped(Figure):
    def draw(self):
        return 'Parallelepiped'

class Cube(Parallelepiped):
    def draw(self):
        return 'Cube'

class Composite(Figure):
    def __init__(self):
        self.__children = []
    def add(self, child):
        self.__children.append(child)
    def remove(self, child):
        self.__children.remove(child)
    def is_composite(self):
        return True
    def draw(self):
        return f'Group({"+".join([child.draw() for child in self.__children])})'

def client_code(figure):
    print(f'Result {figure.draw()}', end='')

def client_code2(figure1, figure2):
    if figure1.is_composite():
        figure1.add(figure2)
    print(f'Result {figure1.draw()}', end='')

if __name__ == '__main__':
    simple = Cube()
    client_code(simple)
    print()

    tree = Composite()

    branch1 = Composite()
    branch1.add(Parallelepiped())
    branch1.add(Parallelepiped())
    branch1.add(Sphere())

    branch2 = Composite()
    branch2.add(Cube())
    branch2.add(Sphere())

    tree.add(branch1)
    tree.add(branch2)

    client_code(tree)
    print()
    client_code2(tree, simple)