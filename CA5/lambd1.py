

reduce(lambda x, y: x+y, [47, 11, 42, 13])

f = lambda a,b: a if (a>b) else b
reduce(f, [47, 11, 42, 13]) 

reduce(lambda x, y: x+y, range(1, 101))

def add(values):
	return reduce(lambda x, y: x + y, values)
	
def divide(values):
	return reduce(lambda x, y: x /float (y) if y!=0 else 'nan', values)	
	
def multiply(values):
	return reduce(lambda x, y: x + y, values)
    
def max(values):
	return reduce(lambda a,b: a if (a>b) else b, values)
	
def min(values):
	return reduce(lambda a,b: a if (a<b) else b, values)

def is_even(values):
	return filter(lambda x: x%2 ==0, values)
	
def is_odd(values):
	return filter(lambda x: x%2 ==1, values)

def is_greater_than_mean(values):
	mean = sum(values)/len(values)
	return filter(lambda x: x>mean, values)	

def add1(first, second):
	#return map(lambda a,b: a if (a<b) else b, values)
    return map(lambda x, y: x+y, first, second)
    
def Multiplication(first, second):
    return map(lambda x, y: x * y, first, second)    
    
def Division(first, second):
    return map(lambda x, y: x /float (y) if y!=0 else 'nan', first, second)

def to_fahrenheit(values):
	return [((float (9) / 5)*x + 32) for x in values]
    
    
	
print 'Sum of two lists:', add1([47, 11, 42, 13], [37, 21, 22, 33])

print 'Division of two lists:', Division ([47, 11, 42, 21], [10, 2, 21, 0])

print 'Multiplication of two lists:', Multiplication ([47, 11, 42, 21], [10, 2, 21, 0])
	
print 'NumberGreaterThanMean:', is_greater_than_mean([47, 11, 42, 13])

print 'EvenNumber:', is_even ([47, 11, 42, 13, 24, 38])

print 'OddNumber:', is_odd ([47, 11, 42, 13, 36, 47])
	
print 'Addation:', add ([47, 11, 42, 13])

print 'Minimum:', min ([47, 11, 42, 13])

print 'Maximum:',max ([47, 11, 42, 13])

celcius = [39.2, 36.7, 37.8]
fahrenheit = [((float)((9) / 5)* x + 32) for x in celcius]
print fahrenheit
	
fahrenheit = to_fahrenheit(celcius)
print fahrenheit


def city_generator():
    yield("Welcome")
    yield(30 + 32)
    yield(3 ** 6)
    yield(max ([47, 11, 42, 13]))
    yield("Bye")

x = city_generator()
print x.next()
print 'Hello'

print x.next()

print x.next()

print x.next()

print x.next()

'''
def pythagorean(n):
	for x in range(1, n):
		for y in range(x, n):
			for z in range(y, n):
				if x **2 + y **2 == z **2:
					yield (x, y, z)
					
					
pyt = pythagorean(30)
for triplet in pyt:
	print triplet
	print sum(triplet)
'''    