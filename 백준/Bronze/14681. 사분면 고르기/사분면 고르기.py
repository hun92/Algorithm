x = int(input())
y = int(input())

if x <0:
    if y < 0:
        print("3")
    else:
        print("2")
elif x > 0:
    if y < 0:
        print("4")
    else:
        print("1")