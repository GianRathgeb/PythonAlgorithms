def is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]):
            return False
    return True

def sort_desc(lst):
    i = 0
    while not is_sorted(lst):
        try:
            if lst[i] > lst[i+1]: lst[i], lst[i+1] = lst[i+1], lst[i]
            else: pass
            i += 1
        except IndexError:
            i = 0

    lst_desc = []
    for el in lst:
        lst_desc.insert(0, el)
    return lst_desc

print(sort_desc([1,4,6,2,3,6,1]))
