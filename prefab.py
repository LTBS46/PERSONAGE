import math


class temp:  # nul subclass for temporary value
    def __init__(self):
        pass


class vector2d:  # vector for 2d gestion of the position
    def __init__(self, x, y):
        # +y : right ; -y : left, writable
        self.x = x
        # +x : up ; -x : down, writable
        self.y = y
        # return the lenght of the vector
        self.lenght = math.hypot(self.x, self.y)
        # return true if the vector is horizontal
        self.y_isnul = self.y == 0
        # return true if the vector is vertical
        self.x_isnul = self.x == 0
        # return true if the vector is nul
        self.isnul = self.x_isnul and self.y_isnul
        self.t = temp()

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


class vector3d:  # vector for 3d gestion of the position
    def __init__(self, x, y, z):
        # +y : right ; -y : left, writable
        self.x = x
        # +x : up ; -x : down, writable
        self.y = y
        # +z : near ; -x : far, writable
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
            self.x1 = ((0 - self.b) - sqrt(self.delta)) / (2 * self.a)
            self.x2 = ((0 - self.b) + sqrt(self.delta)) / (2 * self.a)
            self.x0 = None
        elif self.delta == 0:
            self.x0 = 0 - self.b / (2 * self.a)
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


def sqrt(x):
    math.pow(x, 0.5)


class a:
    def __init__(self):
        pass

    def __abs__(self):
        pass

    def __add__(self, other):
        pass

    def __aenter__(self):
        pass

    def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    def __aiter__(self):
        pass

    def __and__(self, other):
        pass

    def __anext__(self):
        pass

    def __await__(self):
        pass

    def __bool__(self):
        pass

    def __bytes__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass

    def __ceil__(self):
        pass

    def __class_getitem__(cls, item):
        pass

    def __cmp__(self, other):
        pass

    def __coerce__(self, other):
        pass

    def __complex__(self):
        pass
    
    def __contains__(self, item):
        pass
    
    def __copy__(self):
        pass
    
    def __del__(self):
        pass

    def __delete__(self, instance):
        pass
    
    def __delitem__(self, key):
        pass
    
    def __delslice__(self, i, j):
        pass

    def __divmod__(self, other):
        pass
    
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def __float__(self):
        pass
    
    def __floor__(self):
        pass
    
    def __floordiv__(self, other):
        pass

    def __fspath__(self):
        pass
    
    def __ge__(self, other):
        pass
    
    def __get__(self, instance, owner):
        pass
    
    def __getattr__(self, item):
        pass

    def __getinitargs__(self):
        pass
    
    def __getitem__(self, item):
        pass
    
    def __getnewargs__(self):
        pass
    
    def __getstate__(self):
        pass
    
    def __gt__(self, other):
        pass
    
    def __hex__(self):
        pass
    
    def __iadd__(self, other):
        pass

    def __iand__(self, other):
        pass

    def __idiv__(self, other):
        pass

    def __ifloordiv__(self, other):
        pass

    def __ilshift__(self, other):
        pass

    def __imatmul__(self, other):
        pass

    def __imod__(self, other):
        pass

    def __imul__(self, other):
        pass

    def __index__(self):
        pass

    def __instancecheck__(self, instance):
        pass

    def __int__(self):
        pass

    def __invert__(self):
        pass

    def __ior__(self, other):
        pass

    def __ipow__(self, other):
        pass

    def __irshift__(self, other):
        pass

    def __isub__(self, other):
        pass

    def __iter__(self):
        pass

    def __itruediv__(self, other):
        pass

    def __ixor__(self, other):
        pass

    def __le__(self, other):
        pass

    def __len__(self):
        pass

    def __long__(self):
        pass

    def __lshift__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __matmul__(self, other):
        pass

    def __missing__(self, key):
        pass

    def __mod__(self, other):
        pass

    def __mro_entries__(self, bases):
        pass

    def __mul__(self, other):
        pass

    def __neg__(self):
        pass

    def __next__(self):
        pass

    def __oct__(self):
        pass

    def __or__(self, other):
        pass

    def __pos__(self):
        pass

    def __pow__(self, power, modulo=None):
        pass

    def __radd__(self, other):
        pass

    def __rand__(self, other):
        pass

    def __rdiv__(self, other):
        pass

    def __rdivmod__(self, other):
        pass

    def __reversed__(self):
        pass

    def __rfloordiv__(self, other):
        pass

    def __rlshift__(self, other):
        pass

    def __rmatmul__(self, other):
        pass

    def __rmod__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __ror__(self, other):
        pass

    def __round__(self, n=None):
        pass

    def __rpow__(self, other):
        pass

    def __rrshift__(self, other):
        pass

    def __rshift__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    def __rxor__(self, other):
        pass

    def __set__(self, instance, value):
        pass

    def __set_name__(self, owner, name):
        pass

    def __setitem__(self, key, value):
        pass

    def __setslice__(self, i, j, sequence):
        pass

    def __setstate__(self, state):
        pass

    def __sub__(self, other):
        pass

    def __subclasscheck__(self, subclass):
        pass

    def __truediv__(self, other):
        pass

    def __trunc__(self):
        pass

    def __unicode__(self):
        pass

    def __xor__(self, other):
        pass
