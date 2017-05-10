
reduce(lambda x, y: x+y, [47, 11, 42, 13])

f = lambda a,b: a if (a>b) else b
reduce(f, [47, 11, 42, 13]) 

reduce(lambda x, y: x+y, range(1, 101))

print reduce 

def add(values):
	return reduce(lambda x, y: x + y, values)
	
def add(values):
	return reduce(lambda x, y: x /float (y) if y!=0 else 'nan', values)	
	

def max(values):
	return reduce(lambda a,b: a if (a>b) else b, values)
	
def min(values):
	return reduce(lambda a,b: a if (a<b) else b, values)

def is_even(values):
	return filter(lambda x: x%2 ==0, values)
	
def is_odd(values):
	return filter(lambda x: x%2 ==1, values)

def is_greater_than_mean(values, mean):
	mean = sum(values)/len(values)
	return filter(lambda x: x>mean, values)	

def add1(first, second):
	return map(lambda a,b: a if (a<b) else b, values)

def to_fahrenheit(values):
	return [((float (9) / 5)*x + 32) for x in values]	
	
print is_greater_than_mean([47, 11, 42, 13])
	
print add ([47, 11, 42, 13])

print min ([47, 11, 42, 13])

celcius = [39.2, 36.7, 37.8]
fahrenheit = [((float)((9) / 5)* x + 32) for x in celcius]
print fahrenheit

print max ([47, 11, 42, 13])	



fahrenheit = to_fahrenheit(celcius)
print fahrenheit


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