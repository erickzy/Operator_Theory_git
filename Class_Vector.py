from math import sqrt
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise  ValueError('The coordinates must be nonempty')

        except TypeError:
            raise  TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return  Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return  Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return  Vector(new_coordinates)

    def magn(self):
        rsqure = 0
        for x in self.coordinates:
            rsqure = x*x + rsqure
        root = rsqure**0.5
        return root

    """
    #  the Uda solution as below:
    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))
    """


    def dirc(self):
        c = 1./self.magn()
    # the "." after 1 is very important, to make the divided as float
        t = self.times_scalar(c)
        return t

    """"
    # the Uda solution as below:
    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)

        except ZeroDivisionError
            raise Exception('Cannot normalize the zero vector')
    """


"""""

my_vector = Vector([1,2,3])
#my_vector.dimension
#my_vector.coordinates
#print(my_vector)
my_vector2 = Vector([2,3,4])
my_vector3 = Vector([-2,3,4])

"""

"""""
v = Vector([8.218, -9.341])
w = Vector([-1.129, 2.111])
print(v.plus(w))

v = Vector([7.119,8.215])
w = Vector([-8.223,0.878])
print(v.minus(w))
v = Vector([1.671, -1.012, -0.318])
c = 7.41
print(v.times_scalar(c))
"""
"""""
v = Vector([-0.221,7.437])
w = Vector([8.813, -1.331, -6.247])
print(v.magn())
print(w.magn())
"""

v = Vector([5.581, -2.136])
w = Vector([1.996, 3.108, -4.554])
print(v.dirc())
print(w.dirc())

