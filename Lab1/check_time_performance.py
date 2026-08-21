from Lab1 import Vec
import time

V1 = Vec(range(1,30000,2))
V2 = Vec(range(2,30002,2))
print(" ")


start1 = time.perf_counter()
V3= V1 + V2
end1 = time.perf_counter()
print("Time for Addition of 15000 vector size : ", end1 - start1)
print(" ")
print("---------------------------------------------------------------")
print(" ")


start2 = time.perf_counter()
V4 = V1 * 5
end2 = time.perf_counter()
print("Time for Scalar Multiplication of 15000 vector size : ", end2 - start2)
print(" ")
print("---------------------------------------------------------------")
print(" ")


start3 = time.perf_counter()
n = V2.norm()
end3 = time.perf_counter()
print("Time for Norm of 15000 vector size : ", end3 - start3)
print(" ")
print("---------------------------------------------------------------")
print(" ")


sizes = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000]

for n in sizes :
    v1 = Vec(range(n))
    v2 = Vec(range(n))

    start1 = time.perf_counter()
    v3= v1 + v2
    end1 = time.perf_counter()
    print("Time for Addition of ",n," size vector is = ", end1 - start1)
    print(" ")


    start2 = time.perf_counter()
    v4 = v1 * 5
    end2 = time.perf_counter()
    print("Time for Scalar Multiplication of ",n," size vector is = ", end2 - start2)
    print(" ")


    start3 = time.perf_counter()
    norm = v2.norm()
    end3 = time.perf_counter()
    print("Time for Norm of ",n," size vector is = ", end3 - start3)
    print(" ")

    start4 = time.perf_counter()
    v5 = v1-v2
    end4 = time.perf_counter()
    print("Time for Subtraction of ",n," size vector is = ", end4 - start4)
    print(" ")

    start5 = time.perf_counter()
    v5 = -v5
    end5 = time.perf_counter()
    print("Time for Negation of ",n," size vector is = ", end5 - start5)
    print(" ")

    start6 = time.perf_counter()
    v6 = Vec.ones(n)
    end6 = time.perf_counter()
    print("Time for Creating ones of ",n," size is = ", end6 - start6)
    print(" ")

    start7 = time.perf_counter()
    v7 = Vec.zeros(n)
    end7 = time.perf_counter()
    print("Time for Creating ones of ",n," size is = ", end7 - start7)
    print(" ")
    print("---------------------------------------------------------------")
    print(" ")

    
