def chop(list_A):
    del list_A[0]
    del list_A[-1]
    return None
    
def middle(list_B):
    list_C=list_B.copy()
    del list_C[0]
    del list_C[-1]
    return list_C
        
my_list=[1, 2, 3, 4]
print("My list before call chop function: ", my_list)
chop(my_list)
print("My list after call chop function: ", my_list)
my_list=[1, 2, 3, 4]
print("My list before call middle function: ", my_list)
new_list=middle(my_list)
print("My list after call midle function: ", my_list)
print("New list after call middle function: ",new_list )

