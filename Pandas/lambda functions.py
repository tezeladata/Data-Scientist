# A function is an object that is able to accept some sort of input, possibly modify it, and return some sort of output. In Python, a lambda function is a one-line shorthand for function. A simple lambda function might look like this:
square = lambda x: x ** 2
print(square(5))

contains_a = lambda x: "a" in x
print(contains_a("banana"))
print(contains_a("apple"))
print(contains_a("cherry"))

long_string = lambda x: True if len(x) > 12 else False
print(long_string("short"))
print(long_string("photosynthesis"))

ends_in_a = lambda x: x.endswith("a")
print(ends_in_a("data"))
print(ends_in_a("aardvark"))

double_or_zero = lambda x: 2*x if x > 10 else 0
print(double_or_zero(15))
print(double_or_zero(5))

multiple_of_three = lambda x: "multiple of three" if x%3==0 else "not a multiple"
print(multiple_of_three(9))
print(multiple_of_three(10))