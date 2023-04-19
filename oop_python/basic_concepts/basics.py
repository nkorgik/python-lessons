# everything is an object
a = 42
print(a, type(a))

b = 'hello'

def my_function():
    pass

print(type(my_function), type(b))


# Dynamic Typing
x = 5
print(type(x))

x = 'hello'
print(type(x))

# Indentations 
def say_hello():
    print('Hello World!')

say_hello()


# Multiple Inheritance
class A:
    def method_a(self):
        print('Method A')


class B:
    def method_a(self):
        print('Method B')
        

class C(A, B):
    pass
    

c = C()
c.method_a()    
c.method_a()    


# First-class function

def square(x):
    return x*x

def cube(x):
    return x*x*x

def apply(func, x):
    return func(x)

print(apply(square, 5))
print(apply(cube, 3))


# Decorators 

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Before The Function Call')
        result = func(*args, **kwargs)
        print('After The Function Call')
        return result
    
    return wrapper


@my_decorator
def greet(name):
    print(f'Hello, {name}!')

# greet = my_decorator(greet)
greet('Max')


# 

class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius cannot be negative!')
        self._radius = value
    
    
c = Circle(5)
c.radius = 7
print(c.radius)
    

# DUCK typing
class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius**2

    
shapes = [
    Rectangle(2, 3),
    Circle(5),
    Circle(4),
    Rectangle(3, 3)
]

for shape in shapes:
    result = shape.area()
    print(result)
        
    

# Dunder method

class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return f'Vector({self.x}, {self.y})'
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1, v2)
print(v1+v2)
