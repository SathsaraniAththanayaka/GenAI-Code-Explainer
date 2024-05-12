# input = f"""
# x = 5
# y = 3
# print("Sum:", x + y)
# print("Difference:", x - y)
# print("Product:", x * y)
# print("Quotient:", x / y)
# """
# input = f"""
# age = 18
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")
# """
# input = f"""
# for i in range(5):
#     print("Iteration", i)
# """

# input = f"""
# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(fruit)
# """

# input = f"""
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)
# """

# input = f"""
# # Writing to a file
# with open("example.txt", "w") as f:
#     f.write("Hello, World!")

# # Reading from a file
# with open("example.txt", "r") as f:
#     content = f.read()
#     print(content)
# """

# input = f"""
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# person1 = Person("Alice", 30)
# person1.greet()
# """

# input = f"""
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")
# """

# input = f"""
# import datetime

# current_time = datetime.datetime.now()
# print("Current time:", current_time)
# """

# input = f"""
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# fib_sequence = fibonacci()
# for _ in range(10):
#     print(next(fib_sequence), end=" ")
# """

# input = f"""
# class Animal:
#     def speak(self):
#         print("Animal speaks.")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks.")

# dog = Dog()
# dog.speak()
# """

# input = f"""
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print("Factorial of 5:", factorial(5))
# """

input = f"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)
"""
