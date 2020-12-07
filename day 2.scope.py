Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 10:03:53) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2+4
6
>>> 4-3
1
>>> a=3
>>> b=2
>>> a+b
5
>>> a-b
1
>>> b-a
-1
>>> a*b
6
>>> a/b
1.5
>>> a//b
1
>>> print("archana")
archana
>>> print(archana)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(archana)
NameError: name 'archana' is not defined
>>> print("a+b")
a+b
>>> print(a+b)
5
>>> a='hello'
>>> b='world'
>>> print(a+b)
helloworld
>>> print(a b)
SyntaxError: invalid syntax
>>> print("hello" + "world")
helloworld
>>> print("hello" , "world", sep=",")
hello,world
>>> print("hello" , "world", sep="   ")
hello   world
>>> print("hello" , "world", sep="+")
hello+world
>>> print("hello" , "world", sep="\n")
hello
world
>>> print("hello" , "world", sep="\n\n")
hello

world
>>> print("hello" , "world", sep="\n\n",end=".")
hello

world.
>>> a=10
>>> b=20

>>> print("The sum of a and b is :",a+b)
The sum of a and b is : 30
>>> print("The product of a and b is :",a*b)
The product of a and b is : 200
>>> print("The product of 10 and 20 is:",a*b)
The product of 10 and 20 is: 200
>>> a=3
>>> b=5
>>> print("The sum of {0} and {1} is {2},format(a,b,a+b)")
The sum of {0} and {1} is {2},format(a,b,a+b)
>>> print("The sum of {0} and {1} is {2}".format(a,b,a+b))
The sum of 3 and 5 is 8
>>> print("The product of {} and {} is {}".format(a,b,a*b))
The product of 3 and 5 is 15
>>> a=22
>>> b=33
>>> c=a+b
>>> print(f"the sum of {a} and {b} is {c}")
the sum of 22 and 33 is 55
>>> print(f"the sum of {} and {} is {}")
SyntaxError: f-string: empty expression not allowed
>>> print(f"the sum of {1} and {2} is {3})
      
SyntaxError: EOL while scanning string literal
>>> print(f"the sum of {1} and {2} is {3}")
the sum of 1 and 2 is 3
>>> name='archana'
>>> location='siddipet'
>>> print("{name} is in {location}")
{name} is in {location}
>>> print({name} is in {location})
SyntaxError: invalid syntax
>>> print(f"{name} is in {location})
      
SyntaxError: EOL while scanning string literal
>>> print(f"{name} is in {location}")
archana is in siddipet
>>> a=int(input("enter first num: "))
enter first num: 3
>>> b=int(input("enter second num: "))
enter second num: 3
>>> print("The sum of {0},{1} is {2}",format(a,b,a+b))
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print("The sum of {0},{1} is {2}",format(a,b,a+b))
TypeError: format() takes at most 2 arguments (3 given)
>>> print("The sum of {0},{1} is {2}".format(a,b,a+b))
The sum of 3,3 is 6
>>> print("The product of {0},{1} is {2}".format(a,b,a+b))
The product of 3,3 is 6
>>> print("The product of {0},{1} is {2}".format(a,b,a*b))
The product of 3,3 is 9
>>> 9/3
3.0
>>> int(9/3)
3
>>> 9//3
3
>>> float(9/3)
3.0
>>> 