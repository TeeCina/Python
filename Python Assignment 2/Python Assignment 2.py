#Create an empty list called my_list.
my_list = []

#Append the values 10, 20, 30, 40 to my_list.
my_list.append(10)
my_list.append(20)  # 10, 20
my_list.append(30)  # 10, 20, 30
my_list.append(40)  # 10, 20, 30, 40

#Insert the value 15 at index 1 in my_list.
my_list.insert(1, 15)  # 10, 15, 20, 30, 40

#Extend my_list with the values 50, 60, 70.
my_list.extend([50, 60, 70])  # 10, 15, 20, 30, 40, 50, 60, 70

#Remove the value 70 from my_list.
my_list.pop()  # 10, 15, 20, 30, 40, 50, 60

#Sort my_list in ascending order.
my_list.sort()  # 10, 15, 20, 30, 40, 50, 60

#Find and print the index of the value 30 in my_list.
print(my_list.index(30))  # 3
# Output should be: 3
