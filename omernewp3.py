from math import sqrt
NoRoot = True
while NoRoot:
  try:
    a = float(input("Enter the value of a: \n"))
    b = float(input("Enter the value of b: \n"))
    c = float(input("Enter the value of c: \n"))

    Value = (b**2)-(4*a*c)
    sol1 = (-b+sqrt(Value)/(2*a))
    sol2 = (-b-sqrt(Value)/(2*a))

    print((sol1,sol2))
    NoRoot = False 

  except:
        print("There Are no roots \n")
