class MyClass:

    # Defines a "class" attribute
    purpose = "learning"

    def __init__(self, name):
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name

    def method(self):
        return "instance method called", self

    @classmethod
    def class_method(cls):
        return "class method called", cls

    @classmethod
    def class_purpose(cls):
        return cls.purpose

    @classmethod
    def redefine_purpose(cls, new_purpose):
        cls.purpose = new_purpose

    @staticmethod
    def staticmethod():
        return "static method called"

    def __str__(self):
        return "MyClass[purpose=" + self.purpose + ", name=" + self._name + "]"
