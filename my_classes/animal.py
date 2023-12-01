from abc import ABC, abstractmethod


class Animal(ABC):

    # def __init__(self) -> None:
    #	super().__init__()

    @abstractmethod
    def speak(self):
        pass
