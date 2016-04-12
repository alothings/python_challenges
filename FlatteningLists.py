def flatten(l):
    new_l = []
    for item in l:
        new_l.extend(item)
    print new_l

flatten([[1,2],[3,4]])
flatten([[1],[2],[3],[4]])