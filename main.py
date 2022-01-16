class Main:

    def __init__(self, name, value) -> None:
        self.name: str = name
        self.value: str = value

    def get_value(self) -> str:
        return self.value

m = Main('Main', 'General')
print(m.get_value())
