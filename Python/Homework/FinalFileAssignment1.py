n = float(input("How many numbers would you like to get the cube root of?: "))
nums = []
rooted = []
cycle = 1
#Error calculation
def diff(n2,mid) :
    if (n2 > (mid * mid * mid)) :
        return (float(n2 - (mid*mid*mid)))
    else :
        return ((float(mid * mid *mid)- n2))
#Start of the bisection search
def cubicRoot(n2) :
    start = min(-1.0,n2)
    end = max(1.0,n2)
    e = 0.000000000001
    global count
    count = 0
    while start < end :
        mid = (start + end) / 2.0
        error = diff(n2, mid)
        count += 1
        if (error <= e):
            return mid
        if((mid * mid * mid) > n2):
            end = mid
        else:
            start = mid
# user input for number of numbers being cube rooted.
#For loop runs number of inputs and adds inputs into nums array for rooting
for i in range(0, int(n)):
     x = float(input("The number " + str(cycle) + " is: " ))
     nums.append(float(x))
     print("cube root of " + str(x) + " is " + str((cubicRoot(x))) + " and it only took " + str(count) + " guesses!")
     cycle = cycle+1
