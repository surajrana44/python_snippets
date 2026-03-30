 
a = 5
b = 5
print(id(a))  
print(id(b))  # give the same unique refernce address of object

A = 1000
B = 1000
print(id(A))
print(id(B))

a = 'string'
b = 'string'
print(id(a))
print(id(b))

a = 'string is a part of array who store the character'
b = 'string is a part of array who store the character'
print(id(a))
print(id(b))

 # ⁠Memory Optimization –  Python saves space by reusing small integers and immutable objects
 

 # Garbage Collection – Python’s automatic system that frees memory by removing unused objects
