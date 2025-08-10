#Factorial

x = int(input('Number:'))
y = x-1

print(f'{x}!')

while y > 0:
	
	print(f'{x} x {y}')
	
	x=x*y
	
	print(f'= {x}')
	
	y-=1
	
print(f'The factorial is {x}')
	
	