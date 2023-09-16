promt1="Enter Hours: "
promt2="Enter Rate: "
Hours=input(promt1)
Rate=input(promt2)
print(type(Hours))
print(type(Rate))
Hours=int(Hours)
Rate=float(Rate)
print(type(Hours))
print(type(Rate))
Salary=Hours*Rate
print(Salary)