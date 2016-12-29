# _*_ coding: utf-8 _*_

'a class module'

__author__ = 'Lin Lin'

class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.__score = score

	def print_score(self):
		print ('%s: %s' % (self.name, self.__score))

	def get_grade(self):
		if self.__score >= 90: return '成绩优'
		elif self.__score >= 80: return '成绩良' 
		elif self.__score >= 60: return '成绩及格'
		else: return '不及格'

	def get_score(self):
		
		return self.__score




bart = Student('Bart', 50)
hai = Student('Hai', 99)


bart.print_score()
print(bart.get_grade())
bart.age = 32
print (bart.age)
print ('Name:', bart.name)
#print ('Score:', bart.__score)
print ('Score:', bart.get_score())