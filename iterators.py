# An iterator is an object that has countable items
# It can be iterated upon, you can tranverse through the elements
# Lists, tuples, dictionaries and sets are all iterable objects
# They have the iter() method, which can be used to get an iterator

from math import e

my_tuple = ("apple", "banana", "mango")

my_tuple_iterator = iter(my_tuple)

print(next(my_tuple_iterator))
print(next(my_tuple_iterator))

# Even strings are iterable items
my_str = "Benchmark"
my_str_iter = iter(my_str)
print(next(my_str_iter))
print(next(my_str_iter))
print(next(my_str_iter))

# using a for loop to iterate through a iterable

for x in my_str:
    print(x)


class MyNumber:
    def __iter__(self):
        self.first = 1
        return self

    def __next__(self):
        first_number = self.first
        if first_number <= 20:
            self.first += 1

            return first_number
        else:
            raise StopIteration  # Used to stop the iteration from going beyond the allowed rounds


my_number_class = MyNumber()

my_class_inter = iter(my_number_class)
print(next(my_number_class))

for x in my_class_inter:
    print(x)


class Vehicle:
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand

    def move():
        print("Drive!!")


class Car(Vehicle):
    pass
