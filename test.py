from collections import Iterable

a = ["abc", "abcd"]
print(id(a))
s = a[:]
print(id(s))

def get(a):
    n = 0
    while n < a :
        yield n
        n = n + 1

def triangles(h):
    level = [1]
    while h > 0 :
        yield level
        number = len(level) 
        res = [1]
        index = 0
        while index < number - 1:
            res.append(level[index] + level[index + 1])
            index += 1
        res.append(1)
        level = res
        h -= 1

for a in triangles(12):
    print(a)

print(isinstance(1, Iterable))

print(" " == "fsda")

def what():
        pass

a = id(what())
get(1)
b = id(what())

print(a == b)
