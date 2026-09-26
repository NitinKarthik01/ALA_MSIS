
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
        #print(self.elements) # commented this line bcoz, printing itself takes so much time while checking performance for large size of vectors

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


#ASSIGNMENT - 1

    def mean(self) -> float:
        if len(self.elements) <= 0:
            raise ValueError("n must be greater than 0")
        mean = 0
        for x in self.elements:
            mean = mean + x
        mean = mean/len(self.elements)
        return mean


    def de_mean(self):
        if len(self.elements) <= 0:
            raise ValueError("n must be greater than 0")
        return self - ((self.mean())*(Vec([1]*len(self.elements))))



    def std(self)-> float :
        if len(self.elements) <= 0:
            raise ValueError("n must be greater than 0")
        self = self.de_mean()
        std = (self.norm())/(sqrt(len(self.elements)))
        return std

    






