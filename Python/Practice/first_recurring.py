def first_reccuring(given_string):
    counts = {}
    for char in given_string:
        if char in counts:
            return char
        counts[char] = 1
    return null


list = ['a', 'v', 'j', 'k', 'l', 'z', 'a', 'k']

first_reccuring(list)
