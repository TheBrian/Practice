n = float(input("How many numbers would you like to get the cube root of?: "))
nums = []
rooted = []
def diff(n2,mid) :
    if (n2 > (mid * mid * mid)) :
        return (float(n2 - (mid*mid*mid)))
    else :
        return ((float(mid * mid *mid)- n2))
#Start of the bisection search
def cubicRoot(n2) :
    start = 0
    end = float(n2)
    e = 0.01
    while (True) :
        mid = (start + end) / 2
        error = diff(n2, mid)

        if (error <= e) :
            return mid
        if((mid * mid * mid) > n2) :
            end = mid
        else :
            start = mid
# user input for number of numbers being cube rooted.
#For loop runs number of inputs and adds inputs into nums array for later cube rooting
for i in range(0, int(n)):
     x = float(input("Input a number: "))
     nums.append(float(x))
     rooted.append(float(cubicRoot(x)))
print(rooted)

#Just working on the errors till the final file
