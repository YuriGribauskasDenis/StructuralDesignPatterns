from abc import ABC, abstractmethod


class Component(ABC):
    @property
    def parent(self):
        return self.__parent
    @parent.setter
    def parent(self, parent):
        self.__parent = parent
    def add(self, component):
        pass
    def remove(self, component):
        pass
    def is_composite(self):
        return False
    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return 'Leaf'

class Composite(Component):
    def __init__(self):
        self.__children = []
    def add(self, component):
        self.__children.append(component)
    def remove(self, component):
        self.__children.remove(component)
    def is_composite(self):
        return True
    def operation(self):
        return f'Branch({"+".join([child.operation() for child in self.__children])})'

def client_code(component):
    print(f'RESULT {component.operation()}', end='')

def client_code2(component1, component2):
    if component1.is_composite():
        component1.add(component2)
    print(f'RESULT {component1.operation()}', end='')

if __name__ == "__main__":    
    simple = Leaf()
    client_code(simple)
    print()

    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    client_code(tree)
    print()

    client_code2(tree, simple)