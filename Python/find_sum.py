def find_sum(nums, s = 8):
    '''
    list (or any iterable with integers), is passed through and searched for two numbers that add up to sum. The sum can
    be imputed, or it will default to 8.
    :param nums: list of integers that will be searched through for two numbers to equal the desired sum.
    :param s: desired number when adding 2 numbers from list
    :return: two numbers that add up desired sum.
    '''
    for i,number in enumerate(nums[:-1]):
        comp = s - number
        if comp in nums[i+1:]:
            print("Solution found: {} and {}".format(number, comp))
            break
    else:
        print("No Solution")

    