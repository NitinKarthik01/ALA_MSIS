import numpy as np

a = np.array([1,2,3])
print(a.shape)

print(a.shape==(3))    #false
print(a.shape == 3)    #false
print(a.shape == (3,)) #true

print(type((3)))  #int
print(type((3,))) #tuple
print(type(3))    #int


print(isinstance(a.shape,tuple))  #tuple



[0,1,2] == [1,2,3]  # true if all elements in array are true

print(all([True, True, True]))  # true if all true

print(all([True, False, True])) # false if one of them is false




a = np.array([0.12, 0.45, 0.78, 1.34, 2.91])
assert(a.shape == (5,))
assert(a.ndim == 1)
assert(a.size == 5)





a = np.array([
        [0.12, 0.45, 0.78, 1.34, 2.91],
        [0.23, 0.56, 0.89, 1.45, 3.02],
        [0.34, 0.67, 0.90, 1.56, 3.13],
    ])
assert(a.shape == (3, 5))
assert(a.ndim == 2)



a = np.random.rand(3, 3, 4)
assert(a.shape == (3, 3, 4))
assert(a.ndim == 3)





a = np.array(np.arange(1, 25, 1, np.int8))
print(a)
assert(a.shape == (24,))
assert(a.size == 24)
assert(len(a) == 24)                  # The 𝑙𝑒𝑛 function returns the number of elements along the first axis of an array.
assert(a.ndim == 1)
print(" ")


assert (a == [x for x in range(1, 25)]).all()
b = a.reshape(2, 12)                  # The reshape method is used to change the shape of an array without changing its data
print(b)
assert(b.shape == (2, 12))
assert(b.size == 24)
assert(len(b) == 2)                   # The 𝑙𝑒𝑛 function returns the number of elements along the first axis of an array.
assert(b.ndim == 2)
print(" ")




c = a.reshape(4, 6)                   # changed the shappe of 1D array into 2D array with 4 rows and 6 columns with same no.of elements
print(c)
assert(c.shape == (4, 6))
assert(c.size == 24)
assert(len(c) == 4)
assert(c.ndim == 2)
print(" ")





d = a.reshape(24, 1)                   # changed the shappe of 1D array into 2D array with 24 rows and 1 columns with same no.of elements
print(d)
assert(d.shape == (24, 1))
assert(d.size == 24)
assert(len(d) == 24)
assert(d.ndim == 2)
print(" ")




# Check the first row of b from the reshaped array a
assert (b[0] == [x for x in range(1, 13)]).all()


# Check the second row of b from the reshaped array a
assert (b[1] == [x for x in range(13, 25)]).all()



assert(b[:, 0] == [1, 13]).all()       # access the first column
print(b[:, 0])
assert np.array_equal(b[:, 0], [1, 13])




assert np.array_equal(b[:, 1], [2, 14])  # access the second column

assert np.array_equal(b[:, 11], [12, 24]) # access the last column