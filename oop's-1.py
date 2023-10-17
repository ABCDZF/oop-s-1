#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1
class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle

car = Vehicle("Car", 200, 20)
print(car.name_of_vehicle)  # "Car"
print(car.max_speed)  # 200
print(car.average_of_vehicle)  # 20


# In[4]:


#2
class Car(Vehicle):
    def seating_capacity(self, capacity):
        return f"The {self.name_of_vehicle} has a seating capacity of {capacity}."

my_car = Car("My Car", 150, 15)
print(my_car.seating_capacity(5))


# In[5]:


#3
class Engine:
    def start(self):
        return "Engine started."

class FuelSystem:
    def fill_fuel(self, fuel_amount):
        return f"Fuel tank filled with {fuel_amount} liters."

class Car(Engine, FuelSystem):
    def drive(self):
        return "Car is driving."

my_car = Car()
print(my_car.start())  # "Engine started."
print(my_car.fill_fuel(50))  # "Fuel tank filled with 50 liters."
print(my_car.drive())  # "Car is driving."


# In[6]:


#4
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer.")
        self._age = value

person = Person("John Doe", 30)
print(person.name)  # "John Doe"
person.name = "Jane Doe"
print(person.name)  # "Jane Doe"
print(person.age)  # 30
person.age = 35
print(person.age)  # 35


# In[ ]:


#5
class Parent:
    def greet(self):
        print("Hello, I am the parent!")

class Child(Parent):
    def greet(self):
        print("Hello, I am the child!")

parent = Parent()
parent.greet()  # Output: Hello, I am the parent!

child = Child()
child.greet()

