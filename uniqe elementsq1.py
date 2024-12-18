def uniqe_list(i):
    x=[]
    for e in i:
        if e not in x:
            x.append(e)
    return x

print(uniqe_list([1,8,8,8,5,9,5,5,6,7,6])) 