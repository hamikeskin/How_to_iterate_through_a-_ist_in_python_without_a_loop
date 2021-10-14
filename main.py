def iterate (lst, start, end):
    if start < 0 or end >= len(lst) or start > end:
        return
    print(lst[start])
    iterate(lst, start+1, end)
list = [9, 7, 5, 3, 1, 8, 6, 4, 2]
iterate(list, 0, 8)