over_18 = True
over_21 = False
A = True
B = True
Y = False
Z = False

print(not A)
print(not Z)
print("\n")
print(A and B)
print(A and Y)
print(Y and Z)
print("\n")
print(A or B)
print(A or Y)
print(Y or Z)
print("\n")

print(over_18 and over_21)
print(over_18 or over_21)
print(not over_21 or (over_18 or over_21))
print(not over_18)