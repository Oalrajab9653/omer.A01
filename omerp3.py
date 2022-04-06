import cmath

a = float(input('\nnWhat is the value for a? '))
b = float(input('\nnWhat is the value for b? '))
c = float(input('\nWhat is the value for  c? '))

value = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(value))/(2*a)
sol2 = (-b+cmath.sqrt(value))/(2*a)

print('\nThe solution are {0} and {1}'.format(sol1,sol2))

