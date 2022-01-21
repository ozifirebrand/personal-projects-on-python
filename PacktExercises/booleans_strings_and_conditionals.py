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

new_york = "New York"
san_francisco = "San Francisco"
print("\n")
print(new_york > san_francisco)
print(new_york < san_francisco)

print("\n")
ability = "abilities"
print(ability[1:5])
print(ability[:5])
print(ability[-1:])
print(ability[:-2])
print(ability[-5:])

print("\n")
age = 18

if 18 <= age < 21:
    print("At least you can vote")
    print("Poker will have to wait")
    if age == 18:
        print("Perfect!")