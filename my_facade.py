class Move:
    def system_check(self):
        return 'move module activated'
    def operative_state(self):
        return 'move module in action'

class Attack:
    def system_check(self):
        return 'attack module activated'
    def operative_state(self):
        return 'attack module in action'

class Facade:
    def __init__(self, subsystem_01, subsystem_02):
        self.__subs01 = subsystem_01
        self.__subs02 = subsystem_02
    def operate(self):
        logo = [
                    'facade activate subsystems',
                    self.__subs01.system_check(),
                    self.__subs02.system_check(),
                    'facade use subsystem',
                    self.__subs01.operative_state(),
                    self.__subs02.operative_state(),
                ]
        return '\n'.join(logo)
    
def client_code(facade):
    print(facade.operate())

if __name__ == '__main__':
    subsystem1 = Move()
    subsystem2 = Attack()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)