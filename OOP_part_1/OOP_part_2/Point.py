class Point:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return '{}a {}b'.format(self.a,self.b)

    def distance_from_a_to_b(self,other):
        return ((self.a-other.a)**2+(self.b-other.b)**2)**0.5

    def distance_from_origin(self):
        return ((self.a)**2+(self.b)**2)**0.5

class Line:

    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def ponit_to_line(line,point):
        if line.A*point.a+line.B*point.b+line.C == 0:
            return 'Lies on line'
        else:
            return 'does not lies on line'

    def shortest_distance(line,point):
        return abs(line.A*point.a+line.B*point.b + line.C)/(line.A**2+line.B**2)

l1 = Line(1,1,-2)
p1 = Point(1,1)
print(l1.ponit_to_line(p1))
print(l1.shortest_distance(p1))
