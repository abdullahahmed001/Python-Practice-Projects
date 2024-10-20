# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.





def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    def add_two(num1, num2):
        num1 = 5
        num2 = 2
        print(num1 + num2)


    add_two(5, 2)

    n = 0
    while True:
        if n == 3:
            break;
        print(n)
        n = n + 1

    n = 10
    if n > 5:
        print("n is greater than 5")
    elif(n < 5):
        print("n is less than 5")
    else:
        "Give me the right number"

    for i in [2, 1, 5]:
        print(i)

    smallest = None
    print("Before:", smallest)
    for itervar in [3, 41, 12, 9, 74, 15]:
        if smallest is None or itervar < smallest:
            smallest = itervar
        print("Loop:", itervar, smallest)
    print("Smallest:", smallest)


# Given an array of numbers, write a python program to find the largest value
#Need to use a loop

#[4,7,8,9,11]

largest_val= -1
#small_num = 0
for i in [4, 7, 6, 12, 4]:
    if i > largest_val:
        largest_val = i
        print("Largest value so far is: ", largest_val)


print("Largest value found is: ", largest_val)

for n in "banana":
    print(n)

count = 0
sum = 0
for i in [3, 6, 7, 8, 9]:
    count = count + 1
    print(count, i)
    sum = sum + i
print(sum)

found = False
print("Before", found)
for i in [9, 41, 12, 3, 74, 15]:
    if i == 3:
        found = True
    print(found, i)
print("After", found)

# 1. We set the counter variable to a large number
# 2. We print out the bool value before iterating through the list
# 3. Loop through the list to find the smallest value
# 4. Once the smallest value has been found, set the variable to that value
#5. Print out the smallest value

count = 100
found = False
print("Before", found)
for i in [4, 6, 7, 5]:
    if i < count:
        count = i
        found = True
    print(found, i)
print("After: ", count)

#Python program for finding the smallest value
smallest = None
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)

#Pythion code using a break statement
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# Output: 1
#         2

#Continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Output: 1
#         2
#         4
#         5


#Strings in Python

fruit = "banana"
letter = fruit[i-5]
print(letter)
print(len(fruit))












# See PyCharm help at https://www.jetbrains.com/help/pycharm/
