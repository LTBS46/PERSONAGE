import math


class temp: # nul subclass for temporary value
    def __init__(self):
        pass


class vector2d: # vector for 2d gestion of the position
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


    def to_vector3d(self, z): # return a 3d vector see further
        return vector3d(self.x, self.y, z)

    def switch(self): # switch the value of the two axis
        self.t.t1 = self.x
        self.x = self.y
        self.y = self.t.t1
        self.t.t1 = 0

    def add_lenght(self, l): # add length to the vec ; l can be negative
        self.t.t1 = self.x
        self.t.t2 = self.y
        self.x = self.t.t1 + l * (math.pow(self.t.t1, 2) / (math.pow(self.t.t1, 2) + math.pow(self.t.t2, 2)))
        self.x = self.t.t2 + l * (math.pow(self.t.t2, 2) / (math.pow(self.t.t1, 2) + math.pow(self.t.t2, 2)))

    def is_parrallel_to(self, p): # return True if the other vector is parrallel
        if self.y == 0 or p.y == 0:
            if self.y == 0 and p.y == 0:
                return True
            else:
                return (self.y / self.x) == (p.y / p.x) or (self.y / self.x) == -(p.y / p.x)
        else:
            if self.x == 0 and p.x == 0:
                return True
            else:
                return (self.x / self.y) == (p.x / p.y) or (self.x / self.y) == -(p.x / p.y)


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

    def to_vector2d(self, as_x, as_y): # switch two of the axis position
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

    def is_parrallel_to(self, p): # return true if the second vector is parrallel to the first doesnt work if y or z is nul
        return ((self.x / self.y) == (p.x / p.y) and (self.x / self.z) == (p.x / p.z)) or ((self.x / self.y) == -(p.x / p.y) and (self.x / self.z) == -(p.x / p.z))


def iter_int(i):
    temp.t1 = 0
    rdict = {}
    while not temp.t1 == i:
        rdict.__setitem__(temp.t1,temp.t1)
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

class hour:
    def __init__(self, s, m, h):
        self.s = s
        self.m = m
        self.h = h
        self.verif()

    def verif(self):
        while not ((self.s >= 0 and self.s <= 60) and (self.m >= 0 and self.m <= 60) and self.h >= 0 and float.is_integer(self.m) and float.is_integer(self.h)):
            if not float.is_integer(self.h):
                self.m = math.fmod(self.h, 1) * 60
            if not float.is_integer(self.m):
                self.s = math.fmod(self.m, 1) * 60
            while not self.s <= 60:
                self.s -= 60
                self.m += 1
            while not self.m <= 60:
                self.m -= 60
                self.h += 1

    def add_time(self,v ,p ):


"""
class day:
    def __init__(self, d, m, y):
        self.d = 
        self.d = d
        self.y = y
        self.t = temp()
        self.t.t1 = 31
        while t1 >= self.d:
            t1
        self.m = m
        self.verif()



class diary_entry:
    def __init__(self, s, m1, h, d, m2, y):
        self.d = day(s, m1, h)
        self.h = hour(d, m2, y)
        self.verif()

    def verif(self):
        self.d.verif
        self.h.verif
        pass
        self.d.verif
        self.h.verif
"""