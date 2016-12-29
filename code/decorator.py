import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print ('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print ('2016-04-04')

now()