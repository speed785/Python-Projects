#lab8 James Dumitru
#Using built in
number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a number: "))
number_3 = int(input("Enter a number: "))
number_4 = int(input("Enter a number: "))
number_5 = int(input("Enter a number: "))
number_6 = int(input("Enter a number: "))

num_list = []
num_list.append(number_1)
num_list.append(number_2)
num_list.append(number_3)
num_list.append(number_4)
num_list.append(number_5)
num_list.append(number_6)

#Sort in Inputted order
print("~~~~~~ Inputted Order ~~~~~~~~")
print(num_list)

#Sort in increasing order
print("~~~~~~ Increasing Order ~~~~~~")
num_list.sort()
print(num_list)

#Sort in decreasing order
print("~~~~~~ Decreasing Order ~~~~~~")
num_list.sort(reverse=True)
print(num_list)
