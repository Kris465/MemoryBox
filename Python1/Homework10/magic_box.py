def take():
    ls = []
    with open("vars.txt", "r") as f:
        for line in f.readlines():
            ls.append(line)
    f.close()
    print(ls)
    return ls

def put(lst):
    print(lst)
    with open("vars.txt", "w") as f:
        f.write(lst[0])
        f.write(lst[1] + "\n")
        f.write(lst[2] + "\n")
        f.write(lst[3])
    f.close()