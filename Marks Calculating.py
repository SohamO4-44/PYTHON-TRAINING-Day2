m1 = int(input("Enter marks of paper 1: "))
m2 = int(input("Enter marks of paper 2: "))
m3 = int(input("Enter marks of paper 3: "))
# calculating total
total = m1 + m2 + m3
# calculating percentage
percentage = (total / 300) * 100
print("Total marks =", total)
print("Percentage =", percentage)
# checking eligibility
if percentage >= 60:
    print("Eligible for placement")
else:
    print("Not eligible for placement")
