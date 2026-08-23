class Fraction:

    def __init__(self,x,y):
        self.num = x # 2  & other 3
        self.dem = y # 4  & other 6

    def __str__(self):
        return '{}/{}'.format(self.num,self.dem)

    def __add__(self, other):
        new_num = self.num*other.dem + self.dem*other.num
        new_dem = self.dem*other.dem

        return '{}+{}'.format(new_dem,new_dem)

    def __sub__(self, other):
        new_num = self.num*other.dem - self.dem*other.num
        new_dem = self.dem*other.dem

        return '{}-{}'.format(new_num,new_dem)

    def __mul__(self, other):
        new_num = self.num*other.num
        new_dem = self.dem*other.dem

        return '{}*{}'.format(new_num,new_dem)

    def __truediv__(self, other):
        new_num = self.num*other.dem
        new_den = self.dem*other.num

        return '{}/{}'.format(new_num,new_den)

    def convert_to_decimal(self):
        return self.num/self.dem

    

obj1 = Fraction(2,4)
obj2 = Fraction(3,6)

print(obj1)
print(obj1+obj2)
print(obj1-obj2)
print(obj1*obj2)
print(obj1/obj2)
print(obj1.convert_to_decimal())