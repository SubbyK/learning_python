babs_list = [1, "max", 3, "babs"]
print(babs_list)
print(1)
print("hi max i love you")
# print is a function that outputs its arguments on the command prompt

babs_num = 1 + 2
print(babs_num)

# this is a comment. the program will ignore it

# def lets you define new functions; write the name of the function and the viariable

def add(x, y):
	return x + y

def add2(x, y):
	sum = x + y
	return sum

result = add(7,11)
print(result)

# this (doing exponents) is difficult, and will require knowing about loops
# doing exponents using while loop
def exp(x, y):
	total, count = 1, 0
	while count < y:
		total = total * x
		count = count + 1
	return total
	
result = exp(2,2)
print(result)	

# doing exponents using the for loop
# range is a built in python function, range(x,y) returns x-y, including x but excluding y
# range (1,3) returns 1,2
def exp_for(x, y):
	total = 1
	for index in range(y):
		total = total * x
	return total

result = exp_for(2,2)
print(result)

result = exp_for(7,2)
print(result)

result = exp_for(20,0)
print(result)










