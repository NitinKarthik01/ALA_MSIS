
#tup = (10,20)
#print(tup)
#print(type(tup))
# tup[0] = 100  #tuples cant be changes, so it will give error
#l = list(tup) 
#print(l)  # this will print as[10, 20], but for tuples it will print as (10, 20)
#l[0] = 100 # list can be changes
#print(l)  # this will print as [100, 20]

from typing import Self
import random
from math import sqrt

class Vec:
    def __init__(self,src) -> Self:
        for x in src:
            if not isinstance(x,(int, float)):
                raise TypeError(f"Scalar must be a number: {type(x)}")
        self.elements = list(src)
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


    def __imul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(scalar)}")
        for i, val in enumerate(self.elements):
            self.elements[i] = round(val * scalar, 5)
        return self

    

    def __sub__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"Expected vec: {type(self)}")
        if len(self.elements) != len(t.elements):
            raise TypeError(f"Type error - vectors must be of same dimensions")
        return Vec([round(x-y,5) for x,y in zip(self.elements, t.elements)])

    def __radd__(self, other) :
        if not isinstance(other, Vec):
            raise TypeError(f"Expected vec: {type(other)}")
        if len(self.elements) != len(t.elements):
            raise TypeError(f"Type error - vectors must be of same dimensions")
        return Vec([round(other + x, 5) for x in self.elements])

    def __repr__(self) -> str:
        return repr(self.elements)

    def __len__(self) -> int:
        return len(self.elements)


    def __neg__(self) -> Self:
        return Vec([-x for x in self.elements]) 

    def __iadd__(self, t):
        if not isinstance(t, Vec):
            raise TypeError(f"Expected vec: {type(self)}")
        if len(self.elements) != len(t.elements):
            raise TypeError(f"Type error - vectors must be of same dimensions")
        return Vec([round(x+y,5) for x,y in zip(self.elements, t.elements)])

    
    @staticmethod
    def zeros(n: int) -> Self:
        if(n<=0):
            raise ValueError("n must be greater than 0")
        return Vec([0]*n)

    @staticmethod
    def ones(n: int) -> Self:
        if(n<=0):
            raise ValueError("n must be greater than 0")
        return Vec([1]*n)

    @staticmethod
    def uniform(n: int) -> Self:
        if n <= 0:
            raise ValueError("n must be greater than 0")
        return Vec([random.uniform(0, 1) for _ in range(n)])
            

    def norm(self) -> float:
        total = 0
        for x in self.elements:
            total += x**2
        return sqrt(total)


print("Iniailized vectors v1 and v2")
v1 = Vec((3,4))     # you are initializing a vector so it calls __init__ method, and inside __init__ method there is print, so it prints
v2 = Vec((9,10,11)) # same as above
                    # if I initialize a vector with v1=Vec(("hello",5)) --> it raises a typeError  
print("\n")



print("printed v1")
print(v1) # this calls the method __repr__ directly when it see the print(), so this prints Vector v1
          # it calls as v1.__repr__()



print("\n")
print("printed length of v2")
len(v1)   # this calls v1.__len__() and returns the length of the vector
print(len(v2))




print("\n")
# v3 = v1 + v2 gives a typrError (dimension error) bcoz both v1 and v2 are not of same dimesnions(lenghts)
print("Initialized vector v3")
v3 = Vec((19, 20, 21))


print("\n")

print("Added v3 and v2 and stored in v4")
v4 = v3+v2    # v3.__add__(v2)


print("\n")
print("Subtracted v3 and v2 and stored in v5")
v5 = v3-v2    # v3.__sub__(v2)



print("\n")
print("Multiplied v1*2 and stored in v6")
v6 = v1*2    # v1.__mul__(2)



print("\n")
print("Multiplied 2*v2 and stored in v7")
v7 = 2.5*v2    # 2.__rmul__(v2)


print("\n")
print("Multiplied v7*=3 and stored in v7")
v7*=3     # when the interpretor sees *= it calls v7.__imul__(3)
print(v7)


print("\n")
print("Negated v1 and stored in v8")
v8 = -v1       # when the interpreter sees -v1, it calls v1.__neg__()



print("\n")
print("Added v1 and v3 and stored in v9")
v9 = v7 + v3   # when the interpreter sees v7+v3, it calls v1.__add__(v3)



print("\n")
print("Subtracted v2 from v3 and stored in v10")
v10 = v3 - v2  # when the interpreter sees v3-v2, it calls v3.__sub__(v2)



print("\n")
print("Added v1 and v3 using += and stored in v1")
v9 += v3       # when the interpreter sees +=, it calls v9.__iadd__(v3)



print("\n")
print("Created a vector of zeroes")
v11 = Vec.zeros(5)     # zeros() is a static method, so we call it using the class name Vec
print(type(v11.elements))


print("\n")
print("Created a vector of ones")
v12 = Vec.ones(5)      # ones() is a static method, so we call it using the class name Vec



print("\n")
print("Created a vector of uniformly distributed random numbers")
v13 = Vec.uniform(5)   # calls the static method uniform() using the class name Vec and stored in v15



print("\n")
print("Calculated the norm of v3 : ",v13.norm())