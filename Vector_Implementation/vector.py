
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


                                         ##################
                                         # ASSIGNMENT - 1 #
                                         ##################

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


    def dot_product(self, other):
        if len(self) != len(other):
            raise ValueError("Dimensions mismatch")
        return sum(a*b for a,b in zip(self.elements, other.elements))

    def cos_sim(self, other):
        n1 = self.norm()
        n2 = other.norm()
        if n1==0 or n2==0 :
            raise ValueError("Cosine Similarity wont be there for Zero vectors")
        return self.dot_product(other)/(n1*n2)

    def mean_vector(vectors):
        dimensions = len(vectors[0])
        n = len(vectors)
        mean = []
        for i in range(dimensions):
            total = 0
            for vector in vectors:
                total += vector[i]
            mean.append(total / n)
        return mean

################################
# Calculating
# 1. Norm
# 2. Mean
# 3. Demean
# 4. Std Deviation for TEXT DATA
################################

from gensim.models import KeyedVectors

if __name__ == "__main__":

    model = KeyedVectors.load(
        "/Users/nitinsrikarthikeya/Documents/ALA_MSIS/glove50/glove_50_fast.wordvectors",
        mmap="r"
    )

    sentence = input("Enter a sentence : ")

    tokens = sentence.lower().split()

    for word in tokens:

        if word in model.key_to_index:

            vector = Vec(model[word].tolist()) 

            # model[word] -> it access the vector of that word in glove file and converts that into list
            # and make it as a vector for our code

            print("\n\nWord:", word)
            print("\nNorm : ", vector.norm())
            print("\nMean : ", vector.mean())
            print("\nDe-mean : ", vector.de_mean())
            print("\nStandard deviation : ", vector.std())
            print(" ")
            print("*"*80)

        else:
            print(word, "is not in the GloVe vocabulary")


    
    






