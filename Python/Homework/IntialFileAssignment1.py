# user input for number of numbers being cube rooted.
n = int(input("How many numbers would you like to get the cube root of?: "))
nums = []
#For loop runs number of inputs and adds inputs into nums array for later cube rooting
for i in range(0, int(n)) :
     x = int(input("Input a number: "))
     nums.append(x)
#Start of the bisection search
def cubicRoot(n) :
    start = 0
    end = n
