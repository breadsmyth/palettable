class CMYK:
    def __init__(self, c, m, y, k):
        self.c = c
        self.m = m
        self.y = y
        self.k = k

    def to_rgb(self):
        return (
            255 * (1-self.c//100) * (1-self.k//100),
            255 * (1-self.m//100) * (1-self.k//100),
            255 * (1-self.y//100) * (1-self.k//100))


def avg(num1, num2):
    return (num1 + num2) // 2


def mix(color1, color2):
    return (
        avg(color1[0], color2[0]),
        avg(color1[1], color2[1]),
        avg(color1[2], color2[2]))