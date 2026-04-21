print("hello world")

# variables
num1 = 5
num2 = 10
print(num1 + num2)

# this is a function!
def my_function(num1, num2):
    return num1 + num2

new_var = my_function(10, 20)
print(new_var)

# conditionals
if (2 > 3):
    print("this is a line")
    print("this is another line!")
    print("True!")
    if(5 > 3):
        print("inside!")
else:
    print("False!")

# for loops
for i in range(0, 5):
    print("Loop")

# initializing a class
class MyClass():
    x = 25

myClass1 = MyClass()
print(myClass1.x)

# taking user input!
# user_name = input("What is your name? ")
# print("Welcome ", user_name)

# lists
my_list = [1, "hello", True, 10.5] # lists could be mixed!
print(my_list)
print(my_list[1])

# equivalent of a foreach loop!
for i in my_list:
    print(i)


# break and continue!
for i in range(0, 5):
    if(i == 0):
        continue # ignore whatever's after this and go to the next iteration
    if(i == 4): 
        break # ignore whatever's after this and get out of the loop!
    print(i)

a = 5
while(a > 0): # while loop! once the conditions is met, we break out of it!!
    print("while!")
    a-=1 # we need to change our variable, otherwise it'll run forever!

# an infinite loop, crashes your program!

a = 10
if((a > 3) and (a < 6) or a == 10): # multiple conditions!
    print("Hey")