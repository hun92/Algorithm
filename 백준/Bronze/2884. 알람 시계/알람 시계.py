x, y = map(int,input().split())
if y < 45:
    x = x-1
    y = (60+y)-45
    if x < 0:
        print(23,y)
    elif x >= 0:
        print(x,y)
elif y >= 45:
    print(x,y-45)