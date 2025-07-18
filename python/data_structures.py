# Questions and Solutions

#1 Create an empty list called my_list.
my_list = []

#2 Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("List after appending: ", my_list)

#3 Insert the value 15 at the second position in the list.
my_list.insert(1, 15)
print("List after inserrting: ", my_list)

#4 Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])
print("List after extending: ", my_list)

#5 Remove the last element from my_list.
my_list.pop()
print("List after popping last element: ", my_list)

#6 Sort my_list in ascending order.
sorted(my_list)
print("List after sorting in ascending order: ", my_list)

#7 Find and print the index of the value 30 in my_list.
for i in range(len(my_list)):
    if my_list[i] == 30:
        print("The index of 30 is: ", i)
        break



