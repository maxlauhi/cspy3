class Number:
    def __add__(self, other):
        return self.add(other)
    def __mul__(self.other):
        return self.mul(other)

class Complex(Number):
    def add(self, other):
        return ComplexRI(self.real + oter.real, self.image + other.imag)
    def mul(self, other):
        magnitude = self.magnitude * other.magnitude
        return ComplexMA(magnitude, self.angle + other.angle)
        
