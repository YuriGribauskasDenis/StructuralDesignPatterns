from __future__ import annotations


class StockApp:
    # xml request
    def request(self):
        return 'default behaviour (XML)'
class SciLibrary:
    def json_request(self):
        text = 'specific behaviour (json)'
        return text[::-1]
class Adapter(StockApp, SciLibrary):
    def request(self):
        return f'translated behaviour: {self.json_request()[::-1]}'

def client_code(target):
    print(target.request())

if __name__ == '__main__':
    target = StockApp()
    client_code(target)

    outside = SciLibrary()
    print(outside.json_request())

    solution = Adapter()
    client_code(solution)