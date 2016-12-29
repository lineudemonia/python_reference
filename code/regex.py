import re
test = input('Please enter an email address: ')

if re.match(r'[\w\.]+@[\w\.]+com', test):
	print ('ok')
else:
	print ('failed')