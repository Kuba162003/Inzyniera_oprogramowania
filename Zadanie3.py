class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.value = value

if __name__ == "__main__":
    singleton1 = Singleton("Pierwsza instancja")
    print(f"singleton1.value: {singleton1.value}")

    singleton2 = Singleton("Druga instancja")
    print(f"singleton2.value: {singleton2.value}")

    print(f"Czy singleton1 i singleton2 to ten sam obiekt? {singleton1 is singleton2}")
