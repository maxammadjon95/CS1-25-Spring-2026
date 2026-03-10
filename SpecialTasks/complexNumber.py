class ComplexNumber:
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        return ComplexNumber(new_real, new_imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


if __name__ == "__main__":
    real1 = 3
    imaginary1 = 2
    real2 = 1
    imaginary2 = 7

    c1 = ComplexNumber(real1, imaginary1)
    c2 = ComplexNumber(real2, imaginary2)

    result = c1 + c2

    print(result)