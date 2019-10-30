def fizz_buzz(nums):
    '''
    :param nums: iterable of numbers
    :return: return numbers divisible by 5 with fizz, and numbers divisible by 3 with buzz.
    '''

    results = []
    for num in nums:
        if num % 5 == 0 and num % 3 == 0:
            results.append('fizzbuzz')
            results.append(num)
        elif num % 5 == 0:
            results.append('fizz')
            results.append(num)
        elif num %3 == 0:
            results.append('buzz')
            results.append(num)

    if not results:
        return "No Fizz or Buzz"
    else:
        return results

print(fizz_buzz([3,5,7,8,10,15,13]))




