import math


class temp:  # nul subclass for temporary value
    def __init__(self):
        pass


class vector2d:  # vector for 2d gestion of the position
    def __init__(self, x = 0, y = 0, axis = None):
        self.axis = axis
        if self.axis == None:
            # +y : right ; -y : left, writable
            self.x = x
            # +x : up ; -x : down, writable
            self.y = y
        else:
            self.x = x * self.axis.axisx.x + self.axis.origin.x + y * self.axis.axisy.x
            self.x = y * self.axis.axisy.y + self.axis.origin.y + x * self.axis.axisx.y
        # return the lenght of the vector
        self.lenght = math.hypot(self.x, self.y)
        # return true if the vector is horizontal
        self.y_isnul = self.y == 0
        # return true if the vector is vertical
        self.x_isnul = self.x == 0
        # return true if the vector is nul
        self.isnul = self.x_isnul and self.y_isnul
        self.visual = "(" + str(self.x) + ";" + str(self.y) + ")"
        self.t = temp()
        self.droite = f_afine(self.x / self.y, 0)
        self.dict = {self.x, self.y}

    def __add__(self, other):
        self.x += other.x
        self.y += other.y

    def to_vector3d(self, z):  # return a 3d vector see further
        return vector3d(self.x, self.y, z)

    def switch(self):  # switch the value of the two axis
        self.t.t1 = self.x
        self.x = self.y
        self.y = self.t.t1
        self.t.t1 = 0

    def add_lenght(self, l):  # add length to the vec ; l can be negative
        self.t.t1 = self.x
        self.t.t2 = self.y
        self.x = self.t.t1 + l * (math.pow(self.t.t1, 2) / (math.pow(self.t.t1, 2) + math.pow(self.t.t2, 2)))
        self.y = self.t.t2 + l * (math.pow(self.t.t2, 2) / (math.pow(self.t.t1, 2) + math.pow(self.t.t2, 2)))

    def is_parrallel_to(self, p):  # return True if the other vector is parrallel
        if self.y == 0 or p.y == 0:
            if self.x == 0 and p.x == 0:
                return True
            else:
                return (self.y / self.x) == (p.y / p.x) or (self.y / self.x) == -(p.y / p.x)
        else:
            if self.x == 0 and p.x == 0:
                return True
            else:
                return (self.x / self.y) == (p.x / p.y) or (self.x / self.y) == -(p.x / p.y)

    def is_perpendicular_to(self, p):
        self.t.t1 = self.x / self.y
        self.t.t2 = p.x / p.y
        return self.t.t1 == -1 / self.t.t2


class axis2d:
    def __init__(self, origin = vector2d(), i = vector2d(1), j = vector2d(0, 1)):
        self.origin = origin
        self.axisx = i
        self.axisy = j
        self.is_orthonal = (self.axisx.y == 0) and (self.axisy.x == 0)
        self.is_orthonormed = (self.axisx.x/self.axisy.y == 1) and self.is_orthonal


class vector3d:  # vector for 3d gestion of the position
    def __init__(self, x = 0, y = 0, z = 0):
        # +y : right ; -y : left, writable
        self.x = x
        # +x : up ; -x : down, writable
        self.y = y
        # +z : near ; -z : far, writable
        self.z = z
        # return the lenght of the vector
        self.lenght = math.hypot(math.hypot(self.x, self.y), self.z)
        # return true if the vector is horizontal
        self.y_isnul = self.y == 0
        # return true if the vector is vertical
        self.x_isnul = self.x == 0
        # return true if the vector's z is nul
        self.z_isnul = self.z == 0
        # return true if the vector's length is nul
        self.isnul = self.x_isnul and self.y_isnul and self.z_isnul
        self.t = temp

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def to_vector2d(self, as_x, as_y):  # switch two of the axis position
        if as_x == "x":
            as_x = self.x
        elif as_x == "y":
            as_x = self.y
        elif as_x == "z":
            as_x = self.z
        else:
            print("Error arg1 invalid")
            exit()
        if as_y == "x":
            as_y = self.x
        elif as_y == "y":
            as_y = self.y
        elif as_y == "z":
            as_y = self.z
        else:
            print("Error arg2 invalid")
            exit()
        return vector2d(as_x, as_y)

    def is_parrallel_to(self, p):  # return true if the second vector is parrallel to the first doesnt work if y or z is nul
        return ((self.x / self.y) == (p.x / p.y) and (self.x / self.z) == (p.x / p.z)) or ((self.x / self.y) == -(p.x / p.y) and (self.x / self.z) == -(p.x / p.z))


