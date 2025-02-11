def is_balanced_parentheses(s):
    list_added = []

    for i in s:
        list_added.append(i)

    if len(list_added) % 2 == 0:
        return True
    else:
        return False
