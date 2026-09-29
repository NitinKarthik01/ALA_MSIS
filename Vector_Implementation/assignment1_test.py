from vector import Vec

print("started testing ")
#Test cases for mean()
v = Vec([2, 4, 6, 8])
assert v.mean() == 5.0

v = Vec([-2, -4, -6, -8])
assert v.mean() == -5.0

v = Vec([-10, 0, 10, 20])
assert v.mean() == 5.0

v = Vec([0, 0, 0, 0])
assert v.mean() == 0.0

v = Vec([15])
assert v.mean() == 15.0


# Test cases for demean()
v = Vec([2, 4, 6])
assert v.de_mean().elements == [-2.0, 0.0, 2.0]


v = Vec([-2, -4, -6])
assert v.de_mean().elements == [2.0, 0.0, -2.0]


v = Vec([-10, 0, 10])
assert v.de_mean().elements == [-10.0, 0.0, 10.0]


v = Vec([5, 5, 5])
assert v.de_mean().elements == [0.0, 0.0, 0.0]


v = Vec([15])
assert v.de_mean().elements == [0.0]



v = Vec([2, 4, 6])
print("\n",v.std())


v = Vec([-2, -4, -6])
print("\n",v.std())


v = Vec([-10, 0, 10])
print("\n",v.std())


v = Vec([5, 5, 5])
print("\n",v.std())


v = Vec([15])
print("\n",v.std())

print("\ntesting completed")




