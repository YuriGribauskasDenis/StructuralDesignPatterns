class Component:
    def operation(self):
        pass
class ConcreteComponent(Component):
    def operation(self):
        return 'ConcreteComponent'
class Decorator(Component):
    #_component = None
    def __init__(self, component):
        self._component = component
    @property
    def component(self):
        return self._component
    def operation(self):
        return self._component.operation()
class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self.component.operation()})"
class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB({self.component.operation()})"

def client_code(component):
    print(f"RESULT: {component.operation()}", end="")

if __name__ == "__main__":
    simple = ConcreteComponent()
    client_code(simple)
    print()

    decorator1 = ConcreteDecoratorA(simple)
    client_code(decorator1)
    print()
    decorator2 = ConcreteDecoratorB(decorator1)
    client_code(decorator2)