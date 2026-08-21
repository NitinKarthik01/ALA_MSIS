from Lab1 import Vec

print("--- Test Case 2 ---")
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
print("Ones vector :", ones_vec)