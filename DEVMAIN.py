import prefab
from BASE import CLASSE
from BASE import RACE
from BASE import ARME
from BASE import MAGE_TYPE
from BASE import COMP
import superobject


SPOB = superobject.a()
t = prefab.temp
for i in CLASSE.listfunc:
    t.t1 = i
    t.t2 = {i.COMPBASE1, i.COMPBASE2, i.COMPBASE3, i.COMPBASE4}
    for e in t.t2:
        t.t3 = e
for i in ARME.listfunc:
    t.t1 = i
for i in MAGE_TYPE.listfunc:
    t.t1 = i
for i in RACE.listfunc:
    t.t1 = i
for i in COMP.listfunc:
    t.t1 = i
