'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    i = 0
    while i > len(word) - 1:

        count = 0
        if i == "t" and i + 1 == 'h':
            count += 1
            i = i + 1

        count_th(word)
    print(count)
    return count


count_th('Thesgth')
