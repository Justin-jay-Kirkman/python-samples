# import requests

'''
requests
'''

#
# x = requests.get('https://w3schools.com/python/demopage.htm')
#
# print(x.text)

'''
    Class sample
'''
print("OBJECTS/INHERITANCE")
class Animal:
    def __init__(self, name):
        self.name = name

    def printanimal(self):
        print(self.name)

    def getAnimal(self):
        return self.name


class dog(Animal):
    def __init__(self, name):
        # inheritance
        super().__init__(name)
    def speak(self):
        print("My name is " + self.name)

a = Animal('Animal1')
a.printanimal()

d = dog('Dog1')
d.speak()
d.printanimal()
# fstring
print(f"fprint: {d.getAnimal()}")

'''
funtions
'''
#note functions are actually objects

'''
List comprehensions
'''
print("\nLIST COMPREHENSIONS")
x = [x for x in range(10)]
print(x)
x = [[0 for x in range(100)] for y in range(5)]
print(x)
x = [i for i in range(100)]
print(x)

'''
Iterators
'''
print("\nITERATORS")

#start, stop, step
for i in range(1, -10, -2):
    print(i)

'''
collections
'''
print("\nCOLLECTIONS")

start_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(start_array)

copy_array = start_array[:]
print(copy_array)

start_array.append(5)
print(start_array)

copy_array.extend(start_array)
print(copy_array)
copy_array.pop()
print(copy_array)

'''
slices
'''
print("\nSLICES")
start_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(start_array)
reversed = start_array[::-1]
print(reversed)


'''
map
'''

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(array)
mapped_array = map(lambda i: i * 2, array)
print(list(mapped_array))


'''
filter
'''

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(array)
filterped_array = filter(lambda i: i > 5, array)
print(list(filterped_array))


'''
functions args
'''
print("\nFUNCTIONS")
def pass_args(*args, **kargs):
    print(args, kargs)

pass_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [1,2])




