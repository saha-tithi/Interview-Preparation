n=int(input("How many numbers you want to put :"))
my_list = []
for i in range(n):
    # Prompt the user for input in each iteration
    element = input(f"Enter element {i+1}: ")
    # Add the input to the list using the append() method
    my_list.append(element)
difference=int(max(my_list))-int(min(my_list))
print(f"the maximum difference is : {difference}")