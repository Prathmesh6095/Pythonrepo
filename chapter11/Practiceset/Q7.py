# Override the __len__() method on vector of problem 5 to display the dimention of the vector.
class Vector:
    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)
    
v1 = Vector([1, 2, 3])
print(len(v1))
# v2 = Vector(4, 5, 6)
# v3 = Vector(7, 8, 9) # same dimension vector

# print(v1 + v2)# O/p : Vectors(5, 7, 9)
# print(v1 * v2)# O/p : 32

# print(v1 + v3)# O/p : Vectors(8, 10, 12)
# print(v1 * v3)# O/p : 50