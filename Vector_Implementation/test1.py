from vector import Vec


#Test Block main
print(__name__)   # default python makes __name__ = main
print("")
    
print("Iniailized vectors v1 and v2")
v1 = Vec((3,4))     # you are initializing a vector so it calls __init__ method, and inside __init__ method there is print, so it prints
v2 = Vec((9,10,11)) # same as above
                        # if I initialize a vector with v1=Vec(("hello",5)) --> it raises a typeError  
print("\n")



print("printed v1")
print(v1) # this calls the method __repr__ directly when it see the print(), so this prints Vector v1
            # it calls as v1.__repr__()



print("\n")
print("length of v2 ",)
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




#Test Block 1
print("\n")

v1 = Vec((3, 4))
v2 = Vec((1, 2))
print("\n")

print("Addition")
v3 = v1 + v2
print("v1 + v2 =", v3)
print("\n")

print("Scalar Multiplication")
v4 = v1 * 2
print("v1 * 2 =", v4)
print("\n")

print("Norm")
print("norm(v1) =", v1.norm())


# Even without using print function, the vectors are getting printed because, 
# when we are calling the dunder functions and while returning them, we are assigning it to a new vector,
# so here a new object is created and by default when the new object is created ut calls __init__ function, 
# so the elements are getting printed




#Test Block 2
print(" ")
v1 = Vec((2, 4, 6))
print(" ")

print("In place multiplication")
v1 *= 3
print("After *= 3:", v1)
print(" ")

print("Negation")
v2 = -v1
print("Negated vector:", v2)
print(" ")


zeros_vec = Vec.zeros(4)
ones_vec = Vec.ones(4)
print("Zeros vector:", zeros_vec)
print(" ")
print("Ones vector :", ones_vec)



#Test Block 3
v1 = Vec((1, 2))
v2 = Vec((1, 2, 3))
print(v1 + v2) # it generates error bcoz they are not of same dimensions

