# _*_ coding: utf-8 _*_

'an inheritance case'

__author__ = 'Lin Lin'

class Animal(object):
	def run(self):
		print('Animal is running')

class Cat(Animal):
	def run(self):
		print('Cat is running')

class Dog(Animal):
	def run(self):
		print ('Dog is running')

# Even thoug a Timer object is not in the Animal class,
# as long as it also has a run method
# the inheritance wil continue to work
# quite interesting.

class Timer(object):
	def run(self):
		print ('Clock is ticking')

def run_twice(Animal):
	Animal.run()
	Animal.run()

a = Animal()
c = Cat()
d = Dog()
t = Timer()
run_twice(a)
run_twice(c)
run_twice(d)
run_twice(t)
print (isinstance(c, Animal))