from my_classes.animal import Animal


class Dog(Animal):

    def __init__(self) -> None:
        super().__init__()

    def speak(self):
        print("bark")


class ProxyDog:

    def __init__(self) -> None:
        self._dog = Dog()

    def __getattr__(self, item):
        print("Accessing " + item)
        return getattr(self._dog, item)
