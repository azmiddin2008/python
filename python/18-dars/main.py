# function based --> 
#
# Kalit so'z argumentlarini lug'atlarga o'xshatish mumkin, chunki ular qiymatni kalit so'z bilan taqqoslaydi.
# def boo(text):
#     return text.upper()

# def goo(text):
#     return text.lower()

# def func(path):
#     text = path("Salom")
#     return text

# funk_upper = func(boo)
# funk_lower = func(goo)
# print(funk_upper)
# print(funk_lower)

# def boo(text):
#     return text.upper()

# def goo(text):
#     return text.lower()

# def func(path):
#     text = path(input("Bironta narsa kiriting"))
#     return text

# funk_upper = func(boo)
# func_lower = func(goo)
# print(funk_upper)
# print(func_lower)

#  Python global, local variables


# sentence = "My friends"
# def fu():
#     sentence = "My first local variables"
#     return sentence


# print(fu())

#  lambda function --> Lambda istalgancha argument oladi

# x = lambda a, b, c, d : a + b + c + d
# print(x('Mening ', 'dostlarim ', 'juda ', 'kopmas'))

# def foo(a):
#     y = lambda b : b * a
#     return y

# funk = foo(5)
# print(funk(5))

def foo(a):
    y = lambda  b, c, d: b * a * c * d
    return y


funk = foo(5)
triple = foo(6)
print(funk(5, 5, 6))
print(funk(5, 7, 8))
