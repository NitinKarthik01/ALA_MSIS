from Lab1 import Vec



print("--- Test Case 1 ---")
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



