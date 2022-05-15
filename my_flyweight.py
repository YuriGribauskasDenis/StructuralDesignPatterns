import json


class Flyweight:
    def __init__(self, shared_state):
        self.__shared_state = shared_state
    def set_unique_state(self, unique_state):
        self.__unique_state = unique_state
        c = json.dumps(self.__shared_state)
        u = json.dumps(self.__unique_state)
        print(f'Flyweight: inner states {c}, outer states {u}')

class FlyweightFactory:
    __flyweights = {}
    def __init__(self, initial_flyweights):
        for state in initial_flyweights:
            self.__flyweights[self.get_key(state)] = Flyweight(state)
    def get_key(self, state):
        return '_'.join(state)
    def get_flyweight(self, shared_state):
        key = self.get_key(shared_state)
        if not self.__flyweights.get(key):
            print('FlyweightFactory no such Flyweight found, creating new')
            self.__flyweights[key] = Flyweight(shared_state)
        else:
            print('FlyweightFactory Flyweight found')
        return self.__flyweights[key]
    def list_flyweights(self):
        count = len(self.__flyweights)
        print(f'FlyweightFactory: I have {count} flyweights:')
        print('\n'.join(map(str, self.__flyweights.keys())), end='')

def add_car_to_police_database(
    factory, plates, owner,
    brand, model, color):
    print('\n\nClient: Adding a car to database.')
    flyweight = factory.get_flyweight([brand, model, color])
    flyweight.set_unique_state([plates, owner])

if __name__ == '__main__':
    factory = FlyweightFactory([
        ['Chevrolet', 'Camaro2018', 'pink'],
        ['Mercedes Benz', 'C300', 'black'],
        ['Mercedes Benz', 'C500', 'red'],
        ['BMW', 'M5', 'red'],
        ['BMW', 'X6', 'white'],
    ])
    factory.list_flyweights()

    add_car_to_police_database(
        factory, 'CL234IR', 'James Doe', 'BMW', 'M5', 'red')

    add_car_to_police_database(
        factory, 'CL234IR', 'James Doe', 'BMW', 'X1', 'red')

    print()

    factory.list_flyweights()