def iter_int(i):
    temp.t1 = 0
    rdict = {}
    while not temp.t1 == i:
        rdict.__setitem__(temp.t1, temp.t1)
        temp.t1 += 1
    return rdict


def iter_float(i, step):
    temp.t1 = 0
    rdict = {}
    if (math.fmod(i, step)) == 0:
        i -= math.fmod(i, step)
    while not temp.t1 == i:
        rdict.__setitem__(temp.t1, temp.t1)
        temp.t1 += step
    return rdict


class f_afine:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.is_nul = self.a == 0 and self.b == 0
        if self.is_nul:
            self.cross_xv = math.inf
        else:
            if self.b == 0 or self.a == 0:
                self.cross_xv = "Linéaire"
            else:
                self.cross_xv = self.b / self.a

    def f(self, x):
        return (self.a * x) + self.b


class trinome:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.delta = (b * b) - (4 * a * c)
        if self.delta > 0:
            self.x1 = vector2d(((0 - self.b) - math.pow(self.delta, 0.5)) / (2 * self.a), 0)
            self.x2 = vector2d(((0 - self.b) + math.pow(self.delta, 0.5)) / (2 * self.a), 0)
            self.x0 = None
        elif self.delta == 0:
            self.x0 = vector2d(0 - self.b / (2 * self.a), 0)
            self.x1 = None
            self.x2 = None
        else:
            self.x1 = None
            self.x2 = None
            self.x0 = None
        if self.a != 0:
            self.alpha = 0 - self.delta / (4 * self.a)
            self.beta = 0 - self.b / (2 * self.a)
        else:
            self.alpha = None
            self.beta = None
        self.extremum = vector2d(self.beta, self.alpha)
        self.inter_y = vector2d(0, self.c)

    def f(self, x):
        return self.a * x * x + self.b * x + self.c


def afine_to_trinom(a, b):
    temp.t1 = a.a
    temp.t2 = a.b
    temp.t3 = b.a
    temp.t4 = b.b
    temp.t5 = temp.t1 * temp.t3
    temp.t6 = temp.t1 * temp.t4 + temp.t2 * temp.t3
    temp.t7 = temp.t2 * temp.t4
    trinome(temp.t5, temp.t6, temp.t7)


def sqrt(x):
    return math.pow(x, 0.5)


def sqr(x):
    return math.pow(x, 2)


def prompt(*args):
    if args.__len__() == 1:
        return input()
    else:
        rdict = {}
        for i in args:
            print("quelle valeur pour" + i)
            rdict.__setitem__(input(), rdict.__len__() + 1)
        return rdict


class rect2d:
    def __init__(self, pos = vector2d(0, 0), size = vector2d()):
        self.pos = pos
        self.size = size
        self.surface = self.size.x * self.size.y
        self.end = self.pos.__add__(self.size)
        self.cover = {}
        self.t = temp
        for i in iter_float(self.pos.x, 1):
            for a in iter_float(self.pos.y, 1):
                self.cover.__setitem__(vector2d(i, a),-1)

    def is_superposed(self, other):
        self.t.t1 = False
        for i in self.cover:
            if other.cover.__contains__(i):
                self.t.t1 = True
        return self.t.t1

