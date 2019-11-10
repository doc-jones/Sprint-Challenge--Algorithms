'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    count = 0
    if len(word) < 2:
        return count
    else:
        if word[:2] == "th":
            count = count + 1
    word = word[1:]
    return count + count_th(word)
