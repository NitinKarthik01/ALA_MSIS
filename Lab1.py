#tup = (10,20)
#print(tup)
#print(type(tup))
# tup[0] = 100  #tuples cant be changes, so it will give error
#l = list(tup) 
#print(l)  # this will print as[10, 20], but for tuples it will print as (10, 20)
#l[0] = 100 # list can be changes
#print(l)  # this will print as [100, 20]

from typing import Self

class Vec:
    def __init__(self,src) -> Self:
        for x in src:
            if not isinstance(x,(int, float)):
                raise TypeError(f"Scalar must be a number: {type(x)}")
        self.elements = src
        print(self.elements)

    def __add__(self,t: Self) -> Self :
        if not isinstance(t, Vec):
            raise TypeError(f"Expected vec: {type(self)}")
        if len(self.elements) != len(t.elements):
            raise TypeError(f"Type error - vectors must be of same dimensions")
        return Vec([round(x+y,5) for x,y in zip(self.elements, t.elements)])

    def __mul__(self,scalar :int|float) -> Self :
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        return Vec([round(x*scalar,5) for x in self.elements])

    def __rmul__(self,scalar :int|float) -> Self :
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        return Vec([round(x*scalar,5) for x in self.elements])

    def __sub__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected vec: {type(self)}")
        if len(self.elements) != len(t.elements):
            raise TypeError(f"Type error - vectors must be of same dimensions")
        return Vec([round(x-y,5) for x,y in zip(self.elements, t.elements)])

    def __repr__(self) -> str:
        return repr(self.elements[0])

    def __len__(self) -> int:
        return len(self.elements)



v1 = Vec((3,4))
v2 = Vec((1,2))
v3 = v1*2
v4 = 2*v1
v1*=2
v5 = v1+v2
v6 = Vec((1,2))
v7 = v2-v6
print(v7)
