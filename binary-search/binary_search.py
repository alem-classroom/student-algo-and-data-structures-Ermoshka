def binary_search(lst, to_find):
    # search for the element to_find inside lst
    # if found, return index of element
    # else return -1
    mins, maxs = 0, len(lst) - 1
    guess, n = 0, 0
    while maxs >= mins:
        guess = (maxs + mins) // 2
        n += 1
        if lst[guess] == to_find:
            return guess
        elif lst[guess] < to_find:
            mins = guess + 1
        else:
            maxs = guess - 1
    return -1

print(binary_search([1,2,3,4,5,6,7], 4))