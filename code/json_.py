import json

d = dict(name = 'Bob', age = 20, score = 90)
print (json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'

print (json.loads(json_str))

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score


s = Student('Bob', 20, 88)		

def student2dict(std):
	return {
	'name': std.name,
	'age': std.age,
	'score': std.score
	}

print (json.dumps(s, default = student2dict))	