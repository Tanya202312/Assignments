promt=("Enter seconds ")
x=input(promt)
print(type(x))
x=int(x)
print(type(x))
c=x/3600
b=(x/3600)*60
a=c*3600
print(x,"seconds is", c,"hours", b, "minutes", a, "seconds")