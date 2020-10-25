'''
Circuitus, LLC -
An advanced Circle Analytics Company
'''

# this code is transcribed from the following youtube video:
# https://www.youtube.com/watch?v=HTLu2DFOdTg with timestamps
import math         # module for code reuse
# 25:58
from random import random, seed

class Circle(object):       # new-style class
    'An advanced circle analytic toolkit'
    #42:41
    # Flyweigth design pattern supresses
    # the instance ditionary
    __slots__ = ['diameter']

    version = '0.7'     # class variable

    # init isn’t a constructor. It’s job is to initialize the instance variable
    def __init__(self, radius):
        self.radius = radius              # instance variable

    # 39:26
    # Every time we set radius, this will no longer be stored in the instance variable.
    @property   # convert dotted accses to methode calls
    def radius(self):
        'Radius of a circle'
        return self.diameter / 2.0

    # 39:40
    @radius.setter
    def radius(self,radius):
        self.diameter = radius * 2.0

    def area(self):
        'Regular methode'
        'Preform quadrature on a shape of uniform radius'
        # 34:27
        # Goverment request: iso-111110
        p = self.__perimeter()      # 37:07
        r = p / math.pi / 2.0
        # 10:46
        return math.pi * r ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    # 35:35
    'for keeping tiercompaies code working'
    # keeps a spare copy of the function in case someone overrides it
    _Circle__perimeter = perimeter

    # 27:49
    # Alternative constructor need to anticipate subclassing
    @classmethod        # alternative constructor for class methode
    def from_bbd(cls,bbd):
        'Construct a circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    # 30:13
    # a function where you don’t need the self instance
    @staticmethod           # attach function to classes
    def angle_to_grade(angle):
        'Convert angle in degree to a percentage grade'
        return math.tan(math.radians(angle)) * 100.0


# 22:00
class Tire(Circle):
    'Tires are circles with a corrected perimeter'

    def perimeter(self):
        'Circumference corrected for the rubber'
        return Circle.perimeter(self) * 1.25

    _Tier_preimeter = perimeter




def main():
    # 14:20
    # Minimum viable product (NVP!)
    # tutorial
    print("Tutorial")
    print ('Circuituous verson',Circle.version)
    c = Circle(10)
    print("A Cicle of radius", c.radius)
    print("has a area of", c.area())
    print()

def academia():
    print("Academia")
    seed(8675309)
    print('Using Circuituous(tm) version', Circle.version)
    n = 10000000
    circles=[Circle(random()) for i in range(n)]
    print('The average area of',n,'random circles')
    avg = sum([c.area() for c in circles])/n
    print('is %.1f'%avg)
    print()

# 16:21
def rubbersheetcompany():
    print("Rubber sheet company")
    cuts = [0.1, 0.7, 0.8]
    circles = [Circle(r) for r in cuts]
    for c in circles:
        print('A circlet with with a radius of',c.radius)
        print('has a perimenter of',c.perimeter())
        print('and a cold area of',c.area())
        # if you expose an attribute expect at users are going to change them
        c.radius *= 1.1
        print('and a warm area of' ,c.area())
        print()



# 19:45
def nationaltirechain():
    print("National tire chain")
    # 29:15
    t = Tire.from_bbd(45)
    print('A tire of radius',t.radius)
    print('has a inner area of',t.radius)
    print('and an odometer corrected perimeter of')
    print(t.perimeter())
    print()

# 23:45
def nationalgraphicscompany():
    print("National graphics company")
    bbd = 25.1
    c = Circle.from_bbd(bbd)
    print('A circle with a bbd of of 25.1')
    print('has a radius of',c.radius)
    print('an an area of', c.area())
    print()



if __name__ == '__main__':
    main()
    academia()
    rubbersheetcompany()
    nationaltirechain()
    nationalgraphicscompany()