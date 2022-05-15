from abc import ABC, abstractmethod


class Remote:
    def __init__(self, implementation):
        self.implementation = implementation
    def operation(self):
        return f'''Remote: Base operation with:\n
                    {self.implementation.tv_method()}'''
class SuperRemote(Remote):
    def operation(self):
        return f'''SuperRemote: Base operation with:\n
                    {self.implementation.tv_method()}'''
class TV(ABC):
    @abstractmethod
    def tv_method(self):
        pass
class SamsungTV(TV):
    def tv_method(self):
        return 'SAMSUNG'
class AppleTV(TV):
    def tv_method(self):
        return 'APPLE'
def client_code(remote):
    print(remote.operation())

if __name__ == '__main__':
    samsungtv = SamsungTV()
    cheap_remote = Remote(samsungtv)
    client_code(cheap_remote)
    print()
    appletv = AppleTV()
    expensive_remote = SuperRemote(appletv)
    client_code(expensive_remote)