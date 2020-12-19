class Division:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f'fractie = {self.num}/{self.den} \n'

    def __add__(self, other): # self + other
        return Division(self.den * other.num + self.num * other.den, other.den * self.den)

    def __sub__(self, other): # self - other
        return Division(self.den * other.num - self.num * other.den, other.den * self.den)

    # define a custom method (not special like above)
    def inverse(self):
        return Division(self.den, self.num)

fractie1 = Division(2, 3)
fractie2 = Division(10, 20)

# add/substract the num and den from the same instance (Target of this problem)

print(str(fractie1)) # == print(fractie1.__str__())
print(str(fractie2))


print(str(fractie1 + fractie2)) # print(fractie1.__add__(fractie))
print(str(fractie1 - fractie2)) # print(fractie2.__sub__(fractie1))

fractie1_inv = fractie1.inverse()
print(str(fractie1_inv))
