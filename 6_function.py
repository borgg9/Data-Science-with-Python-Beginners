# functions in python script

def absolute_value(num):
	#this funtion return de absolute value of the entered number
	if num >= 0:
		return num
	else:
		return -num


# Output 1
print(absolute_value(10))
print(absolute_value(-10))


def greet(*names):
	#greets all the person in the names tuple
	for name in names:
		print('Hello '+name)



greet('Monica', 'Luke', 'Steve', 'John')