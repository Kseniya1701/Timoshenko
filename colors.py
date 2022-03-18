class colors:
    def __init__(self, name, r, g, b):
        self.name = name
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"{self.name} ({self.r}, {self.g}, {self.b})"

    def __eq__(self, other):
        if isinstance(other, colors):
            return (self.r == other.r and
                    self.g == other.g and
                    self.b == other.b)
        return NotImplemented

red = colors('красный', 255, 0, 0)
green = colors('зеленый', 0, 255, 0)
otherRed = colors('другой красный', 255, 0, 0)

print(otherRed)
print(red)
print(green)

print(red==green)
print(red == otherRed)
