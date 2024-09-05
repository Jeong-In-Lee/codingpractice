import sys

def answer():
    x,y,w,s = map(int, sys.stdin.readline().split())
    total = 0

    if s<=w:
        cross = min(x,y)
        if cross>0:
            total+=(cross*s)
            x-=cross
            y-=cross    
        if (x+y)==1:
            total+=w
        elif (x+y)%2==1:
            total += ((x+y-1)*s + w)
        else:
            total+=(s*(x+y))
    elif s<w*2:
        cross = min(x,y)
        if cross>0:
            total += (s*cross)
            total += ((max(x,y)-cross) * w)
        else:
            total = w*x + w*y
    else:
        total = w*x + w*y

    print(total)
    
        