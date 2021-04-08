class Vector:
    def __init__(self) -> None:
        self.vector = [0, 0, 0]

    def __setattr__(self, name, value) -> None:
        value = float(value)
        if name == "x":
            self.vector[0] = value
        elif name == "y":
            self.vector[1] = value
        elif name == "z":
            self.vector[2] = value
        else:
            object.__setattr__(self, name, value)


a = Vector("x", "y", "z")


print(a)